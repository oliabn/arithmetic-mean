"""Task4
Створіть програму, яка складається з функції, яка приймає три числа і
повертає їх середнє арифметичне, і головного циклу, що запитує у користувача
числа і обчислює їх середні значення за допомогою створеної функції.
"""


def arithmetic_mean(num1, num2, num3):
    return (num1 + num2 + num3) / 3


def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def is_valid_input(inp):
    if len(inp) != 3:
        return False
    return is_float(inp[0]) and is_float(inp[1]) and is_float(inp[2])


# main program
while True:
    numbers = input("Enter 3 numbers by a space, e.g. -2.5 7 10: ").split()

    if not is_valid_input(numbers):
        print("Incorrect input. Try again")
        continue

    numbers = tuple(map(float, numbers))

    print(f"Arithmetic mean of {numbers} = {arithmetic_mean(*numbers):.2f}")

    exit()
