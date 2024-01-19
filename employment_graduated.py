import pandas as pd
import plotly.express as px
import streamlit as st

# Data
data = pd.read_excel('employment_graduated.xlsx')


data.columns = ['Region Group', 'Region', 'Employment Rate 2021', 'Number of Graduates 2021']

# missing data
data['Region Group'] = data['Region Group'].ffill()
data = data.dropna(subset=['Region'])
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
        'text': "Employment rate vs Number of Graduated Students in all Italian Regions in 2021",
        'y': 0.95,
        'x': 0.42,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(
            family="DejaVu Sans, sans-serif",  # Cambio del tipo di carattere in DejaVu Sans
            size=15,
            color="gray"
        )
    }
)

# Legend
scatter_fig.update_layout(
    legend=dict(
        bordercolor="gray",  
        borderwidth=1,  
        y=0.50  
    )
)


scatter_fig.add_shape(
    
    type="line",
    x0=80, y0=-500,  
    x1=80, y1=data['Number of Graduates 2021'].max() + 1000,  
    line=dict(color="Black", width=2)
)
scatter_fig.add_shape(
    
    type="line",
    x0=0, y0=data['Number of Graduates 2021'].max() + 1000,  
    x1=80, y1=data['Number of Graduates 2021'].max() + 1000,  
    line=dict(color="Black", width=2)
)


scatter_fig.update_xaxes(title_text='Employment Rate (%)', range=[0, 80])  
scatter_fig.update_yaxes(title_text='Number of Graduates', range=[-500, data['Number of Graduates 2021'].max() + 1000])


scatter_fig.update_xaxes(showline=True, linewidth=1, linecolor='black')
scatter_fig.update_yaxes(showline=True, linewidth=1, linecolor='black')


scatter_fig.update_layout(plot_bgcolor='white')


scatter_fig.update_xaxes(tickvals=[20, 40, 60])
scatter_fig.update_xaxes(showticklabels=True)


st.plotly_chart(scatter_fig)
