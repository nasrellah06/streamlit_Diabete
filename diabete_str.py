import streamlit as st
import numpy as np
import joblib

st.title("Bienvenue à l'Application de Détection du Diabète")
st.write("**Veuillez remplir les champs suivants**")

model = joblib.load("RForest_model.pkl")

Age = st.number_input("Age")

Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20)


BMI = st.number_input("BMI")

Glucose = st.number_input("Glucose")

BloodPressure = st.number_input("BloodPressure")


HbA1c = st.number_input("HbA1c")

LDL = st.number_input("LDL")

HDL = st.number_input("HDL")

Triglycerides = st.number_input("Triglycerides")


FamilyHistory = [0, 1]
FamilyHistory_choisi = st.selectbox("FamilyHistory", FamilyHistory)


DietType = [0, 1]
DietType_choisi = st.selectbox("DietType", DietType)


Hypertension = [0, 1]
Hypertension_choisi = st.selectbox("Hypertension", Hypertension)




MedicationUse = [0, 1]
MedicationUse_choisi = st.selectbox("MedicationUse", MedicationUse)




# Gender = ["Male", "Female"]
# gender_choisi = st.selectbox("Sélectionnez votre Sexe:", Gender)


# Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20)


# Balance = st.number_input("Balance")
# NumOfProducts = st.number_input("NumOfProducts", min_value=1, max_value=4)

# FamilyHistory = [0, 1]
# FamilyHistory_choisi = st.selectbox("FamilyHistory", FamilyHistory)

# IsActiveMember = [0, 1]
# IsActiveMember_choisi = st.selectbox("ActiveMember", IsActiveMember)

# EstimatedSalary = st.number_input("EstimatedSalary")




# Préparer le vecteur final (assurez-vous que l'ordre correspond au modèle)
features = np.array([[float(Age),
                      float(Pregnancies),
                      float(BMI),
                      float(Glucose),
                      float(BloodPressure),
                      int(HbA1c),
                      int(LDL),
                      float(HDL),
                      int(Triglycerides),
                      int(FamilyHistory_choisi ),
                      int(DietType_choisi),
                      int(Hypertension_choisi ),
                      int(MedicationUse_choisi),]])  

if st.button('Submit'):
        prediction = model.predict(features)[0]
        if prediction == 1:
            st.success("Le patient est **MALADE** .")
        else:
            st.info("Le patient **SAINT** .")
