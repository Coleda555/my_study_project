def get_biggest(numbers: list):
    if not numbers:
        return -1
    result = []
    sort_numbers = sorted(numbers, key=lambda x: int(str(x)[0]), reverse=True)
    print(sort_numbers)
    sort_str = list(map(str, sort_numbers))
    for i in range(1, len(sort_numbers)):
        try:
            if len(sort_str[i - 1]) > 1 and len(sort_str[i]) > 1:
                for j in range(len(sort_str[i - 1])):
                    if int(sort_str[i - 1][j]) > int(sort_str[i][j]):
                        result.append(sort_str[i - 1])
                        print()
                    elif int(sort_str[i - 1][j]) < int(sort_str[i][j]):
                        result.append(sort_str[i])
                        sort_str[i] = sort_str[i - 1]
            else:
                result.append(sort_str[i - 1])
        except IndexError:
            pass
    print(result)
    return int(''.join(result))


print(get_biggest([61, 228, 9, 3, 11]))
# print(get_biggest([1, 2, 3]))
# print(get_biggest([7, 71, 72]))
# print(get_biggest([]))
# print('*' * 100)
# print(71 % 100)
