from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

from src.schemas.parse_instruction import (
    ParseInstructionRequest,
    ParseInstructionResponse,
)

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))


# Create a PydanticOutputParser for the new model
output_parser = PydanticOutputParser(
    pydantic_object=ParseInstructionResponse, strict=True
)

# Generate format_instructions
format_instructions = output_parser.get_format_instructions()

# Prompt template
prompt_template = ChatPromptTemplate(
    [
        (
            "system",
            """You are an AI agent that helps with Ethereum transactions. Please provide the transaction details in the following format:
            
            {format_instructions}""",
        ),
        ("human", "{user_input}"),
    ]
)
# Insert format_instructions into the template
prompt = prompt_template.partial(format_instructions=format_instructions)
chain = prompt | llm | output_parser


def parse_instruction_func(req: ParseInstructionRequest) -> ParseInstructionResponse:
    return chain.invoke({"user_input": req.prompt})
