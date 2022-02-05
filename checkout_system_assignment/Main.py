# 4PINT Assessment 1 - Paul Stuart 000389223
# Checkout System, Main Program using Checkout Class and Product Class

import csv

from checkout_system_assignment.checkout import CheckoutRegister
from checkout_system_assignment.product import Product

# List that store the Product Objects, list for Check out Object instance. Checkout occurrence stored in check out list
# Each time a check out session is recorded it gets added to list with unique identifier from generate_receipt function
product_list = []
checkout_list = []
checkout_instance = CheckoutRegister()


# Item is scanned via barcode and then looped through the product list for comparison then returned
def scan_item(product_barcode):
    for p in product_list:
        p_id = p.get_product_barcode()
        if p_id == product_barcode:
            return p


# Save csv file from transaction with Product Items and Receipt Details
def save_file(checkout_object):
    # Create new csv file with unique name based on receipt number, make the top row contain receipt details
    with open(f"receipt_no_{checkout_object.get_receipt_no()}.csv", "w") as saved_csv:
        # Headers on First Row using DictWriter
        receipt_headers = ['Product ID', 'Product Name', 'Price', 'Product Description']
        csv_write = csv.DictWriter(saved_csv, fieldnames=receipt_headers)
        csv_write.writeheader()

        # Output the Product objects from the checkout Product List into a row in csv file
        for products in checkout_object.get_total_items_array():
            csv_write.writerow({'Product ID': f'{products.get_product_id()}',
                                'Product Name': f'{products.get_product_name()}',
                                'Price': f'{products.get_product_price()}',
                                'Product Description': f'{products.get_product_description()}'})

        # Write the unique data from the object instance of checkout into a row in csv file
        csv_write.writerow({'Product ID': f'receipt No: {checkout_object.get_receipt_no()}',
                            'Product Name': f'Date: {checkout_object.get_date()}',
                            'Price': f'Total Cost: ${checkout_object.get_sale_amount()}',
                            'Product Description': f'Have a nice day!'})


def main():
    with open('productItems.csv', newline='') as csv_file:
        reader2 = csv.reader(csv_file)
        next(reader2, None)  # Skip the header.

        # Unpack each row, every CSV is aligned with Product Class Attribute so new objects can be made
        for id_code, name, description, barcode, price in reader2:
            # Convert the data to right type, remove white space
            id_code = str.lstrip(id_code)
            name = str.lstrip(name)
            description = str.lstrip(description)
            barcode = str.lstrip(barcode)
            price = float(price)

            # Create Product instance, assign the variables to the Product Object parameters and append to list.
            product_list.append(Product(id_code, name, description, barcode, price))

        # Output the current list of items with codes so customer can scan in
        print("----------------------------------------------------------------")
        print("Current Items Available:\n")
        for items in product_list:
            print(items.print_product_details())
        print("----------------------------------------------------------------")

    # While loop that continues to allow for more items to be added and tallied up, input validation used
    continue_shopping = str.upper(input("Do you wish to continue Y/N: "))
    while continue_shopping != 'Y' and continue_shopping != 'N':
        print("Please only enter a Y or N")
        continue_shopping = str.upper(input("Do you wish to continue Y/N: "))

    while continue_shopping == 'Y':
        item_scan = input("Please scan an item, see above listing for codes : ")
        item = scan_item(item_scan)

        # As long as there is a scanned item from the Product list, append it to checkout list variable
        if item is not None:
            checkout_instance.append_products_total_list(item)
            print(item.print_product_details())

            # Add the scanned items to checkout list and output
            print("----------------------------------------------------------------")
            print("Current Checkout Basket:")
            for items in checkout_instance.get_total_items_array():
                print(items.__name_price__())
            print("------------")

            # Display running total after each item is added to the shopping basket
            total = checkout_instance.process_total()
            print("Total: $", total)
            print("\n----------------------------------------------------------------")

        else:
            print("This item is not in the inventory list")
        continue_shopping = str.upper(input("Do you wish to continue Y/N: "))

    # Process payment, generate receipt
    checkout_instance.generate_receipt()
    # Convert String to Float for processing in take_payment() function
    customer_payment = float(input("Please enter amount shown from total: $"))
    while customer_payment < 0:
        customer_payment = float(input("Please enter amount shown from total: $"))

    settlement = checkout_instance.take_payment(customer_payment)

    # Output final Settlement of Payment from Customer
    print("\n-------------- Payment Complete --------------")
    print("Settlement after payment: $", settlement)
    print("------------------ Thank You ------------------")
    checkout_list.append(checkout_instance)
    save_file(checkout_instance)


main()
