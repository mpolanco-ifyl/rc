import streamlit as st
import openai

# Pedir la clave de OpenAI
st.title('Analizador de texto con OpenAI GPT-3')
st.write('Por favor ingrese su clave de OpenAI para continuar.')
openai_key = st.text_input('Clave de OpenAI')

# Autenticar la clave de OpenAI
if openai_key:
    openai.api_key = openai_key
    st.success('Clave de OpenAI autenticada exitosamente.')

# Pedir el texto a analizar
if openai_key:
    st.write('Ingrese el texto que desea analizar.')
    text = st.text_area('Texto')

# Analizar el texto
if openai_key and text:
    prompt = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=150,
        temperature=0.7,
        top_p=1
    )
    conclusion = prompt.choices[0].text
    st.write('Pregunta:', prompt.prompt)
    st.write('Conclusión:', conclusion)

# Botón para analizar
if openai_key and text:
    if st.button('Analizar'):
        st.write('Pregunta:', prompt.prompt)
        st.write('Conclusión:', conclusion)
