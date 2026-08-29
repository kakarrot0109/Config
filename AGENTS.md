# AGENTS.md

本文件是 Claude Cream 仓库根目录的项目级 AI Coding Agent 规范。

适用工具：

- Codex：默认读取根目录 `AGENTS.md`
- Claude Code：通过根目录 `CLAUDE.md` 导入本文件
- 其他能读取 `AGENTS.md` 的编码智能体

使用约定：

1. 个人长期偏好放全局规范；本文件只写项目级约束。
2. 子目录另有 `AGENTS.md` 时，优先遵守距离当前文件更近的规则。
3. 不存在的命令、目录、文档不要写成已可用。

## 1. 项目概况

### 项目名称

```text
Claude Cream
```

### 项目定位

```text
暖色调设计 token 与主题资产库，为 Codex、Cursor / VS Code、Zed、Typora、Obsidian、Ghostty、OpenCode、Neovim、Website 与插画生成提供统一视觉语言。
```

### 主要用户

```text
个人维护者；需要在编辑器、终端、网站与生成式插画间保持同一套奶油 + 珊瑚视觉体系。
```

### 核心目标

```text
以 tokens/tokens.json 为 Codex、Cursor / VS Code、Zed、OpenCode、Neovim、编辑器与终端主题的单一真源，同时独立管理 Website 色板与图像生成规范。
```

### 非目标

当前阶段不处理：

- 不做 Web 应用、包管理发布流水线或在线主题商店
- 不引入 npm / 构建器作为默认安装路径（安装靠 `cp`）
- 不引入付费字体或必须联网才能生效的依赖

不要主动实现非目标中的内容。

---

## 2. 技术栈

### 前端

```text
暂无（主题为 CSS / 终端配置 / 客户端模板文件）
```

### 后端

```text
暂无
```

### 数据库

```text
暂无
```

### UI 与样式

```text
Design Tokens（JSON）→ Cursor / VS Code Theme JSON、Zed Theme JSON、Typora CSS、Obsidian CSS、Ghostty palette、OpenCode Theme JSON、Neovim Lua、CLI 配置模板
```

### 状态管理

```text
无
```

### 包管理器

```text
无；安装与分发通过文件复制
```

### 测试体系

```text
暂无自动化测试；以视觉核对、文件名约束检查、git diff --check 为主
```

### 部署方式

```text
本机 cp 安装到各客户端主题 / 配置目录
```

---

## 3. 常用命令

执行任务前先查看本节，不要猜测命令或混用包管理器。

### 安装依赖

```bash
暂无（无包管理器）
# 代码字体建议本机安装 JetBrainsMono Nerd Font Mono
```

### 本地开发

```bash
# 无 dev server；改 tokens / themes 后按 README 复制到目标客户端验证
```

### 类型检查

```bash
暂无
```

### 单元测试

```bash
暂无
```

### 集成或端到端测试

```bash
# Typora（macOS 示例）
cp themes/typora/*.css themes/typora/.claude-theme-base.css \
  "$HOME/Library/Application Support/abnerworks.Typora/themes/"

# Obsidian（按本机 vault 路径调整）
cp -R themes/obsidian "$HOME/Dev/obsidian-wiki/.obsidian/themes/Claude Cream"

# Ghostty
mkdir -p "$HOME/.config/ghostty/themes"
cp themes/ghostty/config.ghostty "$HOME/.config/ghostty/config"
cp themes/ghostty/claude-cream-light themes/ghostty/claude-cream-dark \
  "$HOME/.config/ghostty/themes/"

# Cursor（macOS / Linux）
mkdir -p "$HOME/.cursor/extensions"
rm -rf "$HOME/.cursor/extensions/kakarrot.claude-cream-0.2.0"
cp -R themes/vscode "$HOME/.cursor/extensions/kakarrot.claude-cream-0.2.0"

# Cursor / VS Code 主题静态验证
themes/vscode/scripts/validate-theme.sh

# 全平台主题静态验证
python3 scripts/validate.py

# Zed（macOS / Linux）
mkdir -p "$HOME/.config/zed/themes"
cp themes/zed/claude-cream.json "$HOME/.config/zed/themes/"

# Zed 主题静态验证
jq empty themes/zed/claude-cream.json

# OpenCode
mkdir -p "$HOME/.config/opencode/themes"
cp themes/opencode/claude-cream.json "$HOME/.config/opencode/themes/"

# Neovim
mkdir -p "$HOME/.local/share/nvim/site/pack/claude-cream/start/claude-cream"
cp -R themes/nvim/colors themes/nvim/lua \
  "$HOME/.local/share/nvim/site/pack/claude-cream/start/claude-cream/"
```

