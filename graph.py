from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition

from state import AgentState
from agent import call_agent_model
from tools import tools

def build_agent_graph():
    """Build and compile the ReAct agent graph state machine."""
    builder = StateGraph(AgentState)

    # Register Nodes
    builder.add_node("agent", call_agent_model)
    builder.add_node("tools", ToolNode(tools))

    # Configure Flow
    builder.set_entry_point("agent")
    
    # Conditional edge: evaluate if the agent emitted a tool call
    builder.add_conditional_edges("agent", tools_condition)
    
    # Send tool output back to agent model
    builder.add_edge("tools", "agent")

    return builder.compile()

app = build_agent_graph()