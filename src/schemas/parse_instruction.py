from typing import Literal
from pydantic import BaseModel, Field


class ParseInstructionRequest(BaseModel):
    prompt: str = Field(..., example="Send 0.0005 ETH to testaddress on ETH chain")


class ParseInstructionResponse(BaseModel):
    target_type: Literal["address", "name"] = Field(..., example="address")
    target: str = Field(..., example="testaddress")
    chain_type_from: str | None = Field(..., example="ETH")
    chain_type_to: str | None = Field(..., example="ETH")
    value: float = Field(..., example=0.0005)
