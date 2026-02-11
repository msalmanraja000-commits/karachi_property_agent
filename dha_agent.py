import streamlit as st
import google.generativeai as genai

# 1. API Key Setup (Jo aapne di hai)
API_KEY = "AIzaSyD1DG-8imvcsXDZj3bW9SR0xYe4Jph2vpE"
genai.configure(api_key=API_KEY)

# 2. Page Setup
st.set_page_config(page_title="DHA Karachi Expert", page_icon="🏝️")

# 3. Expert System Prompt
system_prompt = """
You are the 'DHA Karachi Elite Advisor' from PropTech.AI.
Rules:
- Give expert advice on DHA Phases 1-8 and DHA City.
- Explain A-Lease vs B-Lease.
- Mention water challenges in Phase 5 & 6.
- Encourage users to become 'Filers' for tax savings.
- Tone: Highly professional and helpful.
"""

# 4. Initialize Gemini Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)

st.title("🏝️ DHA Karachi AI Advisor")
st.write("Welcome to The Caseton's automated property concierge.")

# 5. Chat Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("DHA Karachi ke baare mein kuch bhi pochen..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Gemini se jawab lena
        response = model.generate_content(prompt)
        st.markdown(response.text)
    
    st.session_state.messages.append({"role": "assistant", "content": response.text})
