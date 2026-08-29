<p align="center">
  <img src="img/brand/logo.png" width="112" alt="Claude Cream logo">
</p>

<h1 align="center">Claude Cream</h1>

<p align="center">
  <img src="img/brand/banner.png" width="100%" alt="Claude Cream banner">
</p>

> Palette: warm ivory + amber · Mode: light + dark · Font: PingFang SC + JetBrainsMono Nerd Font Mono · License: [MIT](./LICENSE)

[![Palette](https://img.shields.io/badge/palette-warm_ivory_+_amber-b7791f)](https://github.com/kakarrot-dev/claude-cream)
[![Mode](https://img.shields.io/badge/mode-light_+_dark-2d2e2d)](https://github.com/kakarrot-dev/claude-cream)
[![Font](https://img.shields.io/badge/font-PingFang_SC_+_JetBrains_Mono-3d3d3a)](https://github.com/kakarrot-dev/claude-cream)
[![Themes](https://img.shields.io/badge/themes-10_families-dccebf)](#whats-inside)
[![Codex](https://img.shields.io/badge/Codex-light_+_dark-e6bf7a)](themes/codex/README.md)
[![License](https://img.shields.io/badge/license-MIT-b7791f)](./LICENSE)

[中文版](README.zh-CN.md)

A warm editorial theme library for Codex, Cursor / VS Code, Zed, Typora, Obsidian, Ghostty, OpenCode, Neovim, websites, and reusable illustration generation.

Inspired by the [Claude.com](https://claude.com) visual language: layered warm surfaces, restrained amber accents, and a typographic sensibility that makes code feel editorial rather than industrial.

---

## Highlights

- **Warm ivory canvas** `#f5f3e9` — softly layered instead of cold white
- **Amber accent** `#b7791f` — restrained, warm, and clear in interactive states
- **Warm charcoal dark canvas** `#2d2e2d` — depth without a hard black backdrop
- **Chinese-first typography** — PingFang SC system font for prose, JetBrains Mono for code
- **One visual language, ten theme assets** — Codex, Cursor / VS Code, Zed, Typora, Obsidian, Ghostty, OpenCode, Neovim, Website, and Image Generation

## Interface Preview

All images below are real client screenshots. Light is shown on the left and Dark on the right. Project sidebars, personal paths, and account details have been cropped out.

### Codex

![Claude Cream Light and Dark themes in Codex](img/screenshots/codex-light-dark.png)

### Cursor / VS Code

![Claude Cream Light and Dark themes in Cursor and VS Code](img/screenshots/cursor-vscode-light-dark.png)

### Zed

![Claude Cream Light and Dark themes in Zed](img/screenshots/zed-light-dark.png)

### Typora

![Claude Cream Light and Dark themes in Typora](img/screenshots/typora-light-dark.png)

### Obsidian

![Claude Cream Light and Dark themes in Obsidian](img/screenshots/obsidian-light-dark.png)

### Ghostty

![Claude Cream Light and Dark themes in Ghostty](img/screenshots/ghostty-light-dark.png)

## What's Inside

```
claude-cream/
├── themes/
│   ├── codex/               # Importable Codex Light + Dark themes
│   ├── typora/              # Light + Dark Markdown writing theme
│   ├── obsidian/            # Dual-mode knowledge-base theme
│   ├── ghostty/             # Terminal palettes + Ghostty config
│   ├── vscode/              # Five Cursor / VS Code themes
│   ├── zed/                 # Zed Light + Dark local theme
│   ├── opencode/            # OpenCode Light + Dark TUI theme
│   ├── nvim/                # Neovim Light + Dark colorscheme
│   ├── website/             # Website Light + Dark color theme
│   └── image-generation/    # Illustration, avatar, and wallpaper prompts
├── img/
│   ├── brand/               # Project logo and banner
│   └── screenshots/         # Real Light / Dark client screenshots
├── tokens/                  # Shared design tokens, single source of truth
└── scripts/                 # Dependency-free cross-platform validation
```

### Design Tokens

`tokens/tokens.json` is the single source of truth for Codex, Cursor / VS Code, Zed, Typora, Obsidian, Ghostty, OpenCode, and Neovim themes.

| Group | Description |
|---|---|
| `colors.light` / `colors.dark` | 28 semantic color variables per mode |
| `editor.*` | Five-mode editor surfaces, states, focus, selection, and Diff |
| `typography` | Font stacks, sizes, line heights |
| `spacing` / `rounded` | 8 spacing steps + 6 border-radius steps |
| `syntax.*` | Five-mode syntax highlighting tokens |

`tokens/tokens.json` drives Codex, Cursor / VS Code, Zed, Typora, Obsidian, Ghostty, OpenCode, and Neovim through manual mapping. `themes/website` is a separately managed snapshot of the blog palette, while `themes/image-generation` turns that website language into reusable image-generation rules.

## Install

### Codex

Import the complete contents of [`themes/codex/claude-cream-light.theme`](themes/codex/claude-cream-light.theme) and [`themes/codex/claude-cream-dark.theme`](themes/codex/claude-cream-dark.theme) into their matching sections under Codex → Settings → Appearance. See [`themes/codex/README.md`](themes/codex/README.md) for details.

### Cursor / VS Code

```bash
mkdir -p "$HOME/.cursor/extensions"
rm -rf "$HOME/.cursor/extensions/kakarrot.claude-cream-1.0.0"
cp -R themes/vscode "$HOME/.cursor/extensions/kakarrot.claude-cream-1.0.0"
```

Run `Developer: Reload Window`, then select one of the five Claude Cream themes from `Preferences: Color Theme`. The GitHub download, VS Code, Windows, update, and validation instructions are in [`themes/vscode/README.md`](themes/vscode/README.md). No npm, `.vsix`, or marketplace installation is required.

### Zed

```bash
mkdir -p "$HOME/.config/zed/themes"
cp themes/zed/claude-cream.json "$HOME/.config/zed/themes/"
```

Open Zed's Theme Selector and choose `Claude Cream Light` or `Claude Cream Dark`. System-mode settings and Windows installation are documented in [`themes/zed/README.md`](themes/zed/README.md).

### Typora

```bash
# macOS
cp themes/typora/*.css themes/typora/.claude-theme-base.css \
  "$HOME/Library/Application Support/abnerworks.Typora/themes/"
```

Windows: `%APPDATA%\Typora\themes\` &middot; Linux: `~/.config/Typora/themes/`

> Theme file names must use **hyphens** — Typora rejects underscores.
>
> Save open documents and restart Typora manually after copying the files.

### Obsidian

```bash
VAULT="/path/to/your/vault"
mkdir -p "$VAULT/.obsidian/themes"
cp -R themes/obsidian "$VAULT/.obsidian/themes/Claude Cream"
```

Then: Settings &rarr; Appearance &rarr; Themes &rarr; Claude Cream. Dark mode follows Obsidian's native toggle.

Works with the [Style Settings](obsidian://show-plugin?id=obsidian-style-settings) plugin for extra customization.

### Ghostty

```bash
mkdir -p "$HOME/.config/ghostty/themes"
cp themes/ghostty/claude-cream-light themes/ghostty/claude-cream-dark \
  "$HOME/.config/ghostty/themes/"
```

Add this line to your existing `~/.config/ghostty/config`, then restart Ghostty:

```ini
theme = light:claude-cream-light,dark:claude-cream-dark
```

The optional [`config.ghostty`](themes/ghostty/config.ghostty) is a complete opinionated configuration. Review and merge the settings you want instead of replacing your existing config.

### OpenCode

```bash
mkdir -p "$HOME/.config/opencode/themes"
cp themes/opencode/claude-cream.json "$HOME/.config/opencode/themes/"
```

Then run `/themes` and choose `claude-cream`. See [`themes/opencode/README.md`](themes/opencode/README.md).

### Neovim

```bash
mkdir -p "$HOME/.local/share/nvim/site/pack/claude-cream/start/claude-cream"
cp -R themes/nvim/colors themes/nvim/lua \
  "$HOME/.local/share/nvim/site/pack/claude-cream/start/claude-cream/"
```

Then run `:colorscheme claude-cream`. Windows path, Light / Dark variants, and LazyVim setup are in [`themes/nvim/README.md`](themes/nvim/README.md).

### Website

Import the standalone color theme into a website stylesheet:

```css
@import "./themes/website/theme.css";
```

Switch modes with `html[data-theme="light"]` and `html[data-theme="dark"]`. See [`themes/website/README.md`](themes/website/README.md) for scope and source.

### Image Generation

Use [`themes/image-generation/illustration-prompt-template.md`](themes/image-generation/illustration-prompt-template.md) with [`themes/image-generation/style.json`](themes/image-generation/style.json) to create covers and editorial images that match the website. The same directory also includes prompts for [personal social avatars](themes/image-generation/avatar-prompt-template.md) and [desktop or mobile wallpapers](themes/image-generation/wallpaper-prompt-template.md).

Each theme folder contains its own README with installation, mapping, and validation notes.

## Validate

Run the dependency-free cross-platform checks after changing tokens or themes:

```bash
python3 scripts/validate.py
git diff --check
```

## Design Principles

1. **Warm over cool** &mdash; deliberate warmth; no sterile gray or cold white
2. **Serif restraint** &mdash; PingFang SC carries enough character; avoids serif font fallback issues on Windows/Linux
3. **Local-first** &mdash; all assets work offline; no paid fonts, no cloud dependencies
4. **Clear sources of truth** &mdash; shared editor and terminal tokens stay in `tokens/`; Website and Image Generation keep their own documented sources
5. **Minimal customization** &mdash; expose only what matters: page width, font size, accent color

## Requirements

| Platform | Minimum | Notes |
|---|---|---|
| Codex | Supports custom theme import | Import Light and Dark separately |
| Typora | 1.5+ | Windows / macOS / Linux |
| Obsidian | 1.4.0+ | All platforms |
| Ghostty | 1.0+ | macOS / Linux |
| Cursor / VS Code | VS Code API 1.85+ | Shared theme extension |
| Zed | Supports local themes schema v0.2.0 | Light + Dark in one theme family |
| OpenCode | Custom JSON themes | Copy to `~/.config/opencode/themes/` |
| Neovim | 0.9+ with `termguicolors` | Light + Dark Lua colorscheme |
| Website theme | Modern browser | Requires `color-mix()` support |
| macOS | 12+ | PingFang SC system font |

**Fonts**:
- Prose: PingFang SC (built into macOS; system fallback on Windows/Linux)
- Code: JetBrainsMono Nerd Font Mono (install locally; [Nerd Fonts](https://www.nerdfonts.com/font-downloads) recommended)

## Contributing

This is a personal config project, so PRs are reviewed selectively. Issues and design discussions are welcome.

## License

MIT &mdash; see [LICENSE](./LICENSE).

## Credits

- Visual system inspired by [Anthropic Claude](https://claude.com)
- Reference themes: [amm10090/claude-warm-obsidian-theme](https://github.com/amm10090/claude-warm-obsidian-theme) &middot; [YiNNx/typora-theme-lapis](https://github.com/YiNNx/typora-theme-lapis) &middot; [kepano/obsidian-minimal](https://github.com/kepano/obsidian-minimal) &middot; [primer/github-vscode-theme](https://github.com/primer/github-vscode-theme)
- Font: [JetBrains Mono](https://www.jetbrains.com/mono/) (OFL 1.1)
- Brand imagery: generated from the Claude Cream palette and illustration specification in this repository

---

Made with &#x2615; + amber by [KAKARROT](https://github.com/kakarrot-dev)
