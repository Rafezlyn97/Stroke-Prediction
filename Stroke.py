import streamlit as st
import numpy as np
import pandas as pd

st.title("Stroke Prediction Dataset")

st.header("Data collection")
data = pd.read_csv('https://raw.githubusercontent.com/Rafezlyn97/Stroke-Prediction/main/healthcare-dataset-stroke-data.csv')
st.write(pd.DataFrame(data))

Y_name = st.sidebar.selectedbox('Select Label/Y', sorted(data))
X_name = st.sidebar.multiselect('Select Predictors/X', sorted(data), default = sorted(data)[1], help = 'Can Select more than One')

y = data.loc[:,Y_name]
x = data.loc[:,X_name]
X1 = x.select_dtypes(include = ['object']
X2 = x.select_dtypes(exclude = ['object']

if sorted(X1) != []:
  X1 = X1.apply(LabelEncoder().fit_transform)
  X = pd.concat([X2,X1], axis = 1)

y = LabelEncoder().fit_transform(y)


classifier_name = st.sidebar.selectedbox( 'Select Classifier', ('KKN', 'SVM', 'Random Forest'))
