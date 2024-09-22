import google.generativeai as genai
import streamlit as st

# Initialize API key
GOOGLE_API_KEY = "AIzaSyBOgls6F7R3wrHm-hSjtOmxnZn6mv8wc24"
genai.configure(api_key=GOOGLE_API_KEY)

# Model Initiate
model = genai.GenerativeModel('gemini-1.5-flash')

def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit App Title and Logo
st.markdown(
    """
    <style>
    .app-title {
        font-size: 40px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .input-box {
        margin-bottom: 20px;
    }
    .submit-btn {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        cursor: pointer;
    }
    .submit-btn:hover {
        background-color: #45a049;
    }
    .history-box {
        margin-top: 20px;
        border: 1px solid #ddd;
        padding: 10px;
        background-color: #f9f9f9;
    }
    .user-message {
        font-weight: bold;
        color: #2c3e50;
    }
    .bot-response {
        font-style: italic;
        color: #7f8c8d;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Adding a logo (Replace 'path_to_your_logo.png' with the actual path to your logo)
st.image("Q.png", width=200 )


st.write("Powered by Generative AI")

if "history" not in st.session_state:
    st.session_state["history"] = []

# Chat form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(label="Enter your message", max_chars=2000)
    submit_button = st.form_submit_button("Send")  # Removed custom CSS class here

if submit_button:
    if user_input:
        response = get_chatbot_response(user_input)
        st.session_state.history.append((user_input, response))
    else:
        st.warning("Please enter a prompt.")

# Displaying chat history
if st.session_state["history"]:
    st.markdown('<div class="history-box">', unsafe_allow_html=True)
    for user_input, response in st.session_state["history"]:
        st.markdown(f'<p class="user-message">User: {user_input}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bot-response">Bot: {response}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
