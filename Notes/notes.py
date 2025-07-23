"""
import random

def generate_secret_num():
    return random.randint(1, 100)

def ask_name():
    return input("Enter your name:")

def user_guess():
    return input("Guess the secret number 1-100 (q to quit): ").lower().strip()

def play_game(player_name_input):
    secret_num = generate_secret_num()
    attempts = 0
    guesses = []

    while True:
        user = user_guess()

        if user == "q":
            print("Thanks for playing!")
            return False
        try:
            num = int(user)
            guesses.append(num)
            attempts += 1
            if num == secret_num:
                print(f"======{player_name_input}======")
                print(f"You are right! {secret_num} is the correct answer!")
                print(f"You guessed it int {attempts} attempts!")
                print(f"Your guesses: {guesses}")

                play_again = input("Want to play again? (y/n): ").lower().strip()
                if play_again =="y":
                    return  True
                else:
                    print("Thanks for playing!")
                    return False
            elif num > secret_num:
                print(f"{num} is a bit higher! Please try lower.")
            elif num < secret_num:
                print(f"{num} is a bit lower! Please try higher.")

        except ValueError:
            print("Invalid Input! please try again.")

player_name = ask_name()
while play_game(player_name):
    pass

"""

"""
evens = []
odds = []
even_count = 0
odd_count = 0
def add_even(num):
    global  even_count
    evens.append(num)
    even_count += 1
    print(f"The number {num} is even.")
def add_odd(num):
    global  odd_count
    odds.append(num)
    odd_count += 1
    print(f"The number {num} is odd.")

def quit_the_game():
    print(f"Thanks for playing.")
    print(f"There are {even_count} even numbers: {evens}")
    print(f"There are {odd_count} odd numbers: {odds}")

def ask_user():
    return input("Enter a number (q to quit): ")
while True:
    user = ask_user()

    if user == "q":
        quit_the_game()
        break

    try:
        ask = int(user)

        if ask % 2 == 0:
            add_even(ask)
        else:
            add_odd(ask)


    except ValueError:
        print(f"{user} is invalid please try again.")

"""
"""

import random

def random_num():
    return random.randint(1,100)

def game_stop():
    return print("Thanks for playing!")

def play_again():
    return input("Want to play again?(y/n): ").lower().strip()

def game_play():
    target_num = random_num()
    attempts = 10
    total_guesses = 0
    correct_guess = 0
    weak_player = False

    def title():
        return ("============== Guess the secret number ==============\n"
                f"============= You will have {attempts} attempts ============= ")

    def user_input():
        return input(f"Guess the secret number(q to quit): ").lower().strip()

    print(title())
    for i in range(1, attempts + 1):
        user = user_input()

        if user == "q":
            print("Thanks for playing!")
            print(f"The target number was: {target_num}")
            weak_player = True
            break

        try:
            num = int(user)
            if num < 1 or num > 100:
                print(f"{num} is out of range! Please try again.")
                continue

            #add 1 to total_guesses
            total_guesses += 1

            if num == target_num:
                correct_guess = 1 # add 1 when it gets the correct answer

                print(f"You are right! {target_num} is the correct answer! ")
                print(f"You guessed it in {total_guesses} attempts!")
                break
            elif num > target_num:
                print(f"{num} is a bit higher! Please try lower.")
            else:
                print(f"{num} is a bit lower! Please try higher")
            print(f"Attempts left: {attempts - i}")

            # useful hint!
            if abs(num - target_num) <= 5 and num != target_num:
                print("Very close!")

        except ValueError:
            print(f"{user} is invalid input. please try again.")
            continue

    else:
        print("Out of attempts!")
        print(f"The random number was {target_num}")


    if not weak_player: #this line will prevent the accuracy rate to be display
        if total_guesses > 0:
            accuracy_rate = (correct_guess / total_guesses) * 100

        else:
            accuracy_rate = 0

        print(f"Your accuracy rate: {accuracy_rate:.2f}%")
    if play_again() == "y":
        game_play()

    else:
        game_stop()


game_play()
"""
"""
import random

def choose_difficulty():
    print("Choose difficulty level:")
    print("1 - Easy (1 to 50)")
    print("2 - Medium (1 to 100)")
    print("3 - Hard (1 to 200)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return 1, 50
        elif choice == "2":
            return 1, 100
        elif choice == "3":
            return 1, 200
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def random_num(start, end):
    return random.randint(start, end)

def play_game():
    while True:
        start, end = choose_difficulty()
        number = random_num(start, end)
        attempts = 0
        guesses = []

        while True:
            user = input(f"Enter your guess ({start} to {end}, q to quit): ").lower().strip()

            if user == "q":
                print("Thanks for playing!")
                print(f"The random number was: {number}")
                break

            try:
                guess = int(user)

                if not start <= guess <= end:
                    print(f"Please enter a number between {start} and {end}.")
                    continue

                attempts += 1
                guesses.append(guess)

                if guess > number:
                    if abs(guess - number) <= 5:
                        print(f"{guess} is very close!")
                    else:
                        print(f"{guess} is too high! Try a bit lower.")

                elif guess < number:
                    if abs(guess - number) <= 5:
                        print(f"{guess} is very close!")
                    else:
                        print(f"{guess} is too low! Try a bit higher.")

                elif guess == number:
                    accuracy = 100 - (sum(abs(g - number) for g in guesses) / attempts)
                    print(f"You are right! {guess} is the random number!")
                    print(f"You guessed it in {attempts} attempts!")
                    print(f"Your guesses: {guesses}")
                    print(f"Your accuracy: {accuracy:.2f}")

                    break

            except ValueError:
                print("Invalid guess!")

        play_again = input("Want to play again? (y/n): ").lower().strip()
        if play_again != "y":
            print("Goodbye!")
            break

play_game()
"""
"""
def add(num1,num2):
    return num1 + num2
def minus(num1,num2):
    return num1 - num2

user = input("choose operator + - * /: ")
num = int(input("Enter first number: "))
second = int(input("Enter seconde number: "))

if user == "+":
    print("Result:", add(num,second))
if user == "-":
    print("Result:", minus(num,second))
"""
"""
#args
def my_Names(*names):
    for name in names:
        print("Hi", name)

my_Names('mark','dennis','manangan')

"""
""""
#*kwargs
def family_name(*first_name,last_name):
    for names in first_name:
        print(names +" " + last_name)

family_name("Mark","Dennis",last_name="Hotdog")
"""""
"""
#**kwargs
def my_info(**student):
    print(student["name"])
    print(student["age"])
    print(student["course"])
    print(student["year"])

my_info(name="Mark Dennis V. Manangan",age= 24, course="BSCS", year="Fourth year")
"""
"""
def my_status(**student):
    print('name:', student['name'])
    print('course:', student['course'])
my_status(name= 'mark dennis ', course= 'computer science' )
"""
"""
#lambda
add = lambda x : x * 3

user = int(input("Enter a number: "))
print(add(user))

"""
"""
#OOP
class Character:
    def __init__(self, name , hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
        print("Character " + self.name + " Has been created!")

charOne = Character("Mark", 100, 500)
charTwo = Character("Dennis", 100, 500)
"""

