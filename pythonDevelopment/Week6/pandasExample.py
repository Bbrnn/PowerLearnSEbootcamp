import pandas as pd
#create a dataframe
data = {
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25, 30, 35],
  'Score':[85,90,95]
}
df = pd.DataFrame(data)

print(df)

#Access column
print("Names:",df['Name'])

#Filter rows
print("Scores above 90:")
print(df[df['Score'] > 90])