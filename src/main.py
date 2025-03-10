from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.services.check_reputation import check_reputation_func
from src.services.parse_instruction import parse_instruction_func
from src.schemas.check_reputation import CheckReputationRequest, CheckReputationResponse
from src.schemas.parse_instruction import (
    ParseInstructionRequest,
    ParseInstructionResponse,
)
from langchain_core.exceptions import OutputParserException

app = FastAPI(root_path="/api")

origins = [
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/parse_instruction", response_model=ParseInstructionResponse)
async def parse_instruction(req: ParseInstructionRequest):
    try:
        return parse_instruction_func(req)
    except OutputParserException as e:
        raise HTTPException(status_code=400, detail="Invalid input")


@app.get("/check_reputation", response_model=CheckReputationResponse)
async def check_reputation(req: CheckReputationRequest = Depends()):
    return check_reputation_func(req)
