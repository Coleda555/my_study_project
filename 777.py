def move_zeros(lst):
    result = [elem for elem in lst if elem != 0]
    result.extend([0] * (len(lst) - len(result)))
    return result


print(move_zeros([1, 0, 2, 0, 3, 0, 4, 0, 5, 0]))
