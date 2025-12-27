import streamlit as st

# Page config
st.set_page_config(
    page_title="AutoCover - Cover Letter Generator",
    page_icon="",
    layout="wide"
)

# Initialize session state
if "current_view" not in st.session_state:
    st.session_state.current_view = "main"
if "job_parsed" not in st.session_state:
    st.session_state.job_parsed = False
if "job_url" not in st.session_state:
    st.session_state.job_url = ""
if "job_description" not in st.session_state:
    st.session_state.job_description = ""
if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = ""
if "current_question" not in st.session_state:
    st.session_state.current_question = ""
if "current_answer" not in st.session_state:
    st.session_state.current_answer = ""
if "job_notes" not in st.session_state:
    st.session_state.job_notes = ""

# Header with profile button
col1, col2 = st.columns([4, 1])
with col1:
    st.title("AutoCover")
with col2:
    if st.session_state.current_view != "profile":
        if st.button("Set up your profile", use_container_width=True):
            st.session_state.current_view = "profile"
            st.rerun()

# View routing
if st.session_state.current_view == "main":
    from src.components.main_page import render_main_page
    render_main_page()
elif st.session_state.current_view == "profile":
    from src.components.profile_page import render_profile_page
    render_profile_page()
elif st.session_state.current_view == "cover_letter":
    from src.components.cover_letter import render_cover_letter
    render_cover_letter()
elif st.session_state.current_view == "questions":
    from src.components.questions_page import render_questions_page
    render_questions_page()
