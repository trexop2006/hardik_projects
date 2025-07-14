import seaborn as sns
import matplotlib.pyplot as plt

# Load MPG dataset (cars data)
mpg = sns.load_dataset('mpg')

# Clean data
mpg = mpg.dropna()

# Create plots
plt.figure(figsize=(15, 10))

# Violin plot of MPG by origin
plt.subplot(2, 2, 1)
sns.violinplot(x='origin', y='mpg', data=mpg)
plt.title('MPG Distribution by Origin')

# Boxplot of horsepower by cylinders
plt.subplot(2, 2, 2)
sns.boxplot(x='cylinders', y='horsepower', data=mpg)
plt.title('Horsepower by Number of Cylinders')

# Scatter plot of weight vs MPG with origin hue
plt.subplot(2, 2, 3)
sns.scatterplot(x='weight', y='mpg', hue='origin', size='horsepower', data=mpg)
plt.title('Weight vs MPG (Colored by Origin)')

# Pairplot of numerical variables
plt.subplot(2, 2, 4)
sns.pairplot(mpg[['mpg', 'cylinders', 'displacement', 'weight', 'origin']], hue='origin')
plt.suptitle('Pairplot of Car Features', y=1.02)

plt.tight_layout()
plt.show()