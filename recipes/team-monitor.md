# 多 Bot 交接看板

- **适合**：手上有两个以上 Bot、想知道活卡在谁那里的人
- **详细教程**：[用 Bot 监控室看多 Bot 交接](https://grokguide.si/tutorials/team-monitor)

## 场景

Bot 之间互相派活，记录散在各自的对话里。用社区的开源看板 Bot 监控室（grokbot-team-monitor-UI）在本机只读地把交接画出来，再让它在出错或等你时提醒你。

## 准备

- 一台装了 Python 3.9 以上的电脑（Mac、Windows、Linux 都行）
- 想先看看效果：不用 Grok Bot 数据，用演示模式
- 想接自己的脚本或别的 agent：准备一份 JSONL 事件日志

## 步骤

1. 克隆仓库，先跑演示：`python3 backend/server.py --demo --open`，顶栏会写明"演示数据 · 不是真实数据"。
2. 去掉 `--demo` 再启动，它会读本机 Grok Bot 应用的缓存；找不到数据时办公室就空着，不会拿演示团队顶替。
3. 想看自己的流水线：每一步往 JSONL 里追加一行（ask、handoff、error、reply），用 `--events 文件路径` 启动。
4. 在设置 → 提醒里加飞书或钉钉 Webhook，点测试按钮确认收得到。

## 提示词

```text
帮我在你的云电脑上试一下 github.com/Olivia295/grokbot-team-monitor-UI：
1. 先读 README 和 docs/events.md，告诉我它会读哪些文件、会不会往外传东西。
2. 用 --demo 启动，截一张图发给我。
3. 把你今天{{某条 Routine}}的每一步按 docs/events.md 的格式写成 JSONL，用 --events 启动再截一张。
4. 只在本机 127.0.0.1 上跑，不开公网端口，不改 Grok Bot 自己的文件。
```

## 产出

两张截图：演示办公室一张，自己流水线的交接和出错一张；外加一份能继续追加的事件日志。

## 注意事项

- 这是社区项目，不是官方工具；它读的是应用缓存，应用更新后格式可能变。
- 默认只听 127.0.0.1，要给别的设备看时再按 README 设置允许的主机名。
- 截图要分享前打开隐私模式，消息内容会被遮住。
