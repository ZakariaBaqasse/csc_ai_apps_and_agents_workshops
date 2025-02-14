from langchain_ollama import ChatOllama
from langchain_community.tools import TavilySearchResults
from langgraph.prebuilt import create_react_agent
import asyncio


# Initialize the model and tool
llm = ChatOllama(model="llama3.2")
search_tool = TavilySearchResults()


# Build the graph
tools = [search_tool]
app = create_react_agent(llm, tools)


with open("./graph.png","wb") as file:
  file.write(app.get_graph(xray=True).draw_mermaid_png())

final_state = app.invoke(
    {"messages": [{"role": "user", "content": "who won the last world cup?"}]},
    config={"configurable": {"thread_id": 42}}
)
print(final_state["messages"][-1].content)

# async def invoke_graph():
#   async for event in app.astream({"messages": [{"role": "user", "content": "who won the last world cup?"}]}, config={"configurable": {"thread_id": 42}}):
#       for k, v in event.items():
#         if k != "__end__":
#             print(v)

# asyncio.run(invoke_graph())
