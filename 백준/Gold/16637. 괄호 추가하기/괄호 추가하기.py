from operator import add, sub, mul


def calculate(a: int, b: int, o: str) -> int:
    operations = {"+": add, "-": sub, "*": mul}
    return operations[o](a, b)


def solution(idx, number1, result):
    # escape condition
    if idx == len(number) - 1:
        return max(result, number1)

    operation1 = operation[idx]
    number2 = number[idx + 1]
    result = max(result, solution(idx + 1, calculate(number1, number2, operation1), result))

    if idx + 2 < len(number):
        operation2 = operation[idx + 1]
        number3 = number[idx + 2]
        sum_23 = calculate(number2, number3, operation2)
        result = max(result, solution(idx + 2, calculate(number1, sum_23, operation1), result))

    return result


if __name__ == "__main__":
    N = int(input())
    S = input()
    number, operation = list(map(int, S[::2])), list(S[1::2])
    print(solution(0, number[0], float("-inf")))
