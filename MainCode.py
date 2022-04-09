##################
##    IMPORT    ##
##################
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

##################
## PAGE TITLE   ##
##################
image = Image.open('DNA.jpeg')
st.image(image, use_column_width = True)

st.write("""
# DNA Nucleotides Counter Web App


""")
