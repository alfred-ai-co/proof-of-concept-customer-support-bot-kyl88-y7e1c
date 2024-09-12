from typing import Iterator
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from prompts import BEHAVIOUR, EXAMPLES
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


history = {}

llm = ChatGoogleGenerativeAI(
    model='gemini-pro',
    temperature=0.0,
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "human",
            f"{BEHAVIOUR}\n{EXAMPLES}",
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

runnable = prompt | llm | StrOutputParser()


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in history:
        history[session_id] = ChatMessageHistory()
    return history[session_id]

with_message_history = RunnableWithMessageHistory(
    runnable,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

def generate_response(query: str) -> Iterator:
    response = with_message_history.stream(
        {"input": query},
        config={"configurable": {"session_id": "1"}},
    )
    return response