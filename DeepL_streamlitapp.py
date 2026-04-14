import streamlit as st
import torchaudio

st.title('Covid-19 Detection via Cough Audio')

st.text('Upload your cough audio file here:')
audio_file = st.file_uploader("cough audio")

prediction_text = st.text('Probability of COVID-19: -')

