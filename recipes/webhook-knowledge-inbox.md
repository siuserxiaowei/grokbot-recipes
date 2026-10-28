# Webhook 知识入库：先过滤再进 inbox

- **适合**：想用快捷指令把微信摘录、网页剪藏丢进知识库，又怕广告和系统垃圾跟着进来的人
- **详细教程**：[Webhook 知识入库：先过滤再进 inbox](https://grokguide.si/tutorials/webhook-knowledge-inbox)

## 场景

打包 → Webhook/本地 zip → 扩展名白名单 → 正文拒推广词 → 写入 inbox 并记 sha。

## 准备

- 样例 zip 或临时下载链
- inbox 目录

## 步骤

1. 收包
2. 过滤文件名与正文
3. 写入 inbox
4. 打印接受/拒绝清单
