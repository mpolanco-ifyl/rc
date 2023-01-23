import streamlit as st
import openai

# Autenticar con la API de OpenAI
openai.api_key = "mi-clave-api"

st.title("GPT-3 para resolver problemas y conclusiones")

# Obtener el texto
texto = st.text_area("Ingrese el texto a analizar")

# Hacer una solicitud a la API de OpenAI
prompt = {
    "prompt": texto,
    "temperature": 0.7,
    "max_tokens": 256,
}

# Obtener el resultado de la API
response = openai.Completion.create(**prompt)

# Mostrar el resultado
st.write("**Problema:**", response.choices[0]['text'])
st.write("**Conclusion:**", response.choices[1]['text'])