"""
#OOP
class Character:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def show_status(self):
        print(f"Name: {self.name}")
        print(f"Hero hp: {self.hp}")
        print(f"Hero damage: {self.damage}")

print("======Dota Characters=====")

heroesOne= Character("Mirana",100,600)
heroesTwo= Character("Luna",100,590)
heroesThree= Character("Invoker", 100, 700)

characters = [heroesOne, heroesTwo,heroesThree]

for hero in characters:
    hero.show_status()
    print("-" * 17)
"""
"""
#Parent class
class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self)-> str:
        return f"Hi, I am {self.first_name} {self.last_name}"

#Teacher class
class Teacher(Person):
    def __init__(self, first_name: str, last_name:str,position:str):
        super().__init__(first_name,last_name)
        self.position = position

    def introduce(self)-> str:
        base_intro = super().introduce()
        return f"{base_intro}\nPosition: {self.position}"

#Student class
class Student(Person):
    def __init__(self,first_name: str,last_name: str, course: str):
        super().__init__(first_name, last_name)
        self.course = course

    def introduce(self)-> str:
        base_intro = super().introduce()
        return f"{base_intro}\nCourse: {self.course}"


sOne = Student("Mark", "Manangan","BSCS")
tOne = Teacher("Micah","Deocampo", "Teacher 1")

faculty = [sOne,tOne]

print("==== Faculty ====")
for person in faculty:
    print(person.introduce())
    print("-" * 17)
"""
"""
class House:
    def __init__(self,number,people):
        self.number = number
        self.people = people

    def introduce(self):
        return f'House #: {self.number} \nMember: {self.people}'
hOne = House('201', 4)
class Member:
    def __init__(self,name,age,role):
        self.name = name
        self.age = age
        self.role = role

    def introduce(self) -> str:
        return f'Name: {self.name} \nAge: {self.age} \nRole: {self.role}'


pOne = Member('Mark', 24, 'Brother')
pTwo = Member('Micah', 25, 'Sister')
house_member = [hOne,pOne,pTwo]

for member in house_member:
    print(member.introduce())
    print("-" * 17)

"""
"""
class Student:
    def __init__(self, my_name: str, my_course: str, my_year: str):
        self.name = my_name
        self.course = my_course
        self.year = my_year

    def introduce(self):
        print(f"     Name  : {self.name.title()}")
        print(f"     Course: {self.course.title()}")
        print(f"     Year  : {self.year.title()}")

name_of_students = []
valid_years = ['1st year', '2nd year', '3rd year', '4th year']

while True:
    try:
        name = input("Enter your name: ").strip()
        while not name:
            print("Name cannot be empty.")
            name = input("Enter your name: ").strip()

        course = input("Enter your course: ").strip()
        while not course:
            print("Course cannot be empty.")
            course = input("Enter your course: ").strip()

        year = input("Enter your year: ").lower().strip()
        while year not in valid_years:
            print("Invalid year. Please input a valid year (e.g., 1st year, 2nd year)")
            year = input("Enter your year: ").lower().strip()
        year = year.title()

        name_of_students.append(Student(name, course, year))
        print(" ")
        print(" ")
        ask = input("Want to continue? (y/n): ").strip().lower()
        if ask != "y":
            print("\n   Registration Summary:\n")
            break

    except ValueError:
        print("Invalid input. Please try again.")

for idx, person in enumerate(name_of_students, start=1):
    print(f"Student #{idx}")
    person.introduce()
    print("-" * 20)
"""
"""
from arithmetic import Calculator

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
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

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
"""

"""
import  os 

file_path = "C:\\Users\\mmana\\OneDrive\\Desktop\\test"

if os.path.exists(file_path):
    print(f"The locations {file_path} exist")
    if os.path.isfile(file_path):
        print("This is a file.")
    elif os.path.isdir(file_path):
        print('This is directory')
else:
    print("The location doesn't exist.")

"""
"""
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

"""




