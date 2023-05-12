from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

def get_chat_conversation():
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1.0)
    messages = [
        SystemMessage(content="You are an expert data scientist"),
        HumanMessage(content="Write a python script that trains a neural network on simulated data")
    ]
    response = chat(messages=messages)
    #print(response)
    print(response.content, end='\n')


if __name__ == "__main__":
    get_chat_conversation()