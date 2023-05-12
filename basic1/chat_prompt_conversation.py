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


def get_human_message_prompt():
    #template="You are a helpful assistant that translates {input_language} to {output_language}."
    #system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template="{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    return human_message_prompt


def get_system_message_prompt():
    prompt=PromptTemplate(
        template="You are a helpful assistant that translates {input_language} to {output_language}.",
        input_variables=["input_language", "output_language"],
    )
    system_message_prompt = SystemMessagePromptTemplate(prompt=prompt)
    return system_message_prompt


def chat_message_prompt(system_message_prompt, human_message_prompt):
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    return chat_prompt


def get_chat_conversation(chat_prompt):
    llm = OpenAI(temperature=0.9)
    # create llm chain
    chain = LLMChain(llm=llm, prompt=chat_prompt)

    # execute chain
    #result = chain.run({'English', 'French', 'I love programming.'})
    result = chain.run({'input_language':'English', 'output_language':'French', 'text':'I love programming.'})
    print(result)

    result2 = chain.run({'input_language':'English', 'output_language':'French', 'text':'What do I like?'})
    print(result2)
    

if __name__ == "__main__":
    system_message_prompt = get_system_message_prompt()
    human_message_prompt = get_human_message_prompt()
    chat_prompt = chat_message_prompt(system_message_prompt, human_message_prompt)
    # get a chat completion from the formatted messages
    output1 = chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages()
    print(output1)

    get_chat_conversation(chat_prompt)
