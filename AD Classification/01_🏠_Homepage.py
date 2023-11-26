import streamlit as st

st.set_page_config( 
    page_title ="Alzheimer Disease Prediction",
    page_icon = "🧠"
)

st.markdown("""
<style>
.big-font {
    font-size:19px ;
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

st.title("Introducing DoctorGPT")
st.sidebar.success("Select a page above.")

st.markdown('''<p class="big-font">This is a Machine Learning based application which can be used to precisely classify a person that might belong to Demented, Non-Demented and Converted category. Our team has trained a model called DoctorGPT which allows users to find out which category they belong. The model takes your some clinical health data as an input and try to precisely predicit about possiblity of having Alzheimer's Disease.</p>''', unsafe_allow_html=True)

from PIL import Image
i1 = Image.open(r"i1.jpg") 
st.image(i1, output_format = 'auto') 

st.header('How it works?')
st.markdown('''<p class="big-font">DoctorGPT is designed and trained using various Machine Learning Algorithms to precisely predict about the patient. The user have to enter details of a patient and based on the input provided DoctorGPT will use it in the best Algorithm. The data that is requested from the user will be the following clinical data:\n
      Clinical Info:              \n
             1. Age --> Age\n  
             2. EDUC --> Years of Education\n
             3. SES --> Socioeconomic Status / 1-5\n
             4. MMSE --> Mini Mental State Examination [0 = worst to 30 = best]\n
             5. CDR --> Clinical Dementia Rating\n
             6. eTIV --> Estimated total intracranial volume\n
             7. nWBV --> Normalize Whole Brain Volume\n
             8. ASF --> Atlas Scaling Factor\n
             9. Gender --> M/F\n <p class='big-font'>The Algorithm works upon the data provided and will result in a message stating the precise category as the output.</p>''', unsafe_allow_html=True)         

i2 = Image.open(r"ad1.jpg") 
st.image(i2, output_format = 'auto') 


