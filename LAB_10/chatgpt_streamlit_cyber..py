import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("cybersecurity ai assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a cybersecurity expert assistant. "
                "Analyze incidents and threats, provide technical guidance, "
                "use proper terminology and give clear, practical advice."
            )
        }
    ]

for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
prompt = st.chat_input("Ask about cybersecurity")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    with st.chat_message("user"):
        st.markdown(prompt)
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.messages
    )
    answer = completion.choices[0].message.content
    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })