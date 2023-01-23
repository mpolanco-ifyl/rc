import streamlit as st
import openai

# Pedir la API key de OpenAI al usuario
st.title('Analizador de texto con GPT-3')
st.write('Ingrese su API key de OpenAI para autenticarse:')
api_key = st.text_input('API Key')

# Botón para autenticarse
if st.button('Ingresar'):
    openai.api_key = api_key

# Pedir el texto al usuario
st.write('Ingrese el texto a analizar:')
texto = st.text_area('Texto')

# Botón para analizar
if st.button('Analizar'):
    # Usar GPT-3 para encontrar el problema y la conclusión
    prompt = f"Question: {texto}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        top_p=1
    )
    problema = response['choices'][0]['text']
    st.write('Problema:', problema)

    prompt = f"Conclusion: {texto}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        top_p=1
    )
    conclusion = response['choices'][0]['text']
    st.write('Conclusión:', conclusion)
