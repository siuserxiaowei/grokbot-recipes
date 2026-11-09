# 云电脑保活：有截止时间的安静等待

- **适合**：要让云电脑在长任务或远程连接期间别睡过去，又不想它无限挂着耗额度、到点乱杀进程的人
- **详细教程**：[grokguide.si/tutorials/cloud-standby](https://grokguide.si/tutorials/cloud-standby)
- **思路来源**：[aritosi/GrokBot-Cloudstandby](https://github.com/aritosi/GrokBot-Cloudstandby)（MIT）。我们没有照抄它的 README 与 SKILL.md，只把「登记 → 截止 → 单看守前台等待 → 到期只停保活」的用法整理成配方。

## 场景

晚上让 Bot 跑一个要几个小时的任务，或者想过一会儿远程连上云电脑看一眼。怕中途休眠，又怕开了保活就忘了关。

## 准备

- 在 Grok Bot 里装好 `skills/grokbot-cloudstandby`（整目录，含 scripts）
- 想好截止时间（按你的时区）；已有进程就记下 PID

## 步骤

1. 把仓库地址发给 Bot，让它完整安装、装好先不启动。
2. 说清任务和截止：「保活云电脑到今晚 11 点」或「保活 24 小时」。
3. Bot 跑 `ka-start`：返回 START 才起一个后台子 Agent；返回 JOIN 就沿用已有看守。
4. 子 Agent 用**前台** Shell 调 `ka-wait`，一轮约 12 分钟；WAIT 就接下一轮，DONE / EXPIRED 才汇报。
5. 想看进度说「保活状态」（`ka-report`）；不需要了说「停止保活」（`ka-stop`）。

## 提示词

```text
请帮我安装这个技能：https://github.com/aritosi/GrokBot-Cloudstandby
完整安装 skills/grokbot-cloudstandby 目录（SKILL.md 和 scripts），装好先不要启动。
以后我说保活时，遵守：
1) 我没说任务和期限就先问，不自动开 24 小时；截止时间按我的时区。
2) 只有 START 才起一个看守；JOIN 或 BUSY 时不开第二个。
3) 看守必须用前台 Shell 等待，不用 nohup 或后台进程替代。
4) 到期或停止只结束保活登记，不终止我的任务进程。
5) 汇报日志前先检查有没有密钥或账号信息。
```

## 产出

一条带截止时间的保活登记 + 到期/完成时的一段简短汇报（任务名、状态、退出码、日志末尾几行）。

## 注意事项

- 保活本身耗额度；作者给的单账号参考是 5 小时约 2%～3%，以你自己的用量为准。
- 未来才开始的任务不能提前排；到时间再启动。
- 截止时间写过去的时刻会直接报错，不会被悄悄改成明天。

## 小伟点评

我们在云电脑上把 7 个自带测试跑过（7 passed），又实跑一遍：START/JOIN、第二个看守 BUSY、错租约 STALE、到期 EXPIRED、命令任务 exit 0、`ka-stop` 后被盯的进程仍活着。