### Lint

```bash
git diff --check
# 如改 SVG：可用 xmllint 检查结构
```

### 构建

```bash
暂无（无构建产物流水线；token 到主题文件目前为手工映射）
```

### 格式化

```bash
暂无
```

### 数据库迁移

```bash
暂无
```

如果某项命令不存在，写「暂无」，不要自行创建新的工具链，除非任务明确要求。

---

## 4. 目录职责

```text
tokens/
  tokens.json             设计 token 单一真源（SSOT）
  README.md               token 分组与生成说明
themes/
  codex/                  Codex Light/Dark 可导入主题与说明
  vscode/                 Cursor / VS Code 五模式主题、验证脚本与视觉 Fixtures
  zed/                    Zed Light/Dark 本地主题与安装说明
  opencode/               OpenCode Light/Dark TUI 主题
  nvim/                   Neovim Light/Dark Lua 配色方案
  typora/                 Typora Light/Dark 主题 CSS
  obsidian/               Obsidian 主题 + Style Settings
  ghostty/                Ghostty 主题与主配置
  website/                Website Light/Dark 色彩主题
  image-generation/      插画、个人社交头像与壁纸生成风格及提示词
img/                      Logo、横幅、效果图
tasks/
  specs/                  功能规格
  plans/                  开发计划
README.md / README.zh-CN.md
AGENTS.md                 本仓规范（本文件）
CLAUDE.md                 本仓 Claude Code 入口
```

目录规则：

- 修改前先理解目录职责和现有调用关系。
- 新文件放入职责最匹配的现有目录。
- 不创建语义重复的目录。
- 不移动、重命名或整理与任务无关的文件。
- 不为了个人偏好调整现有目录结构。
- 跨层调用必须遵守项目现有架构边界。
- 改颜色 / 字体 / 间距时先改 `tokens/tokens.json`，再同步各平台产物。

---

## 5. 相关项目文档

开始相关任务前，按需读取：

- `README.md` / `README.zh-CN.md`：安装、结构、设计原则
- `tokens/README.md`：token 分组与生成约定
- `themes/codex/README.md`：Codex 主题导入、token 映射与兼容性说明
- `themes/vscode/README.md`：Cursor / VS Code 主题、GitHub 下载与跨平台安装说明
- `themes/zed/README.md`：Zed 本地主题安装、token 映射与验证说明
- `themes/opencode/README.md`：OpenCode 主题安装与 token 映射
- `themes/nvim/README.md`：Neovim 配色安装、LazyVim 配置与 token 映射
- `tasks/specs/`：已确认需求
- `tasks/plans/`：已确认实现计划

不存在的文件不需要创建，除非任务确实需要。当前无根级 `DESIGN.md`、`ARCHITECTURE.md`、`CONTRIBUTING.md`、`tasks/lessons.md`。

当本文档与更具体目录中的 `AGENTS.md` 冲突时，开发本仓以根目录本文件优先。

---

## 6. 实现原则

### 6.1 先理解再修改

修改代码前：

