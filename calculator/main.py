from arithmetic import Calculator
def get_numbers():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return x,y
def run_calculator():

    ope = ['+','-','*','/']

    while True:

        print("=====Simple Calculator=====")

        user = input("Choose operator + - * / (q to quit): ").strip()
        while user not in ope and user.lower() != 'q':
            user = input('Choose valid operator + - * / (q to quit): ').strip()
            if user.lower() == 'q':
                print('Thank you for playing!')
                break
        if user.lower() == 'q':
            print('Thankyou for playing!')
            break
        try:
            x,y = get_numbers()

            calc =Calculator(x,y)

            result = None

            if user == '+':
                result = calc.add()
            elif user == "-":
                result = calc.subtract()
            elif user == '*':
                result = calc.multiply()
            elif user == '/':
                result = calc.divide()

            print(f'Result: {result}')


        except ValueError:
            print('Invalid input. Please try again.')
            continue
    if __name__ == "__main__":
        run_calculator()