# 4PINT Assessment 1 - Paul Stuart 000389223
# Checkout System, Main Program using Checkout Class and Product Class TESTING CLASS

import unittest
from checkout_system_assignment.checkout import CheckoutRegister
from checkout_system_assignment.product import Product

# Checkout Register Object for testing
checkout_1 = CheckoutRegister()
checkout_2 = CheckoutRegister()

# Products for testing and putting into the array
prod_1 = Product('p100', 'Milk', 'Dairy Food', 'X0123456', 3.2)
prod_2 = Product('p200', 'Bread', 'Baked Goods', 'X0654321', 2.5)
prod_3 = Product('p300', 'Eggs', 'Dairy Food', 'X0234567', 6.5)
prod_4 = Product()


class CheckoutTesting(unittest.TestCase):

    # Checkout Date return Value
    def test_get_date(self):
        checkout_1.set_date('2021-03-16')
        self.assertEqual('2021-03-16', checkout_1.get_date())

    # Checkout Get Receipt No return Value
    def test_get_receiptNo(self):
        expected = 45789
        checkout_1.set_receipt_no(expected)
        actual = checkout_1.get_receipt_no()
        self.assertEqual(expected, actual)

    # Checkout Get Sale Amount return Value
    def test_get_sale(self):
        expected = 34.0
        checkout_1.set_sale_amount(expected)
        actual = checkout_1.get_sale_amount()
        self.assertEqual(expected, actual)

    # test Payment from the Customer return Value
    def test_get_customer_pay(self):
        expected = 40
        checkout_1.set_payment_customer(expected)
        actual = checkout_1.get_payment_customer()
        self.assertEqual(expected, actual)

    # Checkout get total items Array (Need the blank prod_4 objet)
    def test_get_total_itemsArray(self):
        checkout_1.append_products_total_list(prod_3)
        checkout_1.append_products_total_list(prod_2)
        checkout_1.append_products_total_list(prod_1)
        actual_array = checkout_1.get_total_items_array()
        test_array = [prod_4, prod_3, prod_2, prod_1]
        self.assertEqual(test_array, actual_array)

    # Return F String output of Product Object
    def test_print_product(self):
        checkout_3 = CheckoutRegister(prod_3, '22-03-21', 12345, 7, 10)
        test = f" Receipt No: {12345}, " \
               f" Date: 22-03-21, " \
               f" Items: {prod_3}, " \
               f" Sale Amount: {7}, " \
               f" Customer Payment: {10}, "
        self.assertEqual(test, checkout_3.print_checkout_details())

    # Generate Receipt Not able to be tested as it uses random function (other getter/setters already tested inside
    # this function and have passed)

    # Return payment settlement from take Payment Function in Checkout
    def test_take_payment(self):
        checkout_2.set_sale_amount(45.0)
        payment_taken = 50
        actual = checkout_2.take_payment(payment_taken)
        expected_change = 5
        self.assertEqual(expected_change, actual)


if __name__ == '__main__':
    unittest.main()
