import streamlit as st
import sympy as sp
import numpy as np
import matplotlib as plt

st.set_page_config(
    page_title="Physik",
    page_icon="🔭"
)

st.write("# Daten graphisch darstellen")

st.markdown('Gib in die erste Zeile die x-Werte durch ein "," getrennt ein und in die zweite Zeile die y-Werte. Dezimalzahlen werden mit einem "." eingegeben, also z.B. "2.3".')