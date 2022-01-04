#----------------------------------------------------#
#----------------------------------------------------#
import streamlit as st
#----------------------------------------------------#
st.set_page_config(layout="centered",
                   page_title="Fliflax",
                   page_icon=":smiley",
                   initial_sidebar_state='expanded'
                   )
#----------------------------------------------------#
st.markdown(""" <style> .font {
    font-size:50px ; 
    #font-family: 'sans-serif'; 
    color: #000000;} 
    </style> """, unsafe_allow_html=True)
#----------------------------------------------------#
col1, col2, col3 = st.columns([2, 5, 0.2])
col1.image("Avatar-con-naming-Fliflax.jpg", use_column_width=True, width = 400)
with col2:
    st.markdown('<div style="text-align:center"><p style="font-family:sans-serif; color:#000000; font-size: 50px;"><b>Modelo<br>Beta-Binomial</b></p></div>', unsafe_allow_html=True)
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("Beta binomial es un método de estimación de la "
         "distribución de contactos que denominamos de Audiencia neta acumulada "
         "(o modelo de acumulación), es decir, se trabaja con un único soporte. ")
st.write("Los datos de inicio son los siguientes: A1 (la audiencia del soporte); "
         "A2 (la audiencia acumulada tras la segunda inserción); n "
         "(el número de inserciones que contratamos en el único soporte que seleccionamos), "
         "y la población.")
#----------------------------------------------------#
# st.markdown("""---""")
#----------------------------------------------------#
st.info("Es importante señalar que en nuestra calculadora, "
         "hemos restringido los valores para evitar los bugs "
         "relacionados con los parámetros de forma alfa y beta. "
         "En nuestra calculadora, la Población debe ser superior o igual a 1.000.000 de personas, "
         "y las audiencias, A1 y A2, deben ser inferiores a 1.000.000. "
         "Por su naturaleza A1 debe ser inferior a A2.")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
import pandas as pd
import numpy as np
#import scipy.stats as stats
from scipy import special
#----------------------------------------------------#
st.write("### Selección de datos:")
#----------------------------------------------------#
col1, col2 = st.columns([5,5])
with col1:
    A1 = st.number_input("Audiencia acumulada tras 1 inserción:", min_value = 1, max_value = pow(10, 6), value = 500000, step=100, key = "A1")
    # st.write("Valor elegido: {:.0f}".format(A1))
with col2:
    A2 = st.number_input("Audiencia acumulada tras 2 inserciones:", min_value = 1, max_value = pow(10, 6), value = 550000, step=100, key = "A2")
    # st.write("Valor elegido: {:.0f}".format(A2))
  
col1, col2 = st.columns([5,5])
with col1:
    P = st.number_input("Población:", min_value = pow(10, 6), max_value = pow(10, 10), value = 1000000, step=100, key = "poblacion")
    # st.write("Valor elegido: {}".format(P))
with col2:    
    Precio = st.number_input("Precio de una inserción €:", min_value = 1, max_value = pow(10, 10), value = 1000000, step=100, key = "precio")
    # st.write("Valor elegido: {}".format(P))

#----------------------------------------------------#
R1=A1/P;R2=A2/P    
#----------------------------------------------------#
if A1 > A2:
  st.write("##### Observaciones:")
  st.error("El valor de A2 es inferior a A1. No olvides corregirlo antes de continuar.")
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)  

if P < A2:
  st.write("##### Observaciones:")
  st.error("El valor de la Población es inferior a A2. No olvides corregirlo antes de continuar.")
else:
  st.write("")
  
try:
  alpha=((R1)*((R2)-(R1)))/(2*(R1)-(R1)*(R1)-(R2))
  beta=(alpha*(1-R1))/(R1)
except ZeroDivisionError as e:
  st.write("#### Observaciones:")
  # datos de muestra:
  alpha = 0.125
  beta = 0.125
  n = 5
  st.error("Se ha producido una excepción al proponerse un valor de A2 que provoca una división por 0. "
             "Recuerda que los parámetros de forma deben ser superiores a 0 ."
             "Debes pues revisarlo antes de continuar. Mientras tanto, "
             "los resultados que ves abajo, se corresponden con valores ficticios de los parámetros de forma "
             "para una audiencia de 500,000 personas y una audiencia acumulada tras la segunda inserción de 550,000.")
  
