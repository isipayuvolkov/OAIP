import random

DESCRIPTION = 'What is the result of the expression?'

def get_question_and_answer():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    question = f'{num1} {operator} {num2}'

    if operator == '+':
        expected_answer = str(num1 + num2)
    elif operator == '-':
        expected_answer = str(num1 - num2)
    else:
        expected_answer = str(num1 * num2)

    return question, expected_answer
