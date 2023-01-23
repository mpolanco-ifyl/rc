import streamlit as st
import openai

# Pedir la clave de OpenAI al usuario
st.title("Autenticación de OpenAI")
openai_key = st.text_input("Ingrese su clave de OpenAI")

# Botón para autenticar
if st.button("Ingresar"):
    # Aviso de confirmación
    st.success("Clave de OpenAI confirmada")

# Pedir el texto al usuario
st.title("Análisis de texto")
text = st.text_area("Ingrese el texto a analizar")

# Botón para analizar
if st.button("Analizar"):
    # Autenticar con la clave de OpenAI
    openai.api_key = openai_key
    # Usar GPT-3 para encontrar el problema y la conclusión
    completion = openai.Completion()
    response = completion.create(
        prompt=text,
        engine="text-davinci-003",
        temperature=0.7,
        max_tokens=150,
        top_p=1,
    )
    # Mostrar el resultado
    st.write("**Problema:**", response["choices"][0]["text"])
    st.write("**Conclusión:**", response["choices"][1]["text"])
