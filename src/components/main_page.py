import streamlit as st
from src.services.linkedin_scraper import fetch_job_description


def render_main_page():
    """Render the main page with job URL input."""
    st.markdown("*Generate personalized cover letters and answers using AI*")

    # URL input
    job_url = st.text_input(
        "LinkedIn Job Posting URL",
        value=st.session_state.get("job_url", ""),
        placeholder="https://www.linkedin.com/jobs/view/XXXXXXXXXX"
    )

    # Parse button
    if st.button("Parse", type="primary"):
        if job_url:
            with st.spinner("Fetching job description..."):
                description, success = fetch_job_description(job_url)
                if success:
                    st.session_state.job_description = description
                    st.session_state.job_url = job_url
                    st.session_state.job_parsed = True
                    # Clear previous generation results
                    st.session_state.cover_letter = ""
                    st.session_state.current_answer = ""
                    st.rerun()
                else:
                    st.error(description)
        else:
            st.warning("Please enter a LinkedIn job URL.")

    # Manual text input option
    with st.expander("Or paste job description manually"):
        manual_description = st.text_area(
            "Job Description",
            height=200,
            placeholder="Paste the job description here..."
        )
        if st.button("Use This Description"):
            if manual_description.strip():
                st.session_state.job_description = manual_description.strip()
                st.session_state.job_url = ""
                st.session_state.job_parsed = True
                # Clear previous generation results
                st.session_state.cover_letter = ""
                st.session_state.current_answer = ""
                st.rerun()
            else:
                st.warning("Please paste a job description.")

    # Show action buttons after successful parse
    if st.session_state.get("job_parsed"):
        st.success("Job description loaded!")

        # Show preview of job description
        with st.expander("View Job Description", expanded=False):
            st.text(st.session_state.job_description)

        st.divider()

        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Cover Letter", type="primary", use_container_width=True):
                st.session_state.current_view = "cover_letter"
                st.rerun()
        with col2:
            if st.button("Questions", type="secondary", use_container_width=True):
                st.session_state.current_view = "questions"
                st.rerun()
