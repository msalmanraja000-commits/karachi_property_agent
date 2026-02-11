import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="DHA Karachi AI Advisor", page_icon="🏝️")

# 2. API Key Setup
# Salman bhai, yahan apni Groq key lazmi dalein
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# 3. System Prompt
system_prompt = """
You are the 'DHA Karachi Elite Advisor'. 
Expertise: DHA Phases 1-8 and DHA City. 
Rules: Mention A-Lease vs B-Lease, Water issues in Phase 5/6, and Filer tax benefits.
"""

st.title("🏝️ DHA Karachi AI Advisor")
st.markdown("---")

# 4. Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages (Yahan colan ka khayal rakha hai)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. User Input
if prompt := st.chat_input("DHA Karachi ke baare mein poochein..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Stable model name
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
           response = completion.choices[0].message.content
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
