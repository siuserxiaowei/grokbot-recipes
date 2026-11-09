# 本机表单问人：答完提交就叫醒 Bot

- **适合**：Bot 一次要问你好几个问题、在聊天里一条条回容易漏，想像填问卷一样一次答完，答完它自己接着干的人
- **详细教程**：[grokguide.si/tutorials/local-forms](https://grokguide.si/tutorials/local-forms)
- **思路来源**：[brett-technical/grokbot-local-forms](https://github.com/brett-technical/grokbot-local-forms)（MIT）。我们没有照抄它的 README，只把「只写 form.json → 本机答题 → 落盘 → webhook 叫醒」整理成配方。

## 场景

Bot 要你确认选题、打分、补充几句话。你想在一张页面上答完，答案留在自己电脑上，Bot 收到通知再继续。

## 准备

- 在 Bot 那里建一个 webhook 触发的例程，拿到它的 Webhook URL 和 key（你自己复制，不贴进聊天）
- 本机有 Python 3；把仓库克隆到你自己的电脑

## 步骤

1. 让 Bot 先把题目和选项列给你确认，不让它自己编。
2. 复制 `example-form/` 成新文件夹，只改 `form.json`，其他文件不动。
3. 先演练：`FORMS_DIR` 指到临时目录，加 `FORM_DISABLE_WEBHOOK=1`，运行 `python server.py`，打开它打印的 127.0.0.1 地址。
4. 把 `webhook.local.json.example` 复制成仓库根目录的 `webhook.local.json`，填入 URL 和 key。
5. 正式答题提交；看页面返回的 `notify_reason`，是 `ok` 才说明 Bot 被叫醒了。

## 提示词

```text
读一下这个仓库的 README：https://github.com/brett-technical/grokbot-local-forms
我要一张表单，用来{{这张表要问清什么}}。先把题目和选项列给我确认，不要自己编。
确认后只写 form.json，id 用 {{kebab-case-名字}}，target_bot 写你自己的名字。
先用 FORMS_DIR 指到临时目录、FORM_DISABLE_WEBHOOK=1 演练一次，把 notify_reason 告诉我。
webhook 的 key 由我自己填进本机的 webhook.local.json，不要让我贴到聊天里。
```

## 产出

每次提交一对带时间戳的 `.md`（带 frontmatter，可放进笔记库）和 `.json`，以及一次发给 Bot 例程的通知。

## 注意事项

- 每次提交都新存一对文件，旧的不覆盖；通知失败答案也不会丢，修好例程再交一次即可。
- 发给 webhook 的记录里带本机文件路径，文件夹名别含隐私。
- 服务闲置默认 1 小时自停（每 30 秒检查一次）。

## 小伟点评

我们在云电脑上用一张中文表单和一个本地假 webhook 跑了 11 条断言，全部通过：演练模式不发通知、空答案 400、缺配置/占位配置都只存不发、配好后带 Bearer 头送达、key 不进答卷文件、对方 500 时答卷仍在、重复提交不覆盖、端口被占自动换、闲置自停。
