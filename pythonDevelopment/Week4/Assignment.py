"""
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
"""
def file_read_and_write():
    try:
        # Ask the user for the input file name
        input_file_name = input("Enter the name of the file to read: ")
        
        # Attempt to open and read the file
        with open(input_file_name, "r") as input_file:
            data = input_file.readlines()

        # Modify the content (e.g., converting all text to uppercase)
        modified_data = [line.upper() for line in data]
        
        # Ask the user for the output file name
        output_file_name = input("Enter the name of the new file to write to: ")
        
        # Write the modified content to the new file
        with open(output_file_name, "w") as output_file:
            output_file.writelines(modified_data)
        
        print(f"File successfully written to {output_file_name}")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
  

# Call the function to test it
file_read_and_write()

