
from customer import create_customer
from menu import Menu
from bank import Bank
from core import Account
my_bank = Bank("DevBank")
list_of_customer = []
menu = Menu()

if __name__ == "__main__":
    while True:

        menu.menu()
        try:
            raw_input = input("Enter your choice (1-6): ").strip()
            if not raw_input.isdigit() or raw_input == "":
                print("❌ Invalid input. Please enter a number between 1 and 6.\n")
                continue
            choice = int(raw_input)
            if choice not in range(1, 7):
                print("❌ Please choose a number between 1 and 6.\n")
                continue
            elif choice == 1:
                Account.show_balance(my_bank)
            elif choice == 2 :
                my_bank.show_summary()
            elif choice == 3:
                customer = create_customer(my_bank)
            elif choice == 4:
                Account.deposit_to_account(my_bank)
            elif choice == 5:
                Account.withdraw_from_account(my_bank)
            elif choice == 6:
                print("Thank you.")
                break
            else:
                print(" ")
                print("Please choose (1-6) only.")
                print(" ")
        except Exception as e:

            print(f"Unexpected error: {e}")
