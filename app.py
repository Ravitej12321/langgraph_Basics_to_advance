import os
from dotenv import load_dotenv
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st 
load_dotenv()

# langsmith Tracking
os.environ["LANGSMITH_API_KEY"] = os.getenv('LANGSMITH_API_KEY')
os.environ["LANGSMITH_TRACING"] = "true"
os.environ['LANGSMITH_PROJECT'] = os.getenv("LANGSMITH_PROJECT")

## prompt Template

prompt  = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respong"\
        "to the question asked in two sentences "),
        ("user","Question:{question}")

    ]
)
st.title("Langchain Demo with Gemma3")
input_text = st.text_input("what question do you have?")

llm = Ollama(model='gemma3:1b')
output_parser =StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    chain_stream = chain.invoke({"question": input_text})
    st.write(chain_stream)