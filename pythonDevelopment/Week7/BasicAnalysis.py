import pandas as pd

# Creating DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
print(df)

#basic filtering
df_filtered = df[df['Age']>30]
print("Filter with age:",df_filtered)

#Multiple conditions
#df_filtered = df[(df['Age]>30)& (df['City]== 'New York')]


#Sorting
df_sorted = df.sort_values(by='Age', ascending=False)
print("Sorted:", df_sorted)

#Aggregate data
grouped = df.groupby('City').agg({'Age':'mean','Name':'count'})
print(grouped)

#Summary statistics

print("Mean of age:",df['Age'].mean())
print("Sum of age:",df['Age'].sum())
print("Max of age:",df['Age'].max())


#Visualization
import matplotlib.pyplot as plt

#plotting as age vs name
plt.plot(df["Name"], df['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title("Name vs Age")
plt.show()