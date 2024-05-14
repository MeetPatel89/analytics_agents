import sqlite3
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate
)
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor, create_tool_calling_agent
from config import API_KEY
import pandas as pd

conn = sqlite3.connect("db.sqlite")

def run_sqlite_query(query: str):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def convert_to_df(query: str):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=[description[0] for description in cursor.description])
    return df

# tools
run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Run a query on the sqlite database",
    func=run_sqlite_query
)

convert_to_df_tool = Tool.from_function(
    name="convert_to_df",
    description="Query the sqlite database, convert the resultset to a pandas dataframe and return it",
    func=convert_to_df
)

tools = [convert_to_df_tool]

# print(run_query_tool("SELECT * FROM sqlite_master"))
# print("")
# print(run_query_tool("SELECT count(*) FROM users"))

llm = ChatOpenAI(
    api_key=API_KEY,
    model="gpt-3.5-turbo",
    temperature=0
)
prompt = ChatPromptTemplate(
    messages=[
        MessagesPlaceholder(variable_name="agent_scratchpad"),
        HumanMessagePromptTemplate.from_template("{input}")
    ]
)

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools
)

# agent_executor.invoke({"input": "How many users are in the database?"})
# agent_executor.invoke({"input": "How many tables are in the database?"})
result = agent_executor.invoke({"input": "Get all tables in the database. Query top 5 records from each table."})
print("")
print(result["output"])
