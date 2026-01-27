
import random

set1 = set()
print(type(set1))

set3 = {"dhiren kumar", 67, "independent", "red", "custom"}

set5 = {"trip to hawaii", 540000, "free tissue paper", 908888, "house appliance"}

a = float(input("enter your numbers:"))
print("chance to win a lucky draw / enter your favourite numbers and see if fate is with you!!!")

new = random.choice(list(set5))
print(new)

