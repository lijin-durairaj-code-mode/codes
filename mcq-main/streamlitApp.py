import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.mcqgenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging


with open('D:\GENERATIVE_AI\projects\mcq\response.json','r') as file:
    RESPONSE_JSON=json.load(file)


st.title('MCQ app with langchain')

with st.form('user_input'):
    uploaded_file=st.file_uploader('upload a PDF file')

    mcq_count=st.number_input('no of MCQ',min_value=3,max_value=30)

    subject=st.text_input('insert subject',max_chars=20)

    tone=st.text_input('complexity of question',max_chars=20,placeholder='simple')
    button=st.form_submit_button('create MCQ')

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner('loading...')
        try:
            text=read_file(uploaded_file)
            with get_openai_callback() as cb:
                response=generate_evaluate_chain({
                    'text':text,
                    'numnber':mcq_count,
                    'subject':subject,
                    'tone':tone,
                    'response_json':json.dumps(RESPONSE_JSON)
                })
        except Exception as e:
            traceback.print_exception(type(e),e,e.__traceback__)
            st.error('Error')
        
        else:
            if isinstance(response,dict):
                quiz=response.get('quiz',None)
                if quiz is not None:
                    table_data=get_table_data(quiz)
                    if table_data is not None:
                        df=pd.DataFrame(table_data)
                        df.index=df.index+1
                else:
                    st.write(response)