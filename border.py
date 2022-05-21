import datetime
first_in = datetime.datetime(2021, 3, 28)
first_out = datetime.datetime(2021, 6, 22)
second_in = datetime.datetime(2021, 7, 14)
second_out = datetime.datetime(2021, 9, 21)
delta = first_out - first_in
delta2 = second_out - second_in
print(delta, delta2)
print(delta + delta2)