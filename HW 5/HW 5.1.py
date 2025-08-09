# Потрібні знання для рішення задач
#
# https://www.w3schools.com/python/python_conditions.asp
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_for_loops.asp
#
# 1. Як вхідні дані запитайте ціле число. Якщо воно ділиться на 3, виведіть "foo"; якщо воно ділиться на 5, виведіть "bar";
# якщо воно ділиться на обидва, виведіть "ham" (а не "foo" або "bar").

enter_number = int(input("Enter a number: "))

if enter_number % 3 == 0 and enter_number % 5 == 0:
    print("ham")
elif enter_number % 3 == 0:
    print("foo")
elif enter_number % 5 == 0:
    print("bar")
else:
    print("Число не ділиться ні на 3, ні на 5")