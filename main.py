#from dotenv import load_dotenv
#load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

st.title('이지인 봇')

content = st.text_input('주제를 제시해주세요.')
result = llm.predict(content + "에 대한 주제를 갖고 이지인을 이름과 연관해서 약오르게 살살 놀려줘")

if st.button('요청하기'):
    with st.spinner('시 작성중...'):
        st.write('시의 주제는 ', content)
        st.write(result)

#print(result)




#from langchain.chat_models import ChatOpenAI
#chat_model = ChatOpenAI()
#chat_model.predict("hi!")