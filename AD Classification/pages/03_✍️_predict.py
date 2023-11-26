import streamlit as st
import pandas as pd
import pickle
#for using the saved model


st.title("Alzheimer's Disease Classification")

gender = st.text_input("Gender (M/F)")
age= st.text_input("Age")
educ= st.text_input("Years of Education")
ses= st.text_input("Socioeconomic Status (1-5)")
mmse= st.text_input("Mini Mental State Examination")
cdr= st.text_input("Clinical Dementia Rating (0-1)")
etiv = st.text_input("Estimated total intracranial volume")
nwbv = st.text_input("Normalize Whole Brain Volume")
asf = st.text_input("Atlas Scaling Factor")

#change the value of variables
#according to our need
if gender == 'M': gender= 1  
else: gender= 0
    

#adding a button
if st.button('Predict/Classify'):
    data= {'M/F':gender,'Age':int(age),'EDUC':int(educ),'SES':float(ses),'MMSE':float(mmse),'CDR':float(cdr),'eTIV':int(etiv),'nWBV':float(nwbv),'ASF':float(asf)}

    df= pd.DataFrame(data,index=[0])

    #load the model
    model= pickle.load(open('clf9','rb'))
        
    predicted= model.predict(df)
        
    if predicted == [0]:
        st.success('This person falls into the Converted category..')
    elif predicted == [1]:
        st.success('This person falls into the Demented category.')
    else:
        st.success('This person falls into the Non-Demented category.')

from PIL import Image
i4 = Image.open(r'd3.jpg') 
st.image(i4, output_format = 'auto') 

