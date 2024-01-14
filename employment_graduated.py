import pandas as pd
import plotly.express as px
import streamlit as st

# Carica i dati
data = pd.read_excel('employment_graduated.xlsx')

# Rinomina le colonne
data.columns = ['Region Group', 'Region', 'Employment Rate 2021', 'Number of Graduates 2021']

# Gestisci i dati mancanti
data['Region Group'] = data['Region Group'].ffill()
data = data.dropna(subset=['Region'])

# Converte i tipi di dati
data['Employment Rate 2021'] = pd.to_numeric(data['Employment Rate 2021'], errors='coerce') * 100

# Crea un'app Streamlit



scatter_fig.update_layout(
    title={
        'text': "Employment rate vs Number of Graduated Students in all Italian Regions, 2021",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(
            family="Arial, sans-serif",  # Cambio del tipo di carattere in Arial
            size=10,
            color="#252525"
        )
    }
)



scatter_fig.update_xaxes(
    tickvals=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    showgrid=True,  # Mostra la griglia
    gridcolor='LightGrey',  # Colore della griglia
    linecolor='Black',  # Colore della linea dell'asse
    linewidth=2,  # Spessore della linea dell'asse
    showticklabels=True  # Mostra le etichette dei valori
)


# Mostra il grafico con Streamlit
st.plotly_chart(scatter_fig)


scatter_fig.update_layout(plot_bgcolor='white')
scatter_fig.update_xaxes(tickvals=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
scatter_fig.update_xaxes(showticklabels=True)

# Mostra il grafico con Streamlit
st.plotly_chart(scatter_fig)
