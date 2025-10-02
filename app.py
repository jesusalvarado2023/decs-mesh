import streamlit as st

st.set_page_config(page_title="Quiz DeCS & MeSH", page_icon=":mortar_board:")

st.image("decsmesh.png")
st.title("Herramientas Digitales para el Aprendizaje")
st.write("Quiz - Dr. Jesus Alvarado H.")
st.info("Selecciona la alternativa correcta y pulsa 'Ver puntaje' 🎈")

# Lista de preguntas (texto corto, 4 opciones cada una, índice de respuesta correcta)
questions = [
    {
        "q": "¿Qué significa MeSH?",
        "opts": [
            "Medicine Subject Headings",
            "Medical Search Heads",
            "Medical Subject Headings",
            "Metadata for Scientific Health"
        ],
        "ans": 2
    },
    {
        "q": "¿Qué organización creó DeCS?",
        "opts": [
            "World Bank",
            "National Library of Medicine (NLM)",
            "Cochrane Collaboration",
            "WHO/PAHO/BIREME"
        ],
        "ans": 3
    },
    {
        "q": "¿En qué bases de datos es especialmente útil DeCS?",
        "opts": [
            "LILACS y SciELO",
            "PubMed/MEDLINE",
            "Embase y Cochrane",
            "arXiv"
        ],
        "ans": 0
    },
    {
        "q": "¿Cuál es el propósito principal de usar términos MeSH/DeCS en búsquedas?",
        "opts": [
            "Aumentar el número de resultados irrelevantes",
            "Estandarizar términos para búsquedas más precisas",
            "Reemplazar la lectura del artículo",
            "Traducir automáticamente artículos"
        ],
        "ans": 1
    },
    {
        "q": "¿Qué característica distingue a DeCS frente a MeSH?",
        "opts": [
            "Está disponible en español, portugués e inglés",
            "Sólo está en inglés",
            "No se actualiza regularmente",
            "No incluye sinónimos"
        ],
        "ans": 0
    },
    {
        "q": "En MeSH, ¿qué son los 'entry terms'?",
        "opts": [
            "Códigos numéricos de identificación",
            "Secciones del artículo",
            "Referencias bibliográficas",
            "Sinónimos que remiten al termino MeSH"
        ],
        "ans": 3
    },
    {
        "q": "Si buscas 'cáncer de mama' en PubMed usando MeSH, ¿cuál término MeSH es más apropiado?",
        "opts": [
            "Breast Disease",
            "Breast Cancerous Syndrome",
            "Mammary Tumor Disorder",
            "Breast Neoplasms"
        ],
        "ans": 3
    },
    {
        "q": "¿Qué organiza MeSH de forma jerárquica?",
        "opts": [
            "Revistas científicas",
            "Autores de artículos",
            "Temas en árbol categorías",
            "Fechas de publicación"
        ],
        "ans": 2
    },
    {
        "q": "¿Cuál es una ventaja de usar DeCS en investigación regional?",
        "opts": [
            "No admite búsquedas en inglés",
            "Incluye información destacada de Europa, Asia y Africa",
            "Incluye términos relevantes para América Latina y el Caribe",
            "Traduce los artículos a español, portugués e inglés"
        ],
        "ans": 2
    },
    {
        "q": "Para hacer una búsqueda sensible y precisa en PubMed conviene:",
        "opts": [
            "Filtrar por nivel del investigador o de la revista",
            "Usar las palabras más importantes que encuentro al leer un artículo",
            "Buscar por el nombre del autor o el identificador de objeto digital (DOI)",
            "Combinar términos MeSH con operadores booleanos"
        ],
        "ans": 3
    }
]

# Contenedor para preguntas
st.markdown("---")

# Usamos session_state para almacenar respuestas del usuario
if 'answers' not in st.session_state:
    st.session_state['answers'] = [None] * len(questions)

# Mostrar preguntas
for i, item in enumerate(questions):
    st.markdown(f"**Pregunta {i+1}.** {item['q']}")
    key = f"q_{i}"
    choice = st.radio("", item['opts'], index=st.session_state['answers'][i] if st.session_state['answers'][i] is not None else 0, key=key, horizontal=False)
    # Guardar índice seleccionado
    st.session_state['answers'][i] = item['opts'].index(choice)
    st.write('')

st.markdown("---")

# Botón para ver puntaje
if st.button("Ver puntaje"):
    score = 0
    total = len(questions)
    feedback = []
    for idx, q in enumerate(questions):
        user_ans = st.session_state['answers'][idx]
        correct = q['ans']
        if user_ans == correct:
            score += 1
            feedback.append((idx+1, True, q['opts'][correct]))
        else:
            feedback.append((idx+1, False, q['opts'][correct]))

    percent = int(score / total * 100)
    st.success(f"Obtuviste {score} / {total} ({percent}%)")

    # Mostrar retroalimentación por pregunta
    with st.expander("Ver retroalimentación por pregunta"):
        for pnum, ok, correct_text in feedback:
            if ok:
                st.write(f"Pregunta {pnum}: ✅ Correcta")
            else:
                st.write(f"Pregunta {pnum}: ❌ Incorrecta — Respuesta correcta: **{correct_text}**")

    # Si acierta todas, mostrar globitos
    if score == total:
        st.balloons()
        st.success("¡Felicidades! Respondiste todas las preguntas correctamente. 🎉")

# Footer: instrucciones para profesores/estudiantes
st.markdown("---")
st.caption("Puedes editar las preguntas en el archivo `streamlit_decs_mesh_quiz.py` y subirlo a GitHub para compartir la app. Para un despliegue rápido usa Streamlit Community Cloud (https://streamlit.io/cloud)")
