from langchain.llms import OpenAI
import os

def get_suggestions():
    llm = OpenAI(temperature=0.9)
    text = "What would be a good company name for a company that makes colorful socks?"
    print(llm(text))
    text2 = "Any other alternative for sock company name?"
    print(llm(text2))
    print(llm("more alternative for sock company name?"))

if __name__ == "__main__":
    get_suggestions()