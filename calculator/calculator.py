from arithmetic import Calculator
from main import get_numbers

def calculator():
    while True:
        operator = input("choose operator + - * /: ")

        x,y = get_numbers()
        calcu = Calculator(x,y)

        if operator == "+":
            result = calcu.add()
            print(result)
        else:
            print("")
if __name__ == "__main__":
    calculator()
