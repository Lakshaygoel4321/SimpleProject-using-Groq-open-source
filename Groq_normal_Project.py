from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import os


# set groq api key
# or on the langchain tracing
# and ste the project name 
os.environ['GROQ_API_KEY'] = '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'
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = 'GROQ_PROJECT'

# Making prompt means how does model behave
prompt = ChatPromptTemplate.from_messages([

    ('system','you are a ai asisstent and you work to give the user answer efficently'),
    ('user','question:{question}')

])

# making function describe the structure 

def prompt_function(llm,temperature,max_token,question):
    model = ChatGroq(model = llm)
    parser = StrOutputParser()    
    chain = prompt|model|parser
    result = chain.invoke({'question':question})

    return result


st.title('OPEN SOURCE ASISSTENT')
st.write('USING GROQ MODEL')

question = st.text_input('CHAT WITH AI')

temperature = st.sidebar.slider('Temperature',min_value=0.0,max_value=1.0,value=0.7)
max_token = st.sidebar.slider('Max Token',min_value=50,max_value=300,value=150)

llm = st.sidebar.selectbox('Choose a Model',['gemma2-9b-it','llama-3.3-70b-versatile','llama-3.1-8b-instant','llama3-70b-8192'])



if st.button('Response'):
    
    response = prompt_function(llm,temperature,max_token,question)  
    st.write(response)

else:

    st.write('Sorry please try again with context')

