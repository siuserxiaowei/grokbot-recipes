# 表格转 Markdown 和 Slack：中文按 2 格对齐

- **适合**：要把表格贴到 Slack 和文档、贴过去总乱的人
- **详细教程**：[grokguide.si/tutorials/table-copy-formats](https://grokguide.si/tutorials/table-copy-formats)

## 场景

要把表格贴到 Slack 和文档、贴过去总乱。

## 准备

- 一份示例数据，先别动真实设置

## 步骤

1. 读 CSV，确认每行列数一样。
2. 出 Markdown 表格，空格子补空格。
3. 出等宽文本，放进代码块。
4. 中文按显示宽度 2 格补齐。
5. 念一遍表头核对。

## 提示词

```text
把 {{文件}} 里的表格转一下：
1. 给我一份 Markdown 表格。
2. 再给一份贴 Slack 用的等宽文本，中文按 2 格对齐。
3. 空格子补齐，告诉我有几行几列。
```

## 产出

Markdown 表格和等宽文本各一份。

## 注意事项

- 读屏用 Markdown 表格更好，等宽文本只给 Slack。
- 发送、删除、购买照旧要你点头。

## 小伟点评

按字数补齐时“乌鲁木齐”那行会歪，按显示宽度才齐。
