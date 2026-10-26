import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Encabezado de la aplicación
st.header('Análisis de datos anuncio de venta de coches')

# 2. Lectura del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

st.write('Selecciona las opciones del gráfico que deseas visualizar:')

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    # Crear histograma del odómetro
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Histograma del Odómetro')
    # Mostrar gráfico interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para el Gráfico de Dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Construir un gráfico de dispersión para Precio vs. Odómetro')
    # Crear gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer",
                             y="price", title="Precio vs. Odómetro")
    # Mostrar gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
