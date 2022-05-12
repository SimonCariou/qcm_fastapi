import csv

q = open("questions.csv", "r")
dict_reader = csv.DictReader(q)

questions = list(dict_reader)

#Adding the question_id to the list of dict in order to be able to get any question index.
for i in range(0, len(questions)):
    questions[i]["question_id"] = i