'''
This agent scrapes websites and facilitates interactive conversations with the scraped content, making data extraction and analysis more efficient.
'''
#%% ---------------------------------------------  IMPORTS  ----------------------------------------------------------#
import os
from main import rec_streamlit, speak_answer, get_transcript_whisper
import time
import requests
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain.chains import VectorDBQA, RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from credentials import OPENAI_API_KEY
import streamlit as st

# --------------------  WEBSITE SCRAPE  -------------------- #
def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return None

# --------------------  SETTINGS  -------------------- #
st.set_page_config(page_title="Home", layout="wide")
st.markdown("""<style>.reportview-container .main .block-container {max-width: 95%;}</style>""", unsafe_allow_html=True)

# --------------------- HOME PAGE -------------------- #
st.title("WEBSCRAPER Agent 🎙️📖")
st.write("""Use the power of LLMs with LangChain and OpenAI to scan through websites! Just input the link, and ask questions immediately! 🚀 Create new content with the support of state of the art language models and 
and voice command your way through your documents. 🎙️""")

st.write("Let's start interacting with GPT-4o!")

# ----------------- SIDE BAR SETTINGS ---------------- #
st.sidebar.subheader("Settings:")
tts_enabled = st.sidebar.checkbox("Enable Text-to-Speech", value=False)

# ------------------- WEBSITE  HANDLER ------------------- #
website = st.text_input('Enter the link of the website you want to analyze:')
if website:
    html_content = get_html_content(website)
    if html_content:
        try:
            # --- Display the file content as code---
            with st.expander("Document Expander (Press button on the right to fold or unfold)", expanded=True):
                st.subheader("Uploaded Document:")
                st.write(html_content)

        except Exception as e:
            st.write("Error reading file:", e)

        # Save the html content to a file.txt
        file_path = "html_content.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        
        # Check if the file was created successfully
        if os.path.exists(file_path):
            st.success("Website successfully scraped!")
            try:
                loader = TextLoader(file_path)
                documents = loader.load()
                
                #Get your splitter ready
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
                texts = text_splitter.split_documents(documents)
                embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
                docsearch = Chroma.from_documents(texts, embeddings)
                qa = VectorDBQA.from_chain_type(llm=OpenAI(openai_api_key=OPENAI_API_KEY), chain_type="stuff", vectorstore=docsearch)
            except Exception as e:
                st.error(f"Error loading document: {e}")
        else:
            st.error("Failed to create html_content.txt file.")
    else:
        st.error("Invalid website. Please enter a valid website.")

# --------------------- USER INPUT --------------------- #
user_input = st.text_area("")

# If record button is pressed, rec_streamlit records and the output is saved
audio_bytes = rec_streamlit()

# ------------------- TRANSCRIPTION -------------------- #
if audio_bytes or user_input:

    if audio_bytes:
        try:
            with open("langchain_webscraper_audio.wav", "wb") as file:
                file.write(audio_bytes)
        except Exception as e:
            st.write("Error recording audio:", e)
        transcript = get_transcript_whisper("langchain_webscraper_audio.wav")
    else:
        transcript = user_input

    st.write("**Recognized:**")
    st.write(transcript)

    if any(word in transcript for word in ["abort recording"]):
        st.write("... Script stopped by user")
        exit()
    # ----------------------- ANSWER ----------------------- #
    with st.spinner("Fetching answer ..."):
        time.sleep(6)

    # Use the CSV agent to answer the question
    query = transcript
    answer  = qa.run(query)
    st.write("AI Response:", answer)
    speak_answer(answer, tts_enabled)
    st.success("**Interaction finished**")
