# 云电脑自愈：重置后把 Tailscale 和常用状态装回来

- **适合**：云电脑常被平台重置、换机或休眠，想让 Tailscale、软件包基线和 gh 登录态自动回来，又不想让脚本代你登录的人
- **详细教程**：[云电脑自愈：重置后把状态装回来](https://grokguide.si/tutorials/box-heal)

## 场景

平台点一次「更新 Bot 的电脑」，`/usr/local/bin`、apt 包和 `~/.bashrc` 会清空；休眠回来后 Tailscale 还可能假在线十几分钟。把自愈套件装进 `/workspace`，每次开 shell 最多十五分钟跑一轮检查：缺什么就按条目修，修不了就标 NEEDS HUMAN，绝不替你登录。

## 准备

- 一台能用的 Grok Bot 云电脑（bash 5、`jq`、`flock`、`timeout`、`setsid`、`ss`，以及免密 `sudo -n`）
- 仓库：https://github.com/heyalchang/grokbot-box-heal（MIT）
- 若要用 Tailscale：事先下载官方静态二进制放到 `/workspace/tailscale/bin/`，并自己完成一次登录；套件从不下载、从不登录
- 若不用 Tailscale：装完后对 `100-tailscale` 和 `150-tailscale-online` 建 `DISABLED` 文件

## 步骤

1. 克隆仓库到云电脑（例如 `/workspace/src/grokbot-box-heal`），进入目录执行 `./install.sh`。想先在沙盒试：`WORKSPACE=/tmp/box-heal-lab BASHRC=/tmp/box-heal-lab/bashrc ./install.sh --no-hook`。
2. 编辑 `/workspace/restore/config.env`（安装时从示例复制，已有文件不会被覆盖）：至少填 `WANT_HOST`、`WANT_TAILNET`；不用 Tailscale 就留空并禁用对应条目。
3. 一次性人工步骤：把 `tailscale` / `tailscaled` 放进 `/workspace/tailscale/bin/`（`chmod 0755`），再亲自完成 Tailscale 登录；可选地把 `gh` 登录持久化到 `/workspace/config/gh`。
4. 日常：任意 shell 会经 `~/.bashrc` 钩子最多每 15 分钟跑一次 `restore-all.sh`。也可手动：`BOX_WORKSPACE=/workspace /workspace/bin/restore-all.sh`。
5. 看 `restore.log` 和各条目状态。出现 NEEDS HUMAN 就按该条目的 `INSTRUCTIONS.md` 处理，不要让 Bot 代登。

## 提示词

```text
请按 https://github.com/heyalchang/grokbot-box-heal 帮我装云电脑自愈套件：
1. 克隆后跑 install.sh；若我只要沙盒，用 WORKSPACE 和 BASHRC 指到临时目录，并加 --no-hook。
2. 编辑 restore/config.env：填我想要的 WANT_HOST / WANT_TAILNET；我不用 Tailscale 时，touch items/{100-tailscale,150-tailscale-online}/DISABLED。
3. 硬规矩：套件从不登录、从不下载 Tailscale 二进制；离线包由我放到 /workspace/tailscale/bin/，首次登录由我点。
4. 不要改我现有的 /workspace/restore（若已有生产套件）；先在沙盒演示目录布局和 restore-all 输出给我看。
5. 装完告诉我下一步一次性人工动作清单，不要替我执行登录。
```

## 产出

`/workspace/restore/` 下的条目与任务、`bin/restore-*.sh`、可选的 bashrc 钩子，以及每次运行写入的 `restore.log`。沙盒演练应能看到 `kit v1.x`、条目列表，以及未配置 Tailscale 时的 `NEEDS HUMAN`。

## 注意事项

- 套件**从不登录、从不下载** Tailscale 二进制；缺状态或缺二进制一律 NEEDS HUMAN。
- 不用 Tailscale 时务必 `DISABLED` 掉 100/150，否则 150 会拉起 watchdog 循环。
- 云电脑上所有 Bot 共用带 sudo 的同一用户，装前看清它会改哪些路径。
- 更新方式：在克隆目录 `git pull` 后再跑一次 `install.sh`（幂等，不覆盖你的 `config.env` 与自建条目）。
