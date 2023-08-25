# Creating a list
my_list = [element1, element2, element3, ...]

# Accessing elements in a list
print(my_list[0])  # Access the first element (index 0)
print(my_list[1])  # Access the second element (index 1)
# ...

# Modifying elements in a list
my_list[0] = new_value

# Appending elements to a list
my_list.append(new_element)

# Removing elements from a list
my_list.remove(element_to_remove)

# Finding the length of a list
length = len(my_list)

# Iterating through a list
for element in my_list:
    print(element)

# Slicing a list (getting a sublist)
sublist = my_list[start_index:end_index]

# Checking if an element is in the list
if element in my_list:
    print("Element is in the list")

# Sorting a list
my_list.sort()

# Reversing a list
my_list.reverse()

# Creating a list with a range of numbers
number_list = list(range(start, end, step))
