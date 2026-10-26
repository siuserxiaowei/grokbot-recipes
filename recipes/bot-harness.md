# 多 Bot 共用规则底座：一个入口、一个写入者

- **适合**：同时用好几个 Bot、规则老对不上或者共享文件被互相覆盖的人
- **详细教程**：[多个 Bot 一起干活，先立一套共用规则](https://grokguide.si/tutorials/bot-harness)
- **思路来源**：[木渡川（@tanglele0318）的 Harness 长文](https://x.com/tanglele0318/status/2114499611465236500)

## 场景

Bot 一多，规则散在各处，版本对不上；几个 Bot 同时写一个文件，后写的把先写的覆盖掉，还不报错。我们实跑过：三个 Bot 同时“读、加一行、写回”，文件里只剩 1 行。

## 步骤

1. 在云电脑 `/workspace/bot-harness` 建 `AGENTS.md`：只写红线、冲突顺序和路由表。
2. `VERSION` 写一行版本号；细则按事项放 `global/rules/`。
3. 项目用两位编号 `NN-` 开头，各带一份 `TODO.md`。
4. 写只读的 `doctor.py`：查版本号、必需文件、断掉的路由、疑似密钥、重复编号、过期 TODO。
5. 共享文件只让管家 Bot 写，其他 Bot 往 `inbox/` 交清单。
6. 规则问题记到 `feedback/当周.md`，批准后统一改，版本号加一。

## 提示词

```text
帮我在云电脑上搭一个多 Bot 共用的规则底座，放在 /workspace/bot-harness：
AGENTS.md 只写红线、冲突顺序（我当轮的话 > 项目规则 > 全局细则 > 其他约定 > 默认习惯）和路由表；
写一个只读的 doctor.py，只报问题不改文件；共享文件只让一个管家 Bot 写，其他 Bot 往 inbox/ 交清单。
先跑一次 doctor.py 给我看结果，再把“开工前先读 AGENTS.md”写进每个 Bot 的技能里。
```
