from langchain_ollama import ChatOllama
from config import settings
from state import AgentState
from tools import tools


model = ChatOllama(
    model=settings.OLLAMA_MODEL,
    base_url=settings.OLLAMA_BASE_URL,
    temperature=0
).bind_tools(tools)

def call_agent_model(state: AgentState) -> dict:
    """Agent node that passes input state to ChatOllama."""
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}