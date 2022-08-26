def check(seq: str):
    list_input = list(seq)
    dict_symbols = {'{': '}', '[': ']', '(': ')'}
    for i in range(len(list_input)):
        if list_input[i] in dict_symbols:
            if list_input.count(list_input[i]) != list_input.count(dict_symbols[list_input[i]]):
                return False
            for j in range(i, len(list_input)):
                if list_input[j] == dict_symbols[list_input[i]]:
                    list_input[i] = 0
                    list_input[j] = 0
                    print(list_input)
                    break
        else:
            if list_input[i] != 0:
                return False
    return True

print(check("(("))

