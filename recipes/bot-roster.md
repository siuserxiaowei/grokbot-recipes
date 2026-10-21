# 花名册和看板：多 Bot 分工不打架

- **适合**：有 3 个以上 Bot 的人
- **详细教程**：[grokguide.si/playbooks/project-channels-roster](https://grokguide.si/playbooks/project-channels-roster)

## 场景

Bot 一多，任务重复做或没人做。

## 准备

- 一个共享文件夹

## 步骤

1. 建一份花名册：每个 Bot 的名字、负责什么、不负责什么。
2. 建一块看板文件：待做 / 进行中 / 完成。
3. 规定 Bot 之间只通过看板交接。
4. 让总管 Bot 每天汇总一次。

## 提示词

```text
请在共享文件夹建两个文件：roster.md（每个 Bot 的名字、负责、不负责）和 board.md（待做 / 进行中 / 完成三栏）。以后所有 Bot 接任务前先在 board.md 认领，做完移到“完成”并写一句结果。每天 {{时间}} 汇总一次发给我。
```

## 产出

两个文件加每日汇总。

## 注意事项

- “不负责什么”比“负责什么”更重要。
- 看板太长时让它归档旧任务。
