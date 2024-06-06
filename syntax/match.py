# https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
import random

flag = bool(random.randint(0, 1))
print(f"{flag=}")

# 1. 
age = 20  # Choose whatever you want

match age:
    case 10:
        print("Teenager")
    case 20 if flag:
        print("youth")
    case 30:
        print("Hey, boy")
    case 40:
        print("Whatever")
    case _:
        print("Gotcha")


match 10, 20:
    case b, a:  # 정의되어 있지 않아도 이렇게 됨;;
        print(f"{a=}")
    case 20, b:
        print(123)
    case 10, 20:
        print('What?')
    case _:
        print('default')

print(b, a)