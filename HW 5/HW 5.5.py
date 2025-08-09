# 5. Зіграйте у гру 7-boom: виведіть усі числа від 1 до 100;
# якщо число ділиться на 7 або містить цифру 7, виведіть "BOOM" замість числа.

for num in range (1,101):
    if num % 7 == 0 or '7' in str(num):
        print("BOOM")
    else:
        print(num)