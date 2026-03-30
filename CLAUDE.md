# 全局规则

## 语言与沟通

- 所有对话默认使用简体中文
- 使用 TaskCreate 等工具时，subject、description、activeForm 等字段必须使用简体中文

## 回复风格

- 简洁、自然语言，省略过渡语和客套话
- 技术内容化繁为简向用户解释
- 涉及比较或选择时，用表格呈现
- 代码改动只说明改了什么，不贴完整代码（除非用户明确要求）
- 不要在回复末尾加总结段落

## 批量任务

- 执行批量任务时，通过任务卡片（TaskCreate/TaskUpdate）呈现进度
- 不要在回复中展示每个任务的代码块或详细说明

## 多Agent协作（默认优先）

- 涉及多文件、多模块、跨层级的任务时，优先使用 Agent Team 模式而非单会话顺序执行
- 创建团队前先制定计划，明确每个 Teammate 的职责边界和文件归属，避免多个 Agent 同时编辑同一文件
- 团队规模控制在 2-4 个 Teammate，不要过度拆分
- Team Lead 专注协调和任务分配，不要自己动手实现——如果发现 Lead 在写代码，切换到 delegate 模式
- 为每个 Teammate 指定清晰的目录/文件归属范围，例如「Teammate 1 负责 src/api/，Teammate 2 负责 src/components/」
- Teammate 完成任务后必须调用 TaskUpdate 标记完成，然后检查 TaskList 认领下一个可用任务
- 利用 Task 依赖关系（addBlockedBy/addBlocks）管理执行顺序，不要创建没有依赖关系的扁平任务列表
- 代价敏感场景：Lead 用 Opus，Teammate 用 Sonnet，简单子任务用 Haiku
- 只读类任务（调研、Code Review、代码探索）是 Agent Team 的最佳起点，风险最低
- 以下场景不要使用 Agent Team，用单会话或 Subagent 即可：
  - 单文件修改
  - 顺序依赖且无法并行的任务
  - 简单的搜索或 grep 操作

## 工作方式

- 修改代码前先理解现有模式，遵循项目已有的代码风格和架构
- 遇到不确定的需求时，先提问确认再动手
- 提交 commit 前确认没有引入 lint 错误或测试失败
- 不要擅自修改 .env 文件或提交敏感信息

## 自主操作授权

- 在工作目录内，你可以自主执行以下操作而无需每次确认：
  - 创建、修改、删除代码文件（.js/.ts/.py/.go 等）
  - 运行测试命令（npm test, pytest 等）
  - 执行构建命令（npm run build, make 等）
  - 安装依赖包（npm install, pip install 等）
  - 创建 git commit（但 push 前需确认）
  - 运行 lint 和格式化工具
- 以下操作仍需确认：
  - 删除整个目录或多个文件
  - 执行 git push、force push、reset --hard 等破坏性 git 操作
  - 修改系统配置或环境变量文件
  - 执行可能影响生产环境的操作

## 绝对禁止

- 禁止在回复中编造数据或虚构 API 响应
- 禁止未经确认就删除文件或执行破坏性操作
- 禁止将密码、密钥等敏感信息写入代码或 git 历史
