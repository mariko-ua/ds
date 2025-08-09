# 4. Зіграйте у гру Fizz-Buzz: виведіть усі числа від 1 до 100; якщо число ділиться на 3, замість числа виведіть "fizz".
# Якщо воно ділиться на 5, замість числа виведіть "Buzz". Якщо воно ділиться на обидва, виведіть "fizz buzz" замість числа.
# Модернізація від чата жпт розібрати потім:
# for num in range(1, 101):
#     out = ""
#     if num % 3 == 0:
#         out += "fizz"
#     if num % 5 == 0:
#         out += "buzz"
#     print(out or num)


for num in range (1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizz buzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)