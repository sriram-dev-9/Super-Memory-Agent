from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated, Sequence
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tools import tools

load_dotenv()

class AgentState(TypedDict):
    messages : Annotated[Sequence[BaseMessage],add_messages]

#Gemini Setup
# llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite-preview-06-17')

# Open AI GPT 4.1 mini Setup
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"
llm = ChatOpenAI(
    openai_api_base=endpoint,
    model_name=model
).bind_tools(tools=tools)



def agent_node(state:AgentState)->AgentState:
    """The main agent node"""
    system_prompt = SystemMessage(
        """You are a helpful Personal Agent with supermemory"""
    )
    prompt = state['messages']
    response = llm.invoke([system_prompt]+prompt)
    return {'messages':[response] + prompt}

tool_node = ToolNode(tools=tools)

def should_continue(state: AgentState) -> str:
    """Simple decider that only checks for tool calls"""
    messages_dict = state["messages"]
    last_message = messages_dict[-1]
    if not last_message.tool_calls:
        return "end"
    else: 
        return "continue"

graph = StateGraph(AgentState)
tool_node = ToolNode(tools=tools)
graph.add_node("tool_node",tool_node)
graph.add_node("agent_node",agent_node)
graph.add_edge(START,"agent_node")
graph.add_edge("tool_node","agent_node")
graph.add_conditional_edges(
    "agent_node",
    should_continue,
    {
        "continue": "tool_node",
        "end": END,
        "": "tool_node"
    }
)
agent = graph.compile()


conversation_history = []
user_input = input("Command: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    inputs = {"messages": conversation_history}
    
    for chunk in agent.stream(inputs, {"recursion_limit": 35}, stream_mode="values"):
        message = chunk["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()
    
    final_result = agent.invoke(inputs)
    conversation_history = final_result["messages"]
    
    user_input = input("Command: ")