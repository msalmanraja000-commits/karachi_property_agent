import streamlit as st
from groq import Groq

# 1. API Key Setup
# Salman bhai, yahan apni Groq key paste karein jo aapne "Allow Secret" ki thi
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# 2. Page Config & Style
st.set_page_config(page_title="DHA Karachi AI Advisor", page_icon="🏝️")
st.title("🏝️ DHA Karachi AI Advisor")
st.markdown("---")

# 3. System Prompt (DHA Knowledge Base)
system_prompt = """
You are the 'DHA Karachi Elite Advisor'. 
Knowledge: 
- DHA Phases 1 to 8 and DHA City Karachi.
- Infrastructure: Phase 8 is the best; Phase 5 and 6 have water issues.
- Legal: Most properties are 99-year lease (A-Lease).
- Taxes: Advise users to become Filers for lower transfer taxes.
Tone: Professional, expert, and trustworthy. 
Agency: PropTech.AI
"""

# 4. Chat History Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. User Input and Llama 3 Response
if prompt := st.chat_input("DHA Karachi ke baare mein kuch bhi poochein..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Calling the Groq API (Llama 3)
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                *st.session_state.messages
            ],
            temperature=0.7,
        )
        response = completion.choices[0].message.content
        st.write(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
