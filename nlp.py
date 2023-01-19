# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 16:28:47 2023

@author: tanus
"""

import numpy as np
import pandas as pd 
import pickle
import streamlit as st
import base64
from PIL import Image
model=pickle.load(open('NB_final_model.pkl','rb'))

st.set_page_config(page_title="Sentiment Analysis Web App",page_icon="",layout="centered",initial_sidebar_state="expanded",)
st.title('Hotel Reviews Classifier')
st.subheader('by Group no 6 ')

image=Image.open("sentiment.jpg")
image=st.image(image, caption='')



st.markdown("""
<style>
body {
    color: #ff0000;
    background-color: #001f;
    etc. 
}
</style>
    """, unsafe_allow_html=True)



st.subheader('Enter Text')
message = st.text_area("Type Here")
if st.button('ANALYZE'):
  disp=""
  a=model.predict([message])[0]
  if(a== 'pos'):
        disp = "Positive Review 😍"
  else:
        disp = "Negative Review 😔"
  st.header(disp)
 
  
  q = model.predict_proba([message])
  

st.sidebar.subheader("About App")

st.sidebar.info("This web app is made as part of Sentiment Analysis Major Project")
st.sidebar.info("Scroll down and type Review in the writing area")
st.sidebar.info("Click on the 'ANALYZE' button to check whether the entered text is 'Positive' or 'Negative' ")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=10,step=1)

if feedback:
  st.header("Thank you for rating the app!")