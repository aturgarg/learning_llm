from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.utilities import BingSearchAPIWrapper
from langchain.tools import DuckDuckGoSearchRun
from langchain.chat_models import ChatOpenAI
from langchain.tools import AIPluginTool, Tool, BaseTool, ClickTool

def execute_search(): 
    search = DuckDuckGoSearchRun()     
    result = search.run("Where is Paris? How many trees are there in paris?")
    print(result)

def execute_agent():    
    
    llm = ChatOpenAI(temperature=0)
    search = DuckDuckGoSearchRun()
    duckduckgo_tool = Tool(
        name='DuckDuckGo Search',
        func= search.run,
        description="Useful for when you need to do a search on the internet to find information that another tool can't find. be specific with your input."
    )

    #tools = load_tools(["serpapi", "llm-math"], llm=llm)
    tools = [duckduckgo_tool]
       
    agent = initialize_agent(tools=tools, 
                             llm=llm,
                             agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                             verbose = True)
    
    agent.run("Where is Paris? How many trees are there in paris?")
  

if __name__ == "__main__":
    execute_agent()
    #execute_search()
