#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
公众号运营助手 - 主程序
提供公众号选题、标题、内容、运营等全流程支持
"""

import json
import sys
from datetime import datetime, timedelta

# ========== 标题库 ==========
TITLE_TEMPLATES = [
    {"pattern": "数字 + 结果", "template": "《{number}个方法，{result}》"},
    {"pattern": "对比 + 反差", "template": "《从{before}到{after}，{time}》"},
    {"pattern": "悬念 + 好奇", "template": "《{question}？{twist}》"},
    {"pattern": "痛点 + 方案", "template": "《{pain}？{solution}》"},
    {"pattern": "情绪 + 立场", "template": "《我{emotion}{statement}》"},
]

SENSITIVE_WORDS = [
    "最", "第一", "绝对", "百分百", "永久", "无敌",
    "赚钱", "暴富", "躺赚", "稳赚", "内幕", "黑幕"
]

# ========== 内容模板 ==========
ARTICLE_TEMPLATES = {
    "热点解读": """
# {title}

【最新】
{hot_event}

【影响】
这对外贸人意味着：
1. {impact1}
2. {impact2}
3. {impact3}

【建议】
建议做好这 3 件事：
1. {advice1}
2. {advice2}
3. {advice3}

【工具】
用 {tool} 可以帮你{tool benefit}

【互动】
你对这个事件怎么看？留言区聊聊
""",

    "方法论": """
# {title}

【场景】
{scene}

【问题】
为什么会出现这个问题：
1. {reason1}
2. {reason2}
3. {reason3}

【方法】
{steps}

【案例】
{case}

【总结】
{summary}
""",

    "案例拆解": """
# {title}

【背景】
{background}

【挑战】
{challenge}

【做法】
{actions}

【结果】
{results}

【启示】
{lessons}
""",

    "避坑指南": """
# {title}

【提醒】
{warning}

【常见骗局】
{scams}

【识别方法】
{identification}

【建议】
{advice}
"""
}

# ========== 功能函数 ==========

def analyze_positioning(industry, target_audience, specialty):
    """分析账号定位"""
    return {
        "账号名称建议": [
            f"{industry}实战笔记",
            f"{industry}增长实验室",
            f"{specialty}指南",
        ],
        "Slogan 建议": [
            f"每天 3 分钟，获取一个{industry}客户",
            f"{industry}实操，先看这里",
        ],
        "目标读者": target_audience,
        "内容方向": [
            "实战方法",
            "案例分析",
            "避坑指南",
            "工具测评",
        ]
    }

def optimize_title(original_title):
    """优化标题"""
    suggestions = []
    
    # 数字型
    suggestions.append(f"《3 个方法，{original_title.replace('如何', '').replace('的', '')}》")
    
    # 对比型
    suggestions.append(f"《从 0 到 100 万，{original_title[:10]}...》")
    
    # 悬念型
    suggestions.append(f"《{original_title.replace('如何', '为什么')}？90% 的人都错了》")
    
    # 痛点型
    suggestions.append(f"《还在为{original_title[:8]}烦恼？这 5 招搞定》")
    
    # 检查敏感词
    issues = [w for w in SENSITIVE_WORDS if w in original_title]
    
    return {
        "原标题": original_title,
        "优化建议": suggestions,
        "敏感词提醒": issues if issues else "无",
        "字数检查": f"{len(original_title)}字（建议 15-25 字）"
    }

def generate_content_calendar(industry, days=7):
    """生成内容日历"""
    calendar = []
    types = ["热点解读", "实战方法", "案例拆解", "避坑指南", "工具测评", "趋势分析", "读者问答"]
    
    today = datetime.now()
    for i in range(days):
        date = today + timedelta(days=i)
        calendar.append({
            "日期": date.strftime("%m-%d"),
            "星期": ["一", "二", "三", "四", "五", "六", "日"][date.weekday()],
            "类型": types[i % len(types)],
            "选题方向": get_topic_suggestion(industry, types[i % len(types)])
        })
    
    return calendar

def get_topic_suggestion(industry, content_type):
    """根据类型生成选题建议"""
    suggestions = {
        "热点解读": f"《{industry}人关注的最新政策/趋势》",
        "实战方法": f"《3 个方法，提升{industry}效率》",
        "案例拆解": f"《从 0 到 100 万，{industry}案例拆解》",
        "避坑指南": f"《{industry}常见的 5 个坑，第 3 个最常见》",
        "工具测评": f"《5 款{industry}工具，哪款最值得入手》",
        "趋势分析": f"《2026 年{industry}的 3 个新机会》",
        "读者问答": f"《读者问：{industry}常见问题解答》"
    }
    return suggestions.get(content_type, "")

def create_article_outline(topic, content_type="方法论"):
    """创建文章大纲"""
    templates = {
        "方法论": {
            "开头": "场景引入 + 痛点描述（100 字）",
            "正文": "3 个方法，每点 400 字（案例 + 步骤）",
            "结尾": "总结 + 金句 + 引导互动（200 字）",
            "总字数": "1500-2000 字"
        },
        "热点解读": {
            "开头": "热点事件描述（150 字）",
            "正文": "影响分析 + 应对建议（3 点，每点 300 字）",
            "结尾": "总结 + 行动呼吁（200 字）",
            "总字数": "1200-1800 字"
        },
        "案例拆解": {
            "开头": "案例背景介绍（200 字）",
            "正文": "挑战→做法→结果（每部分 400 字）",
            "结尾": "经验总结 + 可复用方法（200 字）",
            "总字数": "1500-2500 字"
        }
    }
    
    return {
        "主题": topic,
        "类型": content_type,
        "结构": templates.get(content_type, templates["方法论"]),
        "建议发布时间": "工作日 8:00-9:00",
        "预计阅读时间": "5-8 分钟"
    }

def diagnose_metrics(open_rate, share_rate, follower_growth):
    """诊断公众号数据"""
    feedback = []
    
    if open_rate < 5:
        feedback.append({
            "问题": "打开率偏低（{:.1f}%）".format(open_rate),
            "原因": "标题吸引力不足 / 推送时间不佳 / 粉丝不精准",
            "建议": ["优化标题（用数字/痛点/悬念）", "测试不同推送时间", "清理僵尸粉"]
        })
    elif open_rate < 15:
        feedback.append({
            "问题": "打开率中等（{:.1f}%）".format(open_rate),
            "建议": ["保持稳定更新频率", "增加读者互动", "优化封面图"]
        })
    else:
        feedback.append({
            "问题": "打开率优秀（{:.1f}%）".format(open_rate),
            "建议": ["保持现有风格", "尝试更多选题类型"]
        })
    
    if share_rate < 1:
        feedback.append({
            "问题": "分享率偏低（{:.1f}%）".format(share_rate),
            "建议": ["增加社交货币（让读者显得专业）", "设计金句便于引用", "结尾引导分享"]
        })
    
    return {
        "数据诊断": feedback,
        "行业参考": {
            "打开率": "5% 及格，15% 优秀",
            "分享率": "1% 及格，5% 优秀",
            "涨粉": "10 个/天及格，50 个/天优秀"
        }
    }

# ========== 主程序 ==========

def main():
    if len(sys.argv) < 2:
        print("使用方法：python handler.py <命令> [参数]")
        print("命令：positioning | title | calendar | outline | diagnose")
        return
    
    command = sys.argv[1]
    
    if command == "positioning":
        industry = input("行业：")
        audience = input("目标读者：")
        specialty = input("专业特长：")
        result = analyze_positioning(industry, audience, specialty)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif command == "title":
        title = input("原标题：")
        result = optimize_title(title)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif command == "calendar":
        industry = input("行业：")
        days = int(input("天数（默认 7）：") or 7)
        result = generate_content_calendar(industry, days)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif command == "outline":
        topic = input("文章主题：")
        content_type = input("文章类型（方法论/热点解读/案例拆解）：") or "方法论"
        result = create_article_outline(topic, content_type)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif command == "diagnose":
        open_rate = float(input("打开率（%）：") or 0)
        share_rate = float(input("分享率（%）：") or 0)
        follower_growth = int(input("日涨粉数：") or 0)
        result = diagnose_metrics(open_rate, share_rate, follower_growth)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    else:
        print(f"未知命令：{command}")

if __name__ == "__main__":
    main()
