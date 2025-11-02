# def celsius_to_fahrenheit(c):
#     return (c * 9/5) + 32

# def fahrenheit_to_celsius(f):
#     return (f - 32) * 5/9

# def celsius_to_kelvin(c):
#     return c + 273.15

# def kelvin_to_celsius(k):
#     return k - 273.15

# print("Temperature Converter")
# print("1. Celsius to Fahrenheit ")
# print("2. Fahrenheit to Celsius")
# print("3. Celsius to Kelvin ")
# print("4. Kelvin to Celsius ")
# print("Choose conversion (1-4):")
# choice = input("enter choice: ")

# if choice == '1':
#     temprature = float(input("Enter temperature in Celsius: "))
#     print(f"{temprature}°C = {celsius_to_fahrenheit(temprature)}°F")
# elif choice == '2':
#     temprature = float(input("Enter temperature in Fahrenheit: "))
#     print(f"{temprature}°F = {fahrenheit_to_celsius(temprature)}°C")
# elif choice == '3':
#     temprature = float(input("Enter temperature in Celsius: "))
#     print(f"{temprature}°C = {celsius_to_kelvin(temprature)}K")
# elif choice == '4':
#     temprature = float(input("Enter temperature in Kelvin: "))
#     print(f"{temprature}K = {kelvin_to_celsius(temprature)}°C")
# else:
#     print("Invalid choice")

#===================================================================================================
# def calculate_sum(numbers):
#     return sum(numbers)
# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)
# def max_num(numbers):
#     return max(numbers)
# def min_num(numbers):
#     return min(numbers)
# def remove_duplicates(numbers):
#     return list(set(numbers))
# def sort_asc(numbers):
#     return sorted(numbers)
# def sort_des(numbers):
#     return sorted(numbers ,reverse=True)
# def filter_even(numbers):
#     return [num for num in numbers if num % 2 == 0]
# def filter_odd(numbers):
#     return [num for num in numbers if num % 2 != 0]

# numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
# print(f"numbers is {numbers}")
# print("choose operation:")
# print("1. Sum")
# print("2. average")
# print("3. maximum")
# print("4. minimum")
# print("5. remove duplicates")
# print("6. sort ascending")
# print("7. sort descending")
# print("8.filter even")
# print("9. filter odd")
# operation = input("Enter choice (1-9): ") 

# if operation == "1" :
#     print(calculate_sum(numbers))
# elif operation == "2" :
#     print(calculate_average(numbers))
# elif operation == "3" :
#     print(max_num(numbers))
# elif operation == "4" :
#     print(min_num(numbers))
# elif operation == "5" :
#     print(remove_duplicates(numbers))
# elif operation == "6" :
#     print(sort_asc(numbers))
# elif operation == "7" :
#     print(sort_des(numbers))
# elif operation == "8" :
#     print(filter_even(numbers))
# elif operation == "9" :
#     print(filter_odd(numbers))
# else :
#     print("plz choose invalid option")

#========================================================================================================

# text = input("enter text :")
# text = text.lower()
# total_chr_wSpaces = len(text)
# total_chr_woSpaces = len(''.join(text.split()))
# total_words = len (text.split())
# reverse = text[::-1]
# is_palin = ''.join(text.split()) == ''.join(text.split())[::-1]
# char_freq = {}
# for char in ''.join(text.split()):
#         char_freq[char] = char_freq.get(char, 0) + 1
# max_freq = max(char_freq.values())
# most_common_chars = [char for char, freq in char_freq.items() if freq == max_freq]
# print(f"total char (with spaces) is : {total_chr_wSpaces}")
# print(f"total char (without spaces) is : {total_chr_woSpaces}")
# print(f"total words  is : {total_words}")
# print(f"reversed word is : {reverse}")
# print(f"palindrom : {'yes' if is_palin else 'no'} ")
# print(f"char freq : {char_freq}")
# print(f"the most common chars is : {most_common_chars} appers :{max_freq} times ")

#=============================================================================================
# import random

# while True:
#     number = random.randint(1, 100)
#     attempts = 7

#     print("Guess a number between 1-100.")
#     print(f"You have {attempts} attempts")

#     for attempt in range(1, attempts + 1):
#         while True:
#             try:
#                 guess = int(input(f"Attempt {attempt} - Your guess: "))
#                 if 1 <= guess <= 100:
#                     break
#                 else:
#                     print("Please enter a number between 1-100.")
#             except ValueError:
#                 print("Please enter a number.")

#         if guess < number:
#             print("Too low")
#         elif guess > number:
#             print("Too high")
#         else:
#             print(f"You guessed it right in {attempt} attempts")
#             break

#         remaining = attempts - attempt
#         if remaining > 0:
#             print(f"Attempts left: {remaining}")

#     else:
#         print(f"Game Over! The number was {number}.")

#     restart = input("Play again? (yes/no): ").strip().lower()
#     if restart != "yes":
#         print("Thanks for playing")
#         break

#========================================================================================================
     
# def add_item(cart):
#     name = input("Enter item name: ").strip()
#     try:
#         price = float(input("Enter price: "))
#         qty = int(input("Enter quantity: "))
#     except ValueError:
#         print(" Invalid input")
#         return

