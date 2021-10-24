def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def divide(a, b):
    return a / b


def sum(a, b):
    return a + b


a = int(input('원하는 숫자를 입력하세요'))
b = int(input('다른 숫자를 입력하세요'))
h = input('원하는 연산자(+, -, *, /)를 입력하시오')

if h == '+':
    c = sum(a, b)
elif h == '-':
    c = minus(a, b)
elif h == '*':
    c = multi(a, b)
elif h == '/':
    c = divide(a, b)

print(c)