# Grok Bot 中文配方库 · grokguide 版

> Dato（siuser小伟）和他的 Grok Bot 一起维护：拿来就能用的配方、逐条核对过的生态清单，加上 grokguide.si 的教程索引。

中文 · [English](README.en.md) · [路线图](ROADMAP.md) · [参与贡献](CONTRIBUTING.md)

[![link-check](https://github.com/siuserxiaowei/grokbot-recipes/actions/workflows/link-check.yml/badge.svg)](https://github.com/siuserxiaowei/grokbot-recipes/actions/workflows/link-check.yml)

非官方项目。教程正文在 [grokguide.si](https://grokguide.si)。

## 一眼看完

- **43** 个配方，格式统一，提示词可以直接复制
- **158** 个生态项目和学习资源，每条都打开核对过
- **308** 篇社区教程，见 [社区教程精选](docs/community-tutorials.md)
- **90** 个官方模板市场模板的中文教程，见 [模板市场教程](docs/marketplace-templates.md)
- **149** 篇 grokguide.si 自己的教程

每条后面的小标记说明我们核对到哪一步：📘 读过内容，📦 仓库已核对。完整记录在 [data/items.json](data/items.json)。

## 怎么用

1. 新手先读 [第 0 章](https://grokguide.si/guide/ch00) 和 [第 1 章](https://grokguide.si/guide/ch01)。
2. 想马上干活，从下面挑一个配方，把提示词复制给你的 Bot。
3. 想找现成的工具和模板，看生态清单。

## 配方（43）

格式：适合谁 → 准备什么 → 步骤 → 提示词 → 产出 → 注意事项。变量用 {{占位符}}，示例都是虚构的。

| 配方 | 适合 |
|---|---|
| [批准后定时发帖：一次性 Routine 查重再发](recipes/approved-post.md) | 想让 Bot 定时发帖，又怕它发重复、日期写错、数字没出处的人 |
| [注意力清单：让 Bot 从你的行动里整理重点](recipes/attention-list.md) | 手上项目多、优先级清单总过期的人 |
| [多 Bot 共用规则底座：一个入口、一个写入者](recipes/bot-harness.md) | 同时用好几个 Bot、规则老对不上或者共享文件被互相覆盖的人 |
| [花名册和看板：多 Bot 分工不打架](recipes/bot-roster.md) | 有 3 个以上 Bot 的人 |
| [云电脑自愈：重置后把 Tailscale 和常用状态装回来](recipes/box-heal.md) | 云电脑常被平台重置、换机或休眠，想让 Tailscale、软件包基线和 gh 登录态自动回来，又不想让脚本代你登录的人 |
| [先查来源：会变的事不只信记忆](recipes/check-source-first.md) | Bot 记住的日期、邮箱、订单状态过期了还在照着用的人 |
| [竞品雷达：只报有变化的部分](recipes/competitor-radar.md) | 需要盯竞争对手的人 |
| [研发四个角色：需求、复现、实现、审查](recipes/dev-four-roles.md) | 让 Bot 参与写代码的团队 |
| [先草稿后发送：对外动作全部过人](recipes/draft-then-send.md) | 怕 Bot 替你乱发东西的人 |
| [邮件触发整理：专属邮箱收到就处理](recipes/email-trigger.md) | 经常收固定格式邮件的人 |
| [.env 只比键名：从不打印值](recipes/env-key-diff.md) | 换机器或拉新仓库时总漏配环境变量、又怕密钥进聊天的人 |
| [交付验收：要能打开、能核对的文件](recipes/file-delivery.md) | 让 Bot 做表格、报告的人 |
| [总控派活：一张路由表，重活交给工程师 Bot](recipes/fleet-router.md) | 已经有三五个 Bot、每次都要想“这事该找谁”的人 |
| [两个文件夹快照对比](recipes/folder-snapshot-diff.md) | 备份盘、导出目录、前后版本对不上的人 |
| [免费游戏侦察：只认官方商店](recipes/free-games-scout.md) | 想领限时免费游戏、又不想被转发消息和 Demo 刷屏的人 |
| [推一个任务文件，GitHub Action 叫醒 Bot](recipes/github-webhook.md) | 本地有 Agent 写任务说明、想让 Grok Bot 自动接活的开发者 |
| [群里底牌走私聊通道](recipes/group-private-lane.md) | 多 Bot 群聊里要藏报价、密钥、客户底牌的人 |
| [隐藏前先停表：隐藏不等于暂停](recipes/hide-not-pause.md) | 暂时不想看见某个 Bot、却发现额度还在掉的人 |
| [实跑结果打成离线 HTML 报告](recipes/html-report-pack.md) | 要把多段终端输出交给同事、又不好塞一堆散文件的人 |
| [Linux 新版提醒](recipes/linux-update-watch.md) | 在 Linux 上用 Grok Bot、内置更新管不到的人 |
| [邮件附件归类：只复制不删](recipes/mail-attach-sort.md) | 邮箱附件堆成山、发票合同混在一起的人 |
| [主 Bot 只挂两条 Routine：专项点名才干](recipes/main-bot-slim.md) | 主 Bot 越挂越胖、额度被定时任务吃光的人 |
| [会前简报：有来源、能核对](recipes/meeting-brief.md) | 经常开外部会议的人 |
| [消息热力图：看清最常找哪个 Bot](recipes/msg-heatmap.md) | 开了好几个 Bot、想知道哪些常用、哪些建完就闲着的人 |
| [一人三岗：调研、客服、内容](recipes/one-person-three-roles.md) | 一个人做产品的人 |
| [海外客服：多语言工单先分流](recipes/outbound-support.md) | 做海外用户的团队 |
| [技能钉版本：装之前先对 sha256](recipes/pinned-skills.md) | 想装别人写的技能，又怕作者以后改了内容、或者中途被人动了手脚的人 |
| [安静检查：没变化只打一行 quiet](recipes/quiet-check.md) | 巡检 Routine 多数时候没变化、却老刷屏的人 |
| [额度体检：先停、分级、逐条重开](recipes/routine-budget.md) | 开了很多 Routine 的人 |
| [安全登录：不把密码直接贴给 Bot](recipes/safe-login.md) | 需要 Bot 登录网站的人 |
| [网页截图按日期归档](recipes/screenshot-archive.md) | 要盯公开页有没有改、又不要登录爬站的人 |
| [脚本先跑：固定的活交给脚本，Bot 只看一行结果](recipes/script-first.md) | Routine 每天巡检页面或清单，没变化也要一页页看、额度掉得快的人 |
| [没信号不打扰：通知规则写清楚](recipes/silent-notify.md) | 开了监控类 Routine 的人 |
| [教会一次：把手动操作变成技能](recipes/teach-a-task.md) | 有一件事每周都要手动做一遍的人 |
| [多 Bot 交接看板](recipes/team-monitor.md) | 手上有两个以上 Bot、想知道活卡在谁那里的人 |
| [待办提醒：没做完就再提醒](recipes/todo-nag.md) | 清单 App 一过截止就不管了、事情总被忘掉的人 |
| [完成前验证闸门：不过禁止标 done](recipes/verify-gate.md) | Bot 常说「好了」却缺文件、数字对不上的人 |
| [作战室：几个 Bot 只靠文件交接](recipes/war-room.md) | 想让 3 到 6 个 Bot 分工的人 |
| [一周晚饭：周六排好，过敏当硬规则](recipes/weekly-dinner.md) | 每周都在愁吃什么、家里有人过敏或挑食、想把买菜清单也一起省掉的人 |
| [每周功能对照：让首席 Bot 对照更新日志改你的 Routine](recipes/weekly-feature-check.md) | 已经开了一批 Routine、怕绕路和额度浪费、想跟着官方新功能收紧流程的人 |
| [周报 Routine：每周五自动复盘](recipes/weekly-review.md) | 需要写周报的人 |
| [X 雷达：每天一轮，只推有用的](recipes/x-radar.md) | 做内容、做海外市场的人 |
| [X 传播分工作台：只读扫帖，你自己点发布](recipes/x-virality-score.md) | 在 X 上发内容、想盯一批账号的爆款与趋势词、又不想让 Bot 代发的人 |

## 生态清单（158）

### 官方与工具（18）

- [xAI 开发者文档](https://docs.x.ai) - 模型、接口和工具调用的权威说明，别处说法有冲突时以这里为准。标签：`official` `docs` 📘
- [xai-org（GitHub 组织）](https://github.com/xai-org) - xAI 自己维护的开源组织，SDK 和公开模型都从这里找。标签：`official` `sdk` 📘
- [grokbot-sdk](https://github.com/adam91holt/grokbot-sdk) - 社区写的 TypeScript 库，能读本机 Grok Bot 的名册、记忆和对话，适合想写自动化脚本的人。标签：`sdk` `typescript` 📦
- [grok-bot-cli](https://github.com/ScriptedAlchemy/grok-bot-cli) - 社区命令行工具，在终端里建 Bot、拉群、发消息、清理旧对话，批量操作很方便。标签：`cli` `automation` 📦
- [Grok Bot 模板市场](https://x.ai/bot/marketplace) - 官方模板入口，按岗位分好类，点一下就能导入，新手先逛这里。标签：`official` `templates` 📘
- [官方指南：Grok Bot 101](https://x.ai/bot/guides/grok-bot-101) - 官方作者讲 Bot 的构成、三种对话方式、共享电脑和多 Bot 串联，入门必读。标签：`official` `guide` 📘
- [官方文档：开始使用](https://docs.x.ai/grok-bot/get-started) - 从安装、登录到第一个任务的官方步骤，写请求的五个要素出自这里。标签：`official` `docs` 📘
- [Cursor 中文文档：使用 Grok Bot](https://cursor.com/cn/docs/grok-bot/work) - 官方中文版，讲 Bot、共享电脑、技能和 Routine，查功能细节时用。标签：`official` `chinese` 📘
- [grokbot-linux-port](https://github.com/Nichokas/grokbot-linux-port) - 非官方 Linux 打包，把官方 .deb 原样重打成 Arch、Fedora 和通用压缩包，每天跟版本；Ubuntu、Debian 用户直接装官方包更稳妥。标签：`linux` `packaging` 📦
- [TetherBot](https://github.com/GrokkingGrok/TetherBot) - GNOME 桌面上的 Grok Bot 客户端，作者自己标了早期预览版，Linux 用户可以先装来玩，别指望稳定。标签：`linux` `gnome` `desktop` 📦
- [android-grok-home](https://github.com/drumpat01/android-grok-home) - 把 Grok Bot 做成 Android 桌面启动器的实验项目，基于官方 BDK，喜欢折腾手机的人可以看看。标签：`android` `launcher` `bdk` 📦
- [grokbot-widget](https://github.com/imranbarbhuiya/grokbot-widget) - macOS 悬浮小窗，随时呼出 Bot；安装包没做公证，第一次打开要自己在系统设置里放行。标签：`macos` `widget` 📦
- [grok-rpm（Fedora/RHEL 的 dnf 仓库）](https://github.com/addidotlol/grok-rpm) - 把官方 deb 转成 rpm 做成 dnf 仓库，我们拆包看过依赖和文件；非官方、没有签名，装前和官方版本号对一下。标签：`linux` `fedora` `unofficial` 📦
- [grok-bot-bin（Arch 包）](https://github.com/gallez-tech/grok-bot-bin) - 每天跟官方更新接口重新打 Arch 包，作者提醒先下载再 pacman -U；非官方，没有签名文件。标签：`linux` `arch` `unofficial` 📘
- [omarchy-grok-bot：Omarchy 状态栏上看 Bot 在忙什么](https://github.com/hmarquez-solutions/omarchy-grok-bot) - 给 Omarchy（Arch 系 Linux 桌面）状态栏加一张小脸，Bot 空闲、干活、有未读、等你批准时表情各不同，点开面板能看每个 Bot 的最后一句话；作者标明非官方。标签：`linux` `statusbar` `community` 📘
- [GrokBotChineseFix：Windows 上打不出中文逗号的小补丁](https://github.com/thinkingpower-labs/GrokBotChineseFix) - Grok Bot 在前台时把 Ctrl+逗号换成全角逗号，离线运行、只管这一个按键；Windows 中文输入受这个快捷键困扰的可以装。标签：`windows` `chinese` `input` 📘
- [QuotaPot](https://github.com/Caffrey-Li/QuotaPot) - Mac/Windows 常驻小窗口，盯 Cursor、Claude、Codex、Grok Bot 等用量、对话上下文和磁盘占用，可一键复制整理提示词。标签：`desktop` `quota` `macos` `windows` 📘
- [botter：非官方 Node.js SDK 与 CLI](https://github.com/jethros-projects/botter) - 用类型化接口给 Grok Bot 派活、跟读对话，也能做桌面客户端；走的是非公开接口，随时可能失效，Node 要打过 10 月安全补丁。标签：`sdk` `cli` `unofficial` 📦

### 模板与目录（16）

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
- [Personal Chef](https://github.com/anselmcmakin/personal-chef) - 家庭一周晚饭模板，过敏连「可能含有」都当硬规则、预算超了自己改方案，购物车只装不结账，技能说明写得很细，值得照着改成自己的版本。标签：`template` `meal-plan` `routine` `shopping` 📘
- [Follow-Through：家里周期性的事，记一份账](https://github.com/jeffgreendesign/follow-through) - 生日、每周晚饭、补货这类会回来的事一份记录；没你的话不标完成，断了几天只问一句不刷屏，默认不建 Routine、只和你说话。标签：`template` `household` `chat-only` 📘
- [Firstmate：多 Bot 团队的领队模板](https://x.ai/bot/__4FfrkUdvpdMk6-LKg5r) - 官方模板页可直接添加，思路是一个领队 Bot 对接你、再分派给其他成员；作者的思路长文我们已收在多 Bot 团队教程里，装前看清会建几个 Bot。标签：`template` `team` `lead` 📘
- [grok-bot-templates（ChamathRosh）：小商家用的六个草稿模板](https://github.com/ChamathRosh/grok-bot-templates) - 六个面向小店的模板，产出都只停在草稿、要你确认才发；目前只有排期那个带一键安装，README 里推广链接较多，挑模板本身看就行。标签：`template` `small-business` `draft` 📘
- [灵境 Lingverse：中文写手系列（墨灵）](https://github.com/lingverse-ai/lingverse) - 可一键导入的中文 Bot 系列，第一位「墨灵」专写长文并把同一素材改成多平台版本；内容 CC BY 4.0、代码 MIT。标签：`template` `writing` `chinese` 📘
- [grok-starter-kit：Grok Bot + Claude Code 起步套件](https://github.com/qubicsdata/grok-starter-kit) - 按 AGENTS.md 分阶段接入：第一阶段只读盘点现有配置，没你同意不覆盖；带第二大脑、技能和晨报 Routine。标签：`starter` `claude-code` `routine` 📘

### 技能与连接（36）

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
- [wingman](https://github.com/juangurdian/wingman) - 本机 MCP 桥，让云端 Bot 接管你电脑上已经开着的 Codex 或 Claude Code 会话；和 locum 派新活不同，它是接旧会话，隧道和令牌要管好。标签：`mcp` `bridge` 📦
- [Tune-Up](https://github.com/Viaknox/tune-up) - 专门给其他 Bot 做体检的 Bot，找出跑偏和白耗额度的地方，改动由你批准；会读你其他 Bot 的设定，商业品牌项目。标签：`audit` `skill` 📦
- [grokbot-cli](https://github.com/Nuncio-hq/grokbot-cli) - 在终端或本机编程助手里给 Bot 派活、等回复、处理审批卡，Bot 也能把活留给你本机的助手；非官方，借桌面端登录调未公开接口，只支持 Mac，删改类命令先拿测试 Bot 试。标签：`cli` `mcp` 📦
- [gb2gpt](https://github.com/EdmundLimBoEn/gb2gpt) - 在 ChatGPT 对话里给自己的 Bot 团队派活，自己架一个小服务当中转；要 ChatGPT 付费版的开发者模式和公网 HTTPS 地址，许可不允许商用。标签：`chatgpt` `mcp` 📦
- [Send to Grok Bot](https://github.com/jamespendry/send-to-grok-bot) - 给 x.com 每条帖子加个发送按钮，一键交给你的 Bot，iPhone 走分享菜单；扩展还没上架商店要手动加载，手机路线经作者的中转服务。标签：`chrome-extension` `x` 📦
- [ISR Bot（原 Watchtower）](https://github.com/ken-aisec/grokbot-isr-bot) - 给共用一台云电脑的 Bot 们配一个安全官：装模板前先审、打安全分、放诱饵文件、出周报；默认只读，改动要你点头；仓库已从 Watchtower 更名为 ISR Bot。标签：`security` `audit` 📦
- [grok-bot-local-first](https://github.com/MarkusIsaksson1982/grok-bot-local-first) - 英文技能包，把巡检、比对这类固定步骤交给本机 Python 小脚本，脚本最后只吐一行 JSON，Bot 只在要判断时出手；另有启用和运维说明，付费版是可选项。标签：`skill` `quota` 📦
- [grok-bot-mcp](https://github.com/cherwinyu/grok-bot-mcp) - Windows 上的 MCP 服务，让 Bot 把编程活交给本机代理，最后用 git diff 验收，改动看得见。标签：`mcp` `windows` `coding` 📦
- [grokbot-skills](https://github.com/dallintwatts/grokbot-skills) - 一组技能附带 sha256 清单，装之前先对哈希，被改过就不装；我们照着写了一篇钉版本教程。标签：`skills` `sha256` `security` 📦
- [broom](https://github.com/onlymehdi/broom) - 只靠技能说明清理 Gmail 垃圾信，只挪进回收站、不点退订，银行和订单邮件默认不碰，刚建的仓库，先拿小范围试。标签：`gmail` `skills` `inbox` 📦
- [grok-x-bridge-example](https://github.com/bytec-ai/grok-x-bridge-example) - 中文示例：编程智能体经 Worker 和 D1 唤醒 Grok Bot 去搜 X，再把结果回调回来，想让别的工具借 Bot 的 X 搜索可以参考；没写许可证，只当示例读。标签：`webhook` `cloudflare` `x-search` `chinese` 📘
- [grokbot-telegram-bridge](https://github.com/ssamssae/grokbot-telegram-bridge) - 用自己的 Telegram 机器人和某个 Bot 来回对话，只走 Routine 的 webhook 和本机文件，不碰屏幕自动化；需要一台 Mac，非官方。标签：`telegram` `webhook` `bridge` 📘
- [grok-bot-agents：把重活转给云电脑上的 Claude Code / Codex](https://github.com/AgwaB/grok-bot-agents) - 技能插件加一个小控制器，Bot 自己做轻活、重活交给云电脑里的命令行代理跑完回报；要导入你本机的登录和密钥，每一份都要你点头，想清楚再给。标签：`plugin` `delegate` `cli` 📘
- [my-bot-scripts：一位社区用户的脚本工具箱](https://github.com/wustep/my-bot-scripts) - 每个文件夹一件事：消息热力图、两个账号间加密中继、短信转给不同 Bot 等，都带写给 Bot 看的 SKILL.md；我们在云电脑上跑通了其中的 msg-graph。标签：`skill` `scripts` `stats` 📦
- [claude-grok-bridge：让 Claude Code 把活交给 Grok Bot](https://github.com/francoCosimo95/claude-grok-bridge) - 借 Routine 的调用地址让 Claude Code 给 Bot 派任务、取结果，一行引导就能接上，没有额外依赖；调用地址等于钥匙，别贴进公开仓库。标签：`claude-code` `routine` `bridge` 📘
- [gbb-multica-bridge：把 Bot 接进 Multica（中文说明）](https://github.com/lthero-big/gbb-multica-bridge) - 中文 README，用 gbb 把 Bot 接到 Multica 的运行环境，本机或 SSH 回传都行，还附了恢复脚本；适合已经在用 Multica 的人。标签：`multica` `bridge` `chinese` 📘
- [imessage-relay：用自己的 Mac 把 iMessage 转到 X Chat](https://github.com/PhillipHolland/imessage-relay) - 在你自己的 Mac 上中转 iMessage 和 X Chat，需要再开一个 X 账号；默认只演练不真发，只读本机消息库，安装包带校验值，先演练确认再开。标签：`imessage` `mac` `relay` 📘
- [Holdt：iCloud 日历 MCP](https://github.com/holdtapp/holdt) - 部署在你自己的 Cloudflare 上，让 Bot 读写 iCloud 日历；每次改动先出预览再问你，需要 Apple 专用密码。标签：`mcp` `calendar` `icloud` 📦
- [grokbot-box-heal：云电脑自愈套件](https://github.com/heyalchang/grokbot-box-heal) - 平台重置或休眠后把 Tailscale、软件包基线与 gh 登录态装回；从不代登录、从不下载 Tailscale 二进制，离线包和首次登录要你自己放。标签：`cloud-computer` `tailscale` `recovery` 📘
- [Grok Bridge（niharnm）：多工具任务交接 CLI](https://github.com/niharnm/grok-bridge) - 一个命令行在 Grok Bot 与 Codex、Claude Code、Cursor 等之间双向交接任务；作者自标实验性 alpha，反向调用要你批准本机命令。标签：`bridge` `cli` `multi-agent` 📦

### 多 Bot 团队（23）

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
- [grokbot-executive-team](https://github.com/meir-bot/grokbot-executive-team) - 一套“高管团队”多 Bot 模板，CEO、CFO 等角色分工写好了，适合想照抄分工表的人。标签：`multi-bot` `template` 📦
- [grokbot-delivery-team](https://github.com/puzzle-app/grokbot-delivery-team) - 13 个 Bot 组成的咨询交付团队模板，角色和交接写得细；仓库来自一家做财务软件的公司，带点自家产品。标签：`multi-bot` `template` `consulting` 📦
- [Bot 监控室：多 Bot 交接画成一间小办公室](https://github.com/Olivia295/grokbot-team-monitor-UI) - 本机只读看板，把 Bot 之间谁交给谁、卡在哪画出来，有中文界面和演示模式，也能吃自己写的事件日志；我们在云电脑上跑过演示和日志模式。标签：`monitor` `team` `dashboard` `chinese` 📦
- [yobiru：让不同电脑上的 agent 互相发消息](https://github.com/chekusu/yobiru) - 借 Tailscale 组网，自己的几个 agent 之间能互发消息，也能用链接加朋友的 agent，新版起端到端加密；要装本机服务，先读清权限再接。标签：`team` `messaging` `tailscale` 📘
- [groknet：让不同人的 Bot 互加好友](https://github.com/sudoTomas/groknet) - 通过 MCP 加好友，再用一个接收消息的 Routine 收件；服务托管在作者的服务器上，接收地址的钥匙会交给对方服务，介意的话别接。标签：`team` `mcp` `webhook` 📘
- [dark-factory](https://github.com/ELU-Labs/dark-factory) - 一段提示词让多个 Grok Bot 按工厂流水线改仓库，配合 ELU 做真实用户验证；需要分支保护和预览部署。标签：`multi-bot` `factory` `verification` `prompt` 📘
- [Grok Bot OS：个人舰队起步包](https://github.com/skorten/grokbot-os) - 一个总管当前台、其余 Bot 一岗一事，私人 Notion 只许一个 Bot 写，凡是要发出去的都要你批准。标签：`multi-bot` `notion` `starter` 📘

### Routine 与监控（8）

- [模板：X Post Tracker](https://x.ai/bot/LrOzcsX5ITCY0SfXLmhJn) - 盯自己 X 帖子数据的模板，暴涨或到里程碑才提醒。标签：`template` `x` 📘
- [每周找出大号和你的互动](https://x.com/WaitWhat/status/2112086807093645796) - 英文，X 运营小 Routine · @WaitWhat · 2026-10-19。标签：`x` `routine` 📘
- [每周一给 X 帖子打分](https://x.com/MichaelGannotti/status/2112176393014440149) - 英文，复盘内容但不追点击 · @MichaelGannotti · 2026-10-19。标签：`x` `review` 📘
- [每天扫冒充账号并跟进举报](https://x.com/TeslaAIBot/status/2112683025951535280) - 英文模板，账号安全 · @TeslaAIBot · 2026-10-20。标签：`x` `security` 📘
- [grokbot-quota-ring](https://github.com/SvenKunkka/grokbot-quota-ring) - Mac 菜单栏里的小饼图，看本周额度还剩多少；要交出网站登录 cookie、走未公开接口，介意就手填数字。标签：`quota` `macos` 📦
- [GrokGauge](https://github.com/stevencombs/GrokGauge) - Mac 菜单栏额度环，把 SuperGrok 每周总额度拆成 Grok、Bot、Cursor 各占多少；非官方、读未公开数据，安装脚本会去掉隔离标记，介意就手动装。标签：`quota` `macos` 📦
- [Desk：本地项目看板，留言直达 Bot](https://github.com/TeebooTed/desk) - 单文件本地看板按项目排进度，留言框经本机中转发到 Bot 的 Webhook Routine；一键安装脚本会装开机自启，先克隆下来看一遍再跑。标签：`dashboard` `webhook` `routine` 📘
- [GrugBot Console：Routine 总控台](https://github.com/devprecated/grokbot-management-console) - 一页看所有 Bot 的 Routine 与每次运行，可暂停、改时间、改提示词，出事一键全停；Next.js + Postgres 自托管，部署前看清它读哪些日志。标签：`routine` `dashboard` `self-hosted` 📦

### 一人公司与内容（7）

- [grokbot-for-gtm](https://github.com/bcharleson/grokbot-for-gtm) - 一整套海外外联获客流程，从建名单到处理回复，出海团队可以参考。标签：`gtm` `outbound` 📦
- [模板：Motion Director](https://x.ai/bot/MdpeJPD6eiY7YWUa9bfes) - 一句话出动画短片的模板，适合做产品宣传和短视频。标签：`template` `video` 📘
- [模板：Research by Trond](https://x.ai/bot/v3WI0YuJAr1DLoYdYVXh8) - 只读的研究模板，出带引用的简报，做选题前用。标签：`template` `research` 📘
- [eze-grokbot](https://github.com/eze-is/eze-grokbot) - 中文作者公开的多 Bot 配置，一个 Bot 一个文件夹；没写许可证，只参考结构。标签：`chinese` `config` 📦
- [grok-bot-wechat](https://github.com/bogao6769-netizen/grok-bot-wechat) - 用微信消息触发 Routine 的配方，回复再转回微信。标签：`wechat` `webhook` 📦
- [The Daily Diff（Bot 编的个人报纸）](https://github.com/indrayam/samachar) - 一个由 Bot 每天挑论文和帖子、生成静态报纸的真实站点，想做个人信息日报可以看它的文件分工。标签：`newsletter` `static-site` `example` 📘
- [x-virality-score](https://github.com/monkeyteamvip/x-virality-score) - 只读扫关注列表与趋势词，起草帖子并刷新你自己的 GitHub Pages 看板；发布仍由你点，示范看板只是别人的例子。标签：`x` `dashboard` `routine` `draft` 📘

### 自托管与替代方案（17）

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
- [claudio-bot](https://github.com/IamP5/claudio-bot) - 自己托管的 Claude Code 助手，用 iPhone 远程派活，想要类似 Grok Bot 体验又想数据留在自己机器上的人可以参考。标签：`self-hosted` `claude-code` `ios` 📦
- [agent-harbor](https://github.com/TommyBez/agent-harbor) - 在 macOS 上用 tmux 管一堆 Claude Code、Codex 会话，适合本机同时跑好几个编程代理的人。标签：`macos` `tmux` `coding-agents` 📦
- [Botling：在 Mac 上仿一个 Bot，底层换成 Claude Code / Codex](https://github.com/william1010121/Botling) - 自己电脑上跑的仿制品，驱动本机的 Claude Code 或 Codex 命令行；GPL-3.0 许可，适合想在本机试同类玩法的开发者。标签：`self-hosted` `mac` `claude-code` 📘
- [grokbot-tunnel](https://github.com/exa-pub/grokbot-tunnel) - Go 写的隧道：把 Linux 服务器接成 Grok Bot 的一台电脑，无桌面也能跑命令和读写文件；MIT，星少但文档和安装脚本齐全。标签：`tunnel` `self-host` `go` `linux` 📘
- [Local Bot：Mac 本机跑的 Grok Bot 风格队友](https://github.com/patrick-mns/localbot) - MIT；用 Cua Driver + Docker/Lume 在 Mac 上跑本地队友，最新发布 LocalBot-0.15.2.dmg；星少但更新到 2026-10-27。标签：`self-hosted` `mac` `local` `cua` `docker` 📦

### 硬件（6）

- [groki-bot](https://github.com/JosssphZhou/groki-bot) - M5Stack 桌面小机器人，能用语音把任务交给 Grok Bot。标签：`hardware` `voice` 📦
- [grok-gadgets](https://github.com/adidshaft/grok-gadgets) - 把硬件接到 Grok Bot 的工具包，可以先用模拟器试。标签：`hardware` `sdk` 📦
- [把 Grok Bot 装进 ESP32](https://x.com/Liu_zhongxisn/status/2112118491239379227) - 中文，硬件小项目 · @Liu_zhongxisn · 2026-10-19。标签：`hardware` `esp32` 📘
- [宗主 zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot) - ESP32-S3 圆屏语音终端，说一句话就把活交给 Bot，回复上屏并朗读，中文说明齐全；需要一台常开的电脑跑后端。标签：`hardware` `voice` 📦
- [stackchan-grok-bridge](https://github.com/Dissipative-ATLAS/stackchan-grok-bridge) - 中文项目，让 StackChan 小机器人把问题经 Mac 中转和 Cloudflare 信箱交给 Grok Bot，作者记了真机一次往返约三分钟，适合爱折腾硬件的人看思路；仓库没写许可证。标签：`hardware` `stackchan` `cloudflare` `chinese` 📘
- [小糖：ESP32 圆屏桌面宠物接 Grok Bot](https://github.com/vliuyt/grok-bot-esp32-bridge) - 微雪 1.43 寸圆屏板刷成会眨眼的小宠物，按住按键说话，由 Mac 桥接到你的 Bot；走的是桌面 App 内部接口，作者自己说不保证稳定。标签：`esp32` `hardware` `voice` `chinese` 📘

### 学习资源与合集（27）

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
- [Grok Bot Wiki](https://www.grokbotwiki.com/) - 英文资料站，有模板库和指南，每页标了对照的官方文档日期。标签：`wiki` `english` 📘
- [九类场景与资源库（翔宇工作流）](https://xiangyugongzuoliu.com/grokbot-use-cases/) - 中文，先讲公众号、小红书、抖音怎么拆岗，再按九类场景整理。标签：`usecases` `chinese` 📘
- [48 个玩法按场景整理（大数跨境）](https://www.10100.com/article/153919718) - 中文合集，作者说明是上手前做的功课，适合当灵感清单。标签：`index` `usecases` 📘
- [玩法全景手册（橙皮书合并版）](https://grokbot.aihuangshu.com/) - 中文站点，把橙皮书和英文清单合在一起，每天更新案例。标签：`index` `chinese` 📘
- [grok-bot-hub](https://github.com/ddhjy/grok-bot-hub) - 中文 Grok Bot 导航站源码，把官方文档、模板和社区链接归在一页，新手找入口方便。标签：`chinese` `directory` 📦
- [METAGROK：按编号排的 Grok Bot 小操作合集（英文）](https://metagrok.io/grok-bot) - 独立站，一条一个操作，从建 Bot、开通知到修连不上电脑都有，适合碰到具体问题时查；非官方，界面变了以官方为准。标签：`howto` `index` `english` 📘
- [GrokMag：Grok Bot 独立指南（多语言）](https://grokmag.com/grok-bot/how-it-works/) - 独立站，讲设置、Routine、审批和购物流程，有中文等多个语言版本；非官方，套餐类内容以官方页面为准。标签：`guide` `multilingual` 📘
- [Grok Bot 黑皮书：中文长篇合集](https://github.com/LJMStark/grok-bot-blackbook) - 中文 PDF 长书，按章节讲概念、技能和 Routine，附几十个可改的模板和一份大资源表；内容量大，挑自己用得上的章节看，许可是署名、非商用、相同方式共享。标签：`book` `templates` `chinese` 📘
- [grok-bots.com：Grok Bot 独立使用指南（多语言）](https://grok-bots.com/zh/how-to-use-grok-bot) - 独立站，有中文页，从开始用到常见设置一页讲完，适合新手扫一遍；站方自称非官方，功能细节以官方为准。标签：`guide` `multilingual` `chinese` 📘
- [grokbotguide.ai：Grok Bot 中文问答站](https://grokbotguide.ai/zh/) - 独立站，有中文版，按问题组织，比如怎么设定时任务；站方非官方，功能细节以官方为准。标签：`guide` `faq` `chinese` 📘

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

### 实操教程（21）

一件事一篇，照着做

- [收到邮件就整理：专属邮箱触发 Routine](https://grokguide.si/tutorials/email-trigger-routine)
- [让 Bot 交回能打开、能核对的文件](https://grokguide.si/tutorials/file-delivery)
- [Grok Bot 实操教程](https://grokguide.si/tutorials/)
- [五件事派活：一条好请求怎么写](https://grokguide.si/tutorials/strong-request)
- [会核对来源的每周学习助手](https://grokguide.si/tutorials/learning-scout)
- [用一条只读任务验收插件连接](https://grokguide.si/tutorials/verify-connection)
- [用自己的域名给 Bot 收信](https://grokguide.si/tutorials/domain-mail)
- [研发四角色：需求、复现、实现、验收](https://grokguide.si/tutorials/dev-four-roles)
- [出海客服：多语言来信先分流](https://grokguide.si/tutorials/ticket-triage)
- [把一次手动操作收成技能卡](https://grokguide.si/tutorials/teach-a-task)
- [iPhone 操作按钮一键语音聊天](https://grokguide.si/tutorials/action-button-voice)
- [做一份有来源的会前简报](https://grokguide.si/tutorials/meeting-brief)
- [Bot 做完了却没通知：六步排查](https://grokguide.si/tutorials/notification-checklist)
- [这个插件能干什么？先读官方仓库里的说明书](https://grokguide.si/tutorials/read-plugin-readme)
- [从模板安装到第一次验收](https://grokguide.si/tutorials/template-first-run)
- [用语音和键盘给 Grok Bot 交任务](https://grokguide.si/tutorials/voice-and-keyboard)
- [让 Bot 做一页会自己更新的看板](https://grokguide.si/tutorials/pages-live-report)
- [Routine 只写一行，做法放进技能](https://grokguide.si/tutorials/routine-one-line)
- [让 Bot 自己记经验，更新技能](https://grokguide.si/tutorials/self-updating-skills)
- [人批准以后，用一次性 Routine 发帖](https://grokguide.si/tutorials/approved-post-routine)
- [让 Bot 管待办，没做完就再提醒](https://grokguide.si/tutorials/todo-nag)
- [会变的事先查来源，别只信记忆](https://grokguide.si/tutorials/check-source-first)
- [固定的活交给脚本，Bot 只看一行结果](https://grokguide.si/tutorials/script-first)

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
