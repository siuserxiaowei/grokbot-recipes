# .env 只比键名：从不打印值

- **适合**：换机器或拉新仓库时总漏配环境变量、又怕密钥进聊天的人
- **详细教程**：[grokguide.si/tutorials/env-key-diff](https://grokguide.si/tutorials/env-key-diff)

## 场景

本地能跑，同事拉下来却缺键；对比时不能把密码打出来。

## 准备

- `.env.example`（可提交）和本地 `.env`（勿提交）

## 步骤

1. 只解析键名，跳过注释。
2. 列出两边都有、只在 example、只在 env。
3. 输出禁止出现等号右边。
4. 缺的键人手填；私密键不要写进 example。
5. 不要提交 `.env`，不要整文件贴进聊天。

## 提示词

```text
请对比 {{仓库}}/.env.example 和本地 .env：
1. 只比较键名，绝不打印等号右边的值。
2. 列出：两边都有、只在 example、只在 env。
3. 只在 example 的标成「本地还没配」；只在 env 的提醒可能是私密键或漏写 example。
4. 不要创建、不要提交、不要把 .env 内容贴进聊天。
```

## 产出

一份键名差异清单，不含任何密钥值。

## 注意事项

- `.env` 必须在 gitignore。
- 需要填值时用 Vault 或本地手填，不要让 Bot 猜默认值。
