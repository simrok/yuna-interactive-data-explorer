import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt

# Streamlit 세션 닫기
plt.close('all')

# Matplotlib 플롯 생성
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
st.pyplot(fig)

#BarChart with Pyplot
rand=np.random.normal(1,2,size=20)
fig, ax = plt.subplots()
ax.hist(rand,bins=15)
st.pyplot(fig)

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 this is the app title')
st.header("this is the markdown")
st.markdown("this is the header")
st.headder("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r'''a+ar^1+ar^2+ar^3''')

# st.image("https://images.app.goo.gl/E2yXdXN97kxoAhAq7")

st.checkbox('yes')
st.button('Click')
gender = st.radio('Pick your gender', ['Male', 'Female'])
planet = st.multiselect('choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.selectslider('Pick a mark', ['Bad', 'Good', 'Excellent'])
x = st.slider('Pick a number', 0,50)
   
st.write('성별', gender)
st.write('행성', planet)

st.number_input('Pick a number', 0,10)
#st.text_input('Email address')
#st.date_input('Travelling date')
#st.time_input('School time')
#st.text_area('Description')
#st.file_uploader('Upload a photo')
color = st.color_picker('Choose a favorite color')

st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender",["Male", "Female"])