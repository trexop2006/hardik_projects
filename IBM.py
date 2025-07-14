import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("E:\PRACTICE ON VS CODE\Data Science Python\WA_Fn-UseC_-HR-Employee-Attrition.csv")  # replace with your filename

# Set plot style
sns.set(style="whitegrid")

# 1. Attrition Count
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Attrition", palette="Set2")
plt.title("Employee Attrition Count")
plt.show()

# 2. Attrition by Department
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Department", hue="Attrition", palette="Set1")
plt.title("Attrition by Department")
plt.xticks(rotation=45)
plt.show()

# 3. Attrition by Gender
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Gender", hue="Attrition", palette="Set3")
plt.title("Attrition by Gender")
plt.show()

# 4. Monthly Income Distribution
plt.figure(figsize=(8,4))
sns.histplot(data=df, x="MonthlyIncome", kde=True, bins=30, color='orange')
plt.title("Monthly Income Distribution")
plt.show()

# 5. Age vs Attrition
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x="Attrition", y="Age", palette="coolwarm")
plt.title("Age Distribution by Attrition")
plt.show()

# 6. Correlation Heatmap
plt.figure(figsize=(14,10))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.1f')
plt.title("Correlation Heatmap")
plt.show()

# 7. Work-Life Balance vs Attrition
plt.figure(figsize=(7,4))
sns.countplot(data=df, x="WorkLifeBalance", hue="Attrition", palette="husl")
plt.title("Work-Life Balance vs Attrition")
plt.show()

# 8. Business Travel vs Attrition
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="BusinessTravel", hue="Attrition", palette="Paired")
plt.title("Business Travel vs Attrition")
plt.xticks(rotation=30)
plt.show()
