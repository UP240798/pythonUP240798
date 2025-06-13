# Concatenate strings
print(' '.join(['Thirty', 'Days', 'Of', 'Python']))         # 'Thirty Days Of Python'
print(' '.join(['Programming', 'With', 'Everyone']))        # 'Programming With Everyone'

# Declare variable
organization = "Programming With Everyone"

# Print variable
print(organization)

# String length
print(len(organization))

# Convert to uppercase
print(organization.upper())

# Convert to lowercase
print(organization.lower())

# Formatting: Capitalize, Title Case, and Swap Case
print(organization.capitalize())   # First character uppercase
print(organization.title())        # First letter of each word uppercase
print(organization.swapcase())     # Swap upper/lowercase

# Slice the first word ("Programming")
print(organization[13:])  # 'With Everyone'

# Check if it contains the word "Programming"
print("Programming" in organization)               # True
print(organization.find("Programming"))            # 0
print(organization.index("Programming"))           # 0

# Replace "Programming" with "Python"
print(organization.replace("Programming", "Python"))  # 'Python With Everyone'

# Replace in another string
print("Python for Everyone".replace("Everyone", "You"))

# Split by spaces
print(organization.split())  # ['Programming', 'With', 'Everyone']

# Split string by commas
tech_giants = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_giants.split(", "))

# Character at index 0
print(organization[0])  # 'P'

# Last index
print(organization[-1])  # 'e'

# Character at index 10
print(organization[10])  # 'm'

# Create acronyms
phrase1 = "Python For Beginners"
print(''.join([word[0] for word in phrase1.split()]))  # 'PFB'

phrase2 = "Programming With Everyone"
print(''.join([word[0] for word in phrase2.split()]))  # 'PWE'

# Position of first occurrence of P and W
print(phrase2.index('P'))  # 0
print(phrase2.index('W'))  # 13

# Last occurrence of 'o' in "Programming With People Today"
print("Programming With People Today".rfind('o'))  # 27

# Search for the word 'because'
sentence = "You cannot finish a sentence with because because because is a conjunction"
print(sentence.find("because"))      # 35
print(sentence.rindex("because"))    # 51

# Slice 'because because because'
start = sentence.find("because")
end = sentence.rindex("because") + len("because")
print(sentence[start:end])  # 'because because because'

# Check if string starts or ends with a substring
print(organization.startswith("Programming"))  # True
print(organization.endswith("programming"))    # False

# Strip whitespace from both ends
padded_text = "   Programming With Everyone   "
print(padded_text.strip())

# Check valid identifiers
print("30DaysOfPython".isidentifier())         # False
print("thirty_days_of_python".isidentifier())  # True

# Join library names with '# '
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# Newline between sentences
print("I am enjoying this challenge.\nI wonder what comes next.")

# Tabulation sequence (\t)
print("Name\t\tAge\tCountry\tCity")
print("Michael\t\t30\tUSA\tNew York")

# String formatting
radius = 10
circle_area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} square meters.".format(radius, circle_area))

# Operations using formatting
num1, num2 = 8, 6
print("{} + {} = {}".format(num1, num2, num1 + num2))
print("{} - {} = {}".format(num1, num2, num1 - num2))
print("{} * {} = {}".format(num1, num2, num1 * num2))
print("{} / {} = {:.2f}".format(num1, num2, num1 / num2))
print("{} % {} = {}".format(num1, num2, num1 % num2))
print("{} // {} = {}".format(num1, num2, num1 // num2))
print("{} * {} = {}".format(num1, num2, num1 * num2))
