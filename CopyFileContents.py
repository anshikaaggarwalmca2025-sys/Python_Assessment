# Program to copy contents from one file to another

# Open source file
source_file = open("source.txt", "r")

# Read content
content = source_file.read()

# Close source file
source_file.close()

# Open destination file
destination_file = open("destination.txt", "w")

# Write content
destination_file.write(content)

# Close destination file
destination_file.close()

# Count total words copied
word_count = len(content.split())

# Display result
print("File Copied Successfully")

print("Total Words Copied:", word_count)



#output:
File Copied Successfully
Total Words Copied: 45