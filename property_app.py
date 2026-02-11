import streamlit as st
from groq import Groq
from tavily import TavilyClient

# Page Setup - Isko aik professional Real Estate look di hai
st.set_page_config(page_title="Karachi Property Expert", page_icon="🏢")
st.title("🏙️ Property Bot & Real Estate Advisor")
st.markdown("---")

# 🔐 Load Keys from Streamlit Secrets (Wahi purani keys kaam karengi)
try:
    g_key = st.secrets["GROQ_API_KEY"]
    t_key = st.secrets["TAVILY_API_KEY"]
except Exception:
    st.error("Pehle Streamlit Secrets mein Keys save karein!")
    st.stop()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ilaaqe ka naam likhein (e.g. Bahria Town Karachi rates)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Scanning Karachi Real Estate Market..."):
            try:
                # 1. Targeted Search for Property
                tavily = TavilyClient(api_key=t_key)
                # Specific search query taake behtareen results ayien
                query = f"Current property rates, plots, houses, and amenities in {prompt} Karachi 2026"
                search = tavily.search(query=query, max_results=6)
                
                # 2. AI Real Estate Expert Brain
                client = Groq(api_key=g_key)
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": """You are a senior Real Estate Consultant in Karachi.
                        Your job is to provide:
                        1. Estimated Market Price (Plots & Houses).
                        2. Area Rating (Water, Gas, Security, Electricity).
                        3. Investment Potential (Is it good to buy now?).
                        4. Connectivity (Nearby schools, hospitals, or roads).
                        Use Roman Urdu. Be professional and give detailed insights."""},
                        *st.session_state.messages,
                        {"role": "user", "content": f"Live Market Data: {search['results']}"}
                    ]
                )
                full_response = response.choices[0].message.content
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"Error: {e}")