#     if name in cart:
#         cart[name]["qty"] += qty
#     else:
#         cart[name] = {"price": price, "qty": qty}
#     print(f" {name} added to cart!")


# def remove_item(cart):
#     name = input("Enter item name to remove: ").strip().title()
#     if name in cart:
#         del cart[name]
#         print(f" {name} removed.")
#     else:
#         print(" Item not found.")


# def update_quan(cart):
#     name = input("Enter item name to update: ").strip()
#     if name in cart:
#         try:
#             new_qty = int(input("Enter new quantity: "))
#         except ValueError:
#             print(" Quantity must be a number")
#             return

#         if new_qty > 0:
#             cart[name]["qty"] = new_qty
#             print(f"{name} updated to {new_qty}")
#         else:
#             del cart[name]
#             print(f" {name} removed ")
#     else:
#         print(" Item not found")


# def view_cart(cart):
#     if not cart:
#         print(" Cart is empty")
#         return

#     subtotal = sum(data["price"] * data["qty"] for data in cart.values())
#     discount = subtotal * 0.1 if subtotal > 100 else 0
#     total = subtotal - discount

#     print("Cart")
#     for i, (item, data) in enumerate(cart.items(), start=1):
#         item_total = data["price"] * data["qty"]
#         print(f"{i}. {item} - Qty: {data['qty']}, Unit: ${data['price']:.2f}, Total: ${item_total:.2f}")

#     print(f"Subtotal: ${subtotal:.2f}")
#     if discount > 0:
#         print(f"Discount: ${discount:.2f} (10% off)")
#     print(f"Total: ${total:.2f}")


# def checkout(cart):
#     if not cart:
#         print(" Cart is empty")
#         return

#     total = sum(item["price"] * item["qty"] for item in cart.values())
#     if total > 100:
#         print("10 percent discount applied")
#         total *= 0.9

#     print(f" Final total: ${total:.2f}")
#     cart.clear()
#     print("Thank you")


# def main():
#     cart = {}
#     while True:
#         print("Shopping Cart Menu:")
#         print("1. Add item")
#         print("2. Remove item")
#         print("3. Update quantity")
#         print("4. View cart")
#         print("5. Checkout")
#         print("6. Exit")

#         choice = input("Choose an option: ").strip()
#         if choice == "1":
#             add_item(cart)
#         elif choice == "2":
#             remove_item(cart)
#         elif choice == "3":
#             update_quan(cart)
#         elif choice == "4":
#             view_cart(cart)
#         elif choice == "5":
#             checkout(cart)
#         elif choice == "6":
#             print(" Bye")
#             break
#         else:
#             print("Invalid choice")


# main()

#======================================================================================================================================
file = "contact.txt"
def add_contact() :
    name = input("enter name:").strip()
    phone = input("enter Phone: ").strip()
    email = input("enter Email: ").strip()
    
    with open(file, "a") as f:
        f.write(f"{name}|{phone}|{email}")
        print("saved")
        
def view_contacts():
    try:
        with open(file, "r") as f:
            contacts = f.readlines()
    except:
        print("No contacts found")
        return

    if not contacts:
        print("Contact list is empty")
        return
    for i, line in enumerate(contacts, start=1):
        name, phone, email = line.strip().split("|")
        print(f"{i}. {name} | {phone} | {email}")
def search_contact():
    search_name = input("enter name to search: ").strip().lower()
    found = False
    try:
        with open(file, "r") as f:
            for line in f:
                name, phone, email = line.strip().split("|")
                if search_name in name.lower():
                    print(f" {name} | {phone} | {email}")
                    found = True
    except:
        print("No contacts found")
        return
    if not found :
        print("cant find this name")
def delete_contact():
    name_to_delete = input("Enter name to delete: ").strip().lower()
    try:
        with open(file, "r") as f:
            lines = f.readlines()
    except :
        print("No contacts found.")
        return

    new_lines = []
    deleted = False
    for line in lines:
        name, phone, email = line.strip().split("|")
        if name.lower() != name_to_delete:
            new_lines.append(line)
        else:
            deleted = True

    with open(file, "w") as f:
        f.writelines(new_lines)

    if deleted:
        print(" Contact deleted")
    else:
        print("Contact not found")
def update_contact():
    name_to_update = input("Enter name to update: ").strip().lower()
    try:
        with open(file, "r") as f:
            lines = f.readlines()
    except:
        print("No contacts found")
        return

    updated = False
    new_lines = []

    for line in lines:
        name, phone, email = line.strip().split("|")
        if name.lower() == name_to_update:
            print(f"Editing contact: {name}")
            new_phone = input(f"New phone (old: {phone}): ").strip() or phone
            new_email = input(f"New email (old: {email}): ").strip() or email
            new_lines.append(f"{name}|{new_phone}|{new_email}\n")
            updated = True
        else:
            new_lines.append(line)

    with open(file, "w") as f:
        f.writelines(new_lines)

    if updated:
        print("Contact updated successfully")
    else:
        print(" Contact not found")


def main():
    while True:
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            print(" Goodbye")
            break
        else:
            print(" Invalid choice, please try again")


main()    
        