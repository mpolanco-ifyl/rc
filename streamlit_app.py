import streamlit as st
import openai

# Obtener la API key de OpenAI
openai_api_key = st.text_input("Ingrese su API Key de OpenAI")

# Inicializar el cliente OpenAI
openai.api_key = openai_api_key

# Pedir al usuario que ingrese la instrucción
instruction = st.text_input("Ingrese la instrucción")

# Realizar la consulta a OpenAI
response = openai.Completion.create(
    engine="davinci",
    prompt=instruction,
    max_tokens=100
)

# Mostrar el resultado
st.write("La respuesta de GPT-3 es:")
st.write(response['choices'][0]['text'])
