# Claude Cream for OpenCode

OpenCode TUI 的 Claude Cream 主题。Light 与 Dark 写在同一个 JSON 里，跟随终端浅色 / 深色外观切换。界面色、Diff、Markdown 与语法高亮均映射自 [`../../tokens/tokens.json`](../../tokens/tokens.json)。

## 文件

| 文件 | 用途 |
|---|---|
| `claude-cream.json` | OpenCode 自定义主题（`defs` + `theme`） |

## 安装

### macOS / Linux

```bash
mkdir -p "$HOME/.config/opencode/themes"
cp themes/opencode/claude-cream.json "$HOME/.config/opencode/themes/"
```

### Windows

将 `claude-cream.json` 复制到：

```text
%USERPROFILE%\.config\opencode\themes\
```

然后在 OpenCode 中运行 `/themes`，选择 `claude-cream`。

项目级主题可复制到当前仓库的 `.opencode/themes/`。

## Token 映射

| OpenCode 槽位 | Light | Dark | Token 来源 |
|---|---|---|---|
| `primary` | `#b7791f` | `#e6bf7a` | `colors.*.primary` |
| `accent` | `#8a5a12` | `#f0cf92` | `colors.light.text-accent` / `colors.dark.primary-active` |
| `secondary` | `#2c6f75` | `#75b5bc` | `colors.*.accent-teal` |
| `background` | `#f8f7f2` | `#2d2e2d` | `editor.light.canvas-default` / `colors.dark.canvas` |
| `text` | `#403d36` | `#ddd9cd` | `colors.*.body` |
| `error` / `success` / `warning` | 语义色 | 语义色 | `colors.*.error` / `success` / `warning` |
| `syntax*` | Light 语法 | Dark 语法 | `syntax.light` / `syntax.dark` |
| Diff 前景 / 背景 | 成功绿 / 错误红 | 提亮对应色 | `colors.*` + `editor.*.diff-*` |

`info` 使用与 Ghostty / VS Code 相同的蓝槽（`#375b87` / `#89a8ce`），不在 `tokens.json` 的 `colors` 分组里，而在终端 ANSI 映射中。

## 验证

```bash
python3 -m json.tool themes/opencode/claude-cream.json > /dev/null
python3 scripts/validate.py
```

还应在 OpenCode 中切换系统 Light / Dark，检查会话文本、Diff、Markdown 与代码块。

## 限制

- 这是本地 JSON 安装，不发布 OpenCode 主题市场。
- OpenCode 主题 schema 可能随客户端升级变化；修改时以官方 `https://opencode.ai/theme.json` 为准。
