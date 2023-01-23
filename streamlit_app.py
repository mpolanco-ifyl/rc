import streamlit as st 
import openai

st.title("OpenAI GTP App") 

# Pedir API key de OpenAI al usuario
openai_api_key = st.text_input("Ingrese su API key de OpenAI")

# Crear objeto API de OpenAI
api = openai.API(
    session_or_api_key=openai_api_key
)

# Pedir al usuario que ingrese el texto para analizar
text_to_analyze = st.text_area("Escriba el texto para analizar")

# Realizar el analisis con GTP
completion = api.engine("davinci").completions.create(
    prompt=text_to_analyze,
    max_tokens=50,
    temperature=0.7,
    top_p=1,
    stream="problems_and_solutions",
    logprobs=3,
)

# Mostrar el resultado al usuario
st.write("**Problem:**")
st.write(completion.choices[0].text)

st.write("**Conclusion:**")
st.write(completion.choices[1].text)
