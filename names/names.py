import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


###############################################################################
### tried with binary search tree, but the result was arount 45-50 seconds: ###

# binsearch =  BinarySearchTree(names_1[0])

# for i in names_1:
#     if i in names_1:
#         binsearch.insert(i)

# for j in names_2:
#     if binsearch.contains(j):
#         duplicates.append(j)

### So this is working fast (and basically it's the strech goal), runs under 1 second. ###

duplicates = list(set(names_1).intersection(names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


### The best runtime I got: 0.003816843032836914 seconds.
