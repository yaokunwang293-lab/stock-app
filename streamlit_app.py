import streamlit as st
import requests
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(page_title="AI股票分析系统", page_icon="📈", layout="wide")

st.title("📈 AI股票分析系统（升级版）")

code = st.text_input("请输入股票代码（如：600519.SS / AAPL）：")

if code:
# 获取股票数据
try:
stock = yf.Ticker(code)
df = stock.history(period="3mo")

```
    if df.empty:
        st.error("❌ 股票代码错误或无数据")
    else:
        st.success("✅ 数据获取成功")

        # 当前价格
        current_price = df["Close"].iloc[-1]
        st.metric("当前价格", round(current_price, 2))

        # ===== K线图 =====
        fig = go.Figure(data=[go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"]
        )])

        fig.update_layout(title="K线图", xaxis_title="时间", yaxis_title="价格")
        st.plotly_chart(fig, use_container_width=True)

        # ===== AI分析 =====
        with st.spinner("AI分析中..."):
            url = "https://api.deepseek.com/v1/chat/completions"

            headers = {
                "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "user",
                        "content": f"请分析股票 {code} 最近走势，并给出操作建议"
                    }
                ]
            }

            response = requests.post(url, headers=headers, json=data, timeout=30)
            result = response.json()

            if "choices" in result:
                content = result["choices"][0]["message"]["content"]
                st.subheader("🤖 AI分析结果")
                st.write(content)
            else:
                st.error("❌ AI分析失败")
                st.write(result)

except Exception as e:
    st.error("❌ 出错了")
    st.write(e)
```
