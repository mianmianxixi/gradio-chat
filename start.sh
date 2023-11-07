#!/bin/bash
ps -ef|grep Chatbot|grep -v grep|awk "{print \$2}"|xargs kill -9 >/dev/null 2>&1
source venv/bin/activate
nohup python3 Chatbot.py &
#nohup streamlit run Chatbot.py  &
