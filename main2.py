from config import API_KEY, ROOT_DIR

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOpenAI(
    api_key=API_KEY,
    model="gpt-3.5-turbo",
    temperature=0
)

template = ChatPromptTemplate.from_messages([
    HumanMessage(
        content="Translate this sentence to French: 'I love programming'"
    ),
    AIMessage(
        content="J'adore la programmation"
    ),
    MessagesPlaceholder(variable_name="messages")
]
)

chain = template | llm 

human_prompt = input(">> ")

print(human_prompt)

result = chain.invoke(input = {
    "messages": [
        HumanMessage(
            content=f"{human_prompt}"
        )
    ]
})

print(result)
print(type(result))
print("")
print(result.content)