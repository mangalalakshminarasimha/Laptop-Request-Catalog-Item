# Simple Laptop Request Catalog System

class LaptopRequest:
    def __init__(self, user_name, laptop_model, justification):
        self.user_name = user_name
        self.laptop_model = laptop_model
        self.justification = justification
        self.status = "Pending"

    def approve_request(self):
        self.status = "Approved"

    def reject_request(self):
        self.status = "Rejected"

    def display_request(self):
        print(f"Request by: {self.user_name}")
        print(f"Laptop Model: {self.laptop_model}")
        print(f"Justification: {self.justification}")
        print(f"Status: {self.status}")
        print("-" * 30)

# Sample Laptop Catalog
laptop_catalog = ["Dell Inspiron 15", "HP Pavilion", "Lenovo ThinkPad", "Apple MacBook Air"]

# List to store requests
requests_list = []

def show_catalog():
    print("\nAvailable Laptops:")
    for idx, laptop in enumerate(laptop_catalog, 1):
        print(f"{idx}. {laptop}")
    print()

def create_request():
    user_name = input("Enter your name: ")
    show_catalog()
    choice = int(input("Select a laptop by number: "))
    laptop_model = laptop_catalog[choice - 1]
    justification = input("Enter justification for laptop request: ")

    new_request = LaptopRequest(user_name, laptop_model, justification)
    requests_list.append(new_request)
    print("\nLaptop request submitted successfully!\n")

def view_requests():
    if not requests_list:
        print("\nNo requests found.\n")
        return

    for idx, req in enumerate(requests_list, 1):
        print(f"Request #{idx}")
        req.display_request()

def approve_or_reject():
    view_requests()
    req_id = int(input("Enter the request number to update: ")) - 1
    decision = input("Approve or Reject? (A/R): ").upper()

    if decision == 'A':
        requests_list[req_id].approve_request()
        print("\nRequest approved.\n")
    elif decision == 'R':
        requests_list[req_id].reject_request()
        print("\nRequest rejected.\n")
    else:
        print("\nInvalid choice.\n")

def main():
    while True:
        print("\nLaptop Request Catalog Menu:")
        print("1. Create Laptop Request")
        print("2. View All Requests")
        print("3. Approve/Reject Requests")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_request()
        elif choice == '2':
            view_requests()
        elif choice == '3':
            approve_or_reject()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()