# Alfred AI Customer Support Bot
This is a proof of concept for a customer support bot using Alfred AI. it uses the Streamlit library to create a web-based chat interface and Google's Generative AI for generating responses. 

The underlying framework powering the AI is LangChain and Google Gemini. LangChain is a framework for building LLM applications. It provides a set of tools and abstractions for composing LLM applications.

## Getting Started
Follow these steps to set up and run the project.

1. **Create a Virtual Environment
Create a virtual environment for the project using the following command:

```
python -m venv env
```

This will create a virtual environment named "env" in the project directory.

2. **Activate the Virtual Environment
Activate the virtual environment using the following command. This will depend on your operating system. For example, on macOS and Linux, use the following command:

```
source env/bin/activate
```

On Windows, use the following command:

```
env\Scripts\activate.bat
```

This will activate the virtual environment and allow you to install the required dependencies.

3. **Install the Required Dependencies
Install the required dependencies using the following command:

```
pip install -r requirements.txt
```

This will install all the dependencies specified in the requirements.txt file.

4. Add API Key
Add your Google API key to the .env file. If the .env file does not exist, create it in the root directory of the project.

```
GOOGLE_API_KEY=your_api_key
```

5. **Run the Project
Run the project using the following command:

```
streamlit run main.py
```

This will start the Streamlit server and open the web interface in your browser.

## Project Structure
Here's a brief overview of the key files in the project:

`main.py`: This is the main script that runs the Streamlit application. It handles user input, generates responses using the AI, and manages the chat history.

`ai.py`: This script contains the AI logic for generating responses. It uses Google's Generative AI and the langchain library.

`prompts.py`: This script defines the prompts that are used to generate responses.

`requirements.txt`: This file lists the Python dependencies that need to be installed for the project.

`.gitignore`: This file tells git which files (or patterns) it should ignore.

Remember to replace the API key placeholder in the .env file with your actual API key.