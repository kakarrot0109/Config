# Claude Cream — Token 系统说明

## 概述

`tokens.json` 是编辑器与终端主题的**单一真源（SSOT）**。所有颜色、字体、间距、圆角等设计变量只在此定义一次，再手工映射到各平台主题产物。

## Token 分组

| 分组 | 键 | 用途 | 消费平台 |
|---|---|---|---|
| `colors` | `light.*`, `dark.*` | 颜色体系：画布、UI 强调色、正文强调色、文本、表面、语义色 | Codex、Typora / Obsidian CSS、Ghostty palette、Cursor / VS Code、Zed、OpenCode、Neovim |
| `editor` | 五种模式的编辑器语义角色 | 工作台画布、文字、边框、焦点、选区和 Diff | Cursor / VS Code、Zed、OpenCode、Neovim |
| `typography` | `font-*`, `size-*`, `weight-*` | 字体栈（PingFang SC + JetBrains Mono）和字号层级 | 各平台 font-family / font-size 声明 |
| `spacing` | `xxs` ~ `xxl`, `section` | 间距/内边距，8px 递增体系 | padding / margin 值 |
| `rounded` | `xs` ~ `xl`, `pill` | 圆角半径体系 | border-radius 值 |
| `syntax` | 五种模式的语法高亮色 | 关键字、字符串、注释等 11 类 | Obsidian / Typora 代码高亮、Ghostty ANSI、Cursor / VS Code、Zed、OpenCode、Neovim 高亮 |
| `page` | `width`, `padding` | 编辑区页面宽度和内边距 | Typora `#write` / Obsidian `.markdown-preview-view` |
| `components` | — | 组件级 token 引用（按钮、卡片、代码窗、引用块等） | 设计参考，不直接注入代码 |

## 如何新增颜色变量

1. 在 `colors.light` 和 `colors.dark` 中同步添加同名字段（颜色值可不同）
2. 编辑器专用状态在 `editor` 五个模式中保持同名字段
3. 如果新增语法高亮色，同时在 `syntax` 五个模式中添加
4. 更新本文件“Token 分组”表
5. 手工同步对应主题文件，并运行定向比对

正文链接与强调文字使用 `text-accent` / `text-accent-hover`；`primary` / `primary-active` 保留给按钮、光标、焦点环和图标等 UI 元素。

## 如何同步三平台产物

```
# Typora —— 将 tokens.json 的值写入 CSS `:root` 变量块
tokens.json → claude-theme.css（Light）
tokens.json → claude-theme-dark.css（Dark）

# Obsidian —— tokens.json 的值写入 CSS `:root` / `.theme-dark` 变量块
tokens.json → theme.css（Light + Dark 二合一）

# Ghostty —— 将颜色与语法语义映射到背景、前景、光标、选区和 ANSI 16 色
tokens.json → claude-cream-light / claude-cream-dark

# Cursor / VS Code —— 映射到工作台、TextMate scope 与 Semantic Highlighting
tokens.json → 默认 Light/Dark + Dark Dimmed + Light/Dark High Contrast

# Codex：映射到可导入的 Light / Dark 主题分享字符串
tokens.json → claude-cream-light.theme / claude-cream-dark.theme

# Zed：映射到单个本地主题族中的 Light / Dark 变体
tokens.json → themes/zed/claude-cream.json

# OpenCode：映射到单个 JSON 的 dark / light 变体
tokens.json → themes/opencode/claude-cream.json

# Neovim：映射到 Lua 调色板与高亮组
tokens.json → themes/nvim/lua/claude-cream/palette.lua
```

## 设计决策

- `colors.light.primary === "#b7791f"` — Light 模式使用克制的琥珀金强调色
- `colors.dark.primary === "#e6bf7a"` — Dark 模式提亮为柔和金色以维持对比度
- `colors.light.canvas === "#f5f3e9"` / `colors.dark.canvas === "#2d2e2d"` — 暖象牙与暖炭灰双画布
- 字体策略：中文 `PingFang SC` 走系统调用，代码使用 `JetBrains Mono`
- 当前主题产物采用手工映射；修改 token 后必须同步 Codex、Typora、Obsidian、Ghostty、Cursor / VS Code、Zed、OpenCode 与 Neovim 文件
- `python3 scripts/validate.py` 检查模式字段对称、关键映射、Codex 分享字符串、Ghostty ANSI 完整性、Typora 文件名和正文对比度
- Cursor / VS Code 辅助主题使用原生 `include` 继承默认主题，但覆盖值仍来自 `editor` 与 `syntax`
- 不做衬线标题，统一使用 PingFang SC
