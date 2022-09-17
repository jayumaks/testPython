# ### Exercises: Level 1

# 1. Create an empty tuple

churches = ()


# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers = ('James', "Blessing", 'Joy', 'Emmanuel', 'Victor')
sisters = ('Peace', 'Tina', 'Charity', 'Esther')
# 3. Join brothers and sisters tuples and assign it to siblings

siblings = brothers + sisters


# 4. How many siblings do you have?

len(siblings)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = list(siblings)
family_members.append("Umakhihe")
family_members.append('Paulina')



# ### Exercises: Level 2

# 1. Unpack siblings and parents from family_members

family_members.remove()
print(family_members)
# 1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# 1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
# 1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# 1. Slice out the first three items and the last three items from food_staff_lt list
# 1. Delete the food_staff_tp tuple completely
# 1. Check if an item exists in  tuple:

# - Check if 'Estonia' is a nordic country
# - Check if 'Iceland' is a nordic country

#   ```py
#   nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#   ```

