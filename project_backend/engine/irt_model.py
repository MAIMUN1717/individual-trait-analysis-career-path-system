import math

def irt_probability(theta, a, b):
    return 1 / (1 + math.exp(-a * (theta - b)))

def update_theta(theta, a, b, correct, learning_rate=0.1):
    p = irt_probability(theta, a, b)

    if correct:
        return theta + learning_rate * (1 - p)
    else:
        return theta - learning_rate * p

def item_information(theta, a, b):
    p = irt_probability(theta, a, b)
    return (a ** 2) * p * (1 - p)