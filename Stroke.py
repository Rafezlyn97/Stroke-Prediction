import streamlit as st
import numpy as np
import pandas as pd

st.title("Stroke Prediction Dataset")

st.header("Data collection")
data = pd.read_csv('https://raw.githubusercontent.com/Rafezlyn97/Stroke-Prediction/main/healthcare-dataset-stroke-data.csv')
st.write(pd.DataFrame(data))
