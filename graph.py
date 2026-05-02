from typing import TypedDict
from langgraph.graph import StateGraph, END
from tools import search_web

class GraphState(TypedDict):
    question: str
    answer: str

def router(state):
    question = state["question"]

    if "debales" in question.lower():
        return "rag"

    return "search"

def rag_node(state):
    return {
        "answer": "This answer came from RAG system."
    }

def search_node(state):
    result = search_web(state["question"])

    return {
        "answer": result
    }

workflow = StateGraph(GraphState)

workflow.add_node("rag", rag_node)
workflow.add_node("search", search_node)

workflow.set_conditional_entry_point(
    router,
    {
        "rag": "rag",
        "search": "search"
    }
)

workflow.add_edge("rag", END)
workflow.add_edge("search", END)

app_graph = workflow.compile()