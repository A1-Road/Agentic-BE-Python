from pydantic import BaseModel, Field


class CheckReputationRequest(BaseModel):
    address: str = Field(..., example="0xA2dBbc0EAE6c0402BF2E59d5A100dD7C9395539a")
    chain_type: str = Field(..., example="ETH")


class CheckReputationResponse(BaseModel):
    is_risky: bool = Field(..., example=False)
    risk_detail: str = Field(..., example="No risk detected")
