import streamlit as st
from PIL import Image
st.title("Mi primera app")
st.header("Devon Aoki")
st.write("fast and furious")
image= Image.open('Sukicar.jpg')
st.image(image)
texto= st.text_input('Escribe algo','Text')
st.write('El texto escrito es','Text')
st.subheader("Columnas")
col1,col2= st.columns(2)
with col1:
  st.subheader("Primera columna")
  st.write("Conoces este carro?")
  resp= st.checkbox ("Si")
  if resp:
    st.write("Me encanta")
with col2:
  st.subheader("Segunda columna")
  modo= st.radio("A que personaje conoces",('Toreto','Suki','Brian'))
  if modo== 'Toreto':
    st.write('Es el personaje principal')
  if modo== 'Suki':
    st.write('Hablaremos sobre ella')
  if modo== 'Brian':
    st.write('Su nombre real es Paul')
st.subheader("Botones")
if st.button('Quien es Devon?'):
  st.write('Aun no defino que mostrar xd')
else:
  st.write('Porque no presionas')
with st.sidebar:
  st.subheader("configura la modalidad")
  
    
    
  
