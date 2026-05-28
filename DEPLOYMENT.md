# 部署指南

## 上传到 GitHub

### 1. 创建新仓库

1. 访问 https://github.com
2. 点击右上角 **+** → **New repository**
3. 填写仓库名：`skill-wechat-official-account`
4. 描述：公众号运营助手 Skill
5. 选择 **Public**（公开）
6. **不要** 初始化 README（我们已经有代码了）
7. 点击 **Create repository**

### 2. 推送代码

```bash
cd /workspace/skill-wechat-official-account

# 修改 git remote（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/skill-wechat-official-account.git

# 推送代码
git push -u origin master
```

### 3. 验证上传

访问你的仓库页面，确认文件已上传成功。

---

## 添加到 opencode Skills

### 1. 在 opencode 中添加 Skil

编辑 `~/.opencode/skills.json` 或在项目中配置：

```json
{
  "skills": [
    {
      "name": "wechat-official-account",
      "path": "/workspace/skill-wechat-official-account"
    }
  ]
}
```

### 2. 使用方法

```
/wechat-official-account <你的需求>
```

---

## 更新 Skill

```bash
# 修改代码后
git add .
git commit -m "更新说明"
git push
```

---

## 分享 Skill

### GitHub 链接

```
https://github.com/YOUR_USERNAME/skill-wechat-official-account
```

### 使用方法说明

```bash
# 他人克隆后
git clone https://github.com/YOUR_USERNAME/skill-wechat-official-account.git
cd skill-wechat-official-account
python handler.py <命令>
```
