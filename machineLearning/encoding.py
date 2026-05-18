import pandas as pd
# steps 1-3: read from CSV, select output column, and select feature columns
dataframe = pd.read_csv(r"C:\Users\ASU\Documents\temporary file (0163)\machineLearning\weather_forecast.csv")
y = dataframe["Play"]
x = dataframe.iloc[:, 0:4]

# step 4.1: encoding the data - manually

# way 1: using methods and enumarting the values using a dictionary by hand
# 1: determine what the unique values are in the first column using the unique() method
print(x["Outlook"].unique())
# 2: mapping the unique values of the first column using the map() method
x["Outlook"] = x["Outlook"].map({"Sunny": 0, "Overcast": 1, "Rain": 2})

print(x["Temperature"].unique())
x["Temperature"] = x["Temperature"].map({"Hot": 0, "Mild": 1, "Cool": 2})

print(x["Humidity"].unique())
x["Humidity"] = x["Humidity"].map({"High": 0, "Normal": 1})

# way 2: using a for loop to create the dictionary
uniqueList = x["Windy"].unique()
dic = {}
for i in range(len(uniqueList)):
    dic[uniqueList[i]] = i
x["Windy"] = x["Windy"].map(dic)
print(x)

print(y.unique())
y = y.map({"No": 0, "Yes": 1})
print(y)

# step 4.2: encoding the data - using library
from sklearn.preprocessing import LabelEncoder as enc

encoder = enc()
x["Outlook"] = encoder.fit_transform(x["Outlook"])
x["Temperature"] = encoder.fit_transform(x["Temperature"])
x["Humidity"] = encoder.fit_transform(x["Humidity"])
x["Windy"] = encoder.fit_transform(x["Windy"])
print(x)
# notice: fit_transform() method arranges the data alphabetically before assigning numerical values for each unique value

y = encoder.fit_transform(y)
print(y)
