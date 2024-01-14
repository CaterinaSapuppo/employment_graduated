import pandas as pd
import plotly.express as px
import streamlit as st

# Load the data
data = pd.read_excel('/Users/caterinasapuppo/Desktop/employment_graduated.xlsx')

# Clean and prepare the data
data.columns = ['Region Group', 'Region', 'Employment Rate 2021', 'Number of Graduates 2021']
data['Region Group'] = data['Region Group'].ffill()
data = data.dropna(subset=['Region'])
data['Employment Rate 2021'] = pd.to_numeric(data['Employment Rate 2021'], errors='coerce') * 100

# Create a Streamlit app
st.title('Employment rate vs Number of Graduated Students in all Italian Regions, 2021')

# Scatter plot
scatter_fig = px.scatter(
    data,
    x='Employment Rate 2021',
    y='Number of Graduates 2021',
    color='Region Group',
    hover_name='Region'
)

scatter_fig.update_layout(plot_bgcolor='white')
scatter_fig.update_xaxes(tickvals=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
scatter_fig.update_xaxes(showticklabels=True)

# Display the plot using Streamlit
st.plotly_chart(scatter_fig)
