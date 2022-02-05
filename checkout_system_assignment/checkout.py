# Checkout Class - 4PINT Assessment 1
# Paul Stuart
# 20.9.20

from datetime import date
import random

from checkout_system_assignment.product import Product


class CheckoutRegister:
    def __init__(
            self,
            total_items_array=None,
            time_stamp="Date",
            receipt_no=000,
            sale_amount=0,
            payment_customer=0,
    ):
        if total_items_array is None:
            total_items_array = [Product()]
        self.__total_items_array = total_items_array
        self.__time_stamp = time_stamp
        self.__receipt_no = receipt_no
        self.__sale_amount = sale_amount
        self.__payment_customer = payment_customer

    # GETTERS AND SETTERS
    def get_date(self):
        return self.__time_stamp

    def set_date(self, x):
        self.__time_stamp = x

    def get_receipt_no(self):
        return self.__receipt_no

    def set_receipt_no(self, x):
        self.__receipt_no = x

    def get_sale_amount(self):
        return self.__sale_amount

    def set_sale_amount(self, x):
        self.__sale_amount = x

    def get_payment_customer(self):
        return self.__payment_customer

    def set_payment_customer(self, x):
        self.__payment_customer = x

    def append_products_total_list(self, x):
        self.__total_items_array.append(x)

    def get_total_items_array(self):
        return self.__total_items_array

    # F string will output parameters or variables as a string --------------
    def print_checkout_details(self):
        return f" Receipt No: {self.__receipt_no}, " \
               f" Date: {self.__time_stamp}, " \
               f" Items: {self.__total_items_array}, " \
               f" Sale Amount: {self.__sale_amount}, " \
               f" Customer Payment: {self.__payment_customer}, "

    # Loop through the products in the checkout array, adding each item to give running total --------------
    def process_total(self):
        final_cost = 0
        for items in self.__total_items_array:
            final_cost = final_cost + items.get_product_price()
        self.set_sale_amount(final_cost)
        return final_cost

    # Generate Receipt No. with random number + current date/time stamp --------------
    def generate_receipt(self):
        random_num = random.randrange(1, 1000) * 4
        self.set_receipt_no(random_num)
        date_current = date.today()
        self.set_date(date_current)
        total = self.get_sale_amount()
        print("-------------- Final Receipt --------------")
        print("Receipt Number: {}".format(random_num))
        print("Date: ", date_current)
        print("Total: $", total)

    # Process the payment amount given by customer against the total sale and give change --------------
    def take_payment(self, payment_taken):
        sale_amount = self.get_sale_amount()
        settlement = sale_amount - payment_taken
        if payment_taken > sale_amount:
            settlement = payment_taken - sale_amount
            return settlement
        while settlement > 0:
            print(f"You have ${settlement} remaining on balance")
            remaining_balance = float(input(f"Please enter ${settlement} shown from total: "))
            settlement = settlement - remaining_balance
        return settlement
