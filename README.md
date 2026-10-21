# Grok Bot 中文配方库 · grokguide 版

> Dato（siuser小伟）和他的 Grok Bot 一起维护：拿来就能用的配方、逐条核对过的生态清单，加上 grokguide.si 的教程索引。

中文 · [English](README.en.md) · [路线图](ROADMAP.md) · [参与贡献](CONTRIBUTING.md)

[![link-check](https://github.com/siuserxiaowei/grokbot-recipes/actions/workflows/link-check.yml/badge.svg)](https://github.com/siuserxiaowei/grokbot-recipes/actions/workflows/link-check.yml)

非官方项目。教程正文在 [grokguide.si](https://grokguide.si)。

## 一眼看完

- **17** 个配方，格式统一，提示词可以直接复制
- **91** 个生态项目和学习资源，每条都打开核对过
- **150** 篇社区教程，见 [社区教程精选](docs/community-tutorials.md)
- **104** 篇 grokguide.si 自己的教程

每条后面的小标记说明我们核对到哪一步：📘 读过内容，📦 仓库已核对。完整记录在 [data/items.json](data/items.json)。

## 怎么用

1. 新手先读 [第 0 章](https://grokguide.si/guide/ch00) 和 [第 1 章](https://grokguide.si/guide/ch01)。
2. 想马上干活，从下面挑一个配方，把提示词复制给你的 Bot。
3. 想找现成的工具和模板，看生态清单。

## 配方（17）

格式：适合谁 → 准备什么 → 步骤 → 提示词 → 产出 → 注意事项。变量用 {{占位符}}，示例都是虚构的。

| 配方 | 适合 |
|---|---|
| [注意力清单：让 Bot 从你的行动里整理重点](recipes/attention-list.md) | 手上项目多、优先级清单总过期的人 |
| [花名册和看板：多 Bot 分工不打架](recipes/bot-roster.md) | 有 3 个以上 Bot 的人 |
| [竞品雷达：只报有变化的部分](recipes/competitor-radar.md) | 需要盯竞争对手的人 |
| [研发四个角色：需求、复现、实现、审查](recipes/dev-four-roles.md) | 让 Bot 参与写代码的团队 |
| [先草稿后发送：对外动作全部过人](recipes/draft-then-send.md) | 怕 Bot 替你乱发东西的人 |
| [邮件触发整理：专属邮箱收到就处理](recipes/email-trigger.md) | 经常收固定格式邮件的人 |
| [交付验收：要能打开、能核对的文件](recipes/file-delivery.md) | 让 Bot 做表格、报告的人 |
| [会前简报：有来源、能核对](recipes/meeting-brief.md) | 经常开外部会议的人 |
| [一人三岗：调研、客服、内容](recipes/one-person-three-roles.md) | 一个人做产品的人 |
| [海外客服：多语言工单先分流](recipes/outbound-support.md) | 做海外用户的团队 |
| [额度体检：先停、分级、逐条重开](recipes/routine-budget.md) | 开了很多 Routine 的人 |
| [安全登录：不把密码直接贴给 Bot](recipes/safe-login.md) | 需要 Bot 登录网站的人 |
| [没信号不打扰：通知规则写清楚](recipes/silent-notify.md) | 开了监控类 Routine 的人 |
| [教会一次：把手动操作变成技能](recipes/teach-a-task.md) | 有一件事每周都要手动做一遍的人 |
| [作战室：几个 Bot 只靠文件交接](recipes/war-room.md) | 想让 3 到 6 个 Bot 分工的人 |
| [周报 Routine：每周五自动复盘](recipes/weekly-review.md) | 需要写周报的人 |
| [X 雷达：每天一轮，只推有用的](recipes/x-radar.md) | 做内容、做海外市场的人 |

## 生态清单（91）

### 官方与工具（8）

- [xAI 开发者文档](https://docs.x.ai) - 模型、接口和工具调用的权威说明，别处说法有冲突时以这里为准。标签：`official` `docs` 📘
- [xai-org（GitHub 组织）](https://github.com/xai-org) - xAI 自己维护的开源组织，SDK 和公开模型都从这里找。标签：`official` `sdk` 📘
- [grokbot-sdk](https://github.com/adam91holt/grokbot-sdk) - 社区写的 TypeScript 库，能读本机 Grok Bot 的名册、记忆和对话，适合想写自动化脚本的人。标签：`sdk` `typescript` 📦
- [grok-bot-cli](https://github.com/ScriptedAlchemy/grok-bot-cli) - 社区命令行工具，在终端里建 Bot、拉群、发消息、清理旧对话，批量操作很方便。标签：`cli` `automation` 📦
- [Grok Bot 模板市场](https://x.ai/bot/marketplace) - 官方模板入口，按岗位分好类，点一下就能导入，新手先逛这里。标签：`official` `templates` 📘
- [官方指南：Grok Bot 101](https://x.ai/bot/guides/grok-bot-101) - 官方作者讲 Bot 的构成、三种对话方式、共享电脑和多 Bot 串联，入门必读。标签：`official` `guide` 📘
- [官方文档：开始使用](https://docs.x.ai/grok-bot/get-started) - 从安装、登录到第一个任务的官方步骤，写请求的五个要素出自这里。标签：`official` `docs` 📘
- [Cursor 中文文档：使用 Grok Bot](https://cursor.com/cn/docs/grok-bot/work) - 官方中文版，讲 Bot、共享电脑、技能和 Routine，查功能细节时用。标签：`official` `chinese` 📘

### 模板与目录（10）

- [UseGrokBot](https://usegrokbot.com/) - 按身份整理用例和团队搭法的导航站，适合找灵感，不必从零想。标签：`directory` `cases` 📘
- [kydlikebtc/awesome-grokbot](https://github.com/kydlikebtc/awesome-grokbot) - 大量公开分享链接的索引，会定期检查链接是否还能打开，中英双语。标签：`directory` `links` 📦
- [majiayu000/awesome-grok-bot](https://github.com/majiayu000/awesome-grok-bot) - 数千个分享链接分层整理，带搜索页，想按质量挑模板可以看它。标签：`directory` `links` 📦
- [awesome-grokbot-templates](https://github.com/cs68614-hash/awesome-grokbot-templates) - 只收官方分享链接的模板目录，不搬运提示词，干净好查。标签：`directory` `templates` 📦
- [mergisi/awesome-grokbot](https://github.com/mergisi/awesome-grokbot) - 一批可以直接粘贴的人设和起步团队，适合想快速有个样子的人。标签：`profiles` `teams` 📦
- [templatesgrokbot.com](https://github.com/templatesgrokbot/templatesgrokbot.com) - 按岗位检索的大型模板库，还能通过 MCP 调用；数量多，挑的时候要自己把关。标签：`templates` `mcp` 📦
- [botdirectory.ai](https://github.com/elie222/botdirectory.ai) - 开源的 Bot 提示词目录，不只 Grok Bot 能用，适合翻着找思路。标签：`prompts` `directory` 📦
- [Useful Bots](https://usefulbots.pages.dev/) - 面向视频和内容创作者的模板合集，分类清楚。标签：`templates` `creator` 📘
- [GrokBotDev](https://github.com/ZeroPointRepo/GrokBotDev) - 由一组 Bot 自己维护的玩法目录，本身就是多 Bot 协作的活例子。标签：`directory` `multi-bot` 📦
- [GrokBot HQ](https://github.com/V-harshith/grokbothq) - 按类别列出大量 Bot，还有和其他 AI 助手的对比页。标签：`directory` `compare` 📦

### 技能与连接（16）

- [grok-bot-templates](https://github.com/cobusgreyling/grok-bot-templates) - 把模板当工程来做：有规范、有打分、有团队和 Routine 目录，写自己的模板前对照一下。标签：`templates` `spec` 📦
- [botskills](https://github.com/PramodDutta/botskills) - 每个设定都写明“哪件事必须先问你”，安全边界的写法很值得学。标签：`skills` `guardrails` 📦
- [grok-bot-jev](https://github.com/Bodila51/grok-bot-jev) - 在耗额度的大任务前加一层便宜的判断，思路省钱；依赖第三方服务。标签：`cost` `skill` 📦
- [agent-cookie-sync](https://github.com/markfulton/agent-cookie-sync) - 把本机浏览器的登录状态交给云端 Bot，不用给密码；相当于交出账号权限，只用于不敏感的账号。标签：`browser` `login` 📦
- [devspace](https://github.com/Waishnav/devspace) - 一个很小的 MCP 编程工具，让 Grok Bot 等助手能读写代码。标签：`mcp` `coding` 📦
- [Bland 电话 MCP](https://docs.bland.ai/integrations/mcp/grok-bot) - 官方接入文档，让 Bot 能打电话、发短信，打电话前务必设审批。标签：`mcp` `phone` 📘
- [grokbot-imessage-skill](https://github.com/jeffhuber/grokbot-imessage-skill) - 在 Mac 上让 Bot 读和整理 iMessage，发送前先预览；需要较高系统权限。标签：`skill` `macos` 📦
- [grok-bot-skill](https://github.com/adamanz/grok-bot-skill) - 装在编程工具里的技能，在终端就能给 Grok Bot 发消息、建新 Bot。标签：`skill` `cli` 📦
- [lauren-poteto-rules](https://github.com/unicodef1wn/lauren-poteto-rules) - 把“先看证据再下结论”这类工程习惯写成技能，适合给编程类 Bot。标签：`skill` `engineering` 📦
- [web-access](https://github.com/eze-is/web-access) - 给本机助手增强联网能力的技能，中文说明，会积累各网站的访问经验。标签：`skill` `web` 📦
- [locum](https://github.com/HarjjotSinghh/locum) - 让 Grok Bot 把写代码的活转给你本机的编程工具，只调用官方命令行。标签：`mcp` `coding` 📦
- [Grok Bot Clipper](https://github.com/RongleCat/grok-bot-clipper) - 浏览器扩展，把网页、截图、帖子收进素材篮再交给 Bot。标签：`extension` `clipper` 📦
- [remote-grok-build](https://github.com/Qervas/remote-grok-build) - 在聊天里遥控已关联电脑上的 Grok Build，适合编程用户。标签：`plugin` `grok-build` 📦
- [dev-work-grok-bot-skill](https://github.com/FelixFangX/dev-work-grok-bot-skill) - 把 Bot 配成研发助理的技能，会先问清你的仓库和工具，带审批规则。标签：`skill` `dev` 📦
- [Honcho 记忆插件](https://github.com/plastic-labs/honcho/tree/main/integrations/cursor) - 给多个 Bot 共用一份长期记忆的插件，在连接应用里搜索添加。标签：`memory` `plugin` 📦
- [grokbot-wechat（psylch）](https://github.com/psylch/grokbot-wechat) - 把微信消息桥接到 Grok Bot 的转发程序，带保活和看门狗，想自己部署的人看。标签：`wechat` `bridge` 📦

### 多 Bot 团队（16）

- [botteams](https://github.com/ellelion/botteams) - 一个文件装下一整支团队（Bot、群聊、Routine），看一次性编排怎么写。标签：`teams` `install` 📦
- [grok-bot-profiles](https://github.com/HAEGONG/grok-bot-profiles) - 需求、复现、提交、审查四个角色分开，审查的 Bot 单独对话，分工很清楚。标签：`teams` `dev` 📦
- [overnight](https://github.com/Archive228/overnight) - 六个 Bot 的视频生产线，发布前必须人审，内容号可以学它的把关方式。标签：`teams` `content` 📦
- [grokbot-gtm-team](https://github.com/timscheuerai/grokbot-gtm-team) - 作者公开的十几个销售类 Bot 和建队提示词，一次对话建好整队。标签：`teams` `gtm` 📦
- [AgentPeerChat](https://github.com/AgenticsWorks/AgentPeerChat) - 自托管的 Bot 间消息通道，能把 Grok Bot 和别的助手拉进同一个频道。标签：`self-hosted` `messaging` 📦
- [noodle](https://github.com/pdparchitect/noodle) - Mac 和 iPhone 上的多助手群聊客户端，复用已有订阅。标签：`client` `multi-agent` 📦
- [orca](https://github.com/stablyai/orca) - 管理一群编程助手的工作台，电脑和手机都能用，社区里规模较大。标签：`workspace` `fleet` 📦
- [agentrove](https://github.com/Mng-dev-ai/agentrove) - 自托管的编程工作区，把多家编程助手放在一起编排。标签：`self-hosted` `coding` 📦
- [reason-network](https://github.com/reason-machines/reason-network) - 让团队里各台电脑上的编程助手互相通话，点对点加密。标签：`network` `coding` 📦
- [模板：Chief of Operations](https://x.ai/bot/HQh9l4duDHNmhCuSW_pn-) - 管理全队规则、登记所有 Bot 和 Routine、定期做安全检查的总管模板。标签：`template` `ops` 📘
- [模板：T3 Code Bridge](https://x.ai/bot/_5NG_WsrOdQs2jtUhZeQH) - 让 Grok Bot 指挥并盯着 T3 Code 的编程任务，完成或出错会提醒。标签：`template` `coding` 📘
- [openmeld](https://github.com/amplifthq/openmeld) - 人和多个助手共享上下文、分配任务的开源协作系统。标签：`collab` `open-source` 📦
- [模板：Fleet Lead](https://x.ai/bot/mOunuXA9lKjg8sWImIzgy) - 总指挥模板：只汇报做完的事，对外动作一律等你批准。标签：`template` `lead` 📘
- [a2a-bridge](https://github.com/Rladmsrl/a2a-bridge) - 把靠网址触发的 Routine 包装成标准 A2A 服务，外部助手可以给你的 Bot 派活。标签：`a2a` `webhook` 📦
- [grokbot-desk](https://github.com/realspqrk/grokbot-desk) - 给 Bot 用的审批台，Bot 交上表格和待办，你点批准或驳回。标签：`approval` `dashboard` 📦
- [bot-team-playbook](https://github.com/doublesq97-ui/bot-team-playbook) - 一个主管 Bot 带几个专员，按 8 种身份配好整队，中文提示词能直接贴，交付靠共享文件夹加主管验收。标签：`teams` `chinese` 📦

### Routine 与监控（4）

- [模板：X Post Tracker](https://x.ai/bot/LrOzcsX5ITCY0SfXLmhJn) - 盯自己 X 帖子数据的模板，暴涨或到里程碑才提醒。标签：`template` `x` 📘
- [每周找出大号和你的互动](https://x.com/WaitWhat/status/2112086807093645796) - 英文，X 运营小 Routine · @WaitWhat · 2026-10-19。标签：`x` `routine` 📘
- [每周一给 X 帖子打分](https://x.com/MichaelGannotti/status/2112176393014440149) - 英文，复盘内容但不追点击 · @MichaelGannotti · 2026-10-19。标签：`x` `review` 📘
- [每天扫冒充账号并跟进举报](https://x.com/TeslaAIBot/status/2112683025951535280) - 英文模板，账号安全 · @TeslaAIBot · 2026-10-20。标签：`x` `security` 📘

### 一人公司与内容（5）

- [grokbot-for-gtm](https://github.com/bcharleson/grokbot-for-gtm) - 一整套海外外联获客流程，从建名单到处理回复，出海团队可以参考。标签：`gtm` `outbound` 📦
- [模板：Motion Director](https://x.ai/bot/MdpeJPD6eiY7YWUa9bfes) - 一句话出动画短片的模板，适合做产品宣传和短视频。标签：`template` `video` 📘
- [模板：Research by Trond](https://x.ai/bot/v3WI0YuJAr1DLoYdYVXh8) - 只读的研究模板，出带引用的简报，做选题前用。标签：`template` `research` 📘
- [eze-grokbot](https://github.com/eze-is/eze-grokbot) - 中文作者公开的多 Bot 配置，一个 Bot 一个文件夹；没写许可证，只参考结构。标签：`chinese` `config` 📦
- [grok-bot-wechat](https://github.com/bogao6769-netizen/grok-bot-wechat) - 用微信消息触发 Routine 的配方，回复再转回微信。标签：`wechat` `webhook` 📦

### 自托管与替代方案（12）

- [XinyunOpenBot](https://github.com/dongpen-max/XinyunOpenBot) - 面向中文用户的开源替代，默认简体中文，可接多家模型。标签：`self-hosted` `chinese` 📦
- [OpenGrokBot](https://github.com/wolfqing/OpenGrokBot) - 自托管方案，每个 Bot 一台自己的机器，模型自选。标签：`self-hosted` `byo-model` 📦
- [open-grok-bot](https://github.com/Anil-matcha/open-grok-bot) - 本地优先的工作台，动作默认拒绝、要审批并留记录。标签：`self-hosted` `approval` 📦
- [xiryn](https://github.com/SouravBeraAkaSpeed/xiryn) - 每个助手一台 Docker 桌面，可用 Telegram 遥控。标签：`self-hosted` `docker` 📦
- [DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - 基于 DeepSeek 的开源替代，多 Bot、长期记忆，中英文说明。标签：`self-hosted` `deepseek` 📦
- [lorca](https://github.com/egoist/lorca) - 单人用的加密消息应用，助手住在里面，偏个人通讯。标签：`self-hosted` `messaging` 📦
- [guilds](https://github.com/CigaleAI/guilds) - 团队形态的开源替代，项目较早期，适合关注。标签：`self-hosted` `early` 📦
- [rakazo](https://github.com/elie222/rakazo) - 开源替代，模型和沙盒都自己选，用法接近 Grok Bot。标签：`self-hosted` `byo-model` 📦
- [Codync](https://github.com/leepokai/Codync) - 把本机几十种编程助手变成可以发消息派活的 Bot。标签：`self-hosted` `coding` 📦
- [openbot（nightly-labs）](https://github.com/nightly-labs/openbot) - 本地桌面工作区，各助手有自己的任务队列，能从 Grok Bot 迁移。标签：`self-hosted` `desktop` 📦
- [OpenMausBot](https://github.com/milind-soni/OpenMausBot) - 聊天应用形态的开源替代，底层跑你本机的命令行助手。标签：`self-hosted` `chat` 📦
- [DeepSeek 开源替代的介绍](https://x.com/sitinme/status/2110975023531839754) - 中文，为什么做开源替代、怎么用 · @sitinme · 2026-10-16。标签：`self-hosted` `chinese` 📘

### 硬件（3）

- [groki-bot](https://github.com/JosssphZhou/groki-bot) - M5Stack 桌面小机器人，能用语音把任务交给 Grok Bot。标签：`hardware` `voice` 📦
- [grok-gadgets](https://github.com/adidshaft/grok-gadgets) - 把硬件接到 Grok Bot 的工具包，可以先用模拟器试。标签：`hardware` `sdk` 📦
- [把 Grok Bot 装进 ESP32](https://x.com/Liu_zhongxisn/status/2112118491239379227) - 中文，硬件小项目 · @Liu_zhongxisn · 2026-10-19。标签：`hardware` `esp32` 📘

### 学习资源与合集（17）

- [grokbot-field-notes](https://github.com/unicodef1wn/grokbot-field-notes) - 整理了官方团队直播搭产品时的规则、角色和翻车记录，新手少走弯路。标签：`notes` `rules` 📦
- [awesome-grok-bot（英文）](https://github.com/ZeroPointRepo/awesome-grok-bot) - 英文生态导航，技能、插件和 MCP 比较全。标签：`awesome` `english` 📦
- [CNR Grok Bot 指南](https://cnrcode.com/guides/) - 英文入门四篇，讲功能、Routine、省额度和模板；带一些推广。标签：`guide` `english` 📘
- [铁柱 Grok Bot 学习站](https://bot.tiezhu.si/) - 中文学习站，可以和本站对照着看。标签：`guide` `chinese` 📘
- [Grok Bot 橙皮书](https://github.com/KinGao294/grok-bot-orange-book) - 中文长篇手册，从入门到多 Bot 协作和 Routine。标签：`guide` `chinese` 📦
- [X 上 Grok Bot 文章合集（9 类）](https://x.com/0xlangeai/status/2111396742264742034) - 中文，按主题整理的必读文章 · @0xlangeai · 2026-10-17。标签：`index` `chinese` 📘
- [一位作者的系列教程合集](https://x.com/KinGao476942/status/2110689770892648953) - 中文，一个多月的教程汇总，可以整份发给 Bot 读 · @KinGao476942 · 2026-10-15。标签：`index` `chinese` 📘
- [二十个相关 GitHub 仓库](https://x.com/maestrooth/status/2105310670535184774) - 英文串帖，快速了解生态 · @maestrooth · 2026-09-30。标签：`index` `github` 📘
- [案例合集站推荐](https://x.com/cnyzgkc/status/2095500855797748032) - 中文，介绍 usegrokbot.com · @cnyzgkc · 2026-09-03。标签：`index` `chinese` 📘
- [常驻助手怎么工作（斯坦福讲座）](https://x.com/leerob/status/2108650243365736855) - 英文视频，讲常驻助手的原理和上下文工程 · @leerob · 2026-10-09。标签：`lecture` `english` 📘
- [Grok 中文文档（社区翻译）](https://grok.docs-zh.com/zh-CN/grok-bot/skills-routines-and-automations) - 社区翻译的官方文档中文版，适合对照阅读，以官方原文为准。标签：`docs` `chinese` 📘
- [Grok Bot 新手指南（fmcat）](https://bot.fmcat.top/part2/18-solo) - 中文长篇手册，案例篇讲一人公司、岗位定义和权限分级，进阶篇有飞书和微信接入。标签：`guide` `chinese` 📘
- [grokbot-usage-guide-zh](https://github.com/Spidermanbaout/grokbot-usage-guide-zh) - 中文 GitHub 教程仓库，按建 Bot、描述任务、连接应用分章。标签：`guide` `github` 📦
- [Grok-Bot-Tutorial（jobinben）](https://github.com/jobinben/Grok-Bot-Tutorial) - 中文 GitHub 教程，偏国内安装和常见用途介绍。标签：`guide` `github` 📦
- [grokbot 完整使用指南（xianyu110）](https://github.com/xianyu110/grokbot) - 中文图文教程仓库，10 分钟上手加分主题深入。标签：`guide` `github` 📦
- [从入门到精通长文（觉醒AI）](https://www.jxxy.net/ai/articles/grok-bot-mastery-guide/) - 中文长文合集页，部分内容要登录才能看。标签：`guide` `chinese` 📘
- [GrokBotGuide](https://github.com/JeffShanCha/grokbotguide) - 社区一起写的中英双语手册，从入门路线讲到 Skill、Routine 和工具实战，每篇标了来源；非官方，刚起步。标签：`chinese` `guide` 📦

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

本仓库的结构和最初的候选清单参考了 [sit-in/awesome-grokbot-playbooks](https://github.com/sit-in/awesome-grokbot-playbooks)（MIT 许可）。之后又补充了中文搜索结果里的教程。每一条我们都重新核对过，标题、短评和配方都是自己写的。

## 许可证

配方和清单采用 [MIT](LICENSE)。grokguide.si 的文章和图片、清单里链接的内容，版权归各自作者。
