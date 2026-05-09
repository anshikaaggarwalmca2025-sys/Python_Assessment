# Program to perform set operations

# Input sets from user
set1 = set(map(int, input("Enter elements of Set 1: ").split()))
set2 = set(map(int, input("Enter elements of Set 2: ").split()))

# Union
union_result = set1.union(set2)

# Intersection
intersection_result = set1.intersection(set2)

# Symmetric Difference
symmetric_difference_result = set1.symmetric_difference(set2)

# Subset check
subset_result = set1.issubset(set2)

# Display results
print("\nUnion:", union_result)
print("Intersection:", intersection_result)
print("Symmetric Difference:", symmetric_difference_result)
print("Is Set1 Subset of Set2?:", subset_result)


#output:

Enter elements of Set 1: 1 2 3 4
Enter elements of Set 2: 3 4 5 6

Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Symmetric Difference: {1, 2, 5, 6}
Is Set1 Subset of Set2?: False