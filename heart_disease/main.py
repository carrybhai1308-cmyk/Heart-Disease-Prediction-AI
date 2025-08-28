import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sklearn

#Load Model through joblib
model=joblib.load('Heart_Disease_Model')

# Title of the app
st.title("❤️ Heart Disease Prediction App")

st.text("This app predicts whether a person has heart disease or not based on some medical parameters.")

Age=st.number_input("Age :",min_value=18,max_value=100,value=50,step=5)

Is_Male=st.radio("Gender :",['Male','Female'])

RestingBP=st.number_input("Resting Blood Pressure (in mm Hg) :",min_value=80,max_value=200,value=120,step=10)

Cholesterol=st.number_input("Cholesterol (in mg/dl) :",min_value=100,max_value=600,value=200,step=20)

FastingBS=st.selectbox("Fasting Blood Sugar > 120 mg/df :",["Yes","No"])

MaxHR=st.number_input("Maximum Heart Rate Achieved : ",min_value=60,max_value=220,value=140,step=10)

ExerciseAngina=st.selectbox("Exercise Induced Angina :",["Yes","No"])

Oldpeak=st.number_input("Oldpeak (ST depression induced by exercise relative to rest) :",min_value=-2.5,max_value=6.3,step=1.0)

Chest_Pain=st.selectbox("Chest Pain Type :",["ASY","ATA","NAP","TA"])

Resting_ECG=st.selectbox("Resting Electrocardiographic Results :",["Normal","ST","LVH"])

ST_Slope=st.selectbox("Slope of the peak exercise ST segment :",["Up","Flat","Down"])


# Encoding
ExerciseAngina=1 if ExerciseAngina=="Yes" else 0

Is_Male=1 if Is_Male=="Male" else 0


FastingBS=1 if FastingBS=="Yes" else 0

# Chest_Pain only (NAP & TA Kept)
ChestPainType_NAP=1 if Chest_Pain=="NAP" else 0
ChestPainType_TA=1 if Chest_Pain=="TA" else 0

# Resting_ECG only (Normal & ST Kept)
RestingECG_Normal=1 if Resting_ECG=="Normal" else 0	
RestingECG_ST=1 if Resting_ECG=="ST" else 0

# ST_Slope only (Up & Flat Kept)
ST_Slope_Up=1 if ST_Slope=="Up" else 0
ST_Slope_Flat=1 if ST_Slope=="Flat" else 0


user_input=np.array([[Age,Is_Male, RestingBP,Cholesterol,FastingBS,MaxHR,
       ExerciseAngina,Oldpeak,ChestPainType_NAP,ChestPainType_TA,
       RestingECG_Normal,RestingECG_ST,ST_Slope_Flat,ST_Slope_Up]])

if st.button("Predict"):
    prediction=model.predict(user_input)
    if prediction[0]==1:
        st.error("🫀 High Chance of Heart Disease ,Please Consult to Doctor For Treatment")
    else:
        st.success("😊 NO Heart Disease Detected,You are Healthy")