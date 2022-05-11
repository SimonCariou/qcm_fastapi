from fastapi import FastAPI, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse

import asyncio

from questions import df_questions as questions

from pydantic import BaseModel
from typing import Optional

class Question(BaseModel):
    """ Model describing a question.
    The reponseD is optional as sometimes there isn't one.
    """
    
    question_id: int
    question: str
    subject: str
    use: str
    correct: str
    responseA: str
    responseB: str
    responseC: str
    responseD: Optional[str]


api = FastAPI(
    title='QCM API',
    description="Manage a list of questions as well as their possible answers. The questions\
        have one or multiple correct answers and the questions are ordered by category",
    version="1.0.0"
)

@api.get("/")
def get_root():
    return {"Greeting": "Got root"}

