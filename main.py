#from dotenv import load_dotenv
#load_dotenv()
#from langchain_openai.llms import OpenAI
#result = llm.invoke("내가좋아하는 동물은")
#print(result)
import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

st.title('인공지능 시인')

content = st.text_input('시의주제를 제시해주세요...')

if st.button('시 작성 요청하기'):
    with st.spinner('작성중...'):
        result = chat_model.invoke(content + "에 대한시를 써줘")
        #print(result.content)
        st.write(result.content)




