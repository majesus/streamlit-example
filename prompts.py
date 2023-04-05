import streamlit as st
#------------------------------------------------#
from PIL import Image
img=Image.open('img/fliflax-logo.jpg')
st.set_page_config(#layout="centered",
                   #theme="light",
                   #layout="wide",
                   page_title="Fliflax",
                   page_icon=img,
                   #initial_sidebar_state='expanded'
                   )
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        #footer {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)
#------------------------------------------------#
# Separador estético personalizado
def separador(color):
    st.markdown(
        f'<hr style="border: 1px solid {color};">', unsafe_allow_html=True
    )
#------------------------------------------------#
custom_title = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 25px; line-height: 1.5; color: #B30A1B; font-weight: bold;"
custom_subtitle = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 18px; line-height: 1.5; color: #B30A1B;"
custom_subtitle_black = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 18px; line-height: 1.5; color: #B30A1B;"
custom_style_black = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 16px; line-height: 1.5;"
custom_style = "font-family: Bahnschrift Light, Segoe UI, Arial; font-size: 14px; line-height: 1.5;"

# Aplicar estilos CSS personalizados a toda la página
st.write("""
<style>
    * {
        font-family: Bahnschrift Light, Segoe UI, Arial;
        font-size: 18px;
        line-height: 1.5;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)
#------------------------------------------------#
# Título y descripción de la aplicación
# Función para descargar y almacenar imágenes en caché
@st.cache
def cargar_imagen(url):
    image = Image.open(url_imagen)
    return image
  
# URL de la imagen
url_imagen = "img/fliflax-logo.jpg"
# Descargar imagen
imagen = cargar_imagen(url_imagen)
# Crear dos columnas con anchos ajustados
col1, col2 = st.beta_columns([1, 3])  # La primera columna tendrá un ancho proporcional de 1, y la segunda un ancho proporcional de 3
# Añadir imagen en la primera columna
col1.image(imagen, width=150)
# Añadir título en la segunda columna
col2.title("")
st.markdown(f"<p style='{custom_subtitle_black}'>Por Manuel J. Sánchez Franco, Universidad de Sevilla.</p>", unsafe_allow_html=True)
separador("#B30A1B")
#------------------------------------------------#
st.markdown(f"<p style='{custom_style_black}'>Crea tus propios prompts, y ajusta los parámetros para obtener respuestas precisas y relevantes. A continuación, te formulamos distintas preguntas para alinear tu prompt con tus deseos. Los parámetros empleados están optimizados para GPT4.</p>", unsafe_allow_html=True)
separador("#B30A1B")
#------------------------------------------------#
# Comienza el prompt y elementos adicionales
with st.expander("Preguntas iniciales:"):
    omit = st.radio("¿Deseas que olvide lo anteriormente preguntado?",('No', 'Sí'))
    confirm = st.radio("¿Deseas confirmar que ChatGPT ha comprendido el prompt y los elementos adicionales?",('Sí', 'No'))
    detail = st.radio("La respuesta debe ser:",('equilibrada', 'precisa', 'creativa'))
separador("#B30A1B")
#------------------------------------------------#
# Conceptos clave para la generación de un prompt que genere una respuesta relevante
with st.expander("Conceptos básicos para la generación de un prompt que genere una respuesta relevante:"):
  st.markdown(f"<p style='{custom_subtitle}'>Contexto:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Definición: Información adicional, detalles o antecedentes que ayudan a aclarar o especificar la situación, tema o propósito del prompt.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Diferenciación: El contexto proporciona la base para comprender el prompt y es necesario para establecer una conexión clara entre el tema y la respuesta esperada.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Ejemplo: La empresa ABC ha lanzado recientemente un producto innovador en el mercado de dispositivos electrónicos.</p>", unsafe_allow_html=True)

  st.markdown(f"<p style='{custom_subtitle}'>Prompt:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Definición: La pregunta o instrucción central que se presenta al modelo de lenguaje, diseñada para obtener una respuesta específica o iniciar una discusión sobre un tema.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Diferenciación: El prompt es la parte principal de la interacción, y su contenido determina en gran medida la calidad y relevancia de la respuesta.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Ejemplo: Analice el impacto potencial de la campaña de marketing de la empresa ABC en las ventas de su nuevo producto.</p>", unsafe_allow_html=True)

  st.markdown(f"<p style='{custom_subtitle}'>Material complementario:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Definición: Recursos adicionales, como estudios, gráficos, datos o referencias que pueden ayudar a enriquecer y respaldar la respuesta del modelo de lenguaje.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Diferenciación: El material complementario no forma parte del prompt en sí, pero puede ser útil para proporcionar información adicional o aclaraciones que el modelo podría utilizar en su respuesta.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Ejemplo: Incluya en su análisis datos de la siguiente investigación de mercado: [enlace al estudio].</p>", unsafe_allow_html=True)

  st.markdown(f"<p style='{custom_subtitle}'>Objetivos:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Definición: Los propósitos específicos que se esperan lograr con la respuesta del modelo, como informar, persuadir, analizar o resolver un problema.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Diferenciación: Los objetivos guían el enfoque y el tono de la respuesta, y deben estar alineados con las necesidades y expectativas de la audiencia.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Ejemplo: El objetivo principal de este análisis es identificar oportunidades de mejora en la estrategia de marketing y proponer acciones específicas para incrementar las ventas.</p>", unsafe_allow_html=True)

  st.markdown(f"<p style='{custom_subtitle}'>Tareas:</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Definición: Acciones concretas o pasos que el modelo debe llevar a cabo para cumplir con los objetivos y responder adecuadamente al prompt.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Diferenciación: Las tareas son instrucciones claras y específicas que facilitan la estructuración y el enfoque de la respuesta.</p>", unsafe_allow_html=True)
  st.markdown(f"<p style='{custom_style}'>Ejemplo: a) Identifique los principales canales de marketing utilizados por la empresa ABC, b) Evalúe la efectividad de cada canal en función de los datos proporcionados, y c) Proponga al menos tres acciones de marketing para mejorar el rendimiento de la campaña actual.</p>", unsafe_allow_html=True)#------------------------------------------------#
separador("#B30A1B")
#------------------------------------------------#
contexto = st.text_area("Facilita, si lo deseas, un CONTEXTO para que la respuesta adquiera mayor relevancia:", "")
separador("#B30A1B")
#------------------------------------------------#
# Campos de entrada para el prompt y elementos adicionales
prompt1 = st.text_area("Escribe tu cadena de entrada (o PROMPT) que guía la generación de texto del modelo.", "")
with st.expander("Prompts adicionales en el caso de que desees secuenciarlos:"):
    prompt2 = st.text_input("Escribe tu segundo paso", "")
    prompt3 = st.text_input("Escribe tu tercer paso:", "")
    prompt4 = st.text_input("Escribe tu cuarto paso:", "")
    step = st.radio("¿Deseas que la respuesta siga secuencialmente cada paso?",('Sí', 'No'))
separador("#B30A1B")
#------------------------------------------------#
# Añadir material complementario (por ejemplo, códigos)
anexo = st.text_area("MATERIAL complementario, por ejemplo, ejemplos, código, etc.:", "")
separador("#B30A1B")
#------------------------------------------------#
# Añadir objetivos y tareas
objectives_tasks = st.text_area("¿Cuáles son los OBJETIVOS que persigues en tu respuesta, y las TAREAS necesarias para lograr los objetivos?", "")
separador("#B30A1B")
#------------------------------------------------#
st.markdown(f"<p style='{custom_style_black}'>A continuación, te proponemos un conjunto de claves para dotar a la respuesta esperada de mayor relevancia.</p>", unsafe_allow_html=True)

audience = st.text_input("¿Quiénes son los DESTINATARIOS de la respuesta esperada?", "")
rol = st.multiselect("¿Qué ROL deseas que asuma ChatGPT al generar la respuesta?", ["académico", "analista de datos", "asesor financiero", "asistente personal", "cocinero", "corrector de estilo / ortográfico", "diseñador gráfico", "diseñador web", "diseñador multimedia", "director de arte", "editor de revista académica", "escritor", "estadístico", "generador de prompts", "guía de viaje", "informático", "interiorista", "instrucciones de uso", "matemático", "nutricionista", "programador", "programador de videojuegos", "redactor publicitario", "revisor de artículos académicos", "screenwriter", "storyteller", "traductor"], default=[])
tone = st.multiselect("¿Cuál debe ser el TONO empleado en la respuesta?", ["experto", "formal", "profesional", "informativo", "relajado", "cercano", "divertido", "serio", "persuasivo", "entusiasta"], default=[])
author = st.text_input("ChatGPT debe responder con el ESTILO de un/a autor/a conocido/a:", "")
language = st.selectbox("¿En qué IDIOMA deseas que se genere la respuesta?", ["", "español", "inglés", "alemán", "francés", "italiano", "portugués"])
formato = st.selectbox("¿Cuál debe ser el FORMATO de la respuesta esperada?", ["", "texto", "bullet points", "tabla"])
extension = st.selectbox("¿Qué EXTENSIÓN o duración deseas que tenga la respuesta esperada?", ["", "corto", "medio", "largo"])
site = st.selectbox("¿Deseas que consulta documentación de algún SITE en particular?", ["", "scholar.google.com", "pubmed.ncbi.nlm.nih.gov", "elicit.org"])
separador("#B30A1B")
#------------------------------------------------#
st.markdown(f"<p style='{custom_style_black}'>Parámetros adicionales:</p>", unsafe_allow_html=True)
with st.expander("Temperature:"):
  st.write("La temperatura es un parámetro utilizado en los modelos de lenguaje generativos para controlar la variabilidad en las respuestas generadas. Se refiere a la cantidad de aleatoriedad que se permite en la respuesta generada. Un valor más alto de temperatura genera respuestas más creativas y diversas, mientras que un valor más bajo produce respuestas más predecibles y cercanas a lo que ya ha sido visto en los datos de entrenamiento.")
  st.write("Por ejemplo, si se utiliza una temperatura alta en la generación de un texto, se pueden obtener respuestas como: El cielo es de color rosa, o Los gatos vuelan. Por otro lado, si se utiliza una temperatura baja, es más probable que la respuesta generada sea coherente y realista, como: El cielo es azul, o Los gatos no pueden volar.")
temperature =st.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
separador("#B30A1B")

with st.expander("logit-bias:"):
  st.write("El logit bias es un parámetro utilizado en los modelos de lenguaje generativos para ajustar las probabilidades de ciertos tokens antes de aplicar la función softmax, lo que afecta la selección de tokens durante la generación de texto. Al ajustar el logit bias, puedes hacer que ciertos tokens sean más o menos probables en la salida generada.")
  st.write("Por ejemplo, si deseas que el modelo genere más contenido relacionado con gatos, puedes aumentar el logit bias de tokens relacionados con gatos, como gato, felino o gatito. Por otro lado, si deseas reducir la probabilidad de que aparezcan palabras negativas en la salida, puedes disminuir el logit bias de tokens como triste, malo o negativo.")
logit_bias_tokens = st.text_input("Tokens:", "")
logit_bias =st.slider("logit-bias:", min_value=-2.0, max_value=2.0, value=0.0, step=0.1)
separador("#B30A1B")

with st.expander("Maximum tokens:"):
  st.write("La longitud máxima es el número máximo de tokens (palabras) permitidos en la respuesta generada. Este parámetro se utiliza para controlar la longitud de las respuestas generadas y evitar que sean demasiado largas o demasiado cortas.")
  st.write("Por ejemplo, si se establece una longitud máxima de 50 palabras, el modelo generará una respuesta que no supere esa cantidad.")
max_length = st.slider("Maximum length:", min_value=10, max_value=4096, value=1024, step=10)
separador("#B30A1B")

with st.expander("Top P:"):
  st.write("Top P es un parámetro utilizado para controlar la cantidad de opciones que el modelo tiene para elegir la siguiente palabra en una respuesta generada. Se refiere al porcentaje de las opciones más probables que el modelo considera para la siguiente palabra.")
  st.write("Por ejemplo, si se establece un valor Top P de 0.8, el modelo considerará las palabras con las 80% de mayor probabilidad para la siguiente palabra.")
top_p = st.slider("Top P:", min_value=0.0, max_value=1.0, value=1.0, step=0.1)
separador("#B30A1B")

with st.expander("Stop sequence:"):
  st.write("La secuencia de parada se refiere a una cadena de texto que el modelo utilizará para detener la generación de texto. Es útil para controlar el tema o el enfoque de las respuestas generadas.")
  st.write("Por ejemplo, si se establece una secuencia de parada como: Fin del texto, el modelo generará respuestas hasta que encuentre la secuencia: Fin del texto, luego dejará de generar texto.")
stop_sequence = st.text_input("Stop sequence:", "")
separador("#B30A1B")

with st.expander("Frequency penalty:"):
  st.write("La penalización de frecuencia es un parámetro utilizado para controlar la repetición de palabras en las respuestas generadas. Este parámetro penaliza la repetición de palabras que ya han sido utilizadas en la respuesta generada.")
  st.write("Por ejemplo, si se establece una penalización de frecuencia, el modelo evitará generar respuestas que contengan muchas repeticiones de las mismas palabras.")
frequency_penalty = st.slider("Frequency penalty:", min_value=-2.0, max_value=2.0, value=0.6, step=0.1)
separador("#B30A1B")

with st.expander("Presence penalty:"):
  st.write("La penalización de presencia es un parámetro utilizado para controlar la aparición de ciertas palabras o frases en las respuestas generadas. Este parámetro penaliza la aparición de ciertas palabras o frases en la respuesta generada.")
  st.write("Por ejemplo, si se establece una penalización de presencia para la palabra: política, el modelo evitará generar respuestas que contengan esa palabra o frases relacionadas con ese tema.")
word_presence_penalty = st.text_input("Texto:", "")
presence_penalty = st.slider("Presence penalty:", min_value=-2.0, max_value=2.0, value=0.5, step=0.1)
separador("#B30A1B")

with st.expander("Best of:"):
  st.write("Best of se refiere a la cantidad de respuestas generadas que se presentan al usuario. Este parámetro permite seleccionar el número de respuestas más adecuadas a presentar al usuario.")
  st.write("Por ejemplo, si se establece un valor Best of de 5, el modelo generará 5 respuestas distintas y luego se presentarán las 5 opciones al usuario para que elija la que más le guste o la que mejor se ajuste a sus necesidades.")
best_of = st.slider("Best of:", min_value=1, max_value=5, value=1, step=1)
separador("#B30A1B")

with st.expander("Inject start text:"):
  st.write("Inject start text es un parámetro utilizado para agregar texto específico al inicio de la respuesta generada. Este parámetro se utiliza para controlar el inicio de la respuesta generada y para agregar contexto específico al inicio de la respuesta.")
  st.write("Por ejemplo, si se establece un texto de inicio como: En respuesta a su pregunta sobre el clima..., el modelo generará una respuesta que comienza con esa frase para indicar que se está respondiendo a una pregunta específica.")
inject_start_text = st.text_input("Inject start text:", "")
separador("#B30A1B")

with st.expander("Inject restart text:"):
  st.write("Inject restart text es un parámetro utilizado para agregar texto específico al reinicio de la respuesta generada. Este parámetro se utiliza para controlar el reinicio de la respuesta generada y para agregar contexto específico al reinicio de la respuesta.")
  st.write("Por ejemplo, si se establece un texto de reinicio como: Continuando nuestra conversación anterior..., el modelo generará una respuesta que comienza con esa frase para indicar que se está retomando una conversación anterior y agregar contexto a la respuesta.")
inject_restart_text = st.text_input("Inject restart text:", "")
separador("#B30A1B")

with st.expander("No repeat n-gram size:"):
  st.write("")
  st.write("")
word_repeat_ngram = st.text_input("Token:", "")
repeat_ngram = st.slider("No repeat n-gram size:", min_value=0, max_value=5, value=0, step=1)
separador("#B30A1B")
#------------------------------------------------#
# Construye el prompt completo
def build_full_prompt(contexto, step, omit, confirm, anexo, extension, detail, author, prompt1, prompt2, prompt3, prompt4, audience, rol, tone, objectives_tasks, language, formato, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text, word_repeat_ngram, repeat_ngram, site):
    full_prompt = f"{omit} debes olvidar todo lo anterior antes de comenzar a responder. Y {step} debes seguir secuencialmente los distintos prompts (o pasos) que te he facilitado en tu respuesta. Es importante que recuerdes que la respuesta debe ser altamente {detail}, y debes necesariamente consultar documentación de: site/{site} \n\nA continuación, te facilito los siguientes datos: \n\nContexto de la respuesta: {contexto} \n\nPrimer paso (o prompt): {prompt1} \n\nSegundo paso (o prompt adicional): {prompt2} \n\nTercer paso (o prompt adicional): {prompt3} \n\nCuarto paso (o prompt adicional): {prompt4}. \n\nMaterial complementario: {anexo} \n\nObjetivos y tareas: {objectives_tasks} \n\nNúmero de respuestas (parámetro: best_of): {best_of} \n\n No repetir el token: {word_repeat_ngram}, en grupos de {repeat_ngram} tokens \n\nMás instrucciones: \n\nAudiencia de la respuesta: {audience} \n\nActúa como: {rol} \n\nTono de la respuesta: {tone} \n\nEstilo de la respuesta: {author} \n\nIdioma de la respuesta: {language} \n\nFormato de la respuesta: {formato} \n\nParámetro temperatura (parámetro: temperature) o aleatoriedad: {temperature} \n\nExtensión de la respuesta (parámetro: max_tokens) inferior a: {max_length} tokens \n\nDuración de la respuesta: {extension}. \n\nAl generar tu respuesta ve eligiendo las siguientes palabras con probabilidades de al menos: {top_p} \n\nSi te encuentras la siguiente cadena de texto (o parámetro: stop_sequence): {stop_sequence}, ¡debes parar de escribir! \n\nDe 0 (mayor repetición) a 2 (menor repetición) repite (aproximándose el valor a 0) o evita repetir (aproximándose a el valor a 2) palabras en tu respuesta; el valor (parámetro: frequency_penalty) es: [{frequency_penalty}] \n\nDe 0 (mayor repetición) a 2 (menor repetición) emplea repetidamente (aproximándose el valor a 0) o evita usar en tu respuesta (aproximándose el valor a 2) el siguiente texto: [{word_presence_penalty}], con un valor (o parámetro: presence_penalty) de: [{presence_penalty}]. \n\nComienza la respuesta con el siguiente texto (o parámetro: inject_start_text): [{inject_start_text}] \n\nIncluye el siguiente texto (o parámetro: inject_restart_text) para retomar una conversación anterior y agregar contexto a la respuesta: [{inject_restart_text}] \n\nFinalmente, dime claramente (con un Sí o un No) si has comprendido las instrucciones: {confirm} \n\nEn caso de sí haber comprendido las instrucciones, antes de comenzar a responder señala -en formato bullet points- los puntos clave de mis instrucciones, y acto seguido comienza a responder con relevancia y ajustado a las instrucciones dadas. En caso de no haber comprendido alguna instrucción, dime qué no has comprendido para aclararla."
    return full_prompt

full_prompt = build_full_prompt(contexto, step, omit, confirm, anexo, extension, detail, author, prompt1, prompt2, prompt3, prompt4, audience, rol, tone, objectives_tasks, language, formato, temperature, max_length, top_p, stop_sequence, frequency_penalty, presence_penalty, best_of, inject_start_text, inject_restart_text, word_repeat_ngram, repeat_ngram, site)

if __name__ == '__main__': 
    with st.expander("Consulta aquí el prompt completo para ChatGPT."):
        text_area = st.text_area("", full_prompt, key="prompt_text_area", height=300)
            
        st.markdown("1. Haz clic dentro del área de texto.")
        st.markdown("2. Utiliza `Ctrl+A` o `Cmd+A` para seleccionar todo el texto.")
        st.markdown("3. Copia el texto seleccionado con `Ctrl+C` o `Cmd+C`.")
        st.markdown("4. Pega el texto seleccionado con `Ctrl+V` o `Cmd+V` en [ChatGPT](http://ai.com).")
        
