import streamlit as st
import sympy as sp
import numpy as np
import matplotlib as plt
from PIL import Image

image = Image.open('images/intro.png')

st.set_page_config(
    page_title="Physik",
    page_icon="🔭"
)

st.write("# Tools für Physik")

st.markdown(
    """
    Hier finden sich einige Tools, die in der Physik hilfreich sind. Auf der linken Seite findet sich ein Menü mit Links zu verschiedenen Tools.
    """
)

st.image(image)