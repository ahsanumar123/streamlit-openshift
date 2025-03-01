#import streamlit as st
#selection = st.selectbox(label = "Select One", options =["papu", "chapu","tapu"], index=0)
#st.write(selection)


import streamlit as st
from pptx import Presentation

# Streamlit App Title
st.title("PowerPoint Slide Viewer with Notes")

# File Upload
uploaded_file = st.file_uploader("Upload a PowerPoint file (.pptx)", type=["pptx"])

if uploaded_file:
    # Load Presentation
    prs = Presentation(uploaded_file)
    
    # Extract slides and notes
    slides = {f"Slide {i+1}": slide.notes_slide.text.strip() if slide.has_notes_slide else "No notes available" for i, slide in enumerate(prs.slides)}
    
    if slides:
        # Dropdown for Slide Selection
        selected_slide = st.selectbox("Select a Slide", list(slides.keys()))
        
        # Display Notes
        if selected_slide:
            st.subheader("Slide Notes")
            st.write(slides[selected_slide])
    else:
        st.warning("No slides found in the uploaded PowerPoint.")
