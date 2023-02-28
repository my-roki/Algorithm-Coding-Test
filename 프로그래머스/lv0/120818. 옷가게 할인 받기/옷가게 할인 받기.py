import math


def solution(price):
    discount = {
        500000: 0.8,
        300000: 0.9,
        100000: 0.95,
        0: 1,
    }
    for key, value in discount.items():
        if price >= key:
            return math.floor(price * value)
