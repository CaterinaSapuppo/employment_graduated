import streamlit as st
import pandas as pd
import plotly.express as px
import io
import requests

# Funzione per caricare i dati da GitHub
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/yourusername/yourrepository/main/employment%20-%20graduated%20.xlsx'
    content = requests.get(url).content
    data = pd.read_excel(io.BytesIO(content))
    data.columns = ['Region Group', 'Region', 'Employment Rate 2021', 'Number of Graduates 2021']
    data['Region Group'] = data['Region Group'].ffill()
    data = data.dropna(subset=['Region'])
    data['Employment Rate 2021'] = pd.to_numeric(data['Employment Rate 2021'], errors='coerce') * 100
    return data

# Carica i dati senza interazione dell'utente
data = load_data()

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