- 阅读目标文件及其直接调用方。
- 理解现有数据流、状态流和错误处理方式。
- 检查仓库中是否已有相同或相近实现。
- 确认项目现有命名、类型和组件模式。

不要在未理解现有实现时大范围重写。

### 6.2 最小实现

- 选择满足当前需求的最简单方案。
- 不增加需求之外的功能。
- 不提前设计尚未需要的扩展能力。
- 不为一次性逻辑创建复杂抽象。
- 不引入没有明确收益的配置项或依赖。
- 优先复用项目现有组件、工具函数和基础设施。

### 6.3 最小改动

- 只修改与当前任务直接相关的代码。
- 保持现有架构、风格、命名和格式。
- 不顺手重构相邻代码。
- 不格式化与本次任务无关的文件。
- 不清理原有死代码或历史问题，除非用户明确要求。
- 删除因本次修改产生的无用导入、变量、函数和文件。

每一处改动都应能够追溯到当前需求。

### 6.4 解决根因

修复问题时：

- 优先定位根因，不通过隐藏错误、吞掉异常或硬编码结果掩盖问题。
- 不使用仅对当前示例有效的临时补丁。
- 不为了让测试通过而削弱真实业务约束。
- 无法彻底解决时，明确说明限制和剩余风险。

---

## 7. 决策与询问边界

用户目标明确且风险可控时，直接执行，不重复确认。

出现以下情况时，应先说明问题并询问：

- 存在会明显改变结果的关键需求歧义。
- 需要删除数据、覆盖文件或执行不可逆操作。
- 涉及核心架构、数据库模型、权限或安全模型调整。
- 需要新增重量级依赖或替换现有技术栈。
- 实际工作范围明显超出用户原始要求。
- 多种方案在成本、兼容性或维护性上存在重大差异。
- 改动主色、字体策略或破坏多平台一致性的视觉决策。

轻微实现细节由 Agent 根据现有代码和最简单方案自行决定。

---

## 8. 任务规模与工作流

### 8.1 小任务

包括：

- 文案或样式微调
- 小配置修改
- 明确的单点 bug
- 单文件局部修改
- 用户已经给出准确修改位置

处理方式：

1. 定位相关代码。
2. 直接修改。
3. 运行最相关的验证。
4. 简短汇报结果。

执行前说明：

```text
目标：
改动位置：
验证方式：
```

不创建 Spec、Plan 或任务管理文件。

### 8.2 中型任务

包括：

- 新增局部功能
- 修改多个相关文件
- 调整非核心业务逻辑
- 需要增加测试的功能修改

处理方式：

1. 在回复中给出简短实施步骤和验证方式。
2. 直接执行，无需等待二次确认。
3. 按最小可验证单元修改。
4. 完成后运行相关检查。

通常不创建独立 Spec 或 Plan 文件。若影响面小、用户要求直接改，也可跳过，但必须说明假设和验证方式。

### 8.3 大型或高风险任务

包括：

- 跨模块或跨应用改动
- 核心架构调整
- 数据库结构变更
- 登录、权限、安全、支付
- 多端联动
- 生产数据迁移
- 需求边界存在重大歧义
- 重构 token SSOT、批量改写三平台主题、引入构建工具链

处理方式：

```text
讨论需求边界
→ 编写 Spec
→ 等用户确认
→ 编写可执行 Plan
→ 等用户确认
→ 分阶段实现和验证
→ 同步必要文档
→ 按规则 commit
→ push（仅用户明确允许时）
```

只有大型或需要中断续作的任务才创建持久化计划文件。

---

## 9. Spec 与 Plan

### 9.1 Spec

需要 Spec 时，存放到：

```text
tasks/specs/
```

建议命名：

```text
YYYY-MM-DD-功能名-spec.md
```

Spec 至少包含：

