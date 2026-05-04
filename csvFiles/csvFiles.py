import pandas as pd

# # notice: ways to choose different separators while reading CSV files
# dataCSV = pd.read_csv("student.csv", sep = "\t")
# two = pd.read_csv("differentSep.csv", sep = ";")
# three = pd.read_csv("differentSep.csv", sep = "\t")
# four = pd.read_csv("differentSep.csv", sep = "**")
# # bonus: to read a CSV with a separator that isn't a comma via an excel file, use "From Text/CSV in the data tab, then specify the separator and load

deets = [{"ID": 1, "Name": "Acheron", "Grade": 99, "Average": 97.6}, 
         {"ID": 2, "Name": "Ahmad", "Grade": 98, "Average": 98.2}, 
         {"ID": 3, "Name": "Qusai", "Grade": 97.9, "Average": 92.7}]

# notice: turning the deets list to a CSV file
data = pd.DataFrame(deets)
dataStr = data.to_csv(index = False)
print(dataStr)

# notice: creating a new CSV file
data.to_csv("std.csv", index = False, sep = "\t")

# exercise 6 from powerpoint
marks = pd.read_csv("marks.csv")
print(marks)
GPA = pd.read_csv("marks.csv", usecols = ["GPA"])
print(GPA.mean())
# end of exercise