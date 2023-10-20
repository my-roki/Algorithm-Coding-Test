import sys


def is_palindrome(word):
    return 1 if word == word[::-1] else 0


if __name__ == "__main__":
    word = sys.stdin.readline().rstrip()
    print(is_palindrome(word))