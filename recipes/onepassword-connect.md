# 1Password 连接器：Vault 优先 + 按次批准

- **适合**：想让 Bot 登录网站整理数据或填表，又不想把密码贴进聊天的人
- **详细教程**：[grokguide.si/tutorials/onepassword-connect](https://grokguide.si/tutorials/onepassword-connect)
- **思路来源**：[官方 computer-and-apps / 1Password Support](https://support.1password.com/1password-grok-bot/)；社区讲解 [Mulight @Mulight](https://x.com/Mulight/status/2117189034464493920)

## 场景

Bot 要打开后台、报表站或表单页，但密码进聊天风险高；Vault  alone 不够覆盖所有 Login，又需要按次可见的批准。

## 准备

- Grok Bot 桌面 ≥0.75（或移动 ≥1.16）；同机 1Password ≥8.12.42
- 1password.com 的 Individual / Family 账户（Teams / Business / .ca / .eu 暂不可用）
- 要用的 Login 已在 Personal（Family 上叫 Private）保险库
- 分清：高频低敏 → Vault；要按次批准 → 1Password
- **不要**指望 1Password 代填付款卡、Passkey 或第三方 SSO

## 步骤

1. Connect apps → Password Managers → 1Password → Connect → Allow。
2. 确认条目在 Personal/Private；共享库先搬迁或复制。
3. 下任务时写明：先查 Vault；没有再走 1Password；SSO/验证码/付款卡住就停并交还屏幕。
4. 聊天出现 Review in 1Password 时，核对网站与账号再批准（约 30 天有效）。
5. （可选）用本地虚构策略脚本自检边界：Vault 优先、共享库、SSO、卡、过期批准。
6. 旧 service account 集成：断开后按新连接器重连，并迁移条目。

## 提示词

```text
请按「1Password 连接器」列连接前自检（只要清单，不要替我点 Connect）：
桌面是否 ≥0.75（或移动 ≥1.16），1Password 是否 ≥8.12.42；
账户是否为 1password.com Individual/Family；
Login 是否在 Personal/Private。
下任务时：先查 Vault；没有再用已连接的 1Password 等我批准；
遇到 Passkey、SSO、验证码、付款页：不要重试超过一次，交给我。
不要把密码、OTP、卡号写进聊天。
```

## 产出

连接前自检清单 + 带刹车的登录任务话术 + （可选）边界巡检脚本结果。

## 注意事项

- 新集成不再用 service account；旧共享库条目不会自动可用。
- Bot 看不到明文密码，但同机文件与已登录会话仍要当共享资源管理。
- 批准过期或 1Password 撤回后会再问——不是故障。
- 本配方的巡检是虚构策略表，不是真实 1Password 登录实测。

## 小伟点评

虚构六场景：Vault 命中、个人库 Review、共享库需搬、SSO 人接管、付款卡永不代填、45 天批准过期；ASSERT_OK。
