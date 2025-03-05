import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Cargar el modelo ya entrenado en pickle
with open('Modelo_Pred.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Crear app en streamlit
st.title("Predicción de incumplimiento de pago de tarjetas de crédito")

st.sidebar.header("Informacion del usuario")

# Agregar inputs
limit_bal = st.sidebar.slider("LIMIT_BAL (Cantidad del credito en dolares de taiwan)", 0, 1000000, 50000)
sex = st.sidebar.radio("SEXO (Género)", ["Hombre", "Mujer"])
education = st.sidebar.radio("EDUCACION (Nivel de Educación)", ["Posgrado", "Universidad", "Secundaria", "Otros"])
marriage = st.sidebar.radio("MATRIMONIO (Estado Civil)", ["Casado", "Soltero", "Otros"])
age = st.sidebar.slider("EDAD (Años)", 20, 80, 30)
pay_status_sept = st.sidebar.slider("PAY_0 (Estado de pago de Septiembre, 2005)", -1, 12, 0)
pay_status_aug = st.sidebar.slider("PAY_2 (Estado de pago de Agosto, 2005)", -1, 12, 0)
pay_status_jul = st.sidebar.slider("PAY_3 (Estado de pago de Julio, 2005)", -1, 12, 0)
pay_status_jun = st.sidebar.slider("PAY_4 (Estado de pago de Junio, 2005)", -1, 12, 0)
pay_status_may = st.sidebar.slider("PAY_5 (Estado de pago de Mayo, 2005)", -1, 12, 0)
pay_status_apr = st.sidebar.slider("PAY_6 (Estado de pago de Abril, 2005)", -1, 12, 0)
bill_amt_sept = st.sidebar.slider("BILL_AMT1 (Estado de cuenta de Septiembre, 2005)", 0, 1000000, 5000)
bill_amt_aug = st.sidebar.slider("BILL_AMT2 (Estado de cuenta de Agosto, 2005)", 0, 1000000, 5000)
bill_amt_jul = st.sidebar.slider("BILL_AMT3 (Estado de cuenta de Julio, 2005)", 0, 1000000, 5000)
bill_amt_jun = st.sidebar.slider("BILL_AMT4 (Estado de cuenta de Junio, 2005)", 0, 1000000, 5000)
bill_amt_may = st.sidebar.slider("BILL_AMT5 (Estado de cuenta de Mayo, 2005)", 0, 1000000, 5000)
bill_amt_apr = st.sidebar.slider("BILL_AMT6 (Estado de cuenta de Abril, 2005)", 0, 1000000, 5000)
pay_amt_sept = st.sidebar.slider("PAY_AMT1 (Pago anterior en Septiembre, 2005)", 0, 100000, 500)
pay_amt_aug = st.sidebar.slider("PAY_AMT2 (Pago anterior en Agosto, 2005)", 0, 100000, 500)
pay_amt_jul = st.sidebar.slider("PAY_AMT3 (Pago anterior en Julio, 2005)", 0, 100000, 500)
pay_amt_jun = st.sidebar.slider("PAY_AMT4 (Pago anterior en Junio 2005)", 0, 100000, 500)
pay_amt_may = st.sidebar.slider("PAY_AMT5 (Pago anterior en Mayo, 2005)", 0, 100000, 500)
pay_amt_apr = st.sidebar.slider("PAY_AMT6 (Pago anterior en Abril, 2005)", 0, 100000, 500)

# Definir los mapeos para la educación y el estado civil
education_mapping = {
    "Posgrado": 1,
    "Universidad": 2,
    "Secundaria": 3,
    "Otros": 4
}

marriage_mapping = {
    "Casado": 1,
    "Soltero": 2,
    "Otros": 3
}

# Crear un df con los datos de los inputs
user_input_data = pd.DataFrame({
    "LIMIT_BAL": [limit_bal],
    "SEXO": [1 if sex == "Hombre" else 2],  # Mapear 'Hombre' a 1 y 'Mujer' a 2
    "EDUCACION": [education_mapping[education]],
    "MATRIMONIO": [marriage_mapping[marriage]],
    "EDAD": [age],
    "PAY_0": [pay_status_sept],
    "PAY_2": [pay_status_aug],
    "PAY_3": [pay_status_jul],
    "PAY_4": [pay_status_jun],
    "PAY_5": [pay_status_may],
    "PAY_6": [pay_status_apr],
    "BILL_AMT1": [bill_amt_sept],
    "BILL_AMT2": [bill_amt_aug],
    "BILL_AMT3": [bill_amt_jul],
    "BILL_AMT4": [bill_amt_jun],
    "BILL_AMT5": [bill_amt_may],
    "BILL_AMT6": [bill_amt_apr],
    "PAY_AMT1": [pay_amt_sept],
    "PAY_AMT2": [pay_amt_aug],
    "PAY_AMT3": [pay_amt_jul],
    "PAY_AMT4": [pay_amt_jun],
    "PAY_AMT5": [pay_amt_may],
    "PAY_AMT6": [pay_amt_apr]
})
user_input_data_scaled = scaler.transform(user_input_data)
# Botón para predecir
if st.sidebar.button("Predecir"):
    # Hacer las predicciones usando el modelo creado
    predicted_default = model.predict(user_input_data)

    # Mostrar el resultado de la predicción
    st.subheader("Resultado de la predicción")
    if predicted_default[0] == 1:
        st.write("Se predice que el cliente puede incumplir con el pago de su tarjeta de crédito.")
    else:
        st.write("Se predice que es poco probable que el cliente incumpla con el pago de su tarjeta de crédito.")
