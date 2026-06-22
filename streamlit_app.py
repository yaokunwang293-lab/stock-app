
import streamlit as st
import requests

st.title("AI股票分析系统")

code = st.text_input("输入股票代码：")

if code:
    st.write(f"正在分析 {code}...")

    url = "https://api.deepseek.com/v1/chat/completions"

    headers = {
        "Authorization": "Bearer sk-a4aab40000554b7abffd90b200f17f53
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": f"请分析股票 {code} 的走势，并给出操作建议"
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    try:
        content = result["choices"][0]["message"]["content"]
        st.write(content)
    except:
        st.write("❌ 出错了：", result)
