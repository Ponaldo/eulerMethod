import math


def main():
    print("Welcome to the Euler's method program, input your values:")
    first = float(input("Input the first y-value: "))
    h = float(input("Input the step size: "))
    n = float(input("Input the number n you want to approximate to: "))
    dif = str(input("Input the differential equation(Use the * character to show multiplication, and ** for exponents): "))

    previous = first
    x = 0
    for i in range(math.floor(n/h)):
        y = previous
        previous += h*eval(dif, {"x": x, "y": y})
        x += h
    print("The value is: " + str(previous))


main()


