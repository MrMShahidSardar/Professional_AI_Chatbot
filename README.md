# 🤖 Professional AI Chatbot

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-0.1.16-00ADD8?logo=langchain&logoColor=white)](https://langchain.com)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

A professional AI chatbot with a modern dashboard interface built using **Streamlit** and **LangChain**.  
Supports multiple Hugging Face models with customizable parameters.

![Chatbot Demo](demo.gif)

---

## ✨ Features

- 💬 Conversational AI with memory retention  
- 🎨 Modern gradient UI with glass-morphism design  
- ⚙️ Model configuration panel (temperature, response length)  
- 🤗 Multiple Hugging Face model support  
- 📱 Mobile-responsive interface  
- 🔒 Secure API key management  

---

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/mrmshahidsardar/ai-chatbot.git
cd ai-chatbot
Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file for your Hugging Face API key

env
Copy
Edit
HF_API_KEY=your_huggingface_api_key
▶️ Usage
Start the application

bash
Copy
Edit
streamlit run app.py
Configure settings in the sidebar

Select a Hugging Face model

Adjust temperature and max response length

Enter your Hugging Face API key

Start chatting in the main interface! 🎉

⚙️ Configuration Options
Parameter	Description	Default Value
Model	Hugging Face model repository	HuggingFaceH4/zephyr-7b-beta
Temperature	Creativity of responses (0–1)	0.7
Max Length	Maximum response tokens	200
API Key	Hugging Face API key	-

📦 Dependencies
Python 3.8+

Streamlit – Web app framework

LangChain – LLM integration

langchain_community – Hugging Face integration

python-dotenv – Environment variable management

🤝 Contributing
Contributions are welcome!
Follow these steps:

Fork the repository

Create a new branch

bash
Copy
Edit
git checkout -b feature/your-feature
Commit your changes

bash
Copy
Edit
git commit -am "Add some feature"
Push to your branch

bash
Copy
Edit
git push origin feature/your-feature
Open a pull request

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

📌 Setup Instructions (Detailed)
Virtual Environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
Install Requirements

bash
Copy
Edit
pip install -r requirements.txt
Get Hugging Face API Key

Create an account at huggingface.co

Go to Settings → Access Tokens

Create a new token

Create .env file

env
Copy
Edit
HF_API_KEY=your_api_key_here
Run the App

bash
Copy
Edit
streamlit run app.py
💡 Professional Use Recommendations
Replace with your production LLM (e.g., GPT-4, Claude)

Add authentication for enterprise use

Implement rate limiting

Store conversation history in a database

Include monitoring and analytics

UI Highlights:

Left sidebar for configuration

Central chat display area

Animated message bubbles

Gradient background with glass-morphism effect

Responsive mobile and desktop design

Interactive chat input
