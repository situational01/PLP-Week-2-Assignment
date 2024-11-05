# Creating an empty list
my_list = []

# Appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at the second position
my_list.insert(1, 15)

# Extending my_list with another list
my_list.extend([50, 60, 70])

# Removing the last element
my_list.pop()

# Sorting my_list in ascending order
my_list.sort()

# Finding and printing the index of value 30
index_of_30 = my_list.index(30)

# Output the final list and the index of 30
print("Final list:", my_list)
print("Index of 30:", index_of_30)
