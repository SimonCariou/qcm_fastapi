
# Eval FastAPI - DataScientest

## Use

1. git clone the project
1. install the python packages required by the app the work properly, in requirements.txt
1. run `uvicorn main:api --reload`
1. Run the following curl commands from a terminal

## Routes

### GET /
Allows a user to see if the api is running:

*Example:*
```bash
curl -X 'GET' \
  'http://localhost:8000/' \
  -H 'accept: application/json'
```

### POST /questions?nb_questions=[int]

Allows an authorized user to be able to get a list of questions based on the 'use' and the 'subject' (which is a list of strings)

*Example:*
```bash
curl -X 'POST' \
  'http://localhost:8000/questions?nb_questions=5' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic YWxpY2U6d29uZGVybGFuZA==' \
  -H 'Content-Type: application/json' \
  -d '{
  "subject": [
    "BDD",
	"Systèmes distribués"
  ],
  "use": "Test de positionnement"
}'
```

### PUT /add

```bash
curl -X 'PUT' \
  'http://localhost:8000/add' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic YWRtaW46NGRtMU4=' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "Quel est mon nom ?",
  "subject": [
    "Question personnelle"
  ],
  "use": "Apprendre à me connaître",
  "correct": "Simon",
  "responseA": "Simon",
  "responseB": "Joe",
  "responseC": "Amanda",
  "responseD": "Nick",
  "remark": "Rien à dire"
}'
```

Then to verify that the question has indeed been added to the db we can reach the following route:

### GET /last

Allows the admin to get the latest question added in the database in order to verify that it has been correctly added.

*Example:*

```bash
curl -X 'GET' \
  'http://localhost:8000/last' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic YWRtaW46NGRtMU4='
```