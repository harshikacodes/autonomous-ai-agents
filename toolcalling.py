from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.tools import tool
from rich import print

# creating a tool
@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in a given text"""
    return len(text)

llm = ChatGroq(model = "openai/gpt-oss-120b")

# tool binding 
llm_with_tool = llm.bind_tools([get_text_length])

result = llm_with_tool.invoke("Return the number of character in a given text: 'Hello, how are you?'")

# print(result.tool_calls[0])

if result.tool_calls:
    tool_call = result.tool_calls[0]

tool_name = tool_call['name']
tool_args = tool_call['args']

tool_result = get_text_length.invoke(tool_args)

final_response = llm_with_tool.invoke(f"the lenght of text is {tool_result}")

print(final_response)