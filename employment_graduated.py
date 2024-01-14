import streamlit as st
import pandas as pd
import plotly.express as px

# Carica i dati (Aggiorna il percorso del file o caricalo direttamente)
@st.cache
def load_data():
    data = pd.read_excel('/path/to/your/data.xlsx')  # Aggiorna questo percorso
    data.columns = ['Region Group', 'Region', 'Employment Rate 2021', 'Number of Graduates 2021']
    data['Region Group'] = data['Region Group'].ffill()
    data = data.dropna(subset=['Region'])
    data['Employment Rate 2021'] = pd.to_numeric(data['Employment Rate 2021'], errors='coerce') * 100
    return data

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
