# 消息热力图：看清最常找哪个 Bot

- **适合**：开了好几个 Bot、想知道哪些常用、哪些建完就闲着的人
- **详细教程**：[用 msg-graph 画一张消息热力图](https://grokguide.si/tutorials/msg-heatmap)

## 场景

Bot 一多，凭感觉说不清自己平时在找谁。用社区仓库 wustep/my-bot-scripts 里的 msg-graph，在 Bot 的云电脑上只读导出“每天、每个 Bot 你亲手发了几条”，再用一个本地网页画成热力图、星期分布、每周柱状图和排行。

## 准备

- 一个能用云电脑的 Grok Bot
- 一台能开浏览器的电脑（原作者的做法是在 Mac 上看）

## 步骤

1. 让 Bot 克隆 https://github.com/wustep/my-bot-scripts ，先读 msg-graph 的 README、SKILL.md 和导出脚本。
2. 把 SKILL.md 原样存成技能 msg-graph。
3. 导出时设好时区：`MSG_GRAPH_TZ=Asia/Shanghai python3 export_grokbot_messages.py --out <路径>/messages.json`，默认是美西时间。
4. 把 JSON 放进查看器的 data 文件夹，起一个只听 127.0.0.1 的小网页服务，打开本机查看器地址（默认 `http://127.0.0.1:47821`）。
5. 以后再跑，输出里出现 `unchanged=1` 就说明数字没变，不用再拷。

## 提示词

```text
帮我装一个消息热力图技能：
1. 克隆 https://github.com/wustep/my-bot-scripts ，先读 msg-graph 文件夹，告诉我它读哪些文件、会不会联网、会不会写东西。
2. 没问题就把 SKILL.md 原样存成技能 msg-graph，导出时 MSG_GRAPH_TZ 设成 {{你的时区}}。
3. 起查看器给我看一眼；截图给我之前把 Bot 名字换成字母。
4. 导出的数据只留本机，不提交到任何仓库。
```

## 产出

一份按天、按 Bot 的消息计数 JSON，和一页能按 Bot 筛选的热力图。我们 10-25 的实跑：15 天 187 条，前两个 Bot 占了近九成。

## 注意事项

- 只数你亲手发的消息：Bot 之间互转的不算，十分钟内重复的同一句只算一次，短信中转单列一项。
- 不带消息原文，但 Bot 名字可能带项目名，分享截图前先换掉。
- 查看器会从公共 CDN 加载 React 等前端库；用完把本机端口的进程关掉。
- 社区项目，非官方，MIT 许可。
