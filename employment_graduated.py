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

scatter_fig = px.scatter(
    data,
    x='Employment Rate 2021',
    y='Number of Graduates 2021',
    color='Region Group',
    hover_name='Region',
    # Imposta la dimensione dei punti a 8
)

scatter_fig.update_layout(
    title={
        'text': "Employment rate vs Number of Graduated Students in all Italian Regions, 2021",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(
            family="Arial, sans-serif",  # Cambio del tipo di carattere in Arial
            size=14,
            color="darkgrey"
        )
    }
)

# Sposta la legenda leggermente più in basso
scatter_fig.update_layout(
    legend=dict(
        bordercolor="darkgrey",  # Imposta il colore del bordo della legenda a nero
        borderwidth=1,  # Imposta la larghezza del bordo a 1
        y=0.70  # Imposta la coordinata y della legenda per spostarla leggermente più in basso
    )
)

# Aggiungi etichette degli assi x e y
scatter_fig.update_xaxes(title_text='Employment Rate 2021 (%)')
scatter_fig.update_yaxes(title_text='Number of Graduates 2021', range=[-500, data['Number of Graduates 2021'].max() + 1000])

# Aggiungi linee degli assi x e y
scatter_fig.update_xaxes(showline=True, linewidth=1, linecolor='black')
scatter_fig.update_yaxes(showline=True, linewidth=1, linecolor='black')
scatter_fig.update_layout(plot_bgcolor='white')
scatter_fig.update_xaxes(tickvals=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
scatter_fig.update_xaxes(showticklabels=True)

# Aggiungi una box intorno alla figura
scatter_fig.add_shape(
    type="rect",
    x0=data['Employment Rate 2021'].min(),
    y0=data['Number of Graduates 2021'].min(),
    x1=data['Employment Rate 2021'].max(),
    y1=data['Number of Graduates 2021'].max(),
    line=dict(color="black", width=2),
    opacity=0.3,
)

# Mostra il grafico con Streamlit
st.plotly_chart(scatter_fig)
