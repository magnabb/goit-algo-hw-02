"""
Необхідно розробити функцію, яка приймає рядок як вхідний параметр,
додає всі його символи до двосторонньої черги (deque з модуля collections в Python),
а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом.

Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів,
а також бути нечутливою до регістру та пробілів.
"""

from collections import deque


def is_palindrome(s: str):
    dq = deque()
    dq.extend(s.lower())

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True

def check(s: str):
    print(f'{s} -> {is_palindrome(s)}')

if __name__ == '__main__':
    check('abba')
    check('abab')
    check('12321')
