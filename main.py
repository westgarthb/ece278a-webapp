# installl dependencies necessary
import streamlit as st
import numpy as np
from Pyramids.pyramids import display_pyramids
from Wavelets.wavelets import display_wavelets

# Title
st.title("Pyramids and Wavelets")

st.subheader("by Brycen Westgarth & Jackie Burd")

add_selectbox = st.sidebar.selectbox(
    "Page Select",
    ("Pyramids", "Wavelets")
)

if add_selectbox == 'Pyramids':
    display_pyramids()
else:
    display_wavelets()


# TODO: Wavelets - Page 3
    # wavelets_display()
    # Applition Tool

# TODO: Conclusion (JACKIE)

# Potential Application
            # Slider Tool Blending of faces
            # Embossing - Laplacian Pyramid
            # Blending of face - gaussian and lapacan pyramid
                # Make up imaginary people