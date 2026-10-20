import streamlit as st

st.title("Calculadora")

n1 = st.number_input("Primer número", value=0.0)
n2 = st.number_input("Segundo número", value=0.0)
n3 = st.number_input("Tercer número", value=0.0)
n4 = st.number_input("Cuarto número", value=0.0)

if st.button("Calcular"):
    suma = n1 + n2 + n3 + n4
    st.write(f"La suma es {suma}")
    st.write(f"La suma dividida entre 4 es {suma / 4}")
