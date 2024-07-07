import json

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {index}:")
                print(contact)

    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print(contact)
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self, name):
        found = False
        for contact in self.contacts:
            if name.lower() == contact.name.lower():
                print("Enter new details (leave blank to keep current):")
                new_phone = input(f"New Phone number ({contact.phone_number}): ").strip() or contact.phone_number
                new_email = input(f"New Email ({contact.email}): ").strip() or contact.email
                new_address = input(f"New Address ({contact.address}): ").strip() or contact.address
                contact.phone_number = new_phone
                contact.email = new_email
                contact.address = new_address
                found = True
                print("Contact updated successfully.")
                break
        if not found:
            print("Contact not found.")

    def delete_contact(self, name):
        found = False
        for contact in self.contacts:
            if name.lower() == contact.name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                found = True
                break
        if not found:
            print("Contact not found.")

    def save_contacts(self, filename):
        with open(filename, 'w') as file:
            contacts_json = [vars(contact) for contact in self.contacts]
            json.dump(contacts_json, file, indent=4)
        print(f"Contacts saved to {filename}.")

    def load_contacts(self, filename):
        try:
            with open(filename, 'r') as file:
                contacts_json = json.load(file)
                self.contacts = [Contact(**contact) for contact in contacts_json]
            print(f"Contacts loaded from {filename}.")
        except FileNotFoundError:
            print("No previous contacts found.")

def main():
    contact_book = ContactBook()
    filename = "contacts.json"
    contact_book.load_contacts(filename)

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save Contacts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter Name or Phone Number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            name = input("Enter Name of the contact to update: ")
            contact_book.update_contact(name)

        elif choice == '5':
            name = input("Enter Name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            contact_book.save_contacts(filename)

        elif choice == '7':
            contact_book.save_contacts(filename)
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
