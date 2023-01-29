import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

st.set_page_config(
    page_title="Physik",
    page_icon="🔭"
)

st.write("")
st.markdown('''
# Daten graphisch darstellen
Gib in die erste Zeile die x-Werte durch ein "," getrennt ein und in die zweite Zeile die y-Werte. Dezimalzahlen werden mit einem "." eingegeben, also z.B. "2.3".
''')


anzahlDatensaetze = st.slider('Anzahl Datensätze', 1, 5, 1)
bezeichnungDatensaetze = []

for i in range(anzahlDatensaetze):
    bezeichnung = "Datensatz" + str(i+1)
    bezeichnungDatensaetze.append(bezeichnung)

tabs = st.tabs(bezeichnungDatensaetze)

eingabe_x_werte = []
eingabe_y_werte = []

for i in range(len(tabs)):
    with tabs[i]:
        st.markdown("#### Datensatz %s" % str(i+1))
        eingabe_x_werte.append(st.text_input("x-Werte %d:" % (i+1)))
        eingabe_y_werte.append(st.text_input("y-Werte %d:" % (i+1)))

st.markdown('### Beschriftung der Achsen')

label_xAchse = st.text_input("Beschriftung der x-Achse")
label_yAchse = st.text_input("Beschriftung der y-Achse")

try:
    zeichne_fit = st.checkbox('Kurvenanpassung')
    fig, ax = plt.subplots()

    ax.set_xlabel(label_xAchse)
    ax.set_ylabel(label_yAchse) 
    legende = []
    funktionen = []
    
    for i in range(len(eingabe_x_werte)):
        x_werte = np.fromstring(eingabe_x_werte[i], dtype=float, sep=',')
        y_werte = np.fromstring(eingabe_y_werte[i], dtype=float, sep=',')    
        ax.scatter(x_werte, y_werte)
        #legende.append('Datensatz %d' % (i+1))

    if zeichne_fit:
        anpassung = st.radio("Art der Funktionsanpassung", ('ganzrationale Funktion', 'Exponentialfunktion', 'Trigonometrische Funktion'))
        for i in range(len(eingabe_x_werte)):
            x_werte = np.fromstring(eingabe_x_werte[i], dtype=float, sep=',')
            y_werte = np.fromstring(eingabe_y_werte[i], dtype=float, sep=',')
            x_s=np.arange(np.amin(x_werte), np.amax(x_werte),(np.amax(x_werte)-np.amin(x_werte))/1000)

            x = sp.symbols('x')
            f = sp.Function('f')

            if anpassung == "ganzrationale Funktion":
                bezeichnung_grad = 'Grad des Polynoms für Anpassung von Datensatz %d' % (i+1)
                if i==0:
                    st.markdown('### Grad der Polynome')
                grad = st.slider(bezeichnung_grad, 1, 5, 1)
                model=np.polyfit(x_werte,y_werte,grad)
                model_f=np.poly1d(model)
                ax.plot(x_s,model_f(x_s))
                
                f = 0*x
                zaehler = 0

                for zaehler in range(len(model)):
                    summand = sp.parse_expr("%f * x**(%d)" % (model[zaehler], len(model)-zaehler-1))
                    f += summand
                funktionen.append(r'f_{%d}(x) = ' % (i+1) + sp.latex(f))

            elif anpassung == "Exponentialfunktion":
                # Fit the function a * np.exp(b * t) to x and y
                popt, pcov = curve_fit(lambda t, a, b, c: a * np.exp(b * t) + c, x_werte, y_werte)
                # Extract the optimised parameters
                a = popt[0]
                b = popt[1]
                c = popt[2]
                x_fitted_curve_fit = np.linspace(np.min(x_werte), np.max(x_werte), 100)
                y_fitted_curve_fit = a * np.exp(b * x_fitted_curve_fit) + c
                ax.plot(x_fitted_curve_fit, y_fitted_curve_fit, label=r'curve\_fit')
                f = np.round(a,3)*sp.exp(np.round(b,3)*x)+np.round(c,3)
                funktionen.append(r'f_{%d}(x) = ' % (i+1) + sp.latex(f))
            
            elif anpassung == "Trigonometrische Funktion":
                # Fit the function a * np.exp(b * t) to x and y
                popt, pcov = curve_fit(lambda t, a, b, c, d: a * np.sin(b * (t - c)) + d, x_werte, y_werte)
                # Extract the optimised parameters
                a = popt[0]
                b = popt[1]
                c = popt[2]
                d = popt[3]
                x_fitted_curve_fit = np.linspace(np.min(x_werte), np.max(x_werte), 100)
                y_fitted_curve_fit = a * np.sin(b * (x_fitted_curve_fit-c)) + d
                ax.plot(x_fitted_curve_fit, y_fitted_curve_fit, label=r'curve\_fit')
                f = np.round(a,3)*sp.sin(np.round(b,3)*(x-np.round(c,3)))+np.round(d,3)
                funktionen.append(r'f_{%d}(x) = ' % (i+1) + sp.latex(f))

    st.markdown('''
    ### Funktionsgleichungen
    Funktionsgleichung der Ausgleichskurve
    ''')
    for funk in funktionen:
        st.latex(funk)
    #ax.legend(legende)
    st.pyplot(fig)

except:
    st.markdown("Korrekte Daten eingeben.")