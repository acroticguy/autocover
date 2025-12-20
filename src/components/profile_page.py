import streamlit as st
from src.services.pdf_extractor import extract_text_from_pdf
from src.storage.profile_manager import save_profile, load_profile


def render_profile_page():
    """Render the profile setup page."""
    st.header("Set Up Your Profile")

    # Back button
    if st.button("< Back"):
        st.session_state.current_view = "main"
        st.rerun()

    st.divider()

    # Load existing profile
    if "profile" not in st.session_state:
        st.session_state.profile = load_profile()

    # Two columns for About Me and CV
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("About Me")
        st.markdown("*Tell us about your background, motivations, and what makes you unique.*")

        about_me = st.text_area(
            "Your story",
            value=st.session_state.profile.about_me,
            height=300,
            placeholder="Example: I'm a software engineer with 5 years of experience who's passionate about building products that make a difference...",
            help="Describe your past experiences, what motivates you, your character, and career goals."
        )

        if about_me != st.session_state.profile.about_me:
            st.session_state.profile.about_me = about_me

    with col2:
        st.subheader("Your CV / Resume")

        # File uploader
        uploaded_file = st.file_uploader(
            "Upload your CV (PDF)",
            type=["pdf"],
            help="Upload your resume/CV in PDF format. The text will be extracted automatically."
        )

        if uploaded_file is not None:
            pdf_bytes = uploaded_file.read()
            extracted_text, success = extract_text_from_pdf(pdf_bytes)

            if success:
                st.session_state.profile.cv_text = extracted_text
                st.session_state.profile.cv_filename = uploaded_file.name
                st.success(f"Successfully extracted text from {uploaded_file.name}")
            else:
                st.error(extracted_text)

        # Show extracted text
        if st.session_state.profile.cv_text:
            if st.session_state.profile.cv_filename:
                st.caption(f"From: {st.session_state.profile.cv_filename}")

            cv_text = st.text_area(
                "Review and edit if needed",
                value=st.session_state.profile.cv_text,
                height=250,
                help="You can edit the extracted text if there are any issues."
            )

            if cv_text != st.session_state.profile.cv_text:
                st.session_state.profile.cv_text = cv_text
        else:
            st.info("Upload a PDF to extract your CV content.")

    # Single save button for entire profile
    st.divider()
    if st.button("Save Profile", type="primary"):
        save_profile(st.session_state.profile)
        st.success("Profile saved!")
