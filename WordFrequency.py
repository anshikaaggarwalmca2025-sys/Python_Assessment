# Program to count word frequency

# Input paragraph
paragraph = input("Enter a paragraph: ")

# Convert into lowercase and split words
words = paragraph.lower().split()

# Empty dictionary
frequency = {}

# Count occurrences
for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

# Find most repeated word
most_repeated = max(frequency, key=frequency.get)

# Display frequencies
print("\nWord Frequencies:")

for word, count in frequency.items():
    print(word, ":", count)

# Display most repeated word
print("\nMost Repeated Word:", most_repeated)


#output:
Enter a paragraph: python is easy and python is powerful

Word Frequencies:
python : 2
is : 2
easy : 1
and : 1
powerful : 1

Most Repeated Word: python