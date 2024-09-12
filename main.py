import streamlit as st
from ai import generate_response

st.title("Alfred AI Customer Support Bot")

# Initialize Chat History
if "messages" not in st.session_state: st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept User Input
if query := st.chat_input("Enter your query"):
    st.session_state.messages.append({"role": "user", "content": query})
    # Display User Input
    with st.chat_message("user"):
        st.markdown(query)

    # Display Response
    with st.chat_message("assistant"):
        stream = generate_response(query)
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})