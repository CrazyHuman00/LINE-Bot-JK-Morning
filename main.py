# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
LKが朝起こしてくれるLINEBot
"""

import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

with open("info.json", "r", encoding="utf8") as file:
    info = json.load(file)

# チャンネルアクセストークンの取得
CHANNEL_ACCESS_TOKEN = info["CHANNEL_ACCESS_TOKEN"]
# LINEBotAPIの取得
LINE_BOT_API = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    """
    main
    """
    user_id = info["USER_ID"]
    messages = TextSendMessage(text="おはよう〜\n朝だよ〜おきて〜")
    LINE_BOT_API.push_message(user_id, messages=messages)

if __name__ == "__main__":
    main()
