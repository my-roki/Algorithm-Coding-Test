def solution(order):
    order_str = str(order)
    return order_str.count('3') + order_str.count('6')+ order_str.count('9')