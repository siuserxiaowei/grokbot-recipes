# Grok Bot 中文配方库 · grokguide 版

> Dato（siuser小伟）和他的 Grok Bot 一起维护：可以直接复制的配方，加上一份按主题整理的中文教程索引。

非官方项目。教程正文在 [grokguide.si](https://grokguide.si)，本仓库放配方和索引，方便收藏、复制和提 PR。

## 怎么用

1. 新手先读 [第 0 章](https://grokguide.si/guide/ch00) 和 [第 1 章](https://grokguide.si/guide/ch01)。
2. 想马上干活，从下面的配方挑一个，把提示词复制给你的 Bot。
3. 遇到问题查 [常见问题速查](https://grokguide.si/qa/) 和 [故障排查手册](https://grokguide.si/guide/ch13)。

## 配方（10 个）

统一格式：适合谁 → 准备什么 → 步骤 → 提示词 → 产出 → 注意事项。变量用 {{占位符}}，示例全是虚构内容。

| 配方 | 解决什么 |
|---|---|
| [额度体检：先停、分级、逐条重开](recipes/routine-budget.md) | Routine 多了额度掉得快 |
| [注意力清单：让 Bot 从你的行动里整理重点](recipes/attention-list.md) | 信息太多、优先级清单总过期 |
| [会前简报：有来源、能核对](recipes/meeting-brief.md) | 开会前来不及查背景 |
| [邮件触发整理：专属邮箱收到就处理](recipes/email-trigger.md) | 固定格式的邮件要人工归类 |
| [先草稿后发送：对外动作全部过人](recipes/draft-then-send.md) | 怕 Bot 自己发邮件、发帖 |
| [交付验收：要能打开、能核对的文件](recipes/file-delivery.md) | Bot 交回的东西打不开或对不上 |
| [安全登录：不把密码直接贴给 Bot](recipes/safe-login.md) | Bot 需要登录网站 |
| [花名册和看板：多 Bot 分工不打架](recipes/bot-roster.md) | Bot 多了不知道谁在干什么 |
| [周报 Routine：每周五自动复盘](recipes/weekly-review.md) | 每周总结总是拖 |
| [没信号不打扰：通知规则写清楚](recipes/silent-notify.md) | Bot 太吵或该通知时没通知 |

## 教程索引

### 入门教程（14 章）（16）

从账号、安装到多 Bot 协作，按顺序读

- [第 0 章 · 开始之前：Grok Bot 是什么？](https://grokguide.si/guide/ch00)
- [第 1 章 · 准备账号和套餐](https://grokguide.si/guide/ch01)
- [第 2 章 · 安装和登录](https://grokguide.si/guide/ch02)
- [第 3 章 · 认识你的第一个 Bot](https://grokguide.si/guide/ch03)
- [第 4 章 · 创建自己的专属 Bot](https://grokguide.si/guide/ch04)
- [第 5 章 · Bot 的云电脑](https://grokguide.si/guide/ch05)
- [第 6 章 · 连接你常用的应用（插件）](https://grokguide.si/guide/ch06)
- [第 7 章 · 让 Bot 定时自动干活：Skills 和 Routines](https://grokguide.si/guide/ch07)
- [第 8 章 · 给 Bot 一个专属邮箱](https://grokguide.si/guide/ch08)
- [第 9 章 · 多个 Bot 协作和 Main Bot](https://grokguide.si/guide/ch09)
- [第 10 章 · 安全第一：审批、规则和隐私](https://grokguide.si/guide/ch10)
- [第 11 章 · 省额度指南](https://grokguide.si/guide/ch11)
- [第 12 章 · 实战案例（照着做）](https://grokguide.si/guide/ch12)
- [第 13 章 · 故障排查手册](https://grokguide.si/guide/ch13)
- [第 14 章 · FAQ（从真实问题整理）](https://grokguide.si/guide/ch14)
- [全部章节](https://grokguide.si/guide/)

### 岗位实战（10）

读官方岗位指南后写的我们自己的版本

- [让 Bot 管一群编程 Agent：反馈闭环、30 分钟看板、夜间巡检和“P0 很费额度”](https://grokguide.si/playbooks/engineering-bot-fleet)
- [岗位实战：读官方指南，做自己的版本](https://grokguide.si/playbooks/)
- [法务团队用 Bot：读写分开、草稿交人，这套规矩哪些行业都能照抄](https://grokguide.si/playbooks/legal-ops-draft-then-send)
- [别维护优先级清单了：让 Bot 从你的行动里长出一张“注意力清单”](https://grokguide.si/playbooks/pm-attention-list)
- [只管一个 Bot：售后团队的“幕僚长”和八条定时任务，大多数时候不说话](https://grokguide.si/playbooks/postsales-chief-of-staff)
- [一个项目一个频道：给 Bot 团队配一张花名册和一块看板](https://grokguide.si/playbooks/project-channels-roster)
- [面试前、面试后、夜间寻访：招聘团队的四个小 Bot 怎么分工](https://grokguide.si/playbooks/recruiting-four-bots)
- [跨境卖家：让 Grok Bot 看 Shopify 订单和库存](https://grokguide.si/playbooks/shopify-store-ops)
- [客服队列交给 Bot：五件事怎么分，退款为什么必须等你点头](https://grokguide.si/playbooks/support-five-jobs)
- [每天只看一个 Bot：收件、日历、情报三个先“只读”，再交给总管](https://grokguide.si/playbooks/work-four-bots)

### 实操教程（8）

一件事一篇，照着做

- [收到邮件就整理：专属邮箱触发 Routine](https://grokguide.si/tutorials/email-trigger-routine)
- [让 Bot 交回能打开、能核对的文件](https://grokguide.si/tutorials/file-delivery)
- [Grok Bot 实操教程](https://grokguide.si/tutorials/)
- [做一份有来源的会前简报](https://grokguide.si/tutorials/meeting-brief)
- [Bot 做完了却没通知：六步排查](https://grokguide.si/tutorials/notification-checklist)
- [这个插件能干什么？先读官方仓库里的说明书](https://grokguide.si/tutorials/read-plugin-readme)
- [从模板安装到第一次验收](https://grokguide.si/tutorials/template-first-run)
- [用语音和键盘给 Grok Bot 交任务](https://grokguide.si/tutorials/voice-and-keyboard)

### 常见问题速查（14）

一个问题一页

- [Grok Bot 的审批卡片是什么？Allow once 和 Always allow 有什么区别？](https://grokguide.si/qa/approval-card)
- [Grok Bot 不回复、卡住不动怎么办？](https://grokguide.si/qa/bot-not-responding)
- [Grok Bot 专属邮箱怎么领取？](https://grokguide.si/qa/claim-email)
- [Grok Bot 云电脑卡住、连不上怎么办？](https://grokguide.si/qa/computer-stuck)
- [Grok Bot 怎么连接 Gmail？](https://grokguide.si/qa/connect-gmail)
- [Grok Bot 怎么新建一个自己的 Bot？](https://grokguide.si/qa/create-bot)
- [多个 Grok Bot 怎么建群聊协作？](https://grokguide.si/qa/group-chat)
- [Grok Bot 常见问题速查](https://grokguide.si/qa/)
- [Grok Bot 要登录网站，密码怎么给它才安全？](https://grokguide.si/qa/password-safety)
- [Grok Bot 怎么收费？额度用完了怎么办？](https://grokguide.si/qa/pricing-quota)
- [聊天正常、云电脑连不上：要放行哪些域名](https://grokguide.si/qa/proxy-network)
- [Grok Bot 的 Routine（定时任务）怎么设置？](https://grokguide.si/qa/set-routine)
- [在 X 上 @bot 不回复怎么办？](https://grokguide.si/qa/tag-bot-on-x)
- [怎么教 Grok Bot 一个技能（Skill）？](https://grokguide.si/qa/teach-skill)

### 专题文章（15）

选套餐、选模型、MCP、排查

- [让 Grok Bot 替你买东西：先看金额卡片，再决定付不付](https://grokguide.si/topics/bot-purchases)
- [让 Bot 开一个 Project：和单个 Cloud Agent 有什么不同](https://grokguide.si/topics/bot-start-project)
- [国内能用 Grok Bot 吗？](https://grokguide.si/topics/china-access)
- [让 Grok Bot 派 Cloud Agent 写代码，并指定模型](https://grokguide.si/topics/cloud-agent-model)
- [Grok Bot 怎么接自定义 MCP？](https://grokguide.si/topics/custom-mcp)
- [专题文章总览](https://grokguide.si/topics/)
- [SuperGrok / X Premium+ 绑错账号怎么办？](https://grokguide.si/topics/link-wrong-account)
- [本地 AI 助手和 Grok Bot 互相发消息](https://grokguide.si/topics/local-agent-bridge)
- [Grok Bot 的记忆放在哪](https://grokguide.si/topics/memory)
- [怎么让 Grok Bot 路由到 Opus 5.5？](https://grokguide.si/topics/route-to-opus-55)
- [Routine 不运行？6 步排查](https://grokguide.si/topics/routine-not-running)
- [Grok Bot vs ChatGPT Work vs Claude Cowork](https://grokguide.si/topics/vs-chatgpt-claude)
- [Grok Bot 是什么？和 Grok 聊天有什么区别](https://grokguide.si/topics/what-is-grok-bot)
- [Grok Bot 用的是什么模型？](https://grokguide.si/topics/which-model)
- [Grok Bot 套餐怎么选？](https://grokguide.si/topics/which-plan)

### 推荐 Bot 模板（10）

改进过的可导入模板

- [赛博小晚（改进版）](https://grokguide.si/bots/cyber-xiao-wan)
- [飞书应用管家（改进版）](https://grokguide.si/bots/feishu-app-manager)
- [推荐 Bot 模板](https://grokguide.si/bots/)
- [记账管家（改进版）](https://grokguide.si/bots/ledger)
- [Maples 造型师（改进版）](https://grokguide.si/bots/maples)
- [记忆管家（改进版）](https://grokguide.si/bots/memory-keeper)
- [Muse 管家（改进版）](https://grokguide.si/bots/muse-steward)
- [额度省省助手（改进版）](https://grokguide.si/bots/quota-saver)
- [微信文章捕手（改进版）](https://grokguide.si/bots/wechat-article-catcher)
- [X 调度员（改进版）](https://grokguide.si/bots/x-dispatcher)

### 账号与账单（18）

登录、订阅、退款、额度开关

- [苹果、安卓内购的订阅怎么处理？](https://grokguide.si/account/app-store-google-play)
- [Grok Bot / X 订阅怎么取消？](https://grokguide.si/account/cancel)
- [不用了怎么彻底删除](https://grokguide.si/account/delete-account)
- [谁能合并账号、转 X 订阅？](https://grokguide.si/account/eligibility)
- [团队版与企业部署](https://grokguide.si/account/enterprise-deploy)
- [Grok Bot 额度用完了怎么办？4 个开关讲清楚](https://grokguide.si/account/extra-usage)
- [给 Grok Bot 发文件：格式、数量、大小，和怎么要结果](https://grokguide.si/account/files-attachments)
- [Grok Bot 账号与账单](https://grokguide.si/account/)
- [Grok Bot 手机版：下载、要求、能做什么](https://grokguide.si/account/mobile-app)
- [Grok Bot / X 订阅支持哪些付款方式？](https://grokguide.si/account/payment-methods)
- [Grok Bot 退款规则：退多少、退到哪、多久到账](https://grokguide.si/account/refund)
- [Grok Bot 登录不上怎么办？](https://grokguide.si/account/sign-in)
- [自动充值怎么关、月度上限怎么设、用量在哪看](https://grokguide.si/account/spending-cap-auto-topup)
- [Team Bot：全队共用一个 Bot](https://grokguide.si/account/team-bots)
- [Grok Bot 团队套餐怎么用？](https://grokguide.si/account/team-plans)
- [合并账号后 Grok Bot 数据去哪了？](https://grokguide.si/account/unify-bot-data)
- [套餐升级、降级什么时候生效？](https://grokguide.si/account/upgrade-downgrade)
- [X Premium / Premium+ 用户转 X 订阅](https://grokguide.si/account/x-premium)

### Grok Build（8）

编码命令行的安装、权限和排错

- [Grok Build 和 Codex、Cursor、Gemini CLI 怎么选？我们没做评测，先做了一份“可验证对照表”](https://grokguide.si/grok-build/compare-agents)
- [Grok Build 实战总览：它是什么、怎么装、哪里会踩坑](https://grokguide.si/grok-build/)
- [Grok Build 安装第一步：先读安装脚本，再装，再看没登录能干什么](https://grokguide.si/grok-build/install-first-run)
- [让 Grok Build 无人值守之前：权限模式、deny 规则和一个体检脚本](https://grokguide.si/grok-build/permissions-sandbox)
- [Grok Build 提示词和工作流：写好 /goal，用对 plan，别误会几个命令](https://grokguide.si/grok-build/prompts-workflows)
- [Grok Build 用多少额度、哪个套餐能用：2026-10 的官方说法，以及旧教程为什么不能照抄](https://grokguide.si/grok-build/quota-subscription)
- [Grok Build 常见问题排错：九个我们遇到或在文档里读到的坑](https://grokguide.si/grok-build/troubleshooting)
- [规则、技能、权限都没生效？先看这个目录被信任了没有](https://grokguide.si/grok-build/trust-folder-pitfall)

### 工具与附录（5）

- [Grok Bot Routine 定时任务指令生成器](https://grokguide.si/tools/routine-builder)
- [附录 B · 术语中英对照](https://grokguide.si/appendix/glossary)
- [附录 A · 官方资源导航](https://grokguide.si/appendix/resources)
- [附录 C · 版本说明](https://grokguide.si/appendix/version)
- [D · 实战教程：从零搭建你的 Bot 团队](https://grokguide.si/appendix/video-grok-bot-101)

## 参与贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。不收任何密钥、密码、cookie、经营数字和个人隐私信息。

## 致谢

结构上受 [sit-in/awesome-grokbot-playbooks](https://github.com/sit-in/awesome-grokbot-playbooks)（MIT）启发。本仓库文字和配方均为原创，没有复制其内容。

## 许可证

配方和索引采用 [MIT](LICENSE)。grokguide.si 上的文章和图片版权归原作者。
