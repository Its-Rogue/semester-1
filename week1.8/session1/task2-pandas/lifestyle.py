import pandas
from pathlib import Path

data = pandas.read_csv(Path(__file__).with_name("lifestyle_data.csv"))

# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

print("Data type:", type(data).__name__)

print("Total number of students:", len(data))

print("Mean GPA:", data["GPA"].mean())

print("Sleep standard deviation:",
      data["Sleep_Hours_Per_Day"].std())

print("Maximum study hours:",
      data["Study_Hours_Per_Day"].max())

print("Lowest social hours first:")
print(data.sort_values("Social_Hours_Per_Day", ascending=True).head())

hours_columns = [column for column in data.columns
                 if column.endswith("_Hours_Per_Day")]
data["Total_hours"] = data[hours_columns].sum(axis=1)
print("Total hours column:", data["Total_hours"].head().tolist())

high_stress = data[data["Stress_Level"] == "High"]
low_stress = data[data["Stress_Level"] == "Low"]
print("High-stress mean GPA:", high_stress["GPA"].mean())
print("Low-stress mean GPA:", low_stress["GPA"].mean())
