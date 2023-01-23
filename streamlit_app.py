import streamlit as st

st.title('GTN para encontrar el problema y la conclusión de un artículo')

openai_key = st.text_input('Ingrese su clave de OpenAI')

if openai_key:
    st.write('Clave de OpenAI reconocida')
    st.write('Por favor, ingrese el texto del artículo')
    article_text = st.text_area('Artículo')
    if article_text:
        st.write('Procesando su artículo...')
        # Aquí se usa la API de OpenAI para encontrar el problema y la conclusión
        problem_question = '¿Cuál es el problema que se trata en el artículo?'
        conclusion = 'Aquí está la conclusión que se obtuvo del artículo.'
        st.write('Pregunta del problema:', problem_question)
        st.write('Conclusión:', conclusion)
    else:
        st.write('Por favor, ingrese el texto del artículo.')
else:
    st.write('Por favor, ingrese su clave de OpenAI.')