if alpha <= 0 or beta <= 0:
  st.error("Los parámetros de forma alfa o beta son negativos, y violan un presupuesto de partida. "
           "Debes pues revisarlo antes de continuar. "
           "Es posible que el valor de A2 sea demasiado alto. "
           "Mientras tanto, los resultados que ves abajo, se corresponden con valores por defecto de los parámetros de forma.")
  st.write("##### Observaciones:")
  # datos de muestra:
  alpha = 0.125
  beta = 0.125
  n = 5
else:
  st.write("")  
#----------------------------------------------------#
inserciones = st.slider("Inserciones:", 2, 100, value = 5, step=1, key = "inserciones")
# st.write("Valor elegido: {}".format(inserciones))
#----------------------------------------------------#
n = inserciones
x = np.arange(1,n+1)
alphas = alpha
betas = beta
#----------------------------------------------------#
# https://docs.pymc.io/en/v3/api/distributions/discrete-2.py
# https://docs.scipy.org/doc/scipy/tutorial/stats/discrete_betabinom.html
def BetaBinom(a, b, n, x):
    pmf = special.binom(n, x) * (special.beta(x+a, n-x+b) / special.beta(a, b))
    return pmf

pmf = BetaBinom(alphas, betas, n, x)
# Pi:
y = pmf*1000000
# Ri:
Ri = np.flip(y); Ri = np.cumsum(Ri); Ri = np.flip(Ri)
#----------------------------------------------------#
data = {'exposiciones':  x, 'Pi': y, 'Ri': Ri}

df = pd.DataFrame(data)
df = df.astype(int)
pd.options.display.float_format = '{:,}'.format
df = df.head(n=n)
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("### Resultados:")
#----------------------------------------------------#
st.write("Derivado de tus datos y siempre que se ajusten a las premisas del modelo Beta-Binomial, "
         "con una audiencia de", f"{A1:,.0f}", "y una audiencia acumulada tras la segunda inserción de", f"{A2:,.0f}", 
         ", el valor de la cobertura alcanzada es igual a", f"{round(df['Ri'].iloc[0]):,.0f}", "personas. "
         "Es decir,", f"{round(df['Ri'].iloc[0]):,.0f}", "personas se exponen al menos 1 vez. "
         "Los impactos logrados con", f"{n:,.0f}", "inserciones son", f"{A1 * n:,.0f}"," impactos. "
         "La frecuencia media es pues igual a", f"{df['Ri'].sum() / df['Ri'].iloc[0]:,.3f}","impactos por persona de la cobertura.")
st.write("Junto a lo anterior, el valor GRP es igual a", f"{round(df['Ri'].sum() * 100 / P):,.0f}","impactos por cada 100 personas de la población "
         "que en nuestro caso es igual a", f"{P:,.0f}", "personas. "
         "Y junto a los GRP te mostramos el valor CPP (coste por punto de rating), en este caso "
         "el coste monetario de alcanzar a un 1 % de la población es igual a", f"{round(Precio * n / (df['Ri'].sum() * 100 / P)):,.0f}","€. "
         "El valor CPP es el resultado de divir un presupuesto de", f"{Precio * n:,.0f}", "€ "
         "y los GRP logrados con la programación de inserciones.")
st.write("A continuación, te ofrecemos un breve resumen.")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
col1, col2 = st.columns([5,5])
with col1:
    st.metric(label="Cobertura", value = f"{round(df['Ri'].iloc[0]):,.0f}")
with col2:
    st.metric(label="Frecuencia media", value = f"{df['Ri'].sum() / df['Ri'].iloc[0]:,.3f}")
col1, col2 = st.columns([5,5])
with col1:
    st.metric(label="Impactos", value = f"{A1 * n:,.0f}")
with col2:
    st.metric(label="GRP", value = f"{round(df['Ri'].sum() * 100 / P):,.0f}")
col1, col2 = st.columns([5,5])
with col1:
    st.metric(label="Presupuesto €", value = f"{Precio * n:,.0f}")
