import random

DESCRIPTION = "Find the smallest common multiple of given numbers."

def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    question = f"{num1} {num2} {num3}"
    correct_answer = lcm(lcm(num1, num2), num3)
    return question, correct_answer

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a