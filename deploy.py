import streamlit as st
import joblib

st.title("Iris Species Prediction")

model = joblib.load('knn_iris_model.joblib')

sepal_length = st.number_input(label='Sepal Length (cm)', min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input(label='Sepal Width (cm)', min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input(label='Petal Length (cm)', min_value=0.0, max_value=10.0, value=1.5)
petal_width = st.number_input(label='Petal Width (cm)', min_value=0.0, max_value=10.0, value=0.2)

sample = [[sepal_length, sepal_width, petal_length, petal_width]]

if st.button('Predict Species'):
    prediction = model.predict(sample)
    st.success(f'The predicted species is: {prediction[0]}')    