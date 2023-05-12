from langchain.llms import OpenAI


def get_suggestions():
    llm = OpenAI(model_name="text-davinci-003")
    text = "explain large language models in couple of sentences"
    result1 = llm(text)
    print(result1)
    

if __name__ == "__main__":
    get_suggestions()