import matplotlib.pyplot as plt

#sample data
x = [1,2,3,4,5]
y = [10,20,30,40,50]

#create a line plot
plt.plot(x,y)
plt.title("Sample Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#Sample data
activities = ["Sleeping","Eating","Coding","Gaming"]
hours = [8,2,8,6]

plt.pie(hours, labels=activities,autopct='%1.1f%%')
plt.title("Daily activities")
plt.show()

#Histogram
ages = [22,21,20,23,24,22,20,21,22,25,23]
plt.hist(ages, bins=5, color='purple')
plt.title("Age distribution")
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.show()


#Continue with pandas
import pandas as pd
data = {
  'Year': [2020, 2021, 2022],
  'Users': [100, 150, 200],
}
df = pd.DataFrame(data)

#Plot using pandas + matplotlib
plt.plot(df['Year'],df['Users'], marker='o')
plt.title("Users over years")
plt.xlabel("Year")
plt.ylabel("Users")
plt.grid(True)
plt.show()

#Bar chart with 5 different countries and their population
countries = ["USA", "China", "India", "Brazil", "Russia"]
populations = [331, 1441, 1393, 213, 146]
plt.bar(countries, populations, color='orange')
plt.title("Population of countries")
plt.xlabel("Countries")
plt.ylabel("Population (in millions)")  
plt.show()


#Create a pie chart showing how a student spends 24 hours of their day.
 



 #Make a line chart that shows temperature changes during the day (morning, noon, evening, night).
temperatures = [30,50,60,20]
time = ["Morning","Noon","Evening","Night"]
plt.plot(time, temperatures, marker='o', color='red') 
plt.title("Temperature changes during the day")
plt.xlabel("Time of day")
plt.ylabel("Temperatures")
plt.show()