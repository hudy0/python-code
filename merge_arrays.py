def merge_arrays(array_a, array_b):
    # 1. Merge array_a and array_b
    # 2. Remove duplicates
    # 3. Sort list in ascending order
    return sorted(set(array_a + array_b))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = merge_arrays(a, b)
print(c)

# result [1, 2, 3, 4, 5, 6, 7, 8, 9]
