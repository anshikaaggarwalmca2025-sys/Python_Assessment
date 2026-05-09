# Program to count words, lines, and characters

try:

    # Open file
    file = open("sample.txt", "r")

    # Read file content
    content = file.read()

    # Count characters
    characters = len(content)

    # Count words
    words = len(content.split())

    # Count lines
    lines = len(content.splitlines())

    # Close file
    file.close()

    # Display result
    print("Total Characters:", characters)

    print("Total Words:", words)

    print("Total Lines:", lines)

# Handle file not found error
except FileNotFoundError:

    print("Error: File Not Found")

# Handle other exceptions
except Exception as e:

    print("Unexpected Error:", e)



#output:
Total Characters: 120
Total Words: 20
Total Lines: 5    