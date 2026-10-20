import streamlit as st

st.title("Calculadora")

n1 = st.number_input("nota_1", value= )
n2 = st.number_input("nota_2", value= )
n3 = st.number_input("nota_3", value= )
n4 = st.number_input("nota_4", value= )

if st.button("Calcular"):
    suma = n1 + n2 + n3 + n4
    st.write(f"La suma es {suma}")
    st.write(f"La suma dividida entre 4 es {suma / 4}")
