import streamlit as st
from src.services.question_answerer import generate_answer
from src.config import validate_api_key


def render_questions_page():
    """Render the Q&A view for recruiter questions."""
    st.header("Answer Recruiter Questions")

    # Back button
    if st.button("< Back"):
        st.session_state.current_view = "main"
        st.rerun()

    st.divider()

    # Initialize session state
    if "profile" not in st.session_state:
        from src.storage.profile_manager import load_profile
        st.session_state.profile = load_profile()

    # Check prerequisites
    profile = st.session_state.get("profile")
    about_me = profile.about_me if profile else ""
    cv_text = profile.cv_text if profile else ""
    job_description = st.session_state.get("job_description", "")

    if not about_me or not cv_text:
        st.warning("Please set up your profile first (About Me and CV).")
        return

    if not job_description:
        st.warning("Please parse a job posting first.")
        return

    if not validate_api_key():
        st.error("Gemini API key not configured. Please add GEMINI_API_KEY to your .env file.")
        return

    # Question input
    question = st.text_area(
        "Enter the recruiter's question",
        value=st.session_state.get("current_question", ""),
        placeholder="Example: Why do you want to work with us?\nOr: Tell us about your experience with Python...",
        height=100
    )

    # Generate button
    if st.button("Generate Answer", type="primary"):
        if question:
            st.session_state.current_question = question
            with st.spinner("Generating answer..."):
                try:
                    answer = generate_answer(
                        question=question,
                        about_me=about_me,
                        cv_text=cv_text,
                        job_description=job_description
                    )
                    st.session_state.current_answer = answer
                except Exception as e:
                    st.error(f"Error generating answer: {str(e)}")
        else:
            st.warning("Please enter a question.")

    # Display answer
    if st.session_state.get("current_answer"):
        st.divider()
        st.subheader("Your Answer")

        st.text_area(
            "Generated Answer",
            value=st.session_state.current_answer,
            height=300,
            label_visibility="collapsed"
        )

        # Action buttons
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("Clear", use_container_width=True):
                st.session_state.current_question = ""
                st.session_state.current_answer = ""
                st.rerun()
