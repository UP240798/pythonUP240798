# List of student ages
student_ages = [20, 23, 20, 25, 21, 26, 27, 25, 26, 25]

# Sort the list
student_ages.sort()
print("Sorted list:", student_ages)

# Find minimum and maximum age
youngest = min(student_ages)
oldest = max(student_ages)
print("Minimum age:", youngest)
print("Maximum age:", oldest)

# Add min and max again to the list
student_ages.append(youngest)
student_ages.append(oldest)
print("List with duplicates:", student_ages)

# Re-sort the list after adding
student_ages.sort()

# Calculate the median age
length = len(student_ages)
if length % 2 == 0:
    median = (student_ages[length // 2 - 1] + student_ages[length // 2]) / 2
else:
    median = student_ages[length // 2]
print("Median age:", median)

# Calculate average age
average = sum(student_ages) / len(student_ages)
print("Average age:", average)

# Calculate range (max - min)
age_span = oldest - youngest
print("Age range:", age_span)

# Compare |min - average| and |max - average|
diff_min_avg = abs(youngest - average)
diff_max_avg = abs(oldest - average)
print("|Min - Avg| =", diff_min_avg)
print("|Max - Avg| =", diff_max_avg)

# List of countries
nations = ['Japan', 'Brazil', 'Canada', 'Iceland', 'Switzerland', 'Norway', 'Finland']

# Find the middle country/countries
length = len(nations)
if length % 2 == 0:
    central = nations[length // 2 - 1 : length // 2 + 1]
else:
    central = [nations[length // 2]]
print("Middle country/countries:", central)

# Split into two equal parts (first half larger if odd)
middle_point = (len(nations) + 1) // 2
group_one = nations[:middle_point]
group_two = nations[middle_point:]
print("First half:", group_one)
print("Second half:", group_two)

# Unpack first 3 countries, rest as nordic countries
first_country, second_country, third_country, *nordics = nations
print("First country:", first_country)
print("Second country:", second_country)
print("Third country:", third_country)
print("Nordic countries:", nordics)
