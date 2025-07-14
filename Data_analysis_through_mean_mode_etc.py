import pandas as pd

a = pd.read_csv(r"C:\dataset\dataset2.csv")
b = a["Marks"].mean()

c = a["Marks"].median()
d = a["Marks"].mode()[0]
e = a["Marks"].std()
f = a["Marks"].var()

print("Mean:", b)
print("Median:", c)
print("Mode:", d)
print("Standard Deviation:", e)
print("Variance:", f)