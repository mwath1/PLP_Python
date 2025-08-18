# 1.
my_list = []

# 2.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3.
my_list.insert(1, 15)

# 4.
my_list.extend([50, 60, 70])

# 5.
del my_list[-1]

# 6.
my_list.sort()

# 7.
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Check final list
print("Final my_list:", my_list)