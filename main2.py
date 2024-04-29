from config import API_KEY, ROOT_DIR

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate

from langchain.chains import ConversationChain, LLMChain

from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(
    api_key=API_KEY,
    model="gpt-3.5-turbo",
    temperature=1
)

memory = ConversationBufferMemory(
    memory_key="messages_history",
    return_messages=True
)

prompt = ChatPromptTemplate(
    messages = [
        MessagesPlaceholder(variable_name="messages_history"),
        HumanMessagePromptTemplate.from_template("{human_input}")
    ],
    input_variables=["human_input"]
)

# chain = prompt | llm

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)

while True:
    content = input("HUMAN INPUT: ")
    if content in ["exit", "quit", "done"]:
        break

    response = chain.invoke(input={
        "human_input": f"{content}"
    })

    print(type(response))
    print(response)