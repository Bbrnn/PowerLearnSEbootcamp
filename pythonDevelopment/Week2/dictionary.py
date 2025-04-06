capital_city = {"Kenya":"Nairobi","Tanzania":"Dodoma","Rwanda":"Kigali","Sudan":"Khartoum","Uganda":"Kampala",
"South Sudan":"Juba"}
print(capital_city)

#Adding elemetns to a python dictionary
capital_city["Eritrea"] = "Asmara"
print(capital_city)

#Change value in a dictonary
#Use [] with the key
del capital_city["Eritrea"]
print(capital_city)

#Access the elements of a dictionary
print(capital_city["Kenya"])


#Remove elements in a dictionary
#Using del

#Dictionary Membership Test
squares = {1:1, 3:9, 5:25, 7:49,9:81}
print(1 in squares)
print(49 in squares)
#Iterating through a dictionary

for i in squares:
  print(squares[i])