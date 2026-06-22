import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/students.csv")

print("="*50)
print("STUDENT DATA ANALYSIS")
print("="*50)

print(df)

print("\nAverage Marks")
print("Maths :", df["Maths"].mean())
print("Science :", df["Science"].mean())
print("English :", df["English"].mean())

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Maths"])
plt.title("Maths Marks")
plt.savefig("charts/bar_chart.png")

plt.figure(figsize=(8,5))
plt.scatter(df["Maths"], df["Science"])
plt.title("Maths vs Science")
plt.savefig("charts/scatter_plot.png")

corr = df[["Maths","Science","English"]].corr()

plt.figure(figsize=(6,5))
plt.imshow(corr)
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Heatmap")
plt.savefig("charts/heatmap.png")

print("\nCharts Saved Successfully")