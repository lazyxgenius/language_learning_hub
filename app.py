import streamlit as st
from modules import home, visual_insights, grammar_quest, reading_translation


# Initialize session state
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "home"

# Load the correct page based on session state
if st.session_state["current_page"] == "home":
    home.app()
elif st.session_state["current_page"] == "grammar_fun":
    grammar_quest.app()
elif st.session_state["current_page"] == "image_comprehension":
    visual_insights.app()
elif st.session_state["current_page"] == "reading_translation":
    reading_translation.app()
