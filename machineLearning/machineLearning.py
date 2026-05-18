import pandas as pd

# step 1: read from the CSV file
dataframe = pd.read_csv(r"C:\Users\ASU\Documents\temporary file (0163)\machineLearning\weather_forecast.csv")
print(dataframe)

# step 2: select the output column
y = dataframe["Play"]
print(y)

# step 3: select the feature columns
# way 1:
x = dataframe[["Outlook", "Temperature", "Humidity", "Windy"]]
# way 2:
x = dataframe.iloc[:, 0:4]
print(x)
