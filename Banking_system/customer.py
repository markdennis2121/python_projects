from core import Account

class Customer(Account):
    def __init__(self, name, customer_id):
        super().__init__()
        self.name = name.title()
        self.customer_id = customer_id

def create_customer(bank):
    print("\n🔐 Register New Customer")
    name = input("Enter your name: ").strip()
    customer_id = input("Create a unique ID: ").strip()

    if bank.find_customer(customer_id):
        print("❌ That ID is already taken. Try again.")
        return None

    customer = Customer(name, customer_id)
    bank.add_customer(customer)

    with open("student.txt", "a", encoding="utf-8" ) as f:
        f.write("\n" + "-" * 17 + "\n")
        f.write(f"Name: {customer.name}\n")
        f.write(f"Id: {customer.customer_id}\n")
        f.write(f"Balance: ₱{customer.acc_balance:.2f}\n")
        f.write("-" * 17 + "\n\n")

    print("\n✅ Account has been created successfully!")
    print("-" * 15)
    print(f"Welcome, {customer.name}!\nYour ID is: {customer.customer_id}")
    print("-" * 15 + "\n")
    return customer



