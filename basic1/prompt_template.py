from langchain.prompts import PromptTemplate

def get_prompt():
    # create prompt
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )

    print(prompt.format(product="colorful socks"))


if __name__ == "__main__":
    get_prompt()
