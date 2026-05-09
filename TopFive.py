# Program to display top five frequent words

# Open file
file = open("textfile.txt", "r")

# Read content
content = file.read().lower()

# Close file
file.close()

# Split words
words = content.split()

# Dictionary for frequency
frequency = {}

# Count words
for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

# Sort dictionary by frequency
sorted_words = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

# Display top five words
print("Top Five Frequent Words:\n")

for word, count in sorted_words[:5]:
    print(word, ":", count)


#output:
Top Five Frequent Words:

python : 10
data : 8
code : 7
program : 5
file : 4    