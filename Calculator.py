class Calculator:
    def add(x, y):
        return x + y
    def sub(x, y):
        return x - y
    def mul(x, y):
        return x * y
    def div(x, y):
        return x / y
if __name__ == "__main__":
    x = int(input("x: "))
    y = int(input("y: "))
    action = input("operator (+ - * / !): ")
    if action == "+":
        ("Сумма = ", Calculator.add(x, y))
    elif action == "-":
        (Calculator.sub(x,y))
    elif action == "*":
        ("Произведение = ", Calculator.mul(x, y))
    elif action == "/":
        ("Деление = ", Calculator.div(x, y))