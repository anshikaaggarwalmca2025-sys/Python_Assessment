# Program to check palindrome string

import string

# Input string
text = input("Enter a string: ")

# Remove spaces and punctuation
cleaned_text = ""

for char in text:

    if char.isalnum():
        cleaned_text += char.lower()

# Check palindrome
if cleaned_text == cleaned_text[::-1]:

    print("The string is a Palindrome")

else:

    print("The string is NOT a Palindrome")



#output:
Enter a string: Madam, I'm Adam

The string is a Palindrome    