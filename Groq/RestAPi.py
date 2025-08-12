from fastapi import  FastAPI  
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os
from langserve import add_routes
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
groq_api_key  = os.getenv("GROQ_API_KEY")
model_client = ChatGroq(model = "gemma2-9b-it",api_key=groq_api_key)

generic_template = "Translate into {language} "


prompt = ChatPromptTemplate.from_messages(
    [('system',generic_template),('user','{text}')]
)

output_parser = StrOutputParser()

###

chain = prompt | model_client | output_parser

## app initialization
app  = FastAPI(title="langchain_project",
               version  = "1.0",
               description = "A simple API server using the langchain runnable interfaces")

## adding chain routes
add_routes(
    app,
    chain,
    path= "/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)