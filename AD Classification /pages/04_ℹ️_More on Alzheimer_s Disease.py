import streamlit as st 

st.markdown("""
<style>
.big-font {
    font-size:19px ;
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

st.title("Alzheimer")
st.markdown('- <p class="big-font">Alzheimer’s is a type of dementia that causes problems with memory, thinking and behavior. Symptoms usually develop slowly and get worse over time, becoming severe enough to interfere with daily tasks.</p>', unsafe_allow_html=True)         
st.markdown('- <p class="big-font">Alzheimer’s is not a normal part of aging. The greatest known risk factor is increasing age, and the majority of people with Alzheimer’s are 65 and older. But Alzheimer’s is not just a disease of old age. Approximately 200,000 Americans under the age of 65 have younger-onset Alzheimer’s disease (also known as early-onset Alzheimer’s).</p>', unsafe_allow_html=True)

from PIL import Image
i3 = Image.open(r'i3.webp') 
st.image(i3, output_format = 'auto') 

st.markdown('- <p class="big-font">Alzheimer’s  is the sixth leading cause of death in the United States. Those with Alzheimer’s live an average of eight years after their symptoms become noticeable to others, but survival can range from four to 20 years, depending on age and other health conditions.</p>', unsafe_allow_html=True)         
st.markdown('- <p class="big-font">Alzheimer’s has no current cure, but treatments for symptoms are available and research continues. Although current Alzheimer’s treatments cannot stop Alzheimer’s from progressing, they can temporarily slow the worsening of dementia symptoms and improve quality of life for those with Alzheimer’s and their caregivers. Today, there is a worldwide effort under way to find better ways to treat the disease, delay its onset, and prevent it from developing.</p>', unsafe_allow_html=True)         


st.title("Stages of Alzheimer's disease")

from PIL import Image
stages = Image.open(r'stagesalz.png') 
st.image(stages, output_format = 'auto') 

st.header("Mild Alzheimer’s disease")
st.markdown('<p class="big-font">As Alzheimer’s worsens, people experience greater memory loss and other cognitive difficulties. Problems can include wandering and getting lost, trouble handling money and paying bills, repeating questions, taking longer to complete normal daily tasks, and personality and behavior changes. People are often diagnosed in this stage.</p>', unsafe_allow_html=True)         

st.header("Moderate Alzheimer’s disease")
st.markdown('<p class="big-font">In this stage, damage occurs in areas of the brain that control language, reasoning, conscious thought, and sensory processing, such as the ability to correctly detect sounds and smells. Memory loss and confusion grow worse, and people begin to have problems recognizing family and friends. They may be unable to learn new things, carry out multistep tasks such as getting dressed, or cope with new situations. In addition, people at this stage may have hallucinations, delusions, and paranoia and may behave impulsively.</p>', unsafe_allow_html=True)  

st.header("Severe Alzheimer’s disease")       
st.markdown('<p class="big-font">Ultimately, plaques and tangles spread throughout the brain, and brain tissue shrinks significantly. People with severe Alzheimer’s cannot communicate and are completely dependent on others for their care. Near the end of life, the person may be in bed most or all of the time as the body shuts down.</p>', unsafe_allow_html=True)         

