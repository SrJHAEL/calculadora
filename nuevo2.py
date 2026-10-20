import streamlit as st

st.title("calcuradora de promedio escolar")

n1 = st.number_input("nota 1", min_value=0.0, max_value=5.0)
n2 = st.number_input("nota 2", min_value=0.0, max_value=5.0)
n3 = st.number_input("nota 3", min_value=0.0, max_value=5.0)
n4 = st.number_input("nota 4", min_value=0.0, max_value=5.0)

if st.button("Calcular"):
   promedio = (n1 + n2 + n3 + n4) / 4
   st.write(f"Tu promedio es {promedio:.1f}")
   
   if promedio >= 4.5:
        st.write("excelente")
   elif promedio >= 3.0:
        st.write("esta bien")
   else:
        st.write("dedicate a otra cosa que el estudio no es lo tuyo")
