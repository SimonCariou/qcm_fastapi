from ast import Raise
from fastapi import FastAPI, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse

import asyncio

from questions import questions

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

api = FastAPI(
    title='QCM API',
    description="Manage a list of questions as well as their possible answers. The questions\
        have one or multiple correct answers and the questions are ordered by category",
    version="1.0.0"
)

@api.get("/")
def get_root():
    return {"Greeting": "Got root"}

"""
@api.get("/questions")
def get_all_questions():
    try:
       return questions
    except:
         return {}
"""

@api.post("/questions")
def post_questions_details(nb_questions: int, question: Question):
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
    try:
        if (nb_questions == 5 or nb_questions == 10 or nb_questions == 20 ):
            question_list = list(filter(lambda q: q.get('use') == question.use and q.get('subject') in question.subject , questions))
            shuffle(question_list)
            
            quest = question_list[:nb_questions]

            dict_filter = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
            wanted_keys = ("question", "responseA", "responseB", "responseC", "responseD")
            return [dict_filter(quest[x], wanted_keys) for x in range(0, len(quest)) ]
        
        else:
            return {}

    except:
        return {}
   

