#!/usr/bin/env python3
"""Validate Claude Cream tokens and hand-mapped theme assets."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TOKENS_PATH = ROOT / "tokens" / "tokens.json"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"{path.relative_to(ROOT)}: {error}")


def relative_luminance(color: str) -> float:
    channels = [int(color[index : index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [
        channel / 12.92
        if channel <= 0.04045
        else ((channel + 0.055) / 1.055) ** 2.4
        for channel in channels
    ]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(foreground: str, background: str) -> float:
    lighter, darker = sorted(
        (relative_luminance(foreground), relative_luminance(background)),
        reverse=True,
    )
    return (lighter + 0.05) / (darker + 0.05)


def require_text(path: str, expected: str) -> None:
    content = (ROOT / path).read_text(encoding="utf-8")
    if expected not in content:
        fail(f"{path}: missing mapped value {expected}")


def validate_token_shape(tokens: dict[str, object]) -> None:
    colors = tokens["colors"]
    if set(colors["light"]) != set(colors["dark"]):
        fail("tokens: colors.light and colors.dark keys differ")

    editor_modes = tokens["editor"]
    syntax_modes = tokens["syntax"]
    expected_modes = {
        "light",
        "dark",
        "dark-dimmed",
        "light-high-contrast",
        "dark-high-contrast",
    }
    if set(editor_modes) != expected_modes or set(syntax_modes) != expected_modes:
        fail("tokens: editor and syntax must define the same five modes")
    if len({tuple(sorted(mode)) for mode in editor_modes.values()}) != 1:
        fail("tokens: editor mode keys differ")
    if len({tuple(sorted(mode)) for mode in syntax_modes.values()}) != 1:
        fail("tokens: syntax mode keys differ")


def validate_contrast(tokens: dict[str, object]) -> None:
    colors = tokens["colors"]
    syntax = tokens["syntax"]
    editor = tokens["editor"]

    checks = [
        (
            "colors.light.text-accent",
            colors["light"]["text-accent"],
            colors["light"]["canvas"],
        ),
        (
            "colors.dark.text-accent",
            colors["dark"]["text-accent"],
            colors["dark"]["canvas"],
        ),
    ]
    checks.extend(
        (
            f"syntax.{mode}.comment",
            syntax[mode]["comment"],
            editor[mode]["canvas-default"],
        )
        for mode in syntax
    )

    for name, foreground, background in checks:
        ratio = contrast(foreground, background)
        if ratio < 4.5:
            fail(
                f"{name}: contrast {ratio:.2f}:1 is below 4.5:1 "
                f"({foreground} on {background})"
            )


def validate_theme_mappings(tokens: dict[str, object]) -> None:
    colors = tokens["colors"]
    syntax = tokens["syntax"]

    mappings = {
        "themes/typora/claude-theme.css": [
            colors["light"]["primary"],
            colors["light"]["text-accent"],
            syntax["light"]["comment"],
        ],
        "themes/typora/claude-theme-dark.css": [
            colors["dark"]["primary"],
            colors["dark"]["text-accent"],
            syntax["dark"]["comment"],
        ],
        "themes/obsidian/theme.css": [
            colors["light"]["text-accent"],
            colors["dark"]["text-accent"],
            syntax["light"]["comment"],
            syntax["dark"]["comment"],
        ],
        "themes/vscode/themes/claude-cream-color-theme.json": [
            colors["light"]["text-accent"],
            syntax["light"]["comment"],
        ],
        "themes/vscode/themes/claude-cream-dark-color-theme.json": [
            colors["dark"]["text-accent"],
            syntax["dark"]["comment"],
        ],
        "themes/vscode/themes/claude-cream-dark-dimmed-color-theme.json": [
            syntax["dark-dimmed"]["comment"],
        ],
        "themes/zed/claude-cream.json": [
            f'{colors["light"]["text-accent"]}ff',
            f'{colors["dark"]["text-accent"]}ff',
            f'{syntax["light"]["comment"]}ff',
            f'{syntax["dark"]["comment"]}ff',
        ],
        "themes/opencode/claude-cream.json": [
            colors["light"]["text-accent"],
            colors["dark"]["primary-active"],
            syntax["light"]["comment"],
            syntax["dark"]["comment"],
        ],
        "themes/nvim/lua/claude-cream/palette.lua": [
            colors["light"]["text-accent"],
            colors["dark"]["primary"],
            syntax["light"]["comment"],
            syntax["dark"]["comment"],
        ],
    }
    for path, values in mappings.items():
        for value in values:
            require_text(path, value)


def validate_codex(tokens: dict[str, object]) -> None:
    for mode in ("light", "dark"):
        path = ROOT / "themes" / "codex" / f"claude-cream-{mode}.theme"
        content = path.read_text(encoding="utf-8")
        prefix = "codex-theme-v1:"
        if not content.startswith(prefix):
            fail(f"{path.relative_to(ROOT)}: invalid prefix")
        payload = json.loads(content[len(prefix) :])
        expected = tokens["colors"][mode]
        if payload["variant"] != mode:
            fail(f"{path.relative_to(ROOT)}: variant mismatch")
        if payload["theme"]["accent"] != expected["primary"]:
            fail(f"{path.relative_to(ROOT)}: accent token drift")
        if payload["theme"]["surface"] != expected["canvas"]:
            fail(f"{path.relative_to(ROOT)}: surface token drift")
        if payload["theme"]["ink"] != expected["ink"]:
            fail(f"{path.relative_to(ROOT)}: ink token drift")


def validate_ghostty() -> None:
    for mode in ("light", "dark"):
        path = ROOT / "themes" / "ghostty" / f"claude-cream-{mode}"
        content = path.read_text(encoding="utf-8")
        indexes = {
            int(match.group(1))
            for match in re.finditer(r"^palette\s*=\s*(\d+)\s*=", content, re.MULTILINE)
        }
        if indexes != set(range(16)):
            fail(f"{path.relative_to(ROOT)}: palette must contain indexes 0-15")
        for field in ("background", "foreground", "cursor-color", "selection-background"):
            if not re.search(rf"^{field}\s*=", content, re.MULTILINE):
                fail(f"{path.relative_to(ROOT)}: missing {field}")


def validate_typora_names() -> None:
    for path in (ROOT / "themes" / "typora").glob("*.css"):
        if "_" in path.name:
            fail(f"{path.relative_to(ROOT)}: Typora filenames must use hyphens")


def validate_opencode(tokens: dict[str, object]) -> None:
    path = ROOT / "themes" / "opencode" / "claude-cream.json"
    payload = load_json(path)
    theme = payload["theme"]
    required = {
        "primary",
        "secondary",
        "accent",
        "error",
        "warning",
        "success",
        "info",
        "text",
        "textMuted",
        "selectedListItemText",
        "background",
        "backgroundPanel",
        "backgroundElement",
        "backgroundMenu",
        "border",
        "syntaxComment",
        "syntaxKeyword",
        "markdownHeading",
        "diffAdded",
        "diffRemoved",
    }
    missing = required - set(theme)
    if missing:
        fail(f"{path.relative_to(ROOT)}: missing theme keys {sorted(missing)}")
    if theme["primary"]["light"] != "light-primary":
        fail(f"{path.relative_to(ROOT)}: primary.light must reference light-primary")
    if theme["primary"]["dark"] != "dark-primary":
        fail(f"{path.relative_to(ROOT)}: primary.dark must reference dark-primary")
    defs = payload["defs"]
    if defs["light-primary"] != tokens["colors"]["light"]["primary"]:
        fail(f"{path.relative_to(ROOT)}: light-primary token drift")
    if defs["dark-primary"] != tokens["colors"]["dark"]["primary"]:
        fail(f"{path.relative_to(ROOT)}: dark-primary token drift")
    if defs["light-syn-comment"] != tokens["syntax"]["light"]["comment"]:
        fail(f"{path.relative_to(ROOT)}: light syntax comment token drift")
    if defs["dark-syn-comment"] != tokens["syntax"]["dark"]["comment"]:
        fail(f"{path.relative_to(ROOT)}: dark syntax comment token drift")


def validate_nvim(tokens: dict[str, object]) -> None:
    path = ROOT / "themes" / "nvim" / "lua" / "claude-cream" / "palette.lua"
    content = path.read_text(encoding="utf-8")
    required = [
        tokens["colors"]["light"]["primary"],
        tokens["colors"]["dark"]["primary"],
        tokens["editor"]["light"]["canvas-default"],
        tokens["editor"]["dark"]["canvas-default"],
        tokens["syntax"]["light"]["comment"],
        tokens["syntax"]["dark"]["comment"],
    ]
    for value in required:
        if value not in content:
            fail(f"{path.relative_to(ROOT)}: missing mapped value {value}")
    colors_dir = ROOT / "themes" / "nvim" / "colors"
    for name in ("claude-cream.lua", "claude-cream-light.lua", "claude-cream-dark.lua"):
        if not (colors_dir / name).is_file():
            fail(f"themes/nvim/colors/{name}: missing colorscheme entry")


def main() -> None:
    tokens = load_json(TOKENS_PATH)
    validate_token_shape(tokens)
    validate_contrast(tokens)
    validate_theme_mappings(tokens)
    validate_codex(tokens)
    validate_ghostty()
    validate_typora_names()
    validate_opencode(tokens)
    validate_nvim(tokens)

    subprocess.run(
        [str(ROOT / "themes" / "vscode" / "scripts" / "validate-theme.sh")],
        cwd=ROOT,
        check=True,
    )
    print("Claude Cream cross-platform validation passed")


if __name__ == "__main__":
    main()
