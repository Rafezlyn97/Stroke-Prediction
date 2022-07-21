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
X1 = x.select_dtypes(include = ['object'])
X2 = x.select_dtypes(exclude = ['object'])

if sorted(X1) != []:
  X1 = X1.apply(LabelEncoder().fit_transform)
  X = pd.concat([X2,X1], axis = 1)

y = LabelEncoder().fit_transform(y)


classifier_name = st.sidebar.selectedbox( 'Select Classifier', ('KKN', 'SVM', 'Random Forest'))

option = st.sidebar.selectbox(
    'Select a mini project',
     ['line chart','map','T n C','Long Process'])

if option=='line chart':
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

elif option=='map':
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data)

elif option=='T n C':
    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    show = st.checkbox('I agree the terms and conditions')
    if show:
        st.write(pd.DataFrame({
        'Intplan': ['yes', 'yes', 'yes', 'no'],
        'Churn Status': [0, 0, 0, 1]
        }))

else:
    'Starting a long computation...'
    
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
   
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'
