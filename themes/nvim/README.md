# Claude Cream for Neovim

Neovim Lua 配色方案，包含 Light 与 Dark。编辑器表面、语法高亮、诊断、Git 与终端 ANSI 映射自 [`../../tokens/tokens.json`](../../tokens/tokens.json)。ANSI 16 色与 Ghostty 主题一致。需要 `termguicolors`。

## 文件

| 文件 | 用途 |
|---|---|
| `colors/claude-cream.lua` | 跟随 `vim.o.background` |
| `colors/claude-cream-light.lua` | 固定浅色 |
| `colors/claude-cream-dark.lua` | 固定深色 |
| `lua/claude-cream/` | 调色板与高亮组 |

## 安装

### macOS / Linux

```bash
mkdir -p "$HOME/.local/share/nvim/site/pack/claude-cream/start/claude-cream"
cp -R themes/nvim/colors themes/nvim/lua \
  "$HOME/.local/share/nvim/site/pack/claude-cream/start/claude-cream/"
```

### Windows

将 `colors` 与 `lua` 复制到：

```text
%LOCALAPPDATA%\nvim-data\site\pack\claude-cream\start\claude-cream\
```

原生 Neovim 复制后即可用 `:Telescope colorscheme` 或 `:colorscheme claude-cream` 切换。LazyVim 不行：lazy.nvim 默认会重置 runtimepath，`site/pack` 里的主题进不了选择器。

### LazyVim

lazy.nvim 会重置 runtimepath，所以 packpath 复制之后还要注册插件，否则 Telescope 看不到。职责分开：

| 文件 | 作用 |
|---|---|
| `lua/plugins/claude-cream.lua` | 把主题挂进 runtimepath |
| `lua/plugins/colorscheme.lua` | 只负责启动时 `persist.load`，不写死主题名 |
| `ColorScheme` autocmd | Telescope 换主题时 `persist.save` |

`lua/plugins/claude-cream.lua`：

```lua
return {
  {
    dir = vim.fn.stdpath("data") .. "/site/pack/claude-cream/start/claude-cream",
    name = "claude-cream",
    lazy = false,
    priority = 1000,
  },
}
```

`lua/plugins/colorscheme.lua` 不要写成 `colorscheme = "claude-cream"`。应交给上次保存的名字：

```lua
local persist = require("config.theme_persist")

return {
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = persist.load,
    },
  },
}
```

`ColorScheme` 时保存（可放在 `lua/config/autocmds.lua`）：

```lua
vim.api.nvim_create_autocmd("ColorScheme", {
  callback = function()
    require("config.theme_persist").save()
  end,
})
```

这样用 `:Telescope colorscheme` 或 `<leader>uC` 切换即可，重启后仍是上次选的主题，不必每次改 `colorscheme.lua`。`persist.save` / `persist.load` 自行实现：把 `vim.g.colors_name`（以及需要的 `background`）写到 `stdpath("state")` 再读回来。

不想复制到 packpath 时，把 `dir` 换成仓库里的 `themes/nvim` 路径。`lazy = false` 不能省。

## Token 映射

| Neovim 区域 | Token 来源 |
|---|---|
| 编辑器背景 / 浮层 / 边框 | `editor.*` + `colors.*` |
| 正文、强调、语义状态 | `colors.light` / `colors.dark` |
| 语法与 Treesitter | `syntax.light` / `syntax.dark` |
| Diff / Git 状态 | `editor.*.diff-*` + `colors.*.success` / `error` |
| `:terminal` ANSI 0–15 | Ghostty `claude-cream-light` / `claude-cream-dark` |

字体不由 colorscheme 控制。建议使用 JetBrainsMono Nerd Font Mono。

## 验证

```bash
python3 scripts/validate.py
```

在 Neovim 中还应检查 Light / Dark、Python、Lua、Markdown、Diff、诊断与终端 ANSI。
