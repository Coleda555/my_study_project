a = [0, False]
b = [False, 0]
for i in range(2):
    if a[i] == b[i] and type(a[i]) == type(b[i]):
        print(f'yes, i ={i} type a[{i}] = {type(a[i])}, type b[{i}] = {type(b[i])}')
