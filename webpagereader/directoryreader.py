## here we dont have the openai key that is why it is not working 

from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex 
from llama_index.llms.google_genai import GoogleGenAI

import os 
from dotenv import load_dotenv 
import logging 
import sys 


load_dotenv()


llm = GoogleGenAI(
    model="gemini-2.0-flash",
    # api_key="some key",  # uses GOOGLE_API_KEY env var by default
)

def main(url:str)-> None: 
    documents=SimpleDirectoryReader(url).load_data()
    index=VectorStoreIndex.from_documents(documents)
    query_engine=index.as_query_engine(llm=llm)
    response=query_engine.query("What did the artical saying please summarize it?")
    print(response)
if __name__ == '__main__':
    main(url="data/")