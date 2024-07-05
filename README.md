# 🧭 Project Overview

Welcome to our multifaceted Al-powered project! This repository offers a suite of tools designed to enhance your productivity and streamline your data processing tasks. Here's a quick rundown of the functionalities:

The challenge was to create different types of agents that will carry out several tasks. Using the power of LLMs with LangChain and OpenAI, we were able to create AI Agents that performed different functions. 

Please see below for the 5 different agents that we were able to build:

1. **Multimedia Agent**: Retrieves a youtube video, downloads it, generates the transcription of the video, and allows the user to ask questions regarding the video.
2. **PandasAI Agent**: Allows the user to upload CSV files and to query the CSV. This agent is mostly used to generate plots of the data.
3. **Presentation Agent**: Allows the user to upload a file and generate powerpoint presentations of the data that is presented in their files. Currently supports only .ipynb files.
4. **README Agent**: Allows the user to give a file path on their local machine and generates an associated README file. This will be used by the members of this team to create README files in the future for future assignments.
5. **Web Scraping Agent**: This agent is given a URL as an input and scrapes the web. You are then able to ask questions regarding the data that was generated, and it can retrieve content from the web page.

## 🎛 Project Setup

Please see below for the steps required to get the project running locally.



1. Git clone the project.
2. Create a python virtual environment using conda: `conda create --name myenv` (Optional)
3. Activate the virtual environment: `conda activate myenv`
4. install all requirements in the requirements.txt file: `pip install -r requirements.txt`
5. Run the main.py using streamlit: `streamlit run main.py`

From here you can navigate to the URL that streamlit provides and use the application.

## Demo

![image](https://github.com/Aagam0812/Infinite-Interact/assets/54525273/5688ab93-acd1-43c5-a4f6-7e378a09e09c)


### 🤖 Multimedia Agent

![image](https://github.com/Aagam0812/Infinite-Interact/assets/54525273/ae317f24-c0f1-4327-964d-f4eaee2e9f54)
URL: `https://www.youtube.com/watch?v=o-z3WvMDP0Q&ab_channel=FOX11LosAngeles`

Prompt: Which president died in a helicopter crash?

![image](https://github.com/Aagam0812/Infinite-Interact/assets/54525273/bde97938-85f0-4281-bc90-40e4d6fce309)
![image](https://github.com/Aagam0812/Infinite-Interact/assets/54525273/940205f5-d992-42c3-b87e-d205aae4e912)


### 🐼 PandasAI (CSV Agent)

Upload the salaries.csv file then perform following query:
Can you plot the standard mean distribution for the salary column?

![image](https://github.com/Aagam0812/Infinite-Interact/assets/54525273/d53bd5a6-c1d8-4c0a-aa0c-defc7bb2bfc7)

![image](https://github.com/Aagam0812/Infinite-Interact/assets/54525273/bc7b7660-8b64-4029-9540-ac4da7735b77)

### 📊 Presentation Agent

Upload the .ipynb file, then click on create Presentation button.

![image](https://github.com/Aagam0812/Infinite-Interact/assets/54525273/14909a4b-99bb-4262-881d-a9098d96990d)


### 📚📖 README generator

Query:
This project has the following functionality:

1. We are able to input a Youtube URL and we get a transcript of the video. We can also query questions regarding the video and an AI Agent will answer those questions.
2. We can upload a CSV file and can ask queries regarding that CSV file that will result in plots.
3. We can upload a .ipynb file and create presentations from that file.
4. We can provide a folder structure and generate a README.md file.
5. We can perform webscraping and query webscraped information.

![image](https://github.com/Aagam0812/Infinite-Interact/assets/54525273/6411d55b-c89f-4790-b8b1-cfcd8496d955)

![image](https://github.com/Aagam0812/Infinite-Interact/assets/54525273/09660350-c95b-4e2d-9eb5-7ee193f23d7c)


### 🎙️📖Webscraper

URL: `https://iowapoetry.com/pushcart2021.htm`

Query: Retrieve all of the poem titles, poem authors, and poem content that are on the webpage. There should be six poems in total, and you should structure your output.

![image](https://github.com/Aagam0812/Infinite-Interact/assets/54525273/e49a066c-950a-4de4-9a7f-b363bc7549c6)

