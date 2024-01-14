import streamlit as st
import pandas as pd
import plotly.express as px

# Funzione per caricare i dati da un file caricato dall'utente
def load_data(uploaded_file):
    data = pd.read_excel(uploaded_file)
    data.columns = ['Region Group', 'Region', 'Employment Rate 2021', 'Number of Graduates 2021']
    data['Region Group'] = data['Region Group'].ffill()
    data = data.dropna(subset=['Region'])
    data['Employment Rate 2021'] = pd.to_numeric(data['Employment Rate 2021'], errors='coerce') * 100
    return data

# Caricamento del file tramite l'interfaccia utente
uploaded_file = st.file_uploader("Carica il file Excel", type=["xlsx"])
if uploaded_file is not None:
    data = load_data(uploaded_file)
    # Titolo dell'app
    st.title('Employment rate vs Number of Graduated Students in all Italian Regions, 2021')

    # Grafico
    fig = px.scatter(
        data,
        x='Employment Rate 2021',
        y='Number of Graduates 2021',
        color='Region Group',
        hover_name='Region'
    )

    fig.update_layout(grid=None, plot_bgcolor='white')
    fig.update_xaxes(tickvals=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    fig.update_xaxes(showticklabels=True)

    st.plotly_chart(fig)
