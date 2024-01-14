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
data['Employment Rate 2021'] = pd.to_numeric(data['Employment Rate 2021'], errors='coerce')

# Scatter plot
scatter_fig = px.scatter(
    data,
    x='Employment Rate 2021',
    y='Number of Graduates 2021',
    color='Region Group',
    hover_name='Region'
)


scatter_fig.update_layout(
    title={
        'text': "Employment rate vs Number of Graduated Students in all Italian Regions, 2021",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'right',
        'yanchor': 'top',
        'font': dict(
            family="Arial, sans-serif",  # Cambio del tipo di carattere in Arial
            size=14,
            color="darkgrey"
        )
    }
)

# Aggiungi etichette degli assi x e y
scatter_fig.update_xaxes(title_text='Employment Rate 2021 (%)')
scatter_fig.update_yaxes(title_text='Number of Graduates 2021')

# Aggiungi linee degli assi x e y
scatter_fig.update_xaxes(showline=True, linewidth=1, linecolor='black')
scatter_fig.update_yaxes(showline=True, linewidth=1, linecolor='black')
scatter_fig.update_layout(plot_bgcolor='white')
scatter_fig.update_xaxes(tickvals=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
scatter_fig.update_xaxes(showticklabels=True)

# Mostra il grafico con Streamlit
st.plotly_chart(scatter_fig)
