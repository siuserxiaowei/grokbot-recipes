# 隐藏前先停表：隐藏不等于暂停

- **适合**：暂时不想看见某个 Bot、却发现额度还在掉的人
- **详细教程**：[grokguide.si/tutorials/hide-not-pause](https://grokguide.si/tutorials/hide-not-pause)

## 场景

把竞品雷达之类的 Bot 隐藏了，定时 Routine 其实还在跑。

## 准备

- 一份 Bot 花名册（名字、是否隐藏、每条 Routine 是否启用）

## 步骤

1. 列出每个 Bot 的可见/隐藏状态和启用中的 Routine。
2. 凡是「隐藏=是且启用 Routine＞0」的单独标出。
3. 先暂停或删除那些 Routine，再隐藏。
4. 只读体检，不自动改开关。
5. 一周后再扫一次，防止又被打开。

## 提示词

```text
请只读体检当前 Bot 花名册（我贴名单，或你只读列出来的名单）：
1. 列出每个 Bot：可见/隐藏、Routine 启用数/总数。
2. 凡是「隐藏=是且启用 Routine＞0」的，单独标红。
3. 建议：隐藏前先暂停或删除 Routine；不要自动改任何开关。
4. 出处提醒：官方说过 hiding does not pause the Bot or its routines。
花名册：{{花名册或说明}}
```

## 产出

一份「隐藏仍启用」问题清单；停表后再隐藏。

## 注意事项

- 隐藏和归档以你账号当前界面为准；本配方只保证一件事：隐藏本身不停表。
- 可与「主 Bot 只挂两条」一起用。
