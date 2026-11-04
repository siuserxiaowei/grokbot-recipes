# Codex 派活：bot-codex-delegate 干完再叫醒

- **适合**：想把编码长活交给 Codex，又不想主聊天一直盯盘、也不想云电脑中途睡着的人
- **详细教程**：[grokguide.si/tutorials/bot-codex-delegate](https://grokguide.si/tutorials/bot-codex-delegate)
- **思路来源**：[realTaki/bot-codex-delegate](https://github.com/realTaki/bot-codex-delegate)（MIT；同作者 [bot-keepalive](https://github.com/realTaki/bot-keepalive)）

## 场景

主 Bot 自己轮询 Codex 会烧完整模型回合；一放手云电脑又可能睡。想让额度花在 Codex 上，主聊天空出来干别的。

## 准备

- 云电脑已装并登录 Codex CLI（app-server 与 CLI 共用登录与会话）
- 把上游 `skills/bot-codex-delegate/SKILL.md` 存成 Bot 技能
- 跑 `bash scripts/install-codex-app-server.sh`；默认只听 `127.0.0.1:4500`，沙箱 `workspace-write` + `on-request`
- **不要**默认开 `CODEX_DELEGATE_FULL_ACCESS=1`；全权限仅显式开启

## 步骤

1. 装技能 + 装服务；`status` 确认 app-server 健康。
2. 按 `bot-项目-任务类型` 命名会话（小写连字符，例如 `eng-shopapp-tests`）；同一工作区同时只允许一个写入者。
3. 主聊天把任务派给等待子 agent：前台 Shell 跑 `codex-turn`（单次最长约 13 分钟，到期可续）。
4. 干完再叫醒主 Bot；中途可用 `steer` / `interrupt`。
5. 人审 diff、跑项目测试后再合；回报 ≠ 可以进 main。

## 提示词

```text
请用 bot-codex-delegate 把「{{任务简述}}」派给 Codex：
1) 确认 app-server 健康，默认 workspace-write + on-request，不开 FULL_ACCESS；
2) 会话名 {{bot}}-{{项目}}-{{任务类型}}；同工作区只有我这一路写入；
3) 派给等待子 agent 前台跑 codex-turn，主聊天不要盯盘；
4) 干完叫醒我；可 steer/interrupt；回报后等我人审 diff。
```

## 产出

Codex 会话改动 + waiter 回报摘要；可选 steer 记录。

## 注意事项

- 与 bot-keepalive 同思路：前台 tool call 算活跃；守护/等待仍耗 low-effort 额度。
- `--approve` 默认 decline；危险操作要你显式放行。
- 本配方巡检只核脚本 AST、install 语法与安全默认 + 虚构会话命名表，**未**启动真实 Codex app-server。

## 小伟点评

本机脚本可解析、bash -n 过、安全默认齐；虚构六会话命名 6/6；ASSERT_OK。
