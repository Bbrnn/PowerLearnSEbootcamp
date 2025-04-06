"""
File handling in Python allows you to:

Open files in different modes (e.g., read-only or write mode).
Read and write data in a variety of formats.
Close files to free up system resources
"""
#open file in read mode
with open("example.txt","r") as file:
  content = file.read()
  print(content)

  #Write file
  with open('example.txt','w') as file:
    file.write("Hello, Python!")

#Exception handling

"""
Basic Structure of try-except Blocks ⚙️

try: Runs code that might throw an error.
except: Catches the error, allowing you to respond without crashing.
Example
"""
try: 
  with open("nonexistent.txt", "r") as file:
    data = file.read()

except FileNotFoundError:
  print("file not found.Please check the name of the file")

"""
Advanced Error Handling with finally and Custom Errors 🎩

finally: Runs no matter what, often used to clean up (like closing a file).
Custom Errors: Create custom exceptions for special cases (e.g., EmptyFileError).
"""
try: 
  file=open("sample.txt","r")
except FileNotFoundError:
  print("File not found")

finally:
  file.close()

