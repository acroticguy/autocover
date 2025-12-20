import streamlit as st
from src.services.cover_letter_generator import generate_cover_letter
from src.config import validate_api_key


def render_cover_letter():
    """Render the cover letter generation view."""
    st.header("Cover Letter")

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

    # Generate if not already generated
    if not st.session_state.get("cover_letter"):
        with st.spinner("Generating your cover letter..."):
            try:
                cover_letter = generate_cover_letter(
                    about_me=about_me,
                    cv_text=cv_text,
                    job_description=job_description,
                    temperature=0.7
                )
                st.session_state.cover_letter = cover_letter
            except Exception as e:
                st.error(f"Error generating cover letter: {str(e)}")
                return

    # Display generated cover letter
    st.subheader("Your Cover Letter")

    # Text area for viewing/copying
    st.text_area(
        "Cover Letter",
        value=st.session_state.cover_letter,
        height=400,
        label_visibility="collapsed"
    )

    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        st.download_button(
            label="Download",
            data=st.session_state.cover_letter,
            file_name="cover_letter.txt",
            mime="text/plain",
            use_container_width=True
        )
    with col2:
        if st.button("Regenerate", use_container_width=True):
            st.session_state.cover_letter = ""
            st.rerun()
