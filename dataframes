# dataframes!

import pandas as pd

# building a basic dataframe from a list
std = ["acheron", "ahmad", "qusai", "dalbah"]
students = pd.DataFrame(std)
# notice: using DataFrame class (not method), it converts the list to a dataframe
print(students)

# building a basic dataframe from a dictionary of lists
stdDic = {"IDs": [202420163, 202310113, 202419821, 202510223], "Names": std, "Majors": ["Astrophysics", "Mathematics", "Computer Science", "Data Science"]}
studentsDic = pd.DataFrame(stdDic)
print(studentsDic)

# to print specific columns
print(studentsDic["Names"])

# building a basic dataframe from a list of dictionaries
stdList = [{"ID": 202420163, "Name": "acheron", "Major": "Astrophysics"}, {"ID": 202310113, "Name": "ahmad", "Major": "Mathematics"},
           {"ID": 202419821, "Name": "qusai", "Major": "Computer Science"}, {"ID": 202510223, "Name": "dalbah", "Major": "Data Science"}]

studentsListDic = pd.DataFrame(stdList)
print(studentsListDic)

# notice: when building a dataframe from a dictionary of lists, all lists must have the same number of elements, whereas while building a dataframe from a list of dictionaries, it isn't necessary
