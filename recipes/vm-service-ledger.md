# 虚拟机服务花名册：重置后分清谁来装

- **适合**：虚拟机常重置、工具总要重装，想先分清可自动装和需自己登录的人
- **详细教程**：[虚拟机服务花名册：重置后分清谁来装](https://grokguide.si/tutorials/vm-service-ledger)

## 场景

维护 services.json：可自动装 / 需你登录 / 离线包你来装。脚本从不代登录、从不下载 Tailscale 安装包。

## 准备

- 一份 services.json
- 对照 box-heal 禁令

## 步骤

1. 登记每项 install/health/login/offline_pkg
2. 分类
3. 重置后只自动处理可自动类
4. 你完成登录后再复检
