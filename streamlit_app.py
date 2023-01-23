import streamlit as st
import openai

# Pedir la clave de OpenAI
st.title('Analizador de texto con GPT-3')
st.write('Por favor ingrese su clave de OpenAI para autenticar la aplicación.')
openai_key = st.text_input('Clave de OpenAI')

# Botón para autenticar
if st.button('Ingresar'):
    openai.api_key = openai_key
    st.success('Clave de OpenAI ingresada exitosamente.')

# Pedir el texto a analizar
if openai.api_key:
    st.write('Ingrese el texto que desea analizar.')
    text = st.text_area('Texto')

# Botón para analizar
if st.button('Analizar'):
    # Analizar el texto con GPT-3
    prompt = openai.Completion.create(
        engine="davinci",
        prompt=text,
        max_tokens=50,
        temperature=0.7,
        top_p=1
    )
    # Mostrar el resultado
    st.write('Pregunta:', prompt.choices[0].text)
    st.write('Conclusión:', prompt.choices[1].text)
