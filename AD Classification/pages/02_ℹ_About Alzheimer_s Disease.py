import streamlit as st 

st.markdown("""
<style>
.big-font {
    font-size:19px ;
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

st.title("Alzheimer's Disease Fact Sheet")

st.markdown('- <p class="big-font">Alzheimer’s disease is a brain disorder that slowly destroys memory and thinking skills, and, eventually, the ability to carry out the simplest tasks. In most people with Alzheimer’s, symptoms first appear later in life.</p>', unsafe_allow_html=True)

st.markdown('''- <p class="big-font">Dementia is a general term for loss of memory and other mental abilities severe enough to interfere with daily life. It is caused by physical changes in the brain. Alzheimer's is the most common type of dementia, but there are many kinds.''',True)      
st.markdown('- <p class="big-font">The estimated dementia prevalence for adults ages 60+ in India is 7.4%. About 8.8 million Indians older than 60 years live with dementia. Dementia is more prevalent among females than males and in rural than urban areas.</p>', unsafe_allow_html=True)

st.markdown('- <p class="big-font">The current statistical data and reports reported that India ranks 137 with 14.60% rate of deaths by Alzheimer & Dementia on the list of countries in the world.</p>', unsafe_allow_html=True)         

st.markdown('- <p class="big-font">Alzheimer’s disease is named after Dr. Alois Alzheimer. In 1906, Dr. Alzheimer noticed changes in the brain tissue of a woman who had died of an unusual mental illness. Her symptoms included memory loss, language problems, and unpredictable behavior. After she died, he examined her brain and found many abnormal clumps (now called amyloid plaques) and tangled bundles of fibers (now called neurofibrillary, or tau, tangles).</p>', unsafe_allow_html=True)         

from PIL import Image
i2 = Image.open(r'ad.jpg') 
st.image(i2, output_format = 'auto') 
         
st.markdown('<p class="big-font">These plaques and tangles in the brain are still considered some of the main features of Alzheimer’s disease. Another feature is the loss of connections between neurons in the brain. Neurons transmit messages between different parts of the brain, and from the brain to muscles and organs in the body.</p>', unsafe_allow_html=True)         

st.header("How does Alzheimer's disease affect the brain?")
st.markdown('<p class="big-font">Scientists continue to unravel the complex brain changes involved in Alzheimer’s disease. Changes in the brain may begin a decade or more before symptoms appear. During this very early stage of Alzheimer’s, toxic changes are taking place in the brain, including abnormal buildups of proteins that form amyloid plaques and tau tangles. Previously healthy neurons stop functioning, lose connections with other neurons, and die. Many other complex brain changes are thought to play a role in Alzheimer’s as well.</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">The damage initially appears to take place in the hippocampus and the entorhinal cortex, which are parts of the brain that are essential in forming memories. As more neurons die, additional parts of the brain are affected and begin to shrink. By the final stage of Alzheimer’s, damage is widespread and brain tissue has shrunk significantly.</p>', unsafe_allow_html=True)         
