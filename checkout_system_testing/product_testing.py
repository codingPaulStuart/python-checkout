# 4PINT Assessment 1 - Paul Stuart 000389223
# Checkout System, Main Program using Checkout Class and Product Class TESTING CLASS

import unittest
from checkout_system_assignment.product import Product

# Test Product Object instance
prod_1 = Product()


class ProductTesting(unittest.TestCase):

    # Product ID return Value
    def test_get_product_id(self):
        prod_1.set_product_id(458)
        self.assertEqual(458, prod_1.get_product_id())

    # Product name return Value
    def test_get_product_name(self):
        prod_1.set_product_name('spinach')
        self.assertEqual('spinach', prod_1.get_product_name())

    # Product Description return Value
    def test_get_product_desc(self):
        prod_1.set_product_description('Vegetable')
        self.assertEqual('Vegetable', prod_1.get_product_description())

    # Product Bar Code return Value
    def test_get_product_barcode(self):
        prod_1.set_product_barcode('X048E490T')
        self.assertEqual('X048E490T', prod_1.get_product_barcode())

    # Product Price return Value
    def test_get_product_price(self):
        prod_1.set_product_price(4.0)
        self.assertEqual(4.0, prod_1.get_product_price())

    # Test Product Object Override equals Method, based on barcode
    def test_eq_object_compare(self):
        prod_2 = Product(product_bar_code='X0973845')
        prod_1.set_product_barcode('X048E490T')
        expected = prod_1.__eq__(prod_2)
        wrong = prod_1.__eq__(prod_1)
        self.assertFalse(expected, wrong)

    # Return F String output of Product Object
    def test_print_product(self):
        prod_3 = Product(458, 'spinach', 'Vegetable', 'X048E490T', 4.0)
        print_prod = f" ProductID: {458}, " \
                     f" ProductName: spinach, " \
                     f" ProductDesc: Vegetable, " \
                     f" ProductBarCode: X048E490T, " \
                     f" ProductPrice: {4.0}"
        self.assertEqual(print_prod, prod_3.print_product_details())

    # Return name and price function in Product
    def test_name_price_output(self):
        prod_3 = Product(458, 'spinach', 'Vegetable', 'X048E490T', 4.0)
        prod_name_price = 'spinach' + ": $ " + str(4.0)
        self.assertEqual(prod_name_price, prod_3.__name_price__())


if __name__ == '__main__':
    unittest.main()
