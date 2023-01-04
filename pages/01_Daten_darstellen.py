import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Physik",
    page_icon="🔭"
)

st.write("# Daten graphisch darstellen")

st.markdown('Gib in die erste Zeile die x-Werte durch ein "," getrennt ein und in die zweite Zeile die y-Werte. Dezimalzahlen werden mit einem "." eingegeben, also z.B. "2.3".')
eingabe_x_werte = st.text_input("x-Werte:")
eingabe_y_werte = st.text_input("y-Werte:")
label_xAchse = st.text_input("Beschriftung der x-Achse")
label_yAchse = st.text_input("Beschriftung der y-Achse")

x_werte = np.fromstring(eingabe_x_werte, dtype=float, sep=',')
y_werte = np.fromstring(eingabe_y_werte, dtype=float, sep=',')

fig, ax = plt.subplots()

ax.set_xlabel(label_xAchse)
ax.set_ylabel(label_yAchse)
ax.scatter(x_werte, y_werte)

zeichne_fit = st.checkbox('Kurvenanpassung')

if zeichne_fit:
    grad = st.slider('Grad des Polynoms für Anpassung', 1, 5, 1)
    x_s=np.arange(np.amin(x_werte), np.amax(x_werte),(np.amax(x_werte)-np.amin(x_werte))/1000)

    model=np.polyfit(x_werte,y_werte,grad)
    model_f=np.poly1d(model)

    ax.plot(x_s,model_f(x_s),color="green")

    x = sp.symbols('x')
    f = sp.Function('f')
    f = 0*x
    zaehler = 0

    for zaehler in range(len(model)):
        summand = sp.parse_expr("%f * x**(%d)" % (model[zaehler], len(model)-zaehler-1))
        f += summand
    st.markdown('Funktionsgleichung der Ausgleichskurve')
    st.latex('f(x) = ' + sp.latex(f))

st.pyplot(fig)