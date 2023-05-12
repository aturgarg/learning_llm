from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import os

def get_prompt_and_prediction():
    # llm object
    llm = OpenAI(temperature=0.9)

    # create prompt
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )

    # create llm chain
    chain = LLMChain(llm=llm, prompt=prompt)

    # execute chain
    result = chain.run("colorful socks")
    print(result)



if __name__ == "__main__":
    get_prompt_and_prediction()