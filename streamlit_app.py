
import streamlit as st
import openai

# Pedir la clave de OpenAI
st.title("Autenticación de OpenAI")
openai_key = st.text_input("Ingrese su clave de OpenAI")

if openai_key:
    openai.api_key = openai_key
    st.success("Clave de OpenAI confirmada")

# Botón para analizar
if st.button("Analizar"):
    # Pedir el texto a analizar
    text = st.text_area("Escriba el texto a analizar")

    # Usar GPT-3 para encontrar el problema y la conclusión
    if text:
        prompt = f"""
        Problem: {text}
        Conclusion:
        """
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            top_p=0.9,
        )
        conclusion = response["choices"][0]["text"]
        st.success(conclusion)
