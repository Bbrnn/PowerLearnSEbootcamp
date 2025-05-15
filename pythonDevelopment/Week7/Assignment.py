#Task 1: Load and Explore the Dataset
#IRIS DATASET
import pandas as pd
#load from sklearn
from sklearn.datasets import load_iris
iris = load_iris()

# Convert to DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

df.head()

#Data exploration
df.info() #display data types and missing values
df.isnull().sum()#check for any missing values
df.fillna(df.mean(), inplace=True) #fill missing values with mean



#Task 2: Basic data analysis

#summary statistics for numerical columns
df.describe()

#grouping by species and calculating mean
df_grouped = df.groupby('species').mean()
print(df_grouped)


#Task 3: Data Visualization
import matplotlib.pyplot as plt

#line chart
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.title('Sepal Length Over index')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()
