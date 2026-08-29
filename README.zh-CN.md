<p align="center">
  <img src="img/brand/logo.png" width="112" alt="Claude Cream Logo">
</p>

<h1 align="center">Claude Cream</h1>

<p align="center">
  <img src="img/brand/banner.png" width="100%" alt="Claude Cream 项目横幅">
</p>

[![Palette](https://img.shields.io/badge/palette-warm_ivory_+_amber-b7791f)](https://github.com/kakarrot-dev/claude-cream)
[![Mode](https://img.shields.io/badge/mode-light_+_dark-2d2e2d)](https://github.com/kakarrot-dev/claude-cream)
[![Font](https://img.shields.io/badge/font-PingFang_SC_+_JetBrains_Mono-3d3d3a)](https://github.com/kakarrot-dev/claude-cream)
[![Themes](https://img.shields.io/badge/themes-10_families-dccebf)](#目录结构)
[![Codex](https://img.shields.io/badge/Codex-light_+_dark-e6bf7a)](themes/codex/README.md)
[![License](https://img.shields.io/badge/license-MIT-b7791f)](./LICENSE)

暖色调主题资产库，覆盖 Codex、Cursor / VS Code、Zed、Typora、Obsidian、Ghostty、OpenCode、Neovim、Website 与可复用图像生成规范。

设计灵感来自 [Claude.com](https://claude.com) 的视觉语言：有层次的暖色表面、克制的琥珀金，以及让代码看起来像印刷物而非工业面板的排版质感。

---

## 特点

- **暖象牙画布** `#f5f3e9` &mdash; 避免冷白，并通过表面层次保持温润
- **琥珀金强调** `#b7791f` &mdash; 克制、温暖，同时清晰表达交互状态
- **暖炭灰深色画布** `#2d2e2d` &mdash; 保持深度而不使用生硬纯黑
- **中文优先排版** &mdash; 正文用 PingFang SC 系统字体，代码用 JetBrains Mono
- **一套视觉语言，十类主题资产** &mdash; Codex、Cursor / VS Code、Zed、Typora、Obsidian、Ghostty、OpenCode、Neovim、Website 与 Image Generation

## 界面预览

以下均为真实客户端截图，左侧为 Light，右侧为 Dark。画面已裁去项目侧栏、个人路径与账号信息。

### Codex

![Codex 的 Claude Cream Light 与 Dark 主题对照](img/screenshots/codex-light-dark.png)

### Cursor / VS Code

![Cursor 与 VS Code 的 Claude Cream Light 与 Dark 主题对照](img/screenshots/cursor-vscode-light-dark.png)

### Zed

![Zed 的 Claude Cream Light 与 Dark 主题对照](img/screenshots/zed-light-dark.png)

### Typora

![Typora 的 Claude Cream Light 与 Dark 主题对照](img/screenshots/typora-light-dark.png)

### Obsidian

![Obsidian 的 Claude Cream Light 与 Dark 主题对照](img/screenshots/obsidian-light-dark.png)

### Ghostty

![Ghostty 的 Claude Cream Light 与 Dark 主题对照](img/screenshots/ghostty-light-dark.png)

## 目录结构

```
claude-cream/
├── themes/
│   ├── codex/               # Codex Light + Dark 可导入主题
│   ├── typora/              # Markdown 写作 Light + Dark 主题
│   ├── obsidian/            # 知识库双模式主题
│   ├── ghostty/             # 终端调色板与 Ghostty 配置
│   ├── vscode/              # Cursor / VS Code 五模式主题
│   ├── zed/                 # Zed Light + Dark 本地主题
│   ├── opencode/            # OpenCode Light + Dark TUI 主题
│   ├── nvim/                # Neovim Light + Dark 配色方案
│   ├── website/             # Website 色彩主题（Light + Dark）
│   └── image-generation/    # 插画、头像与壁纸生成提示词
├── img/
│   ├── brand/               # 项目 Logo 与横幅
│   └── screenshots/         # 客户端 Light / Dark 实机截图
├── tokens/                  # 跨平台共享设计 token（单一真源）
└── scripts/                 # 无依赖跨平台校验
```

### 设计 Token

`tokens/tokens.json` 是 Codex、Cursor / VS Code、Zed、Typora、Obsidian、Ghostty、OpenCode 与 Neovim 主题的唯一真源。

| 分组 | 说明 |
|---|---|
| `colors.light` / `colors.dark` | 每种模式 28 个语义色变量 |
| `editor.*` | 五模式编辑器表面、状态、焦点、选区与 Diff |
| `typography` | 字体栈 + 字号 + 行高 |
| `spacing` / `rounded` | 间距 8 档 + 圆角 6 档 |
| `syntax.*` | 五模式代码高亮语义色 |

`tokens/tokens.json` 通过手工映射驱动 Codex、Cursor / VS Code、Zed、Typora、Obsidian、Ghostty、OpenCode 与 Neovim。`themes/website` 独立保存博客色板快照，`themes/image-generation` 将 Website 视觉语言转化为可复用的图像生成规则。

## 安装

### Codex

进入 Codex → 设置 → 外观，将 [`themes/codex/claude-cream-light.theme`](themes/codex/claude-cream-light.theme) 与 [`themes/codex/claude-cream-dark.theme`](themes/codex/claude-cream-dark.theme) 的完整内容分别导入浅色和深色主题。详细说明见 [`themes/codex/README.md`](themes/codex/README.md)。

### Cursor / VS Code

```bash
mkdir -p "$HOME/.cursor/extensions"
rm -rf "$HOME/.cursor/extensions/kakarrot.claude-cream-1.0.0"
cp -R themes/vscode "$HOME/.cursor/extensions/kakarrot.claude-cream-1.0.0"
```

执行 `Developer: Reload Window`，然后在 `Preferences: Color Theme` 中选择五种 Claude Cream 主题之一。GitHub 下载、VS Code、Windows、更新和验证说明见 [`themes/vscode/README.md`](themes/vscode/README.md)。无需 npm、`.vsix` 或扩展市场。

### Zed

```bash
mkdir -p "$HOME/.config/zed/themes"
cp themes/zed/claude-cream.json "$HOME/.config/zed/themes/"
```

打开 Zed Theme Selector，选择 `Claude Cream Light` 或 `Claude Cream Dark`。系统外观联动和 Windows 安装方式见 [`themes/zed/README.md`](themes/zed/README.md)。

### Typora

```bash
# macOS
cp themes/typora/*.css themes/typora/.claude-theme-base.css \
  "$HOME/Library/Application Support/abnerworks.Typora/themes/"
```

Windows：`%APPDATA%\Typora\themes\` &middot; Linux：`~/.config/Typora/themes/`

> 主题文件名必须用**连字符**，否则 Typora 无法加载。
>
> 复制前请保存已打开的文档，复制后手动重启 Typora。

### Obsidian

```bash
VAULT="/path/to/your/vault"
mkdir -p "$VAULT/.obsidian/themes"
cp -R themes/obsidian "$VAULT/.obsidian/themes/Claude Cream"
```

进入 Obsidian &rarr; 设置 &rarr; 外观 &rarr; 主题 &rarr; 选择 Claude Cream。深色模式跟随 Obsidian 原生切换联动。

配合 [Style Settings](obsidian://show-plugin?id=obsidian-style-settings) 插件可额外自定义。

### Ghostty

```bash
mkdir -p "$HOME/.config/ghostty/themes"
cp themes/ghostty/claude-cream-light themes/ghostty/claude-cream-dark \
  "$HOME/.config/ghostty/themes/"
```

在现有 `~/.config/ghostty/config` 中加入下列配置，然后重启 Ghostty：

```ini
theme = light:claude-cream-light,dark:claude-cream-dark
```

可选的 [`config.ghostty`](themes/ghostty/config.ghostty) 是一份完整的个人化配置。请先检查并按需合并，不要直接覆盖现有配置。

### OpenCode

```bash
mkdir -p "$HOME/.config/opencode/themes"
cp themes/opencode/claude-cream.json "$HOME/.config/opencode/themes/"
```

然后在 OpenCode 中运行 `/themes`，选择 `claude-cream`。说明见 [`themes/opencode/README.md`](themes/opencode/README.md)。

### Neovim

```bash
mkdir -p "$HOME/.local/share/nvim/site/pack/claude-cream/start/claude-cream"
cp -R themes/nvim/colors themes/nvim/lua \
  "$HOME/.local/share/nvim/site/pack/claude-cream/start/claude-cream/"
```

然后执行 `:colorscheme claude-cream`。Windows 路径、浅色 / 深色变体和 LazyVim 配置见 [`themes/nvim/README.md`](themes/nvim/README.md)。

### Website

在网站样式入口引入独立色彩主题：

```css
@import "./themes/website/theme.css";
```

使用 `html[data-theme="light"]` 与 `html[data-theme="dark"]` 切换模式。适用范围和来源见 [`themes/website/README.md`](themes/website/README.md)。

### Image Generation

组合使用 [`themes/image-generation/illustration-prompt-template.md`](themes/image-generation/illustration-prompt-template.md) 与 [`themes/image-generation/style.json`](themes/image-generation/style.json)，生成与 Website 一致的封面和编辑插画。同一目录还提供[个人社交头像](themes/image-generation/avatar-prompt-template.md)和[桌面或移动端壁纸](themes/image-generation/wallpaper-prompt-template.md)提示词。

每个主题目录均提供独立 README，说明安装、映射关系与验证方式。

## 校验

修改 Token 或主题后运行无依赖跨平台校验：

```bash
python3 scripts/validate.py
git diff --check
```

## 设计原则

1. **暖色优先** &mdash; 刻意选择暖色调，不做冷灰白
2. **克制衬线** &mdash; PingFang SC 足以撑起编辑气质，避免 Windows/Linux 崩坏
3. **本地优先** &mdash; 所有配置离线可用，不依赖付费字体或云服务
4. **真源边界清晰** &mdash; 编辑器与终端共享 Token 位于 `tokens/`，Website 与 Image Generation 各自记录来源
5. **精简自定义** &mdash; 只暴露真正常用的选项：页宽、字号、主色

## 环境要求

| 平台 | 最低版本 | 备注 |
|---|---|---|
| Codex | 支持自定义主题导入 | 浅色与深色需分别导入 |
| Typora | 1.5+ | Windows / macOS / Linux |
| Obsidian | 1.4.0+ | 全平台 |
| Ghostty | 1.0+ | macOS / Linux |
| Cursor / VS Code | VS Code API 1.85+ | 两者共用主题扩展 |
| Zed | 支持本地主题 schema v0.2.0 | 单个主题族包含 Light + Dark |
| OpenCode | 支持自定义 JSON 主题 | 复制到 `~/.config/opencode/themes/` |
| Neovim | 0.9+ 且开启 `termguicolors` | Light + Dark Lua 配色方案 |
| Website 主题 | 现代浏览器 | 需要支持 `color-mix()` |
| macOS | 12+ | PingFang SC 系统字体 |

**字体**：
- 正文：PingFang SC（macOS 系统自带；Windows/Linux 使用系统 fallback）
- 代码：JetBrains Mono（Typora 已内嵌；Ghostty/Obsidian 需系统安装，推荐 [JetBrainsMono Nerd Font](https://www.nerdfonts.com/font-downloads)）

## 贡献

个人配置项目，PR 谨慎接受。欢迎 Issue 讨论设计选择、报告 Bug、提出新平台适配建议。

## 许可证

MIT &mdash; 详见 [LICENSE](./LICENSE)。

## 致谢

- 视觉系统灵感来自 [Anthropic Claude](https://claude.com)
- 参考主题：[amm10090/claude-warm-obsidian-theme](https://github.com/amm10090/claude-warm-obsidian-theme) &middot; [YiNNx/typora-theme-lapis](https://github.com/YiNNx/typora-theme-lapis) &middot; [kepano/obsidian-minimal](https://github.com/kepano/obsidian-minimal) &middot; [primer/github-vscode-theme](https://github.com/primer/github-vscode-theme)
- 字体：[JetBrains Mono](https://www.jetbrains.com/mono/)（OFL 1.1）
- 品牌视觉：依据本仓 Claude Cream 色板与插画规范生成

---

用 &#x2615; + 琥珀金制作 by [KAKARROT](https://github.com/kakarrot-dev)
