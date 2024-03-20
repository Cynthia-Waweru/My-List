my_list = []
# This is an empty list called my_listmy_list.append(10)

my_list.append(20)
my_list.append(30)
my_list.append(40)
#This appends the following elements to my_list: 10, 20, 30, 40.

my_list.insert(1, 15)
# Inserts the value 15 at the second position in the list.

my_list.extend([50, 60, 70])
# Extends my_list with another list: [50, 60, 70].

my_list.pop()
# Remove the last element from my_list

my_list.sort()
# Sort my_list in ascending order.

index_30 = my_list.index(30)
# Find and print the index of the value 30 in my_list.

print("Modified my_list:", my_list)
print("Index of value 30:", index_30)
# Print the modified my_list and the index of the value 30.