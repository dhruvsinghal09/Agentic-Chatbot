import uuid

import streamlit as st

from src.langgraphagenticai.LLMs.loadllms import LoadLLMs
from src.langgraphagenticai.commonconstants.constants import SELECTED_USECASE
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamLit
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamLitUi


def load_langgraph_agentic_app():
    ui = LoadStreamLitUi()

    #create thread id for in memorySaver()
    if "thread_id" not in st.session_state:
        st.session_state["thread_id"] = str(uuid.uuid4())

    #reset thread to start a new conversation
    if st.button("Reset Conversation"):
        st.session_state["thread_id"] = str(uuid.uuid4())
        st.success("Conversation reset. A new thread has been created.")

    st.sidebar.write(f"Current Thread ID: {st.session_state['thread_id']}")

    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from ui.")
        return

    user_message = st.chat_input("Enter you message:")

    if user_message:
        load_llm = LoadLLMs(user_input)
        llm = load_llm.load_llms()
        graph_builder = GraphBuilder(llm)
        usecase = user_input[SELECTED_USECASE]
        graph = graph_builder.get_graph_by_usecase(usecase)
        DisplayResultStreamLit(graph, usecase, user_message).display_result_on_ui()
    else:
        st.error("Error: Failed to load user input from ui.")
        return
