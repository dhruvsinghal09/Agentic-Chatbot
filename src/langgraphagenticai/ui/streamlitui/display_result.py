import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage

from src.langgraphagenticai.memory.chat_history import ChatHistory


class DisplayResultStreamLit:
    def __init__(self,graph,usecase,user_message):
        self.graph=graph
        self.usecase=usecase
        self.user_message=user_message

    def display_result_on_ui(self):
        usecase=self.usecase
        graph=self.graph
        session_id = st.session_state["thread_id"]
        if usecase=="Basic Chatbot":
            # load or create chat history
            history = ChatHistory.get_session_history(session_id)

            # add user message to history
            history.add_message(HumanMessage(content=self.user_message))

            # build messages from history
            messages = history.messages

            for event in graph.stream({"messages": messages}):
                print(event.values())
                for value in event.values():
                    response = value["messages"].content

                    # store assistant response
                    history.add_message(AIMessage(content=response))
                    print(response)

                    # UI
                    with st.chat_message("user"):
                        st.write(self.user_message)
                    with st.chat_message("assistant"):
                        st.write(response)