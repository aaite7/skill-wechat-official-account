# 公众号运营助手 Skill

<div align="center">

📝 **外贸获客 · 公众号运营 · 内容创作**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)
[![CI](https://github.com/YOUR_USERNAME/skill-wechat-official-account/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/skill-wechat-official-account/actions)

</div>

---

## 快速使用

```bash
# 1. 克隆
git clone https://github.com/YOUR_USERNAME/skill-wechat-official-account.git
cd skill-wechat-official-account

# 2. 运行
python handler.py <命令>
```

## 命令列表

| 命令 | 功能 | 示例 |
|------|------|------|
| `positioning` | 账号定位 | `python handler.py positioning` |
| `title` | 标题优化 | `python handler.py title` |
| `calendar` | 内容日历 | `python handler.py calendar` |
| `outline` | 文章大纲 | `python handler.py outline` |
| `diagnose` | 数据诊断 | `python handler.py diagnose` |

## 示例

### 优化标题
```bash
$ python handler.py title
原标题：美国降息对外贸的影响

输出：
{
  "原标题": "美国降息对外贸的影响",
  "优化建议": [
    "《3 个方法，抓住美林降息的外贸机会》",
    "《从降息到订单增长，外贸人该怎么做》",
    "《为什么降息后你的订单没增加？》"
  ],
  "字数检查": "10 字（建议 15-25 字）"
}
```

### 生成内容日历
```bash
$ python handler.py calendar
行业：外贸
天数：7

输出：7 天内容规划（日期 + 类型 + 选题）
```

## 适用人群

- ✅ 外贸从业者（获客、销售、老板）
- ✅ 企业新媒体运营
- ✅ 个人 IP 创作者
- ✅ 知识付费从业者

## 目录结构

```
skill-wechat-official-account/
├── SKILL.md              # Skill 描述
├── handler.py            # 主程序
├── README.md             # 使用说明
├── DEPLOYMENT.md         # 部署指南
├── LICENSE               # MIT 许可
├── docs/
│   └── title-guide.md    # 标题指南
├── templates/
│   └── article-templates.md  # 文章模板
└── examples/
    └── sample-output.json    # 示例输出
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_USERNAME/skill-wechat-official-account&type=Date)](https://star-history.com)

---

<div align="center">

**觉得有用？请给个 ⭐ Star！**

[Issues](https://github.com/YOUR_USERNAME/skill-wechat-official-account/issues) · [Discussions](https://github.com/YOUR_USERNAME/skill-wechat-official-account/discussions)

</div>
