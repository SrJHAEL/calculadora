import streamlit as st

st.title("yeni te amo pero es que tú eres muy (...) mira lo que tienes que hacer esto es una calculadora de promedios colocas tus cuatro notas y te dará el resultado")

n1 = st.number_input("nota 1", value=0.0)
n2 = st.number_input("nota 2", value=0.0)
n3 = st.number_input("nota 3", value=0.0)
n4 = st.number_input("nota 4", value=0.0)

if st.button("Calcular"):
    suma = n1 + n2 + n3 + n4
    st.write(f"el resultado es {suma / 4}")
nota = 4.0
if nota >= 4.5:
print ("exelente")
elif nota >= 3.0:
print ("esta bien")
else =
print ("dedicate a otra cosa que el estudio no es lo tuyo")
