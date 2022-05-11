import pandas as pd
import csv

q = open("questions.csv", "r")
dict_reader = csv.DictReader(q)

questions = list(dict_reader)