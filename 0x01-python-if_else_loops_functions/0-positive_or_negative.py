#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    print("is positive")
elif number == 0:
    print("is 0")
else:
    print("is negative")
