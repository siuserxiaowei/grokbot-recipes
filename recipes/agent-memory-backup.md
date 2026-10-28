# Agent 系统备份：搬走记忆，不带走密钥

- **适合**：云电脑要重置或换机器，想带走 bots/skills/inbox，又绝不能把 secrets 打进包的人
- **详细教程**：[Agent 系统备份：搬走记忆，不带走密钥](https://grokguide.si/tutorials/agent-memory-backup)

## 场景

对照铁柱「百万撤离」：白名单只拷 bots、skills、inbox；secrets 整夹跳过；正文命中 TOKEN= 也跳过；写出 MANIFEST 并做恢复预检。

## 准备

- 样例或真实的 Agent 家目录结构
- python3

## 步骤

1. 划定白名单目录
2. 跑备份脚本生成 MANIFEST
3. 核对跳过列表
4. 恢复预检通过后再覆盖
