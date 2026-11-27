import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read Dataset
df = pd.read_csv("data/students.csv")

print("\n===== Student Dataset =====")
print(df)

# Total Marks
df["Total"] = df["Assignment"] + df["Midterm"] + df["Final"]

# Average
df["Average"] = df["Total"] / 3

print("\n===== Average Marks =====")
print(df[["Name","Average"]])

print("\nHighest Average")
print(df.loc[df["Average"].idxmax()])

print("\nLowest Average")
print(df.loc[df["Average"].idxmin()])

print("\nClass Average")
print(df["Average"].mean())

print("\nMedian")
print(df["Average"].median())

print("\nStandard Deviation")
print(df["Average"].std())

print("\nTop 5 Students")
print(df.sort_values("Average",ascending=False).head())

print("\nStudents Above 85")
print(df[df["Average"]>=85])

print("\nDepartment Wise Average")
print(df.groupby("Department")["Average"].mean())

# Save Updated CSV
df.to_csv("data/result.csv",index=False)

# Chart
plt.figure(figsize=(10,5))
plt.bar(df["Name"],df["Average"])

plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average")

plt.xticks(rotation=45)

plt.tight_layout()
os.makedirs("charts", exist_ok=True)
plt.savefig("charts/student_average.png")

plt.show()