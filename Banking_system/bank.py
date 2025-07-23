class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_customer(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id:
                return c
        return None

    def show_summary(self):
        print(f"\n🏦 Bank Name: {self.name}")

        if not self.customers:
            print("-" * 17)
            print("📭 No account have been created yet.")
            print(" ")
        else:
            for c in self.customers:
                print(f"👤 Name: {c.name}, ID: {c.customer_id}")







