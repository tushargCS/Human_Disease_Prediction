#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 09:44:59 2024

@author: anurag10
"""

    
#import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models
try:
    diabetes_model = pickle.load(open('/home/anurag10/Desktop/Multiple_disease_prediction_system/Saved_Model/diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('/home/anurag10/Desktop/Multiple_disease_prediction_system/Saved_Model/heart_disease_model.sav', 'rb'))
except FileNotFoundError as e:
    st.error(f"Error loading model: {e}")
    st.stop()

with st.sidebar:
    selected = option_menu('Human Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

if selected == 'Diabetes Prediction':
    # page title
    st.title('Diabetes Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    # Input fields for diabetes prediction
    with col1:
        Glucose = st.text_input('Glucose Level(0-199)')
        Insulin = st.text_input('Insulin Level(0-546)')
        Age = st.text_input('Age of the Person(21-81)')
        
    with col2:
        BloodPressure = st.text_input('Blood Pressure value(0-122)')
        BMI = st.text_input('BMI value(0-67.10)')

    with col3:
        SkinThickness = st.text_input('Skin Thickness value(0-99)')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value(0.078-2.42)')
    

    # Code for Prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        try:
            user_input = [Glucose, BloodPressure, SkinThickness, Insulin,
                          BMI, DiabetesPedigreeFunction, Age]

            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 0:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        except ValueError as e:
            st.error(f"Enter right user input")

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    # Input fields for heart disease prediction
    with col1:
        age = st.text_input('Age(29-77)')
        thalach = st.text_input('Maximum Heart Rate achieved(71-202')
        slope = st.text_input('Slope of the peak exercise ST segment(0,1,2)')

    with col2:
        sex = st.text_input('Sex(Female-0, Male-1)')
        oldpeak = st.text_input('ST depression induced by exercise(0-6.2)')
        ca = st.text_input('ca: Major vessels colored by flourosopy(0,1,2,3,4)')

    with col3:
        cp = st.text_input('Chest Pain types(0,1,2,3)')
        exang = st.text_input('Exercise Induced Angina(0,1)')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect(0,1,2,3)')

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, thalach, oldpeak, exang, slope, ca, thal]

            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except ValueError as e:
            st.error(f"Enter right user input")

    st.success(heart_diagnosis)
 