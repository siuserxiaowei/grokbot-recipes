"""从 data/items.json 和 recipes/ 生成 README.md 与 docs/community-tutorials.md。"""
import json,glob,re
CAT={"A":"官方与工具","B":"模板与目录","C":"技能与连接","D":"多 Bot 团队","E":"Routine 与监控","F":"一人公司与内容","G":"自托管与替代方案","H":"硬件","I":"学习资源与合集",
"T1":"入门与配置","T2":"多 Bot 团队","T3":"Routine 与额度","T4":"连接、技能与记忆","T5":"一人公司与内容","T6":"安全"}
d=[x for x in json.load(open("data/items.json")) if x["kept"]]
proj=[x for x in d if not x["cat"].startswith("T")]; tut=[x for x in d if x["cat"].startswith("T")]
def line(x,mark=False):
    ex=f" · @{x['author']} · {x['date']}" if x.get("author") and x.get("date") else ""
    s=f"- [{x['title']}]({x['url']}) - {x['review']}{ex}。标签："+" ".join(f"`{t}`" for t in x["tags"])
    return s+((" 📘" if x["level"]=="读过文档" else " 📦") if mark else "")
L=["# 社区教程精选","","X、博客和其他网站上的 Grok Bot 教程，按主题整理。标题和短评都是我们自己写的，版权归原作者。","",f"共 {len(tut)} 篇，每篇都打开核对过：还能访问、作者和日期对得上、内容确实讲 Grok Bot。文中的数字是作者自己说的。",""]
for c in ["T1","T2","T3","T4","T5","T6"]:
    g=[x for x in tut if x["cat"]==c]; L+=[f"## {CAT[c]}（{len(g)}）",""]+[line(x) for x in g]+[""]
open("docs/community-tutorials.md","w").write("\n".join(L))
old=open("README.md").read()
idx=old[old.index("## 教程索引"):old.index("## 参与贡献")].strip()
recs=[]
for f in sorted(glob.glob("recipes/*.md")):
    if "_template" in f: continue
    s=open(f).read(); recs.append((f,s.split("\n")[0][2:],re.search(r"\*\*适合\*\*：(.*)",s).group(1)))
R=["# Grok Bot 中文配方库 · grokguide 版","",
"> Dato（siuser小伟）和他的 Grok Bot 一起维护：拿来就能用的配方、逐条核对过的生态清单，加上 grokguide.si 的教程索引。","",
"中文 · [English](README.en.md) · [路线图](ROADMAP.md) · [参与贡献](CONTRIBUTING.md)","",
"[![link-check](https://github.com/siuserxiaowei/grokbot-recipes/actions/workflows/link-check.yml/badge.svg)](https://github.com/siuserxiaowei/grokbot-recipes/actions/workflows/link-check.yml)","",
"非官方项目。教程正文在 [grokguide.si](https://grokguide.si)。","",
"## 一眼看完","",f"- **{len(recs)}** 个配方，格式统一，提示词可以直接复制",f"- **{len(proj)}** 个生态项目和学习资源，每条都打开核对过",f"- **{len(tut)}** 篇社区教程，见 [社区教程精选](docs/community-tutorials.md)","- **90** 个官方模板市场模板的中文教程，见 [模板市场教程](docs/marketplace-templates.md)","- **112** 篇 grokguide.si 自己的教程","",
"每条后面的小标记说明我们核对到哪一步：📘 读过内容，📦 仓库已核对。完整记录在 [data/items.json](data/items.json)。","",
"## 怎么用","","1. 新手先读 [第 0 章](https://grokguide.si/guide/ch00) 和 [第 1 章](https://grokguide.si/guide/ch01)。","2. 想马上干活，从下面挑一个配方，把提示词复制给你的 Bot。","3. 想找现成的工具和模板，看生态清单。","",
f"## 配方（{len(recs)}）","","格式：适合谁 → 准备什么 → 步骤 → 提示词 → 产出 → 注意事项。变量用 {{占位符}}，示例都是虚构的。","","| 配方 | 适合 |","|---|---|"]+[f"| [{t}]({f}) | {w} |" for f,t,w in recs]
R+=["",f"## 生态清单（{len(proj)}）",""]
for c in "ABCDEFGHI":
    g=[x for x in proj if x["cat"]==c]; R+=[f"### {CAT[c]}（{len(g)}）",""]+[line(x,True) for x in g]+[""]
R+=[idx,"","## 参与贡献","","见 [CONTRIBUTING.md](CONTRIBUTING.md)。不收任何密钥、密码、cookie、经营数字和个人隐私信息。","",
"## 致谢","","本仓库的结构和最初的候选清单参考了 [sit-in/awesome-grokbot-playbooks](https://github.com/sit-in/awesome-grokbot-playbooks)（MIT 许可）。之后又补充了中文搜索结果里的教程。每一条我们都重新核对过，标题、短评和配方都是自己写的。","",
"## 许可证","","配方和清单采用 [MIT](LICENSE)。grokguide.si 的文章和图片、清单里链接的内容，版权归各自作者。",""]
open("README.md","w").write("\n".join(R))
print(len(recs),len(proj),len(tut))
