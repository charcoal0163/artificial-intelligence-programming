import pandas as pd

# notice: a backslash is followed by a command (eg. \n), to override this in a file's path, add an 'r' before the string
data = pd.read_excel(r"C:\Users\ASU\Documents\temporary file (0163)\excelFiles\example.xlsx", sheet_name = "marks")
print(data)
print(type(data))

# three ways to rename a column header
# way 1: assignment of copy
data2 = data.rename(columns = {"Name": "Student Name"})
print(data2)
# way 2: altering actual data
data.rename(columns = {"Name": "Student Name"}, inplace = True)
print(data)
# way 3: altering all column headers
data.columns = ["Names", "First Exam", "Assignment", "Second Exam", "Total"]
print(data)

# to show only columns of the dataframe rather than the entire dataframe
# way 1:
print(data.columns)
# way 2:
print(data.columns.ravel())

# notice: the type returned is "Index", but you can index it like a list
cols = data.columns
print(type(cols))
print(f"First column is: {cols[0]}")

# to print a data series
print(data["Assignment"])

# to print a specific record
print(data["Names"][1])

# use a data series in a loop
for i in range(len(data["Names"])):
    print(data["Total"][i])

# notice: to read specific columns rather than all columns in the dataframe, use "usecols" keyword
someData = pd.read_excel(r"C:\Users\ASU\Documents\temporary file (0163)\excelFiles\example.xlsx", sheet_name = "marks", usecols = ["Name", "Total"])
print(someData)

# notice: when the columns don't have headers, use "header" keyword, then rename headers later
sheet = pd.read_excel(r"C:\Users\ASU\Documents\temporary file (0163)\excelFiles\example.xlsx", sheet_name = "Sheet1", header = None)
sheet.columns = ["Names", "First", "Second"]
print(sheet)

# notice: change the format from excel to different formats (dictionary, JSON, CSV)
sheetDic = sheet.to_dict()
print(sheetDic)
dataJSON = sheet.to_json()
print(dataJSON)
sheetCSV = sheet.to_csv(index = False)
print(sheetCSV)

sheet.to_excel("excelExample.xlsx", sheet_name = "grades", index = False)