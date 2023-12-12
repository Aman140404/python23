# Create a set
my_set = {1, 2, 3, 4, 5}

# Add an element to the set
my_set.add(6)

# Remove an element from the set
my_set.remove(5)

# Check if an element is in the set
print(3 in my_set)  # True

# Get the union of two sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
union = set1.union(set2)
print(union)  # {1, 2, 3, 4, 5, 6}

# Get the intersection of two sets
intersection = set1.intersection(set2)
print(intersection)  # {}

# Get the difference of two sets
difference = set1.difference(set2)
print(difference)  # {1, 2, 3}

# Get the symmetric difference of two sets
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  # {1, 2, 3, 4, 5, 6}

# Check if two sets are subsets of each other
print(set1.issubset(set2))  # False
print(set2.issubset(set1))  # False

# Check if two sets are supersets of each other
print(set1.issuperset(set2))  # False
print(set2.issuperset(set1))  # False

# Check if two sets are disjoint (have no elements in common)
print(set1.isdisjoint(set2))  # True
