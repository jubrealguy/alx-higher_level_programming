#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(num1+1, 10):
        if num1 == 8 and num2 == 9:
            print(f"{num1}{num2}")
        else:
            print(f"{num1}{num2}, ", end='')
