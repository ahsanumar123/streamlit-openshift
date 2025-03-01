import streamlit as st
from pptx import Presentation

st.title("PowerPoint Slide Viewer with Notes")

uploaded_file = st.file_uploader("Upload a PowerPoint file (.pptx)", type=["pptx"])

if uploaded_file:
    prs = Presentation(uploaded_file)
    
    # Create a dictionary of slide labels and their corresponding notes.
    slides = {}
    for i, slide in enumerate(prs.slides):
        slide_label = f"Slide {i+1}"
        if slide.has_notes_slide:
            # Access notes text via the notes_text_frame property
            notes_text = slide.notes_slide.notes_text_frame.text.strip()
        else:
            notes_text = "No notes available"
        slides[slide_label] = notes_text

    if slides:
        selected_slide = st.selectbox("Select a Slide", list(slides.keys()))
        st.subheader("Slide Notes")
        st.write(slides[selected_slide])
    else:
        st.warning("No slides found in the uploaded PowerPoint.")
