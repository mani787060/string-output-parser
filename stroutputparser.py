from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser         # here we are importing StrOutputParser which is a simple output parser that extracts string content from the model's response. This is useful when you want to ensure that the output you get from the model is in a clean string format, especially if the model's response might include additional metadata or formatting.


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")


# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()


# this is the beauty of Parser that it can be used anywhere in the chain where we want to extract string output from the model's response.

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
