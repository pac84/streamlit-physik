import streamlit as st

def zeilen_lesen(von, bis):
    with open(r"latex.tex", 'r') as fp:
        # lines to read
        line_numbers = []
        for i in range(von,bis+1):
            line_numbers.append(i)
        # To store lines
        lines = []
        for i, line in enumerate(fp):
            # read line 4 and 7
            if i in line_numbers:
                lines.append(line.strip())
            elif i > 7:
                # don't read after line 7 to save time
                break
    return lines

def lineArrayToString(von, bis):
    lineArray = zeilen_lesen(von,bis)
    ausgabe = ""
    for item in lineArray:
        ausgabe += item + "\n"
    return ausgabe[:-1]

tex = lineArrayToString(6,9)
print(tex)

st.latex(tex)