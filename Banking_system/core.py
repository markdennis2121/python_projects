
class Account:
    def __init__(self):
        self.acc_balance = 0.0  # ✅ safer type for banking logic


    def balance(self):
        return f"Your balance is ${self.acc_balance:.2f}"

    @staticmethod
    def show_balance(bank):
        cust_id = input("Enter customer ID to show balance: ").strip()
        customer = bank.find_customer(cust_id)

        if not customer:
            print("❌ Customer not found.")
            return

        print(customer.balance())

    @staticmethod
    def deposit_to_account(bank):
        cust_id = input("Enter customer ID to deposit: ").strip()
        customer = bank.find_customer(cust_id)
        if not customer:
            print("❌ Customer not found.")
            return
        try:
            amount = float(input("Enter the amount to deposit: "))
            customer.deposit(amount)
        except ValueError:
            print("Invalid amount entered.")

    @staticmethod
    def withdraw_from_account(bank):
        cust_id = input("Enter customer ID to withdraw: ").strip()
        customer = bank.find_customer(cust_id)
        if not customer:
            print("❌ Customer not found.")
            return
        try:
            amount = float(input("Enter the amount to withdraw: "))
            customer.withdraw(amount)
        except ValueError:
            print("Invalid amount entered.")