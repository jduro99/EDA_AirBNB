import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit.components.v1 as components
from PIL import Image
from io import BytesIO
import base64

# CONFIGURACION DE LA PAGINA
st.set_page_config(
    page_title="Análisis de Datos de Airbnb en Málaga",
    page_icon="🏠",
    layout="wide",  # "wide" usa todo el ancho, "centered" centra el contenido.
    initial_sidebar_state="expanded"
)

image = Image.open("img/malaga.jpg")
image = image.resize((1980, 300))  # Establecer el tamaño deseado
buffer = BytesIO()
image.save(buffer, format="PNG")
img_b64 = base64.b64encode(buffer.getvalue()).decode()

# Mostrar la imagen centrada
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{img_b64}" alt="Málaga" style="width:1980px; height:300px;">
    </div>
    """,
    unsafe_allow_html=True
)

# TÍTULO
st.markdown("<h1 style='text-align: center;'>Análisis de datos de Airbnb en Málaga</h1>", unsafe_allow_html=True)

# DESCRIPCIÓN DEL PROYECTO
st.markdown(
    """
    <div style="text-align: center; font-size:18px;">
        Esta aplicación permite explorar y analizar los datos de Airbnb en Málaga, 
        con un enfoque en la rentabilidad por barrio y tipo de alojamiento.
    </div>
    """,
    unsafe_allow_html=True
)


# Cargar los datos
df = pd.read_csv('df_final.csv')

# TABS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dataset", "Información general", "Rentabilidad por Barrio", "Rentabilidad por Tipo de Alojamiento", "Informe y Conclusiones"])


with tab1:
    st.markdown("<h2 style='text-align: center;'>Información general sobre los datos</h2>", unsafe_allow_html=True)
    st.write(df.head(5))

    st.write("""
    Esta pestaña muestra una visión general de los primeros registros del dataset de Airbnb en Málaga.
    Aquí podrás ver las primeras 5 filas, que te darán una idea de cómo se estructura la información, incluyendo datos sobre los barrios, precios, tipos de alojamientos, etc.
    """)

with tab2:
    st.markdown("<h2 style='text-align: center;'>Información General</h2>", unsafe_allow_html=True)

    # Crear dos columnas
    col1, col2 = st.columns(2)

    # Gráfico 1
    with col1:
        st.image("img/Precios_por_categoría.png", width=800)
        st.write("""
        Distribución de los alojamientos por categoría de precio. Podemos observar 4 categorías: Bajo, Medio, Alto y Muy Alto.
        """)

    # Gráfico 2
    with col2:
        st.image("img/disponibiliad_por_categoría_de_precio.png", width=800)
        st.write("""
        Disponibilidad de los alojamientos según su categoría de precio. Podemos observar que los alojamientos de precio bajo son los que menor disponibilidad.
        """)

    # Crear una nueva fila (con `st.columns()` de nuevo)
    col3, col4 = st.columns(2)

    # Gráfico 3
    with col3:
        st.image("img/frecuencia_tipo_alojamiento.png", width=800)
        st.write("""
        Frecuencia de los tipos de alojamiento en Málaga. Podemos observar que los apartamentos completos son los más comunes con mucha diferencia respecto a los demás.
        """)

    # Gráfico 4
    with col4:
        st.image("img/barrios_con_más_alojamientos.png", width=800)
        st.write("""
        Barrios con mayor cantidad de alojamientos en Málaga. Podemos observar que el Centro es el barrio con más alojamientos. Podríamos decir tamibén que es el barrio más turístico y con más competencia.
        """)


with tab3:
    st.markdown("<h2 style='text-align: center;'>Rentabilidad por Barrio</h2>", unsafe_allow_html=True)

    # Crear dos columnas para la primera fila
    col1, col2 = st.columns(2)

    # Gráfico 1
    with col1:
        st.image("img/impacto_barrio_en_precio.png", width=800)
        st.write("""
        Este gráfico muestra el impacto del barrio en el precio de los alojamientos. Podemos observar que el barrio de Churriana es el más caro y el de Bailen-Miraflores el más barato.
        """)

    # Gráfico 2
    with col2:
        st.image("img/ingresios_precio_promedio_barrio.png", width=800)
        st.write("""
        En este gráfico se puede ver la relación entre los ingresos anuales y el precio promedio por noche en cada barrio de Málaga. Puerto de la Torre y Churriana son los barrios con mayor rentabilidad.
        """)

    # Crear una nueva fila (con `st.columns()` de nuevo)
    col3, col4 = st.columns(2)

    # Gráfico 3
    with col3:
        st.image("img/ingresos_calificación_barrio.png", width=800)
        st.write("""
        En este gráfico podemos ver la relación entre los ingresos anuales y la calificación promedio de los alojamientos en cada barrio de Málaga. No parece haber una relación directa entre ambas variables.
        """)

    # Gráfico 4
    with col4:
        st.image("img/ingresos_tasa_oc_barrio.png", width=800)
        st.write("""
        Este gráfico muestra los ingresos anuales y la tasa de ocupación en cada barrio de Málaga. Puerto de la Torre tiene una tasa de ocupación muy elevada. 
        """)

    # Incluir el mapa debajo de los gráficos
    st.write("### Mapa del precio medio de la noche por Barrio en Málaga")
    components.html(open('img/map_malaga.html', 'r').read(), height=600)



with tab4:
        
    st.markdown("<h2 style='text-align: center;'>Rentabilidad por tipo de alojamiento</h2>", unsafe_allow_html=True)
    
    # Crear dos columnas para la primera fila
    col1, col2 = st.columns(2)

    with col1:
        st.image("img/todo_por_tipo_alojamiento.png", width=800)
        st.write("""
        En este gráfico podemos ver los ingresos anuales promedio por tipo de alojamiento. las habitaciones de hotel son las que generan más ingresos, pero son ls más caras y con menor tasa de ocupación. Los alojamientos completos tienen buenos ingresos, precio promedio adsequible u alta tasa de ocupación.
        """)
    
    with col2:
        st.image("img/top10_alojamientos.png", width=800)
        st.write("Top 10 alojamientos con más reseñas y su rating promedio. No parece haber relación entre el número de reseñas y el rating promedio.")

with tab5:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h2 style='text-align: center;'>Informe en PowerBI</h2>", unsafe_allow_html=True)
        st.write("""
        En este informe interactivo de PowerBI podrás explorar los datos de Airbnb en Málaga de forma más detallada.
        Podrás ver información sobre la rentabilidad por barrio y por tipo de alojamiento.
        """)
        iframe_url = "https://app.powerbi.com/view?r=eyJrIjoiYWY2YThjZjctZDEwZS00ZmY1LWJiMWMtMmZmYzdjYjRmM2U1IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
        components.html(
            f'<iframe title="Panel_Airbnb" width="600" height="373.5" src="{iframe_url}" frameborder="0" allowFullScreen="true"></iframe>',
            height=800
        )
    with col2:
        st.markdown("<h2 style='text-align: center;'>Conclusiones del Análisis de Rentabilidad en Málaga</h2>", unsafe_allow_html=True)

        st.subheader("Barrio más rentable")
        st.write("### **Barrio Este**")
        st.write("""
        - Precio promedio competitivo.
        - Proximidad al centro y entorno agradable.
        - Alta rentabilidad equilibrando ingresos, ocupación y ubicación.
        """)

        st.write("### **Churriana**")
        st.write("""
        - Precio promedio elevado.
        - Buena rentabilidad anual con una ocupación moderada.
        - Ideal si la cercanía al centro no es prioritaria.
        """)

        st.subheader("Tipo de alojamiento más rentable")
        st.write("### **Apartamentos completos**")
        st.write("""
        - Alto ingreso anual promedio.
        - Precio asequible y alta tasa de ocupación.
        - Buena calificación (>4), ideales para ingresos constantes.
        """)

        st.write("### **Otros tipos de alojamiento**")
        st.write("""
        - **Habitaciones privadas**: Alta ocupación, pero ingresos bajos debido a precios reducidos.
        - **Habitaciones de hotel**: Rentables solo con estrategias exclusivas debido a baja ocupación y precios altos.
        - **Habitaciones compartidas**: Bajos ingresos y calificaciones. No recomendadas.
        """)

        st.subheader("Recomendaciones finales")
        st.write("#### **Barrio recomendado**")
        st.write("""
        - **Primera opción**: Churriana.
        - **Alternativa**: Este (equilibrio entre entorno, ubicación y rentabilidad)
        """)

        st.write("#### **Alojamiento recomendado**")
        st.write("""
        - Apartamentos completos por su combinación óptima de ingresos, ocupación y calificaciones.
        """)

        st.write("#### **Estrategia de maximización**")
        st.write("""
        - Ajustar precios en temporada alta (abril-agosto).
        - Elegir ubicaciones seguras y atractivas, excluyendo barrios y zonas conflictivas como Palma-Palmilla.
        """)

