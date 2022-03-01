import streamlit as st
import numpy as np
import random as rn
import pandas as pd
import pickle


st.title('Number Extractor')

if st.button('Reset extractor'):
    table_initial = np.arange(1,91)
    with open('outfile', 'wb') as fp:
        pickle.dump(table_initial, fp)


def number_extractor(x):

    n = rn.choice(x)
    x = x[x != n]

    return(x, n)

st.subheader('Table of numbers')
st.markdown("""
<style>
table td:nth-child(1) {
    display: none
}
table th:nth-child(1) {
    display: none
}
</style>
""", unsafe_allow_html=True)


table_numbers = pd.DataFrame(np.arange(1,91).reshape(-1,10))
table_numbers.columns = list(['A','B','C','D','E', 'F', 'G', 'H','I','L'])


with open ('outfile', 'rb') as fp:
    possible_numbers = pickle.load(fp)


def style_specific_cell(x):

    color = 'background-color: lightgreen'
    df1 = pd.DataFrame('', index=x.index, columns=x.columns)
    for i in range(0,9):
        for k in range(0,10):
            if x.iloc[i][k] not in list(possible_numbers): df1.iloc[i][k] = color
    return df1


st.table(table_numbers.style.apply(style_specific_cell, axis=None))


if st.button('Extract Number'):

    possible_numbers, extr = number_extractor(possible_numbers)
    with open('outfile', 'wb') as fp:
      pickle.dump(possible_numbers, fp)

    html_string = "<h3>"+ str(extr) + "</h3>"
    st.markdown(html_string, unsafe_allow_html=True)