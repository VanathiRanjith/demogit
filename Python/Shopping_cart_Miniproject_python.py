# Define bill columns
bill_columns = ['Serial No', 'Item', 'Quantity', 'Total Cost']
bill_data = []

# Shopping cart items with initial quantities and costs
shopping_cart = {
    'Biscuits': {'Serial No': 1, 'Quantity': 5, 'Cost/Item': 20.5},
    'Cereals': {'Serial No': 2, 'Quantity': 10, 'Cost/Item': 90.0},
    'Chicken': {'Serial No': 3, 'Quantity': 20, 'Cost/Item': 100.0}
}

count = 0

while True:
    # Display shopping cart items
    print("Shopping Cart Items:")
    print("{:<10} {:<10} {:<10} {:<10}".format("Serial No", "Item", "Quantity", "Cost/Item"))
    for item, details in shopping_cart.items():
        print("{:<10} {:<10} {:<10} {:<10.2f}".format(details['Serial No'], item, details['Quantity'], details['Cost/Item']))
    user_input = int(input("What do you want to purchase? "))
    item = None
    for key, value in shopping_cart.items():
        if value['Serial No'] == user_input:
            item = key
            break
    if item is not None:
        quantity = int(input(f"How many {item} packets do you want to purchase: "))
        if quantity <= shopping_cart[item]['Quantity']:
            # Update item quantity in shopping cart
            shopping_cart[item]['Quantity'] -= quantity
            total_cost = quantity * shopping_cart[item]['Cost/Item']
            count += 1
            # Add item to bill data list
            new_row = {
                'Serial No': count,
                'Item': item,
                'Quantity': quantity,
                'Total Cost': total_cost
            }
            bill_data.append(new_row)
            input3 = input("Do you want to continue shopping? (Y/N): ")
            if input3.upper() == 'N':
                if count > 0:
                    input4 = input("Enter your name: ")
                    input5 = input("Enter your address: ")
                    input6 = int(input("Enter the distance from the store (5/10/15/30): "))
                    if 0 < input6 <= 15:
                        dc = 50
                        print('Delivery charge: 50 Rs will be levied for distance between 0 to 15km')
                    elif 15 < input6 <= 30:
                        dc = 100
                        print('Delivery charge: 100 Rs will be levied for distance between 15 to 30km')
                    print("------------Bill---------------\n")
                    # Display bill
                    print("{:<10} {:<15} {:<10} {:<10}".format(*bill_columns))
                    for row in bill_data:
                        print("{:<10} {:<15} {:<10} {:<10}".format(row['Serial No'], row['Item'], row['Quantity'], row['Total Cost']))
                    total_cost = sum(row['Total Cost'] for row in bill_data)
                    print("Total items cost:", total_cost)
                    print("Total Bill Amount: Total items cost + Delivery charge is):", total_cost + dc)
                    print("Name:", input4)
                    print("Address:", input5)
                    print("Have a nice day!")
                    print("{:<10} {:<10} {:<10} {:<10}".format("Serial No", "Item", "Quantity", "Cost/Item"))
                    for key, value in shopping_cart.items():
                        print("{:<10} {:<10} {:<10} {:<10.2f}".format(value['Serial No'], key, value['Quantity'], value['Cost/Item']))
                    break
        else:
            print(f"Available quantity of {item} is {shopping_cart[item]['Quantity']}")
    else:
        print("Invalid serial number selected.")
