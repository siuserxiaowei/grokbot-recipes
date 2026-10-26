# 推一个任务文件，GitHub Action 叫醒 Bot

- **适合**：本地有 Agent 写任务说明、想让 Grok Bot 自动接活的开发者
- **详细教程**：[GitHub Action 调 Webhook 叫醒 Bot](https://grokguide.si/tutorials/github-webhook)
- **思路来源**：[范凯：GitHub Action 触发 Grok Bot Webhook](https://x.com/fankaishuoai/status/2111361067041673452)

## 步骤

1. 让 Bot 建一个 Webhook 触发的 Routine：收到 {event, commit, files} 后去仓库读任务文件；同一个 commit 只处理一次。
2. 把 Webhook 地址和 key 放进仓库 Secrets：`GROK_WEBHOOK_URL`、`GROK_WEBHOOK_KEY`。
3. 加 `.github/workflows/wake-bot.yml`，只在 `tasks/**.md` 变化时触发，只传文件名和提交号。
4. 先用 actionlint 检查，再用本地收件器试 key 错、key 对、重复、无关提交四种情况。