```markdown
# 功能规格：功能名

## 背景

为什么要做。

## 目标

要实现什么。

## 非目标

明确不做什么。

## 用户场景

谁在什么场景下使用。

## 需求边界

包含什么，不包含什么。

## 交互流程

用户如何操作，系统如何响应。

## 数据与状态

涉及哪些数据、状态、缓存、本地存储、数据库字段。

## 权限与安全

是否涉及权限、敏感数据、鉴权、日志脱敏。

## 异常情况

只列真实可能发生的异常，不为低概率场景过度设计。

## 验收标准

怎么判断完成。
```

Spec 描述「做什么」和「如何验收」，避免提前陷入实现细节；除非实现约束会影响需求边界。

### 9.2 Plan

需要 Plan 时，存放到：

```text
tasks/plans/
```

建议命名：

```text
YYYY-MM-DD-功能名-plan.md
```

Plan 至少包含：

```markdown
# 开发计划：功能名

## 对应 spec

路径：tasks/specs/xxx.md

## 已确认需求

列出已确认的需求点。

## 当前代码理解

说明现有代码结构和关键文件。

## 实现步骤

按最小可提交单元拆分。

## 涉及文件

列出预计修改文件。

## 验证方式

列出要运行的检查命令。

## 回滚方式

说明如何回滚本次改动。

## 文档同步

说明是否需要更新 README.md、tasks/lessons.md 或其他文档。
```

Plan 必须具体到可以执行和验证，避免使用「完善功能」「优化代码」等模糊描述。

---

## 10. 编码约束

### 10.1 类型

- CSS / JSON / 配置文件保持现有结构与命名。
- 新增 token 时 light / dark 同步同名字段。
- 不通过随意硬编码破坏 SSOT。

### 10.2 函数与模块

- 函数保持单一职责。
- 优先使用项目现有模块边界。
- 不创建只有一处调用且没有降低复杂度的抽象。
- 公共逻辑只有在存在明确复用需求时才提取。

### 10.3 注释

- 注释解释原因、约束和非显而易见的行为。
- 不写重复代码表面含义的注释。
- 修改行为时同步更新相关注释。
- 不保留失效、误导或与代码矛盾的注释。

### 10.4 依赖

新增依赖前必须确认：

- 现有依赖和平台能力无法合理解决问题。
- 新依赖仍在维护，并与当前技术栈兼容。
- 引入收益高于包体积、构建时间和维护成本。
- 不存在明显更轻量的方案。

未经用户确认，不替换核心框架、数据库、构建工具或状态管理方案。

对本项目：默认不引入包管理器与构建流水线；本地优先、离线可用。

---

## 11. UI 与前端规则

存在设计原则时，所有视觉修改必须遵守 §21。

通用规则：

- 优先复用现有 Design Token，不另起一套色板。
- 不随意使用硬编码颜色、间距、圆角和阴影；先写 token。
- 保持 Light / Dark 成对更新。
- 中文优先：正文 PingFang SC，代码 JetBrains Mono。
- 暖色优先：不做冷灰白工业风。
- 精简自定义：只暴露页宽、字号、主色等真正常用项。
- 修改共享 token 时，检查 Codex / Cursor / VS Code / Zed / Typora / Obsidian / Ghostty / OpenCode / Neovim 是否同步。

涉及视觉修改时，应尽量在目标客户端实际打开验证，而不是只依赖静态代码检查。

---

## 12. API 与后端规则

暂无。

---

## 13. 数据库规则

暂无。

---

## 14. 错误处理与日志

- 不静默吞掉真实错误。
- 安装与验证失败时说明目标路径与原因。
- 用户可见错误不得暴露密钥或无关内部路径堆栈。
- 不把正常业务状态错误地记录为系统异常。

---

## 15. 安全规则

默认不要读取、输出、记录或提交：

- API Key
- Token
- 密码
- Cookie
- 私钥
- 证书
- `.env` 中的真实值
- 本地数据库内容
- 生产凭证
- 用户隐私数据

排查配置问题时：

