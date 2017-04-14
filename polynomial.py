from sympy import symbol, diff
import random

def calculate(coefficients, x):
    poly_sum = 0
    count = 0 
    for coefficient in coefficients:
        poly_sum += coefficient * (x**count)
        count += 1
    return poly_sum 

def score(coefficients, x, y, i, degree):
    total_loss = 0
    prediction = calculate(coefficients, x[i])
    delta = prediction - y[i]
    for number in range(0, degree + 1):
        total_loss += delta * (x[i] ** number)
    return total_loss

def update(x, y, coefficients, rate, degree):
    new_coefficients = []
    for number in range(0, len(coefficients)):
        scored = score(coefficients, x, y, number, degree)
        scored = scored / len(x)
        new_coefficient = coefficients[number] - (rate * scored)
        new_coefficients.append(new_coefficient)
    print(new_coefficients)
    return new_coefficients

def start(x, y, rate, degree):
    coefficients = []
    for time in range(0, degree + 1):
        coefficients.append(random.random() * 10)
    print(coefficients)
    count = 0
    while count < 10000000:
        coefficients = update(x, y, coefficients, rate, degree)
        count += 1
    return coefficients

x = [1, 2, 3, 4]
y = [1, 8, 27, 64]
start(x, y, 0.0005, 3)

