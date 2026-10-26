# X 传播分工作台：只读扫帖，你自己点发布

- **适合**：在 X 上发内容、想盯一批账号的爆款与趋势词、又不想让 Bot 代发的人
- **详细教程**：[X 传播分工作台：只读扫帖，你自己点发布](https://grokguide.si/tutorials/x-virality-score)

## 场景

每天刷关注列表很费时间。把关注账号、浏览量门槛和时区写进配置，让 Bot 只读扫原创帖、挖趋势词、给浏览最高的十条写改写草稿，再刷新你自己的 GitHub Pages 看板。发不发、改不改，都由你点。

## 准备

- 一个能用云电脑或本机浏览器的 Grok Bot
- 本机已登录 X 的只读会话（用来扫公开帖，不要提交 cookie）
- 一个你自己的公开 GitHub 仓库，用来挂 Pages 看板
- 仓库：https://github.com/monkeyteamvip/x-virality-score

## 步骤

1. 克隆或导入仓库，把 `config/watchlist.example.json` 复制成 `config/watchlist.json`，填入你的时区、浏览量门槛和关注账号（不要带 `@`）。
2. 把 `board/data.example.json` 复制成 `board/data.json`，写上你的品牌名和 handle；示范看板 `kiosa-board` 只当样子看，不是你的。
3. 按 `board/SETUP.md` 把 `index.html` 和 `data.json` 推到你自己的 Pages 仓库，记下那个 URL。
4. 日常：Bot 扫完后跑 `pipeline/run_day.sh prepare <日期>`，再补全草稿与雷达输入，最后 `pipeline/run_day.sh <日期>` 出摘要和 `PING.txt`。
5. 你从草稿里挑 1–2 条自己发布；Bot 只刷新你的看板，不代发、不点赞、不回复。

## 提示词

```text
请按仓库 AGENTS.md 和 docs/first-run.md 帮我搭 X 传播分工作台：
1. 复制 watchlist / board 的 example 成真实配置，只填我提供的账号和时区，不要编账号。
2. 看板发布到我自己的 GitHub Pages；示范看板只当参考，日常刷新只用我的 URL。
3. 只读扫帖：不点赞、不回复、不转发、不关注、不私信；任何对外发布都先问我、由我确认。
4. 草稿按 templates/DRAFT_RULES.md：同事实不编数字、短连字符、独立成帖、跑 drafts.py check 直到 rejected=0。
5. 中午前给我一段摘要和 PING，我自己挑 1–2 条发出去。
```

## 产出

每天一份摘要（达标帖、趋势词、TOP-10 改写草稿、若干选题），加上你自己 Pages 看板上的 X Score 和 Day Target。

## 注意事项

- 抓取依赖本机已登录的 X 会话，cookie 和密钥不要提交进 Git。
- 示范看板是作者的案例，fork 之后不会自动变成你的。
- `pipeline/drafts.py check` 会拦高重合草稿，被拒就重写，不要强行跳过。
