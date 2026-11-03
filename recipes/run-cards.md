# 编码收尾卡：run-cards 看清跑没跑完

- **适合**：想把长编码交给 Grok Build / Claude Code，又怕 exit 0 其实半路取消、聊天里看不清进度的人
- **详细教程**：[grokguide.si/tutorials/run-cards](https://grokguide.si/tutorials/run-cards)
- **思路来源**：[rystedtcreative/run-cards](https://github.com/rystedtcreative/run-cards)（MIT）

## 场景

大改动丢给编码 CLI 之后，对话里只剩一句「在跑了」。有的任务 exit 0，其实是无头模式缺审批被 cancel，或权限挡住、文件一个没改。

## 准备

- Node.js ≥ 18.17；云电脑 PATH 上有 `run-cards`，以及 `grok` 和/或 `claude`
- （可选）把上游 `skills/grok-build-and-claude-code/SKILL.md` 存成 Bot 技能
- 小改动（一两处）不要走这套，直接改更省

## 步骤

1. 克隆上游并把 `bin/run-cards` 链到 PATH。
2. 大任务用包装启动：`run-cards grok -p "…" --output-format json --always-approve` 或 `run-cards claude -p "…" --output-format json`。
3. 一出现 `open.png` 就贴进原聊天，本回合不要结束。
4. 结束后贴 `close.png`；只认 PASSED / FAILED / TIMED OUT / CANCELLED / BLOCKED。
5. 非 PASSED：说清原因，改参数后重跑并再贴一对卡。PASSED 后仍要人审 diff、跑项目测试。

## 提示词

```text
请把「{{任务简述}}」交给编码 CLI，并用 run-cards 包装：
1) 选 grok 或 claude；
2) 生成 run id，后台：run-cards <cli> -p "…" --output-format json（grok 改文件加 --always-approve）；
3) 立刻贴 open.png，本回合不结束；
4) 结束后贴 close.png，状态只用 PASSED/FAILED/TIMED OUT/CANCELLED/BLOCKED；
5) 非 PASSED 说明原因；密钥不进提示词；PASSED 后等我人审。
```

## 产出

开跑卡 + 收尾卡（PNG/Markdown）+ 一句诚实状态；可选 `run.json`。

## 注意事项

- 包装器透传 CLI 退出码；`$?=0` 仍可能是 CANCELLED/BLOCKED。
- 卡片会展示提示词开头；常见密钥会被遮掩，但仍不要写真实密钥。
- 本配方的巡检是「本机 npm test + 虚构收尾表」，不是本机真实 grok/claude 长任务录屏。

## 小伟点评

本机 npm test 145/145；虚构六收尾 R1–R6 全过；ASSERT_OK。
