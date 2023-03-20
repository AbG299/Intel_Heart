import streamlit as st
import numpy as np
import pandas as pd
import pickle



st.title('PREDICTION OF HEART DISEASE RISK')
col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input('Age')

    dic = {'Female':0,'Male':1}
    arr = list(dic.keys())
    b = st.selectbox("Sex",arr)
    b = dic[b]

    c = st.selectbox('Chest pain type',[0,1,2,3])
    d = st.number_input("Rest Blood Pressure")

with col2:
    e = st.number_input("Cholestrol")

    dic = {'True':1,'False':0}
    arr = list(dic.keys())
    f = st.selectbox("Fasting Blood Sugar>120mg/dl",arr)
    f = dic[f]

    dic = {'Danger':1,'No Danger':0}
    arr = list(dic.keys())
    g = st.selectbox("Resting electro cardiographic result ",arr)
    g = dic[g]


    h = st.number_input("Max Heart Rate ")
    
    
with col3:
    dic = {'Yes':1,'No':0}
    arr = list(dic.keys())
    i = st.selectbox("Exercise Induced angina ",arr)
    i = dic[i]

    j = st.number_input("St depression induced by exercise",step=1.,format="%.3f")
    k = st.number_input("Slope of peak exercise ST segment")
    l = st.selectbox("Number of major vessels",[0,1,2,3])
    dic = {'Normal':1,'Fixed defect':2,'Reversable defect':3}
    arr = list(dic.keys())
    m = st.selectbox("Exercise Induced angina ",arr)
    m = dic[m]



file = open('intel_model.pkl','rb')
model = pickle.load(file)


def predict(): 
    row = np.array([a,b,c,d,e,f,g,h,i,j,k,l,m])
    col=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']
    
    X = pd.DataFrame([row], columns = col)
    prediction = model.predict(X)
    if prediction[0] == 0:
        st.title(':green[RESULT : NO HEART DISEASE:thumbsup:]')
        st.balloons()
    else: 
        st.title(':red[RESULT : AT RISK :thumbsdown:]')
    with st.sidebar:
            st.title('**:blue[PREVIOUS INPUT VALUES]**')
            st.table(X.T)
trigger = st.button('Predict', on_click=predict)


file.close()