import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="DHA Karachi AI Expert", page_icon="🏝️")

# 2. API Key Setup
# Salman bhai, yahan apni Groq wali key daal dein
GROQ_API_KEY = ""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" -- GROQ API KEY
client = Groq(api_key=GROQ_API_KEY)

# 3. Expert System Prompt
system_prompt = """
You are the 'DHA Karachi Elite Advisor'. 
Focus: Phase 1-8 and DHA City. 
Rules: Mention A-Lease vs B-Lease, Water shortages in Phase 5/6, and Filer tax benefits. 
Tone: Professional and helpful.
"""

st.title("🏝️ DHA Karachi AI Advisor")
st.caption("Powered by Llama 3 (PropTech.AI)")

# 4. Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. User Input and Response
if prompt := st.chat_input("DHA ke bare mein puchen..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Llama 3 model use kar rahe hain jo bohat fast hai
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                *st.session_state.messages
            ],
            model="llama3-8b-8192",
        )
        response = chat_completion.choices[0].message.content
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
