from fastapi import FastAPI, HTTPException, Request, status, Depends
from fastapi.responses import JSONResponse

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

import asyncio

from questions import questions
from auth_users import authorized_users

from random import shuffle

from pydantic import BaseModel
from typing import Optional, List

class Question(BaseModel):
    """ Model describing a question.
    """
    question_id: Optional[int]
    question: Optional[str]
    subject: List[str]
    use: str
    correct: Optional[str]
    responseA: Optional[str]
    responseB: Optional[str]
    responseC: Optional[str]
    responseD: Optional[str]

responses = {
    200: {"message": "OK"},
    404: {"message": "Item not found"},
    302: {"message": "The item was moved"},
    403: {"message": "Not enough privileges"}
}

api = FastAPI(
    title='QCM API',
    description="Manage a list of questions as well as their possible answers. The questions\
        have one or multiple correct answers and the questions are ordered by category",
    version="1.0.0"
)
security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_auth_status(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    if not(authorized_users.get(username)) or not(pwd_context.verify(credentials.password, authorized_users[username]['hashed_password'])):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True

class NumberOfQuestionsOutOfBound(Exception):
    """ Raised when trying to reach post / questions with a number of questions different from 5, 10 or 20.
    """
    def __init__(self):
        return

@api.exception_handler(NumberOfQuestionsOutOfBound)
async def NumberOfQuestionsOutOfBoundHandler(request: Request, exception: NumberOfQuestionsOutOfBound):
    return JSONResponse (status_code = 500, content = {"message": "Number of questions in the request out of bounds. Must be one of [5, 10, 20]"})

@api.get("/", responses = responses)
async def get_root():
    return {"Greetings": "The API is running"}

@api.post("/questions", responses = responses)
async def post_questions_details(nb_questions: int, question: Question, isUserAuthenticated: bool = Depends(get_auth_status)):
    """ Returns only the question and the 4 possible answers being given a number as parameter (5, 10 or 20),
    and a Question with only 'use' and 'subject' in the body (all the other attributes are optional).

    POST example:
    request to 127.0.0.1:8000/questions?nb_questions=10 withe the request body:
    {
        "subject": [
            "Machine Learning",
            "Streaming de données"
        ],
        "use": "Test de validation"
        }
    """

    results = {}

    if (nb_questions == 5 or nb_questions == 10 or nb_questions == 20 ):
        question_list = list(filter(lambda q: q.get('use') == question.use and q.get('subject') in question.subject , questions))
        shuffle(question_list)
        
        quest = question_list[:nb_questions]

        dict_filter = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
        wanted_keys = ("question", "responseA", "responseB", "responseC", "responseD")

        results = [dict_filter(quest[x], wanted_keys) for x in range(0, len(quest)) ]
    
    else:
        raise NumberOfQuestionsOutOfBound()

    return results


   

