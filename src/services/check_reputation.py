from cdp_langchain.agent_toolkits import CdpToolkit
from cdp_langchain.utils import CdpAgentkitWrapper
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os
import src.env
from src.schemas.check_reputation import CheckReputationRequest, CheckReputationResponse

load_dotenv()

# Initialize CDP wrapper
cdp = CdpAgentkitWrapper()
# Create toolkit from wrapper
toolkit = CdpToolkit.from_cdp_agentkit_wrapper(cdp)

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# Get tools and create agent
tools = toolkit.get_tools()
agent_executor = create_react_agent(llm, tools)


def check_reputation_func(command: CheckReputationRequest) -> CheckReputationResponse:
    query_prompt = f"check the reputation of {command.address} on {command.chain_type}"
    # AI のレスポンスを stream で取得
    events = agent_executor.stream(
        {"messages": [("user", query_prompt)]}, stream_mode="values"
    )
    for event in events:
        last_message = event["messages"][-1].content
        if "suspicious" in last_message:
            bool_val = True
        else:
            bool_val = False
    return CheckReputationResponse(is_risky=bool_val, risk_detail=last_message)
