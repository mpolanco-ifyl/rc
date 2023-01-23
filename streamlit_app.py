import streamlit as st
import openai

# Solicitando la API Key de OpenAI
openai_api_key = st.text_input("Por favor introduzca la API Key de OpenAI:")

# Inicializando la API
openai.api_key = openai_api_key

# Texto del artículo
article_text = st.text_area(
    "Introduzca el texto del artículo aquí:")

# Obteniendo el problema y conclusión
if article_text:
    gpt = openai.Completion.create(
        engine="davinci",
        prompt=article_text,
        max_tokens=500,
        temperature=0.7,
        top_p=1,
        n=1,
    )

    problem_text = gpt['choices'][0]['text']
    conclusion_text = gpt['choices'][1]['text']

    # Mostrando los resultados
    st.write("El problema es:")
    st.write(problem_text)
    st.write("La conclusión es:")
    st.write(conclusion_text)
