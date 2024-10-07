import numpy as np
import pandas as pd
import streamlit as st

st.title("THIS IS YOUR FIRST APPLICATION")
st.write("This is just an Example!!!!")

data=pd.DataFrame({
    "Name":["Sachin","Gautam","Suresh","Ram","Yuvraj"],
    "Marks":[92,67,88,90,75]}
)

st.write("Details of Students are given below:")
st.write(data)

chart_data=pd.DataFrame(
    np.random.randn(20,5),columns=['A','B','C','D','E']
)

st.line_chart(chart_data)
st.bar_chart(chart_data)
