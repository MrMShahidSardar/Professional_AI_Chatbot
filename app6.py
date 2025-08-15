# app.py
import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #6e8efb, #a777e3);
    }
    .chat-container {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        height: 70vh;
        overflow-y: auto;
    }
    .message {
        padding: 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        max-width: 80%;
    }
    .user-message {
        background-color: #6e8efb;
        color: white;
        margin-left: auto;
    }
    .bot-message {
        background-color: #f1f1f1;
        margin-right: auto;
    }
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.9) !important;
    }
    .header-title {
        font-size: 2.5rem !important;
        color: white !important;
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar configuration
with st.sidebar:
    st.title("⚙️ Configuration")
    st.subheader("AI Model Settings")
    
    # Model selection
    model_repo = st.selectbox(
        "HuggingFace Model",
        ("HuggingFaceH4/zephyr-7b-beta", "mistralai/Mistral-7B-Instruct-v0.2"),
        index=0
    )
    
    # Parameters
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.05)
    max_length = st.slider("Max Response Length", 50, 500, 200, 50)
    
    # API Key
    hf_token = st.text_input("HuggingFace API Key", type="password", 
                            value=os.getenv("HF_API_KEY", ""))
    
    if st.button("Initialize Chat"):
        if not hf_token:
            st.error("Please enter your HuggingFace API key")
        else:
            os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token
            try:
                llm = HuggingFaceEndpoint(
                    repo_id=model_repo,
                    temperature=temperature,
                    max_new_tokens=max_length
                )
                st.session_state.conversation = ConversationChain(
                    llm=llm,
                    memory=ConversationBufferMemory()
                )
                st.success("Chat initialized successfully!")
            except Exception as e:
                st.error(f"Error initializing model: {str(e)}")

# Main chat interface
st.markdown('<h1 class="header-title">🤖 Professional AI Assistant</h1>', unsafe_allow_html=True)

# Display chat history
chat_container = st.container()
with chat_container:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(f'<div class="message {"user-message" if message["role"] == "user" else "bot-message"}">'
                        f'{message["content"]}</div>', 
                        unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# User input
user_input = st.chat_input("Type your message here...")

if user_input and st.session_state.conversation:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate response
    with st.spinner("Thinking..."):
        response = st.session_state.conversation.predict(input=user_input)
    
    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Rerun to update display
    st.rerun()
elif user_input and not st.session_state.conversation:
    st.error("Please initialize the chat in the sidebar first")