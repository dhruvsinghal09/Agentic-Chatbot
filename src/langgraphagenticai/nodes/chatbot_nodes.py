from langchain_community.chat_models import ChatOllama
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from src.langgraphagenticai.state.graph_state import State


class ChatbotNodes():
    def __init__(self, llm):
        self.llm = llm

    def chatbot(self,state:State):
        """This node will be used to retrieve data from llm by chatbot"""
        llm=self.llm
        result=llm.invoke(state["messages"])
        return {"messages":result}