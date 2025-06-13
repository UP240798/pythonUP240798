# Declare an empty list
empty_list = []

# Declare a list with more than 5 elements
fruits = ['apple', 'banana', 'pear', 'watermelon', 'grape', 'orange']

# Get the length of the list
print("Length:", len(fruits))

# Get the first, middle, and last elements
print("First:", fruits[0])
print("Middle:", fruits[len(fruits)//2])
print("Last:", fruits[-1])

# List with mixed data types
personal_info = ['JohnDoe', 21, 1.75, 'Single', '123 Maple Street']

# Declare list of tech companies
tech_brands = ['Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list
print("Tech companies:", tech_brands)

# Number of companies
print("Number of companies:", len(tech_brands))

# First, middle, and last company
print("First:", tech_brands[0])
print("Middle:", tech_brands[len(tech_brands)//2])
print("Last:", tech_brands[-1])

# Modify one company
tech_brands[1] = 'YouTube'
print("After modification:", tech_brands)

# Add a company
tech_brands.append('Intel')
print("After appending:", tech_brands)

# Insert a company in the middle
tech_brands.insert(len(tech_brands)//2, 'Spotify')
print("After inserting in the middle:", tech_brands)

# Capitalize first company name (excluding IBM)
tech_brands[0] = tech_brands[0].upper()
print("First company uppercased:", tech_brands)

# Join the list with '#;  '
print('#;  '.join(tech_brands))

# Check if a company exists
print("Does Google exist?", 'Google' in tech_brands)

# Sort the list alphabetically
tech_brands.sort()
print("Sorted list:", tech_brands)

# Reverse the list
tech_brands.reverse()
print("Reversed list:", tech_brands)

# Slice the first 3 companies
print("First 3:", tech_brands[:3])

# Slice the last 3 companies
print("Last 3:", tech_brands[-3:])

# Slice the middle company/companies
length = len(tech_brands)
if length % 2 == 0:
    middle_items = tech_brands[length//2 - 1 : length//2 + 1]
else:
    middle_items = [tech_brands[length//2]]
print("Middle item(s):", middle_items)

# Remove the first company
tech_brands.pop(0)
print("After removing first:", tech_brands)

# Remove middle company/companies
length = len(tech_brands)
if length % 2 == 0:
    del tech_brands[length//2 - 1 : length//2 + 1]
else:
    del tech_brands[length//2]
print("After removing middle:", tech_brands)

# Remove the last company
tech_brands.pop()
print("After removing last:", tech_brands)

# Clear all companies
tech_brands.clear()
print("Cleared list:", tech_brands)

# Delete the list entirely
del tech_brands
# print(tech_brands)  # This would raise an error if uncommented

# Merge front-end and back-end tech
frontend_stack = ['HTML', 'CSS', 'JavaScript', 'React', 'Redux']
backend_stack = ['Node.js', 'Express', 'MongoDB']
full_stack = frontend_stack + backend_stack
print("Full Stack:", full_stack)

# Insert Python and SQL after Redux
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print("Updated Full Stack:", full_stack)
