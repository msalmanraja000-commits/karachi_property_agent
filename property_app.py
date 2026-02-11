import streamlit as st
from groq import Groq
from tavily import TavilyClient

# Page Setup
st.set_page_config(page_title="Karachi Realistic Property Expert", page_icon="🏢")
st.title("🏙️ Property Bot & Karachi Property Advisor")
st.markdown("---")

# 🔐 Load Keys from Streamlit Secrets
try:
    g_key = st.secrets["GROQ_API_KEY"]
    t_key = st.secrets["TAVILY_API_KEY"]
except Exception:
    st.error("Please add GROQ_API_KEY and TAVILY_API_KEY in Streamlit Secrets!")
    st.stop()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ilaaqe ka naam likhein (e.g. Surjani Town or DHA Phase 8)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Market ki asliyat check ho rahi hai..."):
            try:
                # 1. Enhanced Search Query for Ground Realities
                tavily = TavilyClient(api_key=t_key)
                search_query = f"current property rates in {prompt} Karachi 2026 ground reality problems water electricity crime gas issues"
                search = tavily.search(query=search_query, max_results=6)
                
                # 2. AI Real Estate "Strict" Expert
                client = Groq(api_key=g_key)
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": """You are a street-smart Karachi Real Estate Expert. 
                        Your goal is to give a TRUTHFUL picture of the area.
                        - If there is a water crisis, say it clearly.
                        - Mention the 'Tanker Culture' if applicable.
                        - Discuss Security (Chori-chakari ka scene kaisa hai?).
                        - Differentiate between 'Lease' and 'Goth' lands.
                        - Give an estimated price range but warn that it varies.
                        - Speak in Roman Urdu like a seasoned broker. 
                        - Be realistic, not just a salesman."""},
                        *st.session_state.messages,
                        {"role": "user", "content": f"Live Market & Issues Data: {search['results']}"}
                    ]
                )
                full_response = response.choices[0].message.content
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"Error: {e}")
