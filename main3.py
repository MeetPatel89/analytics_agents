from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from config import API_KEY, ROOT_DIR

llm = ChatOpenAI(
    api_key=API_KEY,
    model="gpt-3.5-turbo",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are a helpful assistant. Answer all questions to the best of your ability."),
        MessagesPlaceholder(variable_name="messages_history"),
        HumanMessage(content="And 3 more?")
    ]
)

chain = prompt | llm

response = chain.invoke(
    {
        "messages_history": [
            HumanMessage(content='What is 1 + 1?'), 
            AIMessage(content='1 + 1 = 2')
        ]
    }
)

print(type(response))
print(response)