"""
🔹 Challenge: Create a program that reads a text file, processes its content, and writes the results to a new file.

📌 Task Requirements:
Create a file called input.txt and write at least five lines of text into it.
Write a Python script to:
Read the contents of input.txt.
Count the number of words in the file.
Convert all text to uppercase.
Write the processed text and the word count to a new file called output.txt.
Print a success message once the new file is created.
"""
def process_text_file(input_file,output_file):
    """
    Reads a text file, counts words, converts to uppercase, and writes to a new file.

    Args:
        input_file: The path to the input text file.
        output_file: The path to the output text file.
    """
def process_text_file(input_file, output_file):
    """
    Reads a text file, counts words, converts to uppercase, and writes to a new file.

    Args:
        input_file: The path to the input text file.
        output_file: The path to the output text file.
    """
    try:
        with open(input_file, 'r') as infile:
            text = infile.read()

        words = text.split()
        word_count = len(words)
        uppercase_text = text.upper()

        with open(output_file, 'w') as outfile:
            outfile.write(uppercase_text)
            outfile.write(f"\nWord Count: {word_count}")

        print(f"Successfully processed '{input_file}' and created '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create input.txt with sample content
with open("input.txt", "w") as f:
    f.write("This is a sample text file.\n")
    f.write("It contains multiple lines.\n")
    f.write("Python is a powerful language.\n")
    f.write("Counting words and converting to uppercase.\n")
    f.write("This is the last line.\n")
    f.write("Extra words for counting.")

# Process the files
process_text_file("input.txt", "output.txt")  