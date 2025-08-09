# 2. Як вхідні дані запитайте два числа та виведіть яке з них менше і яке більше

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print(f"{first_number} > {second_number}" if first_number > second_number else f"{first_number} < {second_number}")