with col2:
    st.metric(label="CPP", value = f"{round(Precio * n / (df['Ri'].sum() * 100 / P)):,.0f}")  
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#    
# Mostrar la tabla de Pi y Ri:
# Convierto en index columna de exposiciones, y vuelco en otra tabla porque si no, me genera arror en Matplotlib.
df1 = df.set_index('exposiciones')
if st.checkbox("Si deseas ver los primeros 5 valores de Pi y Ri alcanzados, marca la casilla.", False):
    st.write('###### Tabla 1. Distribución de contactos Pi (y acumulada Ri)')
    st.table(df1.head().style.format("{:,.0f}").set_properties(**{'text-align': 'center'}).set_properties(**{'background-color': '#ffffff'})) 
    st.info("En nuestro Anexo de abajo, puedes ver todos los valores de Pi y Ri.")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
df1 = df.set_index('exposiciones')
df1 = pd.DataFrame(df1)

if st.checkbox("Si deseas ver la representación gráfica de la distribución de contactos Pi (y acumulada Ri), marca la casilla.", False):
    st.write('###### Figura 1. Distribución de contactos Pi')
    st.bar_chart(df1[['Pi']], use_container_width = True)
    st.write('###### Figura 2. Distribución de contactos acumulada Ri')
    st.bar_chart(df1[['Ri']], use_container_width = True)
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("### Frecuencia efectiva mínima")
#----------------------------------------------------#
if df.lt(0).any().any() == True:
  st.write("#### Observaciones:")
  st.error("Puedes comprobar que en la tabla se muestran valores extraños, por ejemplo, valores negativos. "
            "Es debido probablemente a que el valor de A2 es superior a A1, y eso no es posible. "
            "Corrígelo antes de seleccionar ningún valor de i.")
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)

st.write("En este apartado puedes seleccionar los valores de Pi y Ri cuyo valor desees conocer de modo preciso. "
         "El valor i que elijas, puede corresponderse, por ejemplo, con la frecuencia efectiva mínima que "
         "has prupuesto como objetivo en tu plan de medios y soportes. "
         "Recuerda que la frecuencia efectiva mínima es el mínimo número de impactos por persona de la cobertura efectiva para alcanzar "
         "(por encima de un determinado nivel crítico) "
         "los objetivos de comunicación.")
pd.options.display.float_format = '{:,}'.format
df1 = df.set_index('exposiciones')
selected_indices = st.multiselect('Selecciona el/los valor/es i:', df1.index)
selected_indices = map(lambda selected_indices:selected_indices, selected_indices)
selected_rows = df1.loc[selected_indices]
st.write('###### Tabla 2. Valores de Pi y Ri seleccionados')
# st.table(selected_rows)
st.table(selected_rows.style.format("{:,.0f}").set_properties(**{'text-align': 'center'}).set_properties(**{'background-color': '#ffffff'})) 
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("### Referencias:")
#----------------------------------------------------#
st.info("Finalmente, para profundizar en estos materiales, te recomendamos consultar la tesis doctoral de "
         "Joaquín Aldás Manzano de 1998, Catedrático actualmente en la Universidad de Valencia. ")
st.info("También, te recomendamos visitar el siguiente enlace: [Wikipedia: Beta-Binomial](https://es.wikipedia.org/wiki/Distribuci%C3%B3n_beta-binomial)")
#----------------------------------------------------#
st.markdown("""---""")
#----------------------------------------------------#
st.write("### Anexo")
#----------------------------------------------------#
if df.lt(0).any().any() == True:
  st.write("#### Observaciones:")
  st.error("Puedes comprobar que en la tabla se muestran valores extraños, por ejemplo, valores negativos. "
            "Es debido probablemente a que el valor de A2 es superior a A1, y eso no es posible.")
else:
  st.markdown('<p style="font-family:Consolas; color:black; font-size: 14px;"></p>', unsafe_allow_html=True)

st.write('###### Anexo 1. Distribución de contactos Pi (y acumulada Ri)')
#df = df.set_index('exposiciones')
if st.checkbox("Si deseas ver la tabla completa de valores de Pi y Ri alcanzados, marca la casilla.", False):
    st.write('###### Anexo. Distribución de contactos Pi (y acumulada Ri)')
    st.table(df1.style.format("{:,.0f}").set_properties(**{'text-align': 'center'}).set_properties(**{'background-color': '#ffffff'})) 
    st.write('Parámetros de forma: alfa: ',f"{alphas:,.3f}",'y beta: ',f"{betas:,.3f}")
#----------------------------------------------------#
import altair as alt
g = alt.Chart(df).mark_line().encode(
    x='exposiciones',
    y='Pi'
)
st.line_chart(g, use_container_width = True)
#----------------------------------------------------#
