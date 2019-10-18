import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)   <= Time Complexity O(n^2) because of double loop


# HASHTABLE solution
# hashtable = {}

# for name_1 in names_1:
#   hashtable[name_1] = 0

# for name_2 in names_2:
#   if name_2 in hashtable:  # average Runtime on my pc 0.0065 secs
#     duplicates.append(name_2)  # Time Complexity O(n) 2 loops (but single loops)


# ARRAY soloution
duplicates = [name for name in names_1 if name in names_2] 

# Researched the *in* operator:

# The complexity of in depends entirely on what L is. e in L will become L.__contains__(e).

# Here is the summary for in:

# list - Average: O(n)
# set/dict - Average: O(1), Worst: O(n)

# Worst is O(n) and the *in* operator is nested in our list comprehension(the list comprehension should be also O(n))
# so the answer should be because it is nested O(n^2) but its way faster than our double loop so not sure here



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

