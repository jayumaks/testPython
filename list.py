


# 1. Declare an empty list

emptyList = []

# 2. Declare a list with more than 5 items

nameClothes =['Boulevard', 'Couture', 7, True, 'Felix', 'Tard']

# 3. Find the length of your list

print(len(nameClothes))

# 4. Get the first item, the middle item and the last item of the list

print(nameClothes[0])
print(nameClothes[3])
print(nameClothes[5])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['Oluwashola', 28, '19.58m', 'married', 'Ugbowo']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using _print()_

print(it_companies)

# 8. Print the number of companies in the list

print(len(it_companies))

# 9. Print the first, middle and last company

print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

# 10. Print the list after modifying one of the companies



# 11. Add an IT company to it_companies

it_companies.append('Netflix')

# 12. Insert an IT company in the middle of the companies list

it_companies.insert(3,'IrokoTv')


# 13. Change one of the it_companies names to uppercase (IBM excluded!)

it_companies.insert

# 14. Join the it_companies with a string '#;&nbsp; '

string = ['#;&nbsp; ']
it_companies += string

# 15. Check if a certain company exists in the it_companies list.

does_exist = 'Netflix' in it_companies

# 16. Sort the list using sort() method

it_companies.sort()

# 17. Reverse the list in descending order using reverse() method

it_companies.reverse()

# 18. Slice out the first 3 companies from the list

it_companies[0:3]

# 19. Slice out the last 3 companies from the list

it_companies[-3:]

# 20. Slice out the middle IT company or companies from the list
# 21. Remove the first IT company from the list

it_companies.remove('Facebook')

# 22. Remove the middle IT company or companies from the list

it_companies.remove('Apple')

# 23. Remove the last IT company from the list

it_companies.remove('Netflix')

# 24. Remove all IT companies from the list

it_companies.clear()

# 25. Destroy the IT companies list

del it_companies

# 26. Join the following lists:

#     ```py
#     front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#     back_end = ['Node','Express', 'MongoDB']
#     ```


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
# ````

full_stack = front_end.extend(back_end)

front_end.insert(4, 'Python')
front_end.insert(5, 'SQL')


# ### Exercises: Level 2

# 1. The following is a list of 10 students ages:

# ```sh
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ```

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Sort the list and find the min and max age

ages.sort()
mini = ages[0]
maxi = ages[9]

# - Add the min age and the max age again to the list

ages.append(mini, maxi)

# - Find the median age (one middle item or two middle items divided by two)



# - Find the average age (sum of all items divided by their number )
# - Find the range of the ages (max minus min)
# - Compare the value of (min - average) and (max - average), use _abs()_ method

# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.



