import streamlit as st

class DisplayResultStreamLit:
    def __init__(self,graph,usecase,user_message):
        self.graph=graph
        self.usecase=usecase
        self.user_message=user_message

    def display_result_on_ui(self):
        usecase=self.usecase
        graph=self.graph
        if usecase=="Basic Chatbot":
            for event in graph.stream({"messages":("user",self.user_message)},):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(self.user_message)
                    with st.chat_message("assistant"):
                        st.write(value['messages'].content)