import streamlit as st


def app():
    st.title('Language Learning Hub 📚')
    st.write('Boost Your Language Skills with Personalized Exercises!')

    # List of modules
    if st.button("Grammar Quest"):
        st.session_state["current_page"] = "grammar_fun"
        st.rerun()

    if st.button("Visual Insights"):
        st.session_state["current_page"] = "image_comprehension"
        st.rerun()

    if st.button("Reading Interpretation & Translation"):
        st.session_state["current_page"] = "reading_translation"
        st.rerun()
