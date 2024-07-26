import streamlit as st 
import pandas as pd
import pickle
from streamlit_option_menu import option_menu

# Load the model
diabetes = pickle.load(open('models/diabetes.sav', 'rb'))
heart = pickle.load(open('models/heart_disease.sav', 'rb'))

with st.sidebar:

    selected = option_menu('Multiple disease Prediction System',
                           ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart'],
                          default_index=0
                           )
if selected == 'Diabetes Prediction':

    # Page configuration
    st.title('Diabetes Prediction System')
    st.write('Please enter the following details to predict diabetes status:')

    # User inputs
    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input('Pregnancies', min_value=0)
        glucose = st.number_input('Glucose', min_value=0)
        blood_pressure = st.number_input('Blood Pressure', min_value=0)
        skin_thickness = st.number_input('Skin Thickness', min_value=0)

    with col2:
        insulin = st.number_input('Insulin', min_value=0)
        bmi = st.number_input('BMI', min_value=0.0, format='%f')
        diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, format='%f')
        age = st.number_input('Age', min_value=0)

    # Predict button
    if st.button('Predict Diabetes'):
        input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]],
                                columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
        prediction = diabetes.predict(input_data)[0]

        if prediction == 0:
            st.success('The person is not diabetic.')
        else:
            st.error('The person is diabetic.')


if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction System')
    st.write('Please enter the following details to predict heart status:')
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input('Age',min_value=0)
        sex = st.number_input('Gender: 1-male , 0-female', min_value=0, max_value=1)
        cp = st.number_input('Chest pain type --> 1,2,3,0 (essentially of 4 types)',min_value=0,max_value=4)
        trestbps = st.number_input('Resting blood pressure',min_value=0)
        chol = st.number_input('Serum cholesterol',min_value=0)
        fbs	= st.number_input('Fasting blood sugar',min_value=0)
        restecg = st.number_input('Resting electro-cardiographic result',min_value=0)

    with col2:

        thalach = st.number_input('Maximum heart rate achieved',min_value=0)
        exang = st.number_input('exercise induced angina 1-Y ,0-N',min_value=0)
        oldpeak = st.number_input('ST depression induced by exercise relative to rest',min_value=0)
        slope = st.number_input('The slope of the peak exercise ST segment')
        ca = st.number_input('Number of major vessels (0-3) colored by fluorosopy',min_value=0)
        thal = st.number_input('Thal: 3 = normal; 6 = fixed defect; 7 = reversable defect',min_value=0)


    if st.button('Predict Heart'):

        input_data = pd.DataFrame([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]],
                                  columns=['age','sex','cp','trestbps',	'chol','fbs','restecg','thalach','exang','oldpeak',	'slope','ca','thal']
                                  )

        prediction_h = heart.predict(input_data)[0]

        if prediction_h == 0:
            st.success('The person does not have a heart disease.')

        else:
            st.warning('The person has heart disease.')
