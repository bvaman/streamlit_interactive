import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

st.title('Chip Performance Trends')
st.markdown('Chip dataset')

# Read the chip dataset
chip_data=pd.read_csv('chip_dataset.csv')
chip_data.drop(columns=chip_data.columns[0],axis=1,inplace=True) # filtering out unwanted columns
st.write(chip_data)

# sidebar selections 
st.sidebar.header('Pick two variables for your scatterplot')
x_val=st.sidebar.selectbox("Pick your x-axis:",chip_data.select_dtypes(include=np.number).columns.to_list())
y_val=st.sidebar.selectbox("Pick your y-axis:",chip_data.select_dtypes(include=np.number).columns.to_list())

st.markdown('')
st.markdown('')
# Scatter Plot
scatter = alt.Chart(chip_data, title=f"Correlation between {x_val} and {y_val}").mark_circle().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    color='Type',
   # size='Vendor',
    tooltip=(x_val,y_val) 
)
st.altair_chart(scatter,use_container_width=True)