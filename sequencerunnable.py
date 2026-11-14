from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# model
model = ChatGroq(model = "openai/gpt-oss-120b")

# output parser
parser = StrOutputParser()

# format the prompt
formatted_prompt = prompt.format_messages(topic="Machine Learning")

# call the model manually
response = model.invoke(formatted_prompt)

# parse the output manually
final_output = parser.parse(response.content)

print(final_output)