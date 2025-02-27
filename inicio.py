import streamlit as st
from PIL import Image
st.title("Mi primera app")
st.header("Devon Aoki")
st.write("fast and furious")
image= Image.open('Sukicar.jpg')
st.image(image)
texto= st.text_input('Escribe algo','Text')
st.write('El texto escrito es','Text')
