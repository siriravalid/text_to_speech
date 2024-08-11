# app.py
import streamlit as st
from gtts import gTTS
import tempfile

st.title("Text-to-Speech")

# Create a session state to keep track of the text
if 'text' not in st.session_state:
    st.session_state.text = ""

# Text area for user input
st.session_state.text = st.text_area("Enter text to convert to speech", value=st.session_state.text)

if st.button("Convert"):
    if st.session_state.text:
        # Generate speech from text
        tts = gTTS(text=st.session_state.text, lang='en')
        
        # Save to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
            tts.save(tmp_file.name)
            # Read the file and play it
            with open(tmp_file.name, 'rb') as audio_file:
                st.audio(audio_file.read(), format='audio/mp3')
        
        st.write("Text-to-Speech conversion successful.")
    else:
        st.write("Please enter some text.")
