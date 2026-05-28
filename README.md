# 公众号运营助手 Skill

<div align="center">

📝 帮助外贸从业者、内容创作者运营微信公众号

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)

</div>

---

## 📖 简介

这个 Skill 提供公众号全流程运营支持，包括：
- **账号定位**：名称、Slogan、人设规划
- **标题优化**：10 万 + 标题公式
- **内容规划**：30 天内容日历
- **文章创作**：写作模板、大纲生成
- **运营诊断**：数据分析、优化建议

## 🚀 快速开始

### 安装

```bash
# 克隆到本地
git clone https://github.com/YOUR_USERNAME/skill-wechat-official-account.git

# 进入目录
cd skill-wechat-official-account

# 无需安装依赖，直接运行
```

### 使用方法

```bash
# 账号定位
python handler.py positioning

# 标题优化
python handler.py title

# 内容日历
python handler.py calendar

# 文章大纲
python handler.py outline

# 数据诊断
python handler.py diagnose
```

## 📋 功能详解

### 1. 账号定位 (`positioning`)

帮助确定公众号方向和人设。

**输入示例：**
```
行业：外贸获客
目标读者：外贸老板、SOHO、业务员
专业特长：客户开发、邮件营销
```

**输出：**
- 账号名称建议（5 个）
- Slogan 建议（3 个）
- 内容方向规划

### 2. 标题优化 (`title`)

将普通标题改写为爆款标题。

**输入示例：**
```
原标题：美国降息对外贸的影响
```

**输出：**
- 5 个优化版本
- 敏感词检查
- 字数建议

### 3. 内容日历 (`calendar`)

生成未来 N 天的内容规划。

**输入示例：**
```
行业：外贸
天数：7
```

**输出：**
- 每日选题
- 内容类型
- 发布时间建议

### 4. 文章大纲 (`outline`)

生成文章结构和写作框架。

**输入示例：**
```
主题：客户开发方法
类型：方法论
```

**输出：**
- 文章结构
- 每部分字数
- 预计阅读时间

### 5. 数据诊断 (`diagnose`)

分析公众号运营数据。

**输入示例：**
```
打开率：3.5
分享率：0.8
日涨粉：5
```

**输出：**
- 问题诊断
- 优化建议
- 行业参考标准

## 📁 目录结构

```
skill-wechat-official-account/
├── SKILL.md              # Skill 描述文件
├── handler.py            # 主程序
├── README.md             # 使用说明（本文件）
├── docs/                 # 文档
│   ├── title-guide.md    # 标题写作指南
│   └── content-guide.md  # 内容创作指南
├── templates/            # 模板
│   └── article-templates.md
└── examples/             # 示例
    └── sample-output.json
```

## 💡 使用场景

### 场景 1：新号启动
```bash
# 第 1 步：定位
python handler.py positioning

# 第 2 步：规划内容
python handler.py calendar

# 第 3 步：写文章
python handler.py outline
```

### 场景 2：标题优化
```bash
# 写了好文章但打开率低
python handler.py title
```

### 场景 3：运营诊断
```bash
# 分析为什么没增长
python handler.py diagnose
```

## 🎯 最佳实践

### 标题技巧
- 使用数字：《3 个方法...》
- 制造悬念：《为什么...》
- 直击痛点：《...怎么办？》
- 立场鲜明：《我劝你...》

### 内容节奏
- 周一：本周前瞻
- 周二 - 四：干货方法
- 周五：工具/资源
- 周末：轻松内容

### 发布时间
- 工作日：8:00-9:00（通勤）
- 午休：12:00-13:00
- 晚间：20:00-21:00

## ⚠️ 注意事项

1. **合规第一**：避免敏感词、违规话题
2. **持续输出**：每周至少 2-3 更
3. **数据驱动**：每周分析优化
4. **读者互动**：回复每条评论

## 📚 学习资源

- [微信公众平台官方文档](https://developers.weixin.qq.com/doc/)
- [新榜](https://www.newrank.cn/) - 行业数据
- [清博指数](http://www.gsdata.cn/) - 账号排名

## 🤝 贡献

欢迎提 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 👤 作者

你的名字 - [@your-twitter](https://twitter.com)

---

<div align="center">
<strong>如果觉得有用，请给个 ⭐ Star！</strong>
</div>