- 优先读取 `.env.example`、配置代码和变量名称。
- 只确认变量是否存在，不输出变量值。
- 日志、测试数据和回复中的敏感信息必须脱敏。

发现敏感信息已进入 Git 暂存区或提交记录时，立即停止后续 push，并说明风险。

---

## 16. 验证规则

代码修改后运行与改动最相关的验证，不机械执行无关命令。

建议顺序：

1. 确认 `tokens/tokens.json` 与目标主题文件一致
2. 修改 Codex 时校验 `codex-theme-v1:` 前缀、JSON schema、Light/Dark variant 与 token 映射
3. 修改 Cursor / VS Code 时运行 `themes/vscode/scripts/validate-theme.sh`
4. 修改 Zed 时运行 `jq empty themes/zed/claude-cream.json`，并按官方 `themes/v0.2.0` schema 检查字段、Light/Dark 对称性与 token 映射
5. 修改 OpenCode / Neovim 时确认 JSON 或 Lua 能解析，且 primary / 语法 comment 仍映射自 tokens
6. 检查 Typora 主题文件名是否使用连字符
7. 需要时导入或 `cp` 到目标客户端并目视核对
8. `git diff --check`
9. SVG 变更可用 `xmllint` 检查

### Bug 修复

优先：

1. 复现问题。
2. 编写或定位能够覆盖问题的测试（本项目以视觉复现步骤代替）。
3. 修复根因。
4. 验证原问题不再出现。
5. 检查是否引入回归。

### 无法验证时

必须说明：

- 哪些验证未运行
- 未运行的原因
- 已完成哪些替代检查
- 仍然存在什么风险

验证失败时还必须说明：

- 失败命令
- 失败原因
- 是否由本次改动导致
- 下一步建议

不要声称未实际运行的测试、构建或页面验证已经通过。不要隐藏失败。

---

## 17. 文档同步

只有当修改影响长期使用、开发或维护方式时，才更新文档。

需要考虑更新文档的情况：

- 安装或启动方式变化
- 环境变量变化
- API 或数据库结构变化
- 核心功能或操作方式变化
- 项目目录或架构变化
- 新增长期有效的限制或约定
- token 分组变化

普通修复、临时过程和实现流水账不写入 `README.md`。

中英文 README 若同时存在，涉及安装路径、目录结构、设计原则的变更应两边同步。

只有产生可跨任务复用的新经验时，才更新 `tasks/lessons.md` 或类似经验文档。当前仓库尚无 `tasks/lessons.md`，确有必要时再创建。

### 17.1 README.md

适合写入：

- 安装、启动、构建方式
- 环境变量
- 核心功能与架构
- 开发命令
- 配置说明
- 已知限制

不写：

- 临时过程
- 普通修复流水账
- 无关想法

### 17.2 tasks/lessons.md

适合写入：

- bug 根因
- 框架限制
- 项目约定
- 调试经验
- 不要重复犯的错误
- 已确认不可行方案

写入前必须去重；已有类似内容时更新原条目，不新增重复条目。

推荐格式：

```md
## YYYY-MM-DD

### 主题

- 现象：
- 根因：
- 解决：
- 以后注意：
```

---

## 18. Git 规则

默认行为：

- 可以查看 `git status`、`git diff` 和提交历史。
- 只修改当前任务需要的文件。
- 不自动 commit 或 push，除非用户明确要求或项目另有明确约定。
- 不覆盖用户尚未提交的改动。

若项目约定「完成已确认 Plan 后默认提交」，按以下流程：

```text
git status
→ 只添加本次相关文件
→ 运行验证
→ git commit
→ git push（仅用户明确允许时）
```

提交前检查：

- 当前分支是否正确；默认不在 `main` / `master` / `production` / `release` 上做中大型任务，除非用户明确允许
- 暂存区是否只包含当前任务相关文件
- 是否包含密钥、`.env`、缓存、构建产物或大文件
- 相关验证是否已经完成
- `README.md` 和 `tasks/lessons.md` 是否已检查
- commit message 是否准确描述本次改动

