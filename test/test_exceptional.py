
import unittest
import sys
sys.path.append("..")
from usecase import Purchase
from myexception import InvalidWholeSaleError
class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_exception_revised.txt","w") as f:
            pass
    def test_whole_sale_error(self):
        #self.assertRaises(InvalidWholeSaleError,Purchase.obtain_purchase_with_amount,"101,2-3-2021,venu,ball,200,2,guard,200.00,2,helmet,1500.00,4")
        try:
            obj=Purchase.obtain_purchase_with_amount("101,2-3-2021,venu,bat,500.00,4,helmet,1500.00,4,vickets,1500.00,2")
            with open("output_exception_revised.txt","a") as f:
                f.write("TestWholeSaleError=False\n")
        except InvalidWholeSaleError as e:
            with open("output_exception_revised.txt","a") as f:
                f.write("TestWholeSaleError=True\n")

    def test_value_error(self):
        #self.assertRaises(ValueError,Purchase.obtain_purchase_with_amount,"101abc,2-3-2021,venu,ball,200,2,guard,200.00,2,helmet,1500.00,4,vickets,1500.00,2")
        try:
            obj=Purchase.obtain_purchase_with_amount("101abc,2-3-2021,venu,bat,500.00,4,ball,200,2,guard,200.00,2,helmet,1500.00,4,vickets,1500.00,2")
            with open("output_exception_revised.txt","a") as f:
                f.write("TestValueError=False\n")
        except ValueError as e:
            with open("output_exception_revised.txt","a") as f:
                f.write("TestValueError=True\n")
