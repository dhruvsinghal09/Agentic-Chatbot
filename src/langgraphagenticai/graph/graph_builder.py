from langgraph.checkpoint.memory import MemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph

from src.langgraphagenticai.nodes.chatbot_nodes import ChatbotNodes
from src.langgraphagenticai.state.graph_state import State


class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph_builder=StateGraph(State)

    def workflow(self):
        self.chatbotnodes=ChatbotNodes(self.llm)
        self.graph_builder.add_node("chatbot",self.chatbotnodes.chatbot)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)


    def get_graph_by_usecase(self,usecase:str):
        if usecase=="Basic Chatbot":
            self.workflow()
            return self.graph_builder.compile()
        else:
            raise ValueError(f"Unknown usecase: {usecase}")