# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:56:11 2025

@author: AINDR
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open('trained_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_trained_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

breat_cancer_model=pickle.load(open('Breast_cancer_model.sav', 'rb'))

lung_disease_model=pickle.load(open('Lung_disease_model.sav', 'rb'))

hiv_disease_model=pickle.load(open('HIV_disease_model.sav', 'rb'))

heart_stoke_disease_model=pickle.load(open('Heart_stoke_data.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction','Breast Cancer Prediction',
                            'Lung Cancer Prediction','HIV Prediction',
                            'Heart Stroke Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person','x-diamond-fill','lungs','bi-virus','heart-pulse-fill'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4,col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)     





#breast cancer prediction
if selected == 'Breast Cancer Prediction':

    # page title
    st.title('Breast Cancer Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
       mean_radius = st.text_input('Mean Radius Value')

    with col2:
        mean_texture = st.text_input('Mean Texture Value')

    with col3:
        mean_perimeter = st.text_input('Mean Perimeter value')

    with col1:
        mean_area = st.text_input('Mean Area value')

    with col2:
        mean_smoothness = st.text_input('Mean Smoothness Value')



    # code for Prediction
    breast_diagnosis = ''  


    # creating a button for Prediction    
    if st.button("Breast cancer Test Result"):   
        
        user_input = [mean_radius,	mean_texture, mean_perimeter,	mean_area,	mean_smoothness]

        user_input = [float(x) for x in user_input]

        breast_cancer_prediction = breat_cancer_model.predict([user_input])

        if breast_cancer_prediction[0] == 1:
            breast_diagnosis = "The person has Breast Cancer"
        else:
            breast_diagnosis = "The person does not have Breast Cancer"

    st.success(breast_diagnosis)   
    
    
    
    

# Lung Disease Prediction Page
if selected == 'Lung Cancer Prediction':

    # page title
    st.title('Lung Cancer Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        smoke = st.radio('Are you a Smoker', ['T', 'F'])

    with col2:
        FVC = st.text_input('Forced Vital Capacity Value')

    with col3:
       FEC1 = st.text_input('Forced Expiratory Volume in 1 Second')

    with col1:
        PEFR = st.radio('Peak Expiratory Flow Rate',['T','F'])

    with col2:
        O2 = st.radio('oxygen level status',['T','F'])

    with col3:
      ABG_P_O2 = st.radio('Arterial Blood Gas Partial Pressure of Oxygen',['T','F'])

    with col1:
       ABG_P_CO2 = st.radio('Arterial Blood Gas Partial Pressure of Carbon Dioxide',['T','F'])

    with col2:
        ABG_pH_Level = st.radio('Arterial Blood Gas ph level',['T','F'])

    with col3:
       Scan = st.radio('scan performed',['X-ray', 'MRI', 'CT'])

    with col1:
        Asthama = st.radio('patient has asthma',['T','F'])

    with col2:
        Other_diseaes = st.radio('Other diseaes',['T','F'])

    with col3:
        AGE= st.text_input('AGE')


    # code for Prediction
    lung_diagnosis = ''

    # creating a button for Prediction

    if st.button('Lung Cancer Disease Test Result'):

        user_input = [smoke, FVC, FEC1,	PEFR,	O2,	ABG_P_O2,	ABG_P_CO2,	ABG_pH_Level,	Scan,	Asthama,	Other_diseaes,	AGE	]

        user_input = [float(x) for x in user_input]

        lung_prediction = lung_disease_model.predict([user_input])

        if lung_prediction[0] == 1:
            lung_diagnosis = 'The person is having Lung disease'
        else:
            lung_diagnosis = 'The person does not have any Lung disease'

    st.success(lung_diagnosis)





# HIV Disease Prediction Page
if selected == 'HIV Prediction':

    # page title
    st.title('HIV Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')

    with col2:
        Marital_Staus = st.radio('Marrital Status',['Unmarried','Married','Divorced','Widowed','Cohabiting'])

    with col3:
        STD = st.radio('Sexually Transmitted Disease',['YES','NO'])

    with col1:
     Educational_Background = st.radio('Educational Background',['Senior High School','College Degree','Junior High School','Illiteracy','Primary School'])

    with col2:
      HIV_TEST_IN_PAST_YEAR = st.radio('HIV_TEST_IN_PAST_YEAR',['YES','NO'])

    with col3:
     AIDS_education = st.radio('AIDS education',['YES','NO'])

    with col1:
      Places_of_seeking_sex_partners= st.radio('Places of seeking sex partners',['Public Bath','Park','Bar','Internet','Others','None'])

    with col2:
       SEXUAL_ORIENTATION = st.radio('SEXUAL ORIENTATION',['Heterosexual','Bisexual','Homosexual'])

    with col3:
       Drug_taking = st.radio('Drug taking',['YES', 'NO'])


    # code for Prediction
    hiv_diagnosis = ''

    # creating a button for Prediction

    if st.button('HIV Prediction Test Result'):

        user_input = [Age,	Marital_Staus	,STD,	Educational_Background,	HIV_TEST_IN_PAST_YEAR,	AIDS_education,	
                      Places_of_seeking_sex_partners,	SEXUAL_ORIENTATION,	Drug_taking	]

        user_input = [float(x) for x in user_input]

        hiv_prediction = hiv_disease_model.predict([user_input])

        if hiv_prediction[0] == 1:
            hiv_diagnosis = 'The person is having HIV'
        else:
            hiv_diagnosis = 'The person does not have HIV'

    st.success(hiv_diagnosis)
    
    
    
    
    
# Heartstroke Disease Prediction Page
if selected == 'Heart Stroke Prediction':

    # page title
    st.title('Heart Stroke using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.radio('Gender',['Male','Female'])

    with col2:
        age = st.text_input('Age')

    with col3:
        hypertension = st.radio('hypertension',[0,1])

    with col1:
       heart_disease = st.radio('heart disease',[0,1])

    with col2:
    	ever_married = st.radio('ever_married',['Yes','No'])

    with col3:
     work_type= st.radio('work type',['Private','Self-employed','Govt_job','children'])

    with col1:
      Residence_type= st.radio('Residence_type',['Urban','Rural','Bar','Internet','Others','None'])

    with col2:
      avg_glucose_level= st.text_input('Average Glucose Level')

    with col3:
      bmi = st.text_input('BMI')
      
    with col1:
      smoking_status= st.radio('smoking_status',['formerly smoked','never smoked','smokes','Unknown'])


    # code for Prediction
    hstroke_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Stroke Prediction Test Result'):

        user_input = [gender, age,	hypertension,	heart_disease,	ever_married,	work_type,	Residence_type,	avg_glucose_level,	bmi,	smoking_status		]

        user_input = [float(x) for x in user_input]

        hstroke_prediction = heart_stoke_disease_model.predict([user_input])

        if hstroke_prediction[0] == 1:
            hstroke_diagnosis = 'The person is likely to have a Heart stroke'
        else:
            hstroke_diagnosis = 'The person is not likely to have a Heart stroke'

    st.success(hstroke_diagnosis)

            