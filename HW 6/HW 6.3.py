import random

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Введіть позитивне ціле число.")
            return value
        except ValueError as e:
            print(f"Error: {e}")

numbers_students = int(input("Введіть кількість учнів:  "))
students = []
passed_scores = []
falled_scores = []

for i in range(numbers_students):
    print(f"\nStudent #{i + 1}")

    name = input("Введіть ім'я: ").strip()
    score = random.randint(50, 100)
    passed = random.choice([True, False])
    print(score, passed)
    student_info = [name, score, passed]
    students.append(student_info)
    if passed:
        passed_scores.append(score)
    else:
        falled_scores.append(score)

print(students)

min_passing_score = min(passed_scores, default=100)
max_failing_score = max(falled_scores, default=50)

if min_passing_score >= max_failing_score:
    print("Справедливо")
    print(f"Прохідний бал знаходиться в діапазоні", [max_failing_score], " - ", [min_passing_score])
else:
    print("Не справедливо")