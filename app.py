import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(
    "C:\\Users\\Felipe Rodriguez\\Desktop\\TripleTen\\p7\\vehicles_us.csv")

st.header("Información Automotriz")

hist_button = st.button("Construir histograma")
if hist_button:
    st.write(
        "Creación de un histograma sobre anuncios de coches basado en el archivo CSV")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Mostrar gráfico de dispersión precio vs odómetro")
if scatter_button:
    st.write("Creación de un gráfico de dispersión de precio vs odómetro")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
