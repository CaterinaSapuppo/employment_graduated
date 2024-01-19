# Import necessary libraries
import pandas as pd
import plotly.express as px
import streamlit as st

# Load data from an Excel file
data = pd.read_excel('employment_graduated.xlsx')

# Rename columns for clarity
data.columns = ['Region Group', 'Region', 'Employment Rate 2021', 'Number of Graduates 2021']

# Fill missing values in 'Region Group' column and drop rows with missing 'Region'
data['Region Group'] = data['Region Group'].ffill()
data = data.dropna(subset=['Region'])

# Convert 'Employment Rate 2021' column to numeric, handling errors
data['Employment Rate 2021'] = pd.to_numeric(data['Employment Rate 2021'], errors='coerce')

# Create a scatter plot using Plotly Express
scatter_fig = px.scatter(
    data,
    x='Employment Rate 2021',
    y='Number of Graduates 2021',
    color='Region Group',
    hover_name='Region'
)

# Customize plot layout
scatter_fig.update_layout(
    title={
        'text': "Employment rate vs Number of Graduated Students in all Italian Regions in 2021",
        'y': 0.95,
        'x': 0.42,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(
            family="DejaVu Sans, sans-serif",
            size=15,
            color="gray"
        )
    },
    legend=dict(
        bordercolor="gray",
        borderwidth=1,
        y=0.50
    )
)

# Add horizontal and vertical lines to the plot
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

# Customize axes and plot background
scatter_fig.update_xaxes(title_text='Employment Rate (%)', range=[0, 80], showline=True, linewidth=1, linecolor='black')
scatter_fig.update_yaxes(title_text='Number of Graduates', range=[-500, data['Number of Graduates 2021'].max() + 1000], showline=True, linewidth=1, linecolor='black')
scatter_fig.update_xaxes(tickvals=[20, 40, 60], showticklabels=True)
scatter_fig.update_layout(plot_bgcolor='white')

# Display the plot in Streamlit
st.plotly_chart(scatter_fig)
