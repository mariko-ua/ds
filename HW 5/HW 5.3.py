# 3. Як вхідні дані запитайте три числа і виведіть найменше, середнє та найбільше. Припустимо, всі вони різні

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

listsort = [first_number, second_number, third_number]
listsort.sort()
print(listsort)



# OR

# first_number = int(input("Enter first number: "))
# second number = int(input("Enter second number: "))
# third number = int(input("Enter third number: "))
#
# small = min(first_number, second_number, third_number)
# big = max(first_number, second_number, third_number)
# middle = first_number + second_number + third_number - small - big
#
# print(small, middle, big)