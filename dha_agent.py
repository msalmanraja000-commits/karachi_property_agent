import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="DHA Karachi AI Advisor", page_icon="🏝️")

# 2. API Key Setup
# Salman bhai, yahan apni Groq key daalein
GROQ_API_KEY =  "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"

client = Groq(api_key=GROQ_API_KEY)

# 3. System Prompt (The Knowledge Base)
system_prompt = """
You are the 'DHA Karachi Elite Advisor' from The Caseton PropTech.
Rules:
- Give expert advice on DHA Phases 1-8 and DHA City Karachi.
- Phase 8 is high-end; Phases 5 and 6 have water supply issues.
- Explain A-Lease (99 years) importance.
- Mention tax benefits for 'Filers' in property transactions.
- Keep the tone professional, helpful, and sophisticated.
"""

st.title("🏝️ DHA Karachi AI Advisor")
st.caption("Real Estate Intelligence by PropTecSolutions")
st.markdown("---")

# 4. Chat History Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages
