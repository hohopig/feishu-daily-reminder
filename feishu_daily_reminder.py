#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
飞书群定时提醒脚本
每天早上10:00自动发送提醒消息到飞书群
"""

import requests
import json
from datetime import datetime

# 飞书群机器人Webhook地址
WEBHOOK_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/23c43dfa-8593-4c0b-b966-bfb8fa38e1c9"

# 飞书文档链接
DOC_URL = "https://anker-in.feishu.cn/wiki/Ic8nwynOYiogR0ktKQvchDEVnAb"

def send_feishu_message():
    """发送飞书群消息"""

    # 获取当前日期
    today = datetime.now().strftime("%Y年%m月%d日")
    weekday = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"][datetime.now().weekday()]

    # 构造消息内容（富文本格式）
    message = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {
                    "tag": "plain_text",
                    "content": "📝 设备稳定性测试记录提醒"
                },
                "template": "blue"
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": f"**{today} {weekday}**\n\n各位同学早上好！👋\n\n请及时更新设备稳定性测试记录表，记录以下信息：\n- 设备状态\n- 挂测时长\n- 测试结果\n- 异常情况"
                    }
                },
                {
                    "tag": "hr"
                },
                {
                    "tag": "action",
                    "actions": [
                        {
                            "tag": "button",
                            "text": {
                                "tag": "plain_text",
                                "content": "📊 打开记录表"
                            },
                            "type": "primary",
                            "url": DOC_URL
                        }
                    ]
                },
                {
                    "tag": "note",
                    "elements": [
                        {
                            "tag": "plain_text",
                            "content": "💡 提示：点击上方按钮直接跳转到表格进行更新"
                        }
                    ]
                }
            ]
        }
    }

    try:
        # 发送POST请求
        response = requests.post(
            WEBHOOK_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(message),
            timeout=10
        )

        # 检查响应
        result = response.json()

        if result.get("code") == 0:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✅ 消息发送成功")
            return True
        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ❌ 消息发送失败: {result}")
            return False

    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ❌ 发送失败，错误: {str(e)}")
        return False

if __name__ == "__main__":
    send_feishu_message()
