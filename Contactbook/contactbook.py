contacts = []

while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\n----- Contact List -----")
            for i, contact in enumerate(contacts, start=1):
                print(f"\nContact {i}")
                print("Name   :", contact["Name"])
                print("Phone  :", contact["Phone"])
                print("Email  :", contact["Email"])
                print("Address:", contact["Address"])

    elif choice == "3":
        search = input("Enter Name or Phone Number: ")

        found = False
        for contact in contacts:
            if search == contact["Name"] or search == contact["Phone"]:
                print("\nContact Found")
                print("Name   :", contact["Name"])
                print("Phone  :", contact["Phone"])
                print("Email  :", contact["Email"])
                print("Address:", contact["Address"])
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter Name to Update: ")

        found = False
        for contact in contacts:
            if contact["Name"] == name:
                contact["Phone"] = input("New Phone: ")
                contact["Email"] = input("New Email: ")
                contact["Address"] = input("New Address: ")
                print("Contact updated successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter Name to Delete: ")

        found = False
        for contact in contacts:
            if contact["Name"] == name:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please enter 1 to 6.")