#%% ----------------------------- IMPORTS  -----------------------------------
# import libraries
import streamlit as st
import credentials
import os
import openai
from gtts import gTTS
import io
from audio_recorder_streamlit import audio_recorder
from IPython.display import Audio
import pandas as pd


#%% ----------------------------- LANGCHAIN FUNCTIONS -----------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
OPENAI_API_KEY = credentials.OPENAI_API_KEY


# %% ----------------------------- AUDIO RECORDING STREAMLIT -----------------------------------
def rec_streamlit():
    """Record audio and return the audio bytes"""
    audio_bytes = audio_recorder(energy_threshold=(-1.0, 1.0), pause_threshold=6.0, text="",
                                 recording_color="#FF0000", neutral_color="#49DE49", icon_name="microphone", icon_size="3x")

    return audio_bytes


#%% ----------------------------- OPEN AI FUNCTIONS  -----------------------------------
def get_transcript_whisper(file_path):
    '''Get the transcript of the audio file'''
    openai.api_key = OPENAI_API_KEY
    with open(file_path, "rb") as file:
        #transcription = openai.Audio.transcribe("whisper-1", file, response_format="json")
        transcription= openai.audio.transcriptions.create(model="whisper-1", file=file)
        #print(transcription["text"])
    transcribed_text = transcription.text

    return transcribed_text


#%% ----------------------------- SPEAK FUNCTIONS -----------------------------------
def speak_answer(answer, tts_enabled):
    if not tts_enabled:
        return

    tts = gTTS(text=answer, lang="en")
    with io.BytesIO() as f:
        tts.write_to_fp(f)
        f.seek(0)
        audio = Audio(f.read(), autoplay=True)
        st.write(audio)


#%% ----------------------------- MAIN APPLICATION FUNCTIONS -----------------------------------
def home():
    # ------------------ SETTINGS ------------------
    st.set_page_config(page_title="Home", layout="wide",)
    st.markdown("""<style>.reportview-container .main .block-container {max-width: 95%;}</style>""",
                unsafe_allow_html=True)

    # ------------------ HOME PAGE ------------------
    st.title("Infinite Interact: Multi-Agent Operational Suite 🤖")
    st.write("""This repository is the result of an advanced project aimed at developing a suite of intelligent agents designed to perform a variety of tasks. These agents harness the power of Large Language Models (LLMs) in conjunction with LangChain and OpenAI, enabling users to efficiently navigate and manage their documents. By leveraging these technologies, the agents can extract information and insights with remarkable speed, create new content, and allow users to control their documents through voice commands. 🚀🎙️""")
    st.write("We wills how you 5 different agents that we build\n"
             "1. **Multimedia Analysis Agent 🎥🔍**\n"
             "2. **DataFrame Assistant Agent 📊🗂️**\n"
             "3. **Presentation Creator Agent 📑🖥️**\n"
             "4. **Documentation Generator Agent 📋📁**\n"
             "5. **WebContent Extractor Agent 🌐🕸️**\n""")



    # ------------------ SIDE BAR SETTINGS ------------------
    st.sidebar.subheader("Settings:")
    tts_enabled = st.sidebar.checkbox("Enable Text-to-Speech", value=False)


# Run home function
if __name__ == "__main__":
    home()
