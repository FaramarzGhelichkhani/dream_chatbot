import httpx
import os
from .prompts import get_chat_prompt
from langchain_openai import ChatOpenAI
from langchain.output_parsers.json import SimpleJsonOutputParser


HTTP_PROXY = os.getenv("HTTP_PROXY")
MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

def get_llm_response(user_dream):
    parser = SimpleJsonOutputParser()
    prompt =  get_chat_prompt()
    llm = ChatOpenAI(temperature=0, model_name=MODEL_NAME, 
                     http_client=httpx.Client(proxy=HTTP_PROXY)
                     )
    chain = (prompt | llm | parser) 
    response = chain.invoke({"dream_text":user_dream})
    return response
