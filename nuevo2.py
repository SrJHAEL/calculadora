import streamlit as st

st.title("Calculadora")

n1 = st.number_input("nota 1", value=0)
n2 = st.number_input("nota 2", value=0)
n3 = st.number_input("nota 3", value=0)
n4 = st.number_input("nota 4", value=0)

if st.button("Calcular"):
    suma = n1 + n2 + n3 + n4
    st.write(f"el resultado es {suma / 4}")
