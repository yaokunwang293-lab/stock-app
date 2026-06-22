import streamlit as st

st.title("我的股票分析系统")

code = st.text_input("输入股票代码：")

if code:
    st.write(f"你输入的是：{code}")
