import streamlit as st
import requests

st.set_page_config(page_title="AI股票分析", page_icon="📈")

st.title("📈 AI股票分析系统")

code = st.text_input("请输入股票代码（如：600519）：")

if code:
    with st.spinner("AI正在分析中，请稍等..."):

        url = "https://api.deepseek.com/v1/chat/completions"

        headers = {
            "Authorization": "Bearer sk-a8c4efc18aea4c558260f3a3ae5e6a1e
            "Content-Type": "application/json"
        }

        data = {
            "model": "deepseek-chat",
            "messages": [
                {
                    "role": "user",
                    "content": f"""
请对股票 {code} 进行专业分析，包括：
1. 当前趋势（上涨/下跌/震荡）
2. 支撑位和压力位
3. 短线和中线操作建议
4. 是否适合买入

用简洁清晰的中文回答
"""
                }
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=data, timeout=30)
            result = response.json()

            content = result["choices"][0]["message"]["content"]

            st.success("分析完成 ✅")
            st.write(content)

        except Exception as e:
            st.error("❌ 出错了")
            st.write(result)
