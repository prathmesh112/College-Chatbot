import streamlit as st


st.set_page_config(page_title="🎓 Prathmesh's AI Chatbot", layout="centered")

st.markdown("""
    <style>
        .chat-bubble {
            background-color: #f0f2f6;
            border-radius: 12px;
            padding: 12px 16px;
            margin: 8px 0;
            max-width: 90%;
            font-size: 16px;
        }
        .user-bubble {
            background-color: #DCF8C6;
            text-align: right;
            margin-left: auto;
        }
        .bot-bubble {
            background-color: #e3e3e3;
            text-align: left;
            margin-right: auto;
        }
        .avatar {
            width: 40px;
            border-radius: 50%;
            margin-right: 10px;
        }
        .message-row {
            display: flex;
            align-items: flex-start;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Prathmesh's AI Chatbot")
st.markdown("Ask me anything about my background, college, or skills!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your question:")

if user_input:
    with st.spinner("Thinking..."):
        def ask_bot(user_input):
    
            return "This is a response."


        
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", bot_response))
      
import streamlit as st

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You: ", "")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    
    # Define bot_response before using it
    bot_response = "This is a dummy response"  # Replace with your chatbot logic
    st.session_state.chat_history.append(("bot", bot_response))

for speaker, message in st.session_state.chat_history:
    st.write(f"{speaker}: {message}")


for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"""
        <div class="message-row" style="justify-content: flex-end;">
            <div class="chat-bubble user-bubble">{message}</div>
            <img class="avatar" src="https://i.imgur.com/8KHKhxS.png" alt="You">
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="message-row">
            <img class="avatar" src="https://i.imgur.com/kGkSg1v.png" alt="Bot">
            <div class="chat-bubble bot-bubble">{message}</div>
        </div>
        """, unsafe_allow_html=True)
