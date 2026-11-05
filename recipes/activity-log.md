# 活动账本：哈希链记下来，改一行就露馅

- **适合**：个人版没有 Action Recording，又想知道每个 Bot 干过什么、改过没、密钥有没有漏的人
- **详细教程**：[grokguide.si/tutorials/activity-log](https://grokguide.si/tutorials/activity-log)
- **思路来源**：[deximple/grokbot-activity-log](https://github.com/deximple/grokbot-activity-log)（MIT）。我们**没有**照搬上游全文与全部命令表，只保留装 CLI → 挂 skill → 日审私有同步的最短闸门。

## 场景

对话记录导不出去、也验不了有没有被改。需要一份本机 append-only 账本：任务开闭、动作、审批、备注都进哈希链；`verify` 能抓到改行；同步默认拒公仓。

## 准备

- Python 3.8+；能 clone GitHub
- 一个私有 git 远程（给 `gblog sync`）
- 愿意给 Bot 挂私有 skill，并在描述里要求「开任务就记」

## 步骤

1. `git clone https://github.com/deximple/grokbot-activity-log && cd grokbot-activity-log && ./install.sh`
2. 把 `skills/activity-log/SKILL.md` 存成私有技能；按 `docs/bot-description.md` 补一句记账规矩。
3. 登记别名：`gblog alias add --slug ops --display "Ops" --alias ops-bot`（每个 Bot 一个 ASCII slug）。
4. 干活顺序：`task-start` → 每个动作 `log` → 审批 `approval` → 重要文件 `archive` → `task-end`。
5. 建日审 Routine：`verify --all` →（可选）归档今日对话 → `report` / `status` → `gblog sync` 到**私有**仓。
6. 每周看一次 `capture` + `coverage`；缺口写进描述或 skill，不要补假时间戳。

## 提示词

```text
你负责维护本机活动账本（gblog）。开任何任务前先：
TID=$(gblog task-start --bot {{你的slug}} --task "<我给你的任务原话>")
之后每个浏览器/Shell/连接器/发信/委派动作立刻 gblog log；每次审批立刻 gblog approval；重要产物 gblog archive。
结束时 gblog task-end，并在回复末尾写 Ledger 脚注（条数、TID、head 前 12 位）。
禁止把密码、Bearer、PEM、一次性验证码写入 --detail。verify 变红时只报告 FAIL 行，不擅自 seal、不改历史。
日审只同步到我配置的私有远程；不要推公仓，不要联系任何人。
```

## 产出

可验证的本地账本 + 日审节奏 + （可选）本地五事件巡检 ASSERT_OK。

## 注意事项

- 这是个人版的替代账本，不是官方 Enterprise Action Recording。
- 本配方不替你接真实多 Bot 长期跑账，也不宣称覆盖所有密钥形态。
- 上游 README / skill / routine 全文请回原仓；本页只留闸门。

## 小伟点评

本地五事件：生命周期 OK、35 单测过、改行 hash mismatch、密钥形被洗、status 列出 bot；ASSERT_OK。
