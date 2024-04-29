from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from operator import itemgetter

from config import API_KEY, ROOT_DIR

llm = ChatOpenAI(
    api_key=API_KEY,
    model="gpt-3.5-turbo",
    temperature=0
)

output_parser = StrOutputParser()

# all templates in one spot
template_1 = "Write a very short {language} function that will {description}"
template_2 = """
    Given the information {information} about a person I want you to create:
    1. A short summary
    2. Interesting fact(s) about them
"""

template_3 = "Write a test for the following {language} code:\n {code}"

code_prompt = PromptTemplate(
    template=template_1,
    input_variables=["language", "description"]
)

# prompt template for the second prompt chained to the above prompt
code_prompt_2 = PromptTemplate(
    template=template_3,
    input_variables=["language", "code"]
)

# code_prompt = PromptTemplate(
#     template=template_2,
#     input_variables=["information"]
# )

chain_1 = code_prompt | llm | output_parser

result = chain_1.invoke({
    "language":"java",
    "description":"return numbers from 1 to 10"
}
)

# result = chain.invoke({
#     "information": "Name: John Doe\nAge: 25\nOccupation: Software Engineer\nHobbies: Reading, Writing, and Coding\nLocation: New York\n"
# })

print("")
print("-- Output of the first chain --")
print(result)

chain_2 = (
    {
        "language": itemgetter("language"),
        "code": chain_1
    }
    | code_prompt_2
    | llm
    | output_parser
)

result = chain_2.invoke({
    "language":"python",
    "description":"return numbers from 1 to 10 according to Zen of Python"
})

print("")
print("-- Output of the second chain --")
print(result)