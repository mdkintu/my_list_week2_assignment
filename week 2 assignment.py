# Create an empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert at the second position (index 1)
my_list.insert(1, 15)

# Extend with another list
my_list.extend([50, 60, 70])

# Remove the last element 
my_list.pop()

# Sort in ascending order
my_list.sort()

# Find the index of 30 and print it
index_of_30 = my_list.index(30)
print(index_of_30)