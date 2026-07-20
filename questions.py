import random


def get_questions(difficulty):
    questions = {}
    difficulty = difficulty.strip().lower()

    if difficulty == "easy":
        min_num, max_num, num_question = 1, 10, 10
    elif difficulty == "medium":
        min_num, max_num, num_question = 1, 50, 20
    elif difficulty == "hard":
        min_num, max_num, num_question = 1, 100, 30
    else:
        raise ValueError("Invalid difficulty")

    for i in range(1, num_question + 1):
        op = random.choice(["+", "-", "*", "/"])

        if op == "/":
            num2 = random.randint(1, 10)
            ans = random.randint(1, 10)
            num1 = num2 * ans

        elif op == "-":
            num1 = random.randint(min_num, max_num)
            num2 = random.randint(min_num, num1)
            ans = num1 - num2

        elif op == "+":
            num1 = random.randint(min_num, max_num)
            num2 = random.randint(min_num, max_num)
            ans = num1 + num2

        elif op == "*":
            num1 = random.randint(min_num, max_num)
            num2 = random.randint(min_num, max_num)
            ans = num1 * num2

        q = f"{num1} {op} {num2}"

        questions[i] = {"question": q, "answer": ans}

    return questions
