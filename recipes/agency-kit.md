# 多 Bot 小公司开工包：RULES + 一呼一吸

- **适合**：想用几份纯文本把多 Bot 小公司的规矩、座位和省额度习惯一次齐备的人
- **详细教程**：[grokguide.si/tutorials/agency-kit](https://grokguide.si/tutorials/agency-kit)
- **思路来源**：[DensitySystems/grokbot-agency-kit](https://github.com/DensitySystems/grokbot-agency-kit)（MIT，2026-11-02）

## 场景

Bot 越建越多：经理抢活干、中间来回催进度、Routine 没事也刷屏、规则文件里还夹着密钥字样。需要一套短规矩：谁委派、怎么交接、怎么安静、密钥只写位置。

## 准备

- 一个你本人当 Owner 的工作区（本地文件夹或云电脑目录均可）
- 先读上游 `RULES.md` 与 `CREDIT-SAVING.md`（约十分钟）
- 只建你今天真需要的经理席，不要一次九个域
- 密钥放密钥管理器；文件里只用角色名或位置指代

## 步骤

1. 把上游仓库里的纯文本拷进自己的工作区，把 `<OWNER>` 等占位符改成自己的称呼。
2. 用自己的话重写 `RULES.md`：只有你亲口说过的才算规矩；Bot 不得自行加检查项。
3. 按 `ORG-STRUCTURE.md` 建 Lead + 一两个域经理；席位模板从 `seat-templates/` 抄短档案。
4. Routine 一次加一条，默认安静：见 `routines/quiet-watcher.md`、`keep-alive.md`、`webhook-inbound-dedupe.md`。
5. 席位过长或换阶段时走 `HANDOFF.md`：先写交接文件，再开继任席，旧席归档不删历史。
6. （可选）用本地虚构巡检脚本核对：经理委派、一呼一吸、安静 NOOP、文件无密钥字面量。

## 提示词

```text
请按「多 Bot 小公司开工包」帮我列一版落地清单（只要清单，不要替我建真实多 Bot）：
1) 用我的话改写 RULES：批准、一呼一吸、经理只委派、对外联络边界、文件不写密钥；
2) 今天只需要哪些域经理（最多两个）及各自一句话职责；
3) 先加哪一条安静 Routine，无变化时必须静默；
4) 交接时必须有的章节（开放闸门、已核实状态、密钥位置）。
提醒：不要把真实密钥、账号、主机写进任何文件；本清单不是云端多 Agent 实测。
```

## 产出

可编辑的规矩草稿 + 精简席位表 + 安静 Routine 候选 + （可选）虚构巡检 ASSERT_OK 输出。

## 注意事项

- 上游是纯文本开工包，不是可执行软件；改完要用你自己的话约束。
- 经理抢活、中途来回催、没事刷屏，都会把额度烧在协调上。
- 本配方的巡检是虚构规则表，不是真实多 Bot 或 Cursor cloud agents 实测。

## 小伟点评

虚构六事件：经理委派、一呼一吸、安静 NOOP、有变化才发、密钥样例拦截、违规呼吸检出；ASSERT_OK。
