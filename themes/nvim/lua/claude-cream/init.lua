local M = {}

function M.load(style, name)
  if style ~= "light" and style ~= "dark" then
    style = vim.o.background == "dark" and "dark" or "light"
  end

  local palette = require("claude-cream.palette")[style]
  vim.o.termguicolors = true
  vim.o.background = style
  vim.cmd("highlight clear")
  if vim.fn.exists("syntax_on") == 1 then
    vim.cmd("syntax reset")
  end
  vim.g.colors_name = name or "claude-cream"
  require("claude-cream.groups").apply(palette)
end

return M
