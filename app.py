import streamlit as st

st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')

st.text('Hello World. Streamlit text')
name='Yugeon Kwak'
st.text('Hi, %s'%name)

st.markdown('## This is markdown')

st.success('성공적으로 저장하였습니다.')
st.warning('업로드할 수 없는 파일 형식입니다.')
st.info('알려드립니다.')
st.error('This is an error')
st.exception('This is an exception')

st.write('Normal Text')
st.write('## This is a markdown text')
st.write(1+2)
st.write(dir(st))

st.help(range)

st.title(' Data Display Elements')
st.header('Iris data display')

import pandas as pd

df=pd.read_csv('iris.csv')
st.subheader('Method 1')
st.dataframe(df)

st.subheader('Method 2')
st.dataframe(df.style.highlight_max(axis=0))

st.subheader('Method 3: static table')
st.table(df)

st.header('display json')
st.json(
    {'data': 'name'}
)

st.header('display code')
st.code('''
def sayHello():
    print('Hello Streamlit')
''', language='python')

col1, col2, col3=st.columns(3)
col1.metric('Temperature','70 F','1.2 F')
col2.metric('Wind','9 mph','-8%')
col3.metric('Humidity','86%','4%')

name='Yugeon Kwak'
if st.button('Submit',key=1):
    st.write('Name: %s'%name)
if st.button('Submit',key=2):
    st.write('Full Name: %s'%name)

st.header('Radio Button')
status=st.radio('What is your status',('Active','Inactive'))
if status=='Active':
    st.success('You are active')
elif status=='Inactive':
    st.warning('You are inactive')

st.header('Checkbox')
agree=st.checkbox('I agree')
if agree:
    st.write('You agreed')

my_lang=['Python','C','C++','C#','Go','Java']
choice=st.selectbox('Language',my_lang)
st.write('You selected %s'%choice)