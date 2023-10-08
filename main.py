import streamlit as st
import pandas as pd
import numpy as np


# st.title("Abhilash")
# st.sidebar.title('sidebar title')
# st.header('Saurabh')
# st.subheader("InfoByte")
# st.write("this is a normal text")
# st.success("vikas")
# st.warning("ch")
# st.info("ut")
# st.error("ya")


# st.title("Calculator")
# col1,col2 = st.columns([1,1])
# with col1:
#     n1=st.text_input("Enter a number",value='0')
# with col2:
#     n2=st.text_input("Enter second number",value='0')
#
# op = st.selectbox('Select Operation',['+','-','*','/'])
#
# n1=float(n1)
# n2=float(n2)
#
# if op == '+':
#     result = n1+n2
# elif op == '-':
#     result = n1-n2
# elif op == '*':
#     result = n1*n2
# elif op == '/':
#     result = n1/n2
#
# c1,c2,c3 = st.columns([1,1,1])
#
# with c2:
#     btn=st.button('Calculator')
# if btn:
#     st.success(f"The Result is {result}.")