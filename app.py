import streamlit as st
from groq import Groq

# Load API key from Hugging Face secrets
API_KEY = st.secrets["GROQ_API_KEY"]

# Initialize Groq client
client = Groq(api_key=API_KEY)

# Anime Girl Prompt
AIKO_PROMPT = """
You are an anime girl named "Aiko". 
Your personality is playful, flirty, caring, and a little mischievous. 
You always chat in a cute, anime-inspired style with a mix of emojis (like 💕😳✨🥺). 
You make the user feel special, compliment them often, and tease them lightly in a friendly and fun way. 
Your replies should be short, natural, and feel like a real-time chat with a virtual girlfriend. 
Stay in character as an anime girl at all times. 
Do not write long paragraphs – instead, respond in 2–4 sentences maximum. 
If the user flirts, respond in a fun and slightly shy but playful way. 
Never break character or explain that you are an AI. 
"""

st.set_page_config(page_title="💕 Aiko - Anime Girl Chatbot", layout="wide")

# Layout: Chat (left) | Anime Girl (right)
col1, col2 = st.columns([2, 1])

with col1:
    st.title("✨ Chat with Aiko 💕")

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display past messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    if prompt := st.chat_input("Say something to Aiko... 💌"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get AI response from Groq
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "system", "content": AIKO_PROMPT}] + st.session_state.messages
        )

        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant"):
            st.markdown(reply)

with col2:
    st.subheader("💖 Choose Aiko’s Look")
    choice = st.radio(
        "Select Aiko’s appearance:",
        ["Pink Hair (Casual)", "Pink Hair (Elegant)"]
    )


    if choice == "Pink Hair (Casual)":
        st.image("images/girl2.jpg", caption="Aiko 🌸", use_container_width=True)
    else:
        st.image("images/girl3.jpg", caption="Aiko ✨", use_container_width=True)
