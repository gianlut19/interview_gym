

# AI Interview Simulator 🏋🏻

## Overview

The **AI Interview Simulator** is an interactive tool designed to help users improve their interview skills by simulating realistic job interviews. By using AI-powered interviewers, users can practice responding to a variety of questions and receive feedback based on the context of a specific job post and company backstory. The simulator alternates between two types of interviewers: a **friendly** interviewer and a **strict** interviewer, to help users prepare for both supportive and challenging interview scenarios.

### Scope

This project aims to provide an immersive and dynamic platform for job seekers to practice their interview skills. By simulating both friendly and demanding interviewers, users are exposed to various question types and interview styles, which can help them refine their responses, improve their communication, and build confidence. 

The AI-driven interview process uses a machine learning model from Hugging Face, allowing for real-time question generation based on user input and job-specific context. The main features include:

- **Customizable interview scenarios** based on job descriptions and company backgrounds.
- **Two types of interviewers** (friendly and strict) to provide a varied interview experience.
- **Real-time conversation flow**, where users can respond to questions, and the system generates follow-up questions based on the conversation history.

## Features

- **Simulated Job Interviews**: Conduct practice interviews with AI-powered agents.
- **Friendly and Strict Interviewers**: Two types of interviewers based on personality (friendly or strict), allowing users to practice both relaxed and intense interview scenarios.
- **Dynamic Question Generation**: Questions are generated in real-time based on the job description and company backstory, simulating a realistic interview.
- **Conversation History**: The system keeps track of the conversation and alternates questions, adapting based on previous responses.

## How to Set Up

### Prerequisites

1. **Python 3.x**: Make sure you have Python 3.7 or higher installed.
2. **Streamlit**: Streamlit is used to build the user interface. Install it by running:
    ```bash
    pip install streamlit
    ```
3. **Langchain**: This project uses the Langchain library for integrating with the Hugging Face model. Install it via:
    ```bash
    pip install langchain
    ```
4. **Hugging Face API Key**: To interact with Hugging Face models, you’ll need an API key. You can create a Hugging Face account and get your API key from [Hugging Face's website](https://huggingface.co/). Once you have the API key, you can configure it with the following environment variable:
    ```bash
    export HF_HOME="<path_to_hugging_face_api_key>"
    ```

### Installation Steps

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. Open your browser and navigate to `http://localhost:8501` to interact with the AI Interview Simulator.

### Usage

1. **Start the Interview**: 
   - When you launch the app, you will be prompted to input the job post and the company backstory. This information will help the AI generate relevant questions for your interview.

2. **Answer Questions**: 
   - Once the interview starts, the AI will ask the first question, and you can type your response in the text area provided.
   - The conversation will continue with alternating questions from the friendly and strict interviewers, based on the history of your responses.

3. **End the Interview**:
   - If you wish to terminate the interview at any time, simply click the "Termina colloquio" button. This will reset the session, allowing you to start a new interview.

## Features to Improve

While the AI Interview Simulator provides a solid foundation for practicing interviews, there are several improvements and enhancements that could be implemented in future iterations of the tool:


1. **Question Variety and Difficulty Levels**:
   - The questions generated could be made more varied and categorized into different difficulty levels (e.g., beginner, intermediate, advanced). This way, users can choose the type of interview they wish to practice (e.g., for an entry-level role or a senior position).

2. **Voice-based Interaction**:
   - Adding a voice interaction feature could improve the experience by allowing users to speak their answers, simulating a real-world interview more closely.

3. **Handling Multiple Rounds**:
   - Simulating multiple rounds of interviews (e.g., HR interview, technical interview, managerial interview) with different question types and interviewers could make the platform more versatile.

