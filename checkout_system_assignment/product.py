# Product Class - 4PINT Assessment 1
# Paul Stuart
# 20.9.20


class Product:

    def __init__(
            self,
            product_id='DEF_ID',
            product_name='DEF_NAME',
            product_description='DEFAULT_DESC',
            product_bar_code='DEF_BARCODE',
            product_price=0
    ):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_description = product_description
        self.__product_bar_code = product_bar_code
        self.__product_price = product_price

    def Product(self, barcode):
        self.__product_bar_code = barcode

    # GETTERS AND SETTERS
    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, x):
        self.__product_id = x

    def get_product_description(self):
        return self.__product_description

    def set_product_description(self, x):
        self.__product_description = x

    def get_product_barcode(self):
        return self.__product_bar_code

    def set_product_barcode(self, x):
        self.__product_bar_code = x

    def get_product_price(self):
        return self.__product_price

    def set_product_price(self, x):
        self.__product_price = x

    def get_product_name(self):
        return self.__product_name

    def set_product_name(self, x):
        self.__product_name = x

    # F string will output parameters or variables as a string
    def print_product_details(self):
        return f" ProductID: {self.__product_id}, " \
               f" ProductName: {self.__product_name}, " \
               f" ProductDesc: {self.__product_description}, " \
               f" ProductBarCode: {self.__product_bar_code}, " \
               f" ProductPrice: {self.__product_price}"

    # Compare 2 Product Objects Overload
    def __eq__(self, other):
        if self.__product_bar_code == other.__product_bar_code:
            return True
        return False

    # String Output of Product Name and Price
    def __name_price__(self):
        return self.__product_name + ": $ " + str(self.__product_price)
