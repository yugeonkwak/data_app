import streamlit as st
import pandas as pd

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

'''st.title(' Data Display Elements')
st.header('Iris data display')

df=pd.read_csv('iris.csv')
st.subheader('Method 1')
st.dataframe(df)

st.subheader('Method 2')
st.dataframe(df.style.hightlight_max(axis=0))

st.subheader('Method 3: static table')
st.table(df)'''

'''st.header('display json')
st.json({'data': 'name'})

st.header('display code')
st.code('''
def sayHello():
    print('Hello Streamlit')
''', language='python')'''

