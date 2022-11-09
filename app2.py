#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import joblib
import pandas as pd 

st.title('Algal data estimator')
model1 = joblib.load('xgmodel.joblib')
model2 = joblib.load('xgmodel2.joblib')

if "enable" not in st.session_state:
    st.session_state.enable = False
    
chlorodat = st.checkbox("I have chlorophyl data")
if chlorodat:
    st.session_state.enable = True
    
    chla = st.number_input("Input Chlorophyll-a content")
    
temperature = st.number_input("Input water temperature")
pH = st.number_input("Input water pH")
Do = st.number_input("Input DO")


if st.session_state.enable==False:
    def predict(): 
        prediction = model2.predict(X),
        if prediction[0] == 1: 
            st.write('Low algal activity')
        elif prediction[0]==2: 
            st.write('High activity')
        elif prediction[0]==0:
            st.write('Moderate activity')
    st.button('predict',on_click=predict)
    model = model2
    X = pd.DataFrame({'Temp(℃)':[temperature],
                     'pH':[pH],
                     'DO(㎎/L)':[Do]})

if st.session_state.enable==True:
    def predict2(): 
        prediction = model1.predict(X),
        if prediction[0] == 1: 
            st.write('Low algal activity')
        elif prediction[0]==2: 
                st.write('High activity')
        elif prediction[0]==0:
                st.write('Moderate activity')
    st.button('predict', on_click=predict2)
    model = model1
    X = pd.DataFrame({'Temp(℃)':[temperature],
                          'pH':[pH],
                          'DO(㎎/L)':[Do],
                          'Chl-a (㎎/㎥)': [chla]})
    