commit message 建议使用：

```text
类型: 简短说明
```

常用类型：

```text
feat
fix
docs
refactor
test
chore
style
perf
```

未经用户明确确认，禁止执行：

```bash
git push --force
git push --force-with-lease
git reset --hard
git clean -fd
git rebase
git checkout -- .
git restore .
```

涉及删除、覆盖历史或丢失本地改动的命令，都应视为高风险操作。

---

## 19. 完成标准

任务满足以下条件才可以报告完成：

- 需求已按确认范围实现。
- 没有明显的需求外功能。
- 没有无关改动。
- 相关验证已运行，或已明确说明无法运行。
- 没有隐藏已知失败。
- 没有敏感信息泄露。
- 必要的长期文档已同步。
- 剩余风险和限制已说明。

普通任务完成后使用以下格式汇报：

```text
已完成。

改动：
- 文件或模块：关键变化

验证：
- 命令或检查：结果

文档：
- README.md：已检查 / 已更新 / 无需更新
- tasks/lessons.md：已检查 / 已更新 / 无需更新

Git：
- commit：xxx / 未执行，原因：xxx
- push：已完成 / 未执行，原因：xxx

风险：
- 无 / xxx
```

不要贴完整代码或完整 diff，除非用户明确要求。
不要用长篇过程描述代替结果。

---

## 20. Claude Code 兼容层

项目根目录额外创建 `CLAUDE.md`，内容保持极简：

```md
# Claude Code 项目入口

请先读取并遵守：

@AGENTS.md

补充规则：

- 默认使用简体中文沟通。
- 不要在终端展示大段代码或完整 diff，除非用户明确要求。
- 中大型任务先按 AGENTS.md 编写 Spec 和 Plan，确认后再实现。
```

根目录 `CLAUDE.md` 仅服务本仓开发。

---

## 21. Claude Cream 特有规则

### 21.1 设计原则与 Token SSOT

设计原则：

1. 暖色优先，不做冷灰白
2. 克制衬线：正文用 PingFang SC，避免跨平台衬线崩坏
3. 本地优先：离线可用，不依赖付费字体或云服务
4. 真源边界：`tokens/tokens.json` 驱动 Codex、Cursor / VS Code、Zed、Typora、Obsidian、Ghostty、OpenCode 与 Neovim，Website 与 Image Generation 独立记录来源
5. 精简自定义：只暴露页宽、字号、主色等关键项

改色 / 字体 / 间距 / 圆角 / 语法高亮：

1. 先改 `tokens/tokens.json`
2. 再映射到 Codex、Cursor / VS Code、Zed、Typora、Obsidian、Ghostty、OpenCode、Neovim 产物
3. 需要时更新 `tokens/README.md` 分组说明

### 21.2 各客户端安装路径

| 客户端 | 安装动作 |
| --- | --- |
| Codex | 将 `themes/codex/*.theme` 的完整内容分别导入浅色与深色主题 |
| Typora | `cp` 主题 CSS 到各系统 Typora themes 目录 |
| Obsidian | `cp -R themes/obsidian` 到目标 vault 的 `.obsidian/themes/Claude Cream` |
| Ghostty | `cp` config 与 light/dark 主题到 `~/.config/ghostty/` |
| Cursor / VS Code | 从 GitHub 下载后复制 `themes/vscode` 到对应 `extensions/kakarrot.claude-cream-<version>` |
| Zed | `cp themes/zed/claude-cream.json` 到 `~/.config/zed/themes/` |
| OpenCode | `cp themes/opencode/claude-cream.json` 到 `~/.config/opencode/themes/` |
| Neovim | `cp -R themes/nvim/{colors,lua}` 到 `~/.local/share/nvim/site/pack/claude-cream/start/claude-cream/` |

### 21.3 Codex 主题约束

- 浅色与深色主题分别保存为 `.theme` 单行分享字符串。
- 文件必须使用 `codex-theme-v1:` 前缀，后接合法 JSON。
- `variant` 必须与文件名的 `light` / `dark` 一致。
- `accent`、`surface`、`ink` 与 `semanticColors` 必须映射自 `tokens/tokens.json`。
- Codex 主题导入格式可能随客户端升级变化，修改时需以当前应用导出的分享字符串验证 schema。
- 无法自动控制 Codex 客户端时，只能报告静态验证通过，实际导入与视觉验收保持未验证。

### 21.4 Cursor / VS Code 主题约束

- GitHub 仓库是唯一分发入口，不生成 `.vsix`，不发布扩展市场。
- 默认安装方式是复制 `themes/vscode`，不要求 npm、yarn、`vsce` 或构建器。
- `package.json` 声明的主题文件必须全部存在，版本与 README 安装目录一致。
- 默认 Light / Dark 的工作台颜色键必须对称。
- 辅助主题使用 VS Code 原生 `include` 继承默认主题，只覆盖模式差异。
- `editor` 与 `syntax` 五模式必须保持同名字段。
- 修改后运行 `themes/vscode/scripts/validate-theme.sh`。
- 实际视觉验收使用 `themes/vscode/fixtures/`，至少检查 Python、TypeScript、JSON、Markdown、Diff、终端、Command Palette 与 Peek / Debug。
- 全局 `workbench.colorCustomizations` 会覆盖主题；只针对某主题的调整必须限定到 `[Claude Cream ...]`。

### 21.5 Typora 文件名必须连字符

- Typora 主题文件名必须使用连字符（hyphen），例如 `claude-theme.css`。
- 禁止下划线文件名，否则 Typora 无法加载。
- 新增或重命名 Typora 主题文件时先检查此约束。

### 21.6 Zed 主题约束

- 本地主题保存为 `themes/zed/claude-cream.json`，一个主题族同时包含 `Claude Cream Light` 与 `Claude Cream Dark`。
- 主题必须使用 Zed 官方 `https://zed.dev/schema/themes/v0.2.0.json` schema。
- Light / Dark 的 `style` 字段必须对称，语法高亮分别映射自 `syntax.light` / `syntax.dark`。
- 编辑器表面映射自 `editor.light` / `editor.dark`，文本、边框和状态色映射自 `colors.light` / `colors.dark`。
- 修改后至少运行 JSON 解析、schema 字段检查、Light / Dark 字段对称性、语法 token 映射检查和 `git diff --check`。
- 无法实际打开 Zed 时，只能报告静态验证通过，导入与视觉验收保持未验证。

### 21.7 OpenCode 主题约束

- 本地主题保存为 `themes/opencode/claude-cream.json`，Light / Dark 写在同一个 JSON 的 `theme.*.light` / `theme.*.dark`。
- 必须包含 OpenCode TUI 使用的基础色、Diff、Markdown 与 syntax 槽位。
- `defs.light-primary` / `defs.dark-primary` 与 syntax comment 必须映射自 `tokens/tokens.json`。
- 修改后运行 `python3 scripts/validate.py`。
- 无法实际打开 OpenCode 时，只能报告静态验证通过。

### 21.8 Neovim 主题约束

- 本地配色保存在 `themes/nvim/`，通过 `colors/*.lua` 与 `lua/claude-cream/` 加载。
- `palette.lua` 的 Light / Dark 必须映射自 `tokens/tokens.json` 与 Ghostty ANSI。
- 提供 `claude-cream`（跟随 `vim.o.background`）、`claude-cream-light` 与 `claude-cream-dark`。
- 不引入包管理器或 colorscheme 框架；安装靠复制到 Neovim packpath。
- 修改后运行 `python3 scripts/validate.py`。
- 无法实际打开 Neovim 时，只能报告静态验证通过。
