import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests



# Task 1: Create a NumPy array of numbers from 1 to 10 and calculate the mean
array = np.arange(1,10)
print("Array:", array)
print("Mean:", np.mean(array))



# Task 2: Load a small dataset into a pandas DataFrame and display summary statistics
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Score": [85, 90, 95, 100]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())



# Task 3: Fetch data from a public API using requests and print a key piece of information
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    post_data = response.json()
    print("\nFetched Data from API:")
    print("Title of the post:", post_data["title"])
else:
    print("\nFailed to fetch data from API. Status code:", response.status_code)

# Task 4: Plot a simple line graph using matplotlib
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()