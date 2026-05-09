# Program to separate vowels and consonants

# Input sentence
sentence = input("Enter a sentence: ")

# Lists for vowels and consonants
vowels = []
consonants = []

# Vowel characters
vowel_letters = "aeiouAEIOU"

# Traverse sentence
for char in sentence:

    # Check alphabet only
    if char.isalpha():

        if char in vowel_letters:
            vowels.append(char)

        else:
            consonants.append(char)

# Display result
print("\nVowels List:")
print(vowels)

print("\nConsonants List:")
print(consonants)


#output:
Enter a sentence: Python Programming

Vowels List:
['o', 'o', 'a', 'i']

Consonants List:
['P', 'y', 't', 'h', 'n', 'P', 'r', 'g', 'r', 'm', 'm', 'n', 'g']