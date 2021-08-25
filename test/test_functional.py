import unittest
import sys
sys.path.append("..")
from usecase import Purchase
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_revised.txt","w") as f:
            pass
    def test_object_type(self):
        #self.assertTrue(Purchase.obtain_purchase_with_amount("101,2-3-2021,venu,bat,500.00,4,ball,200,2,guard,200.00,2,helmet,1500.00,4,vickets,1500.00,2"),Purchase)
        obj=Purchase.obtain_purchase_with_amount("101,2-3-2021,venu,bat,500.00,4,ball,200,2,guard,200.00,2,helmet,1500.00,4,vickets,1500.00,2")
        if type(obj)!=type(None):
            #print(obj)
            #print(type(obj))
            with open("output_revised.txt","a") as f:
                f.write("ObtainPurchaseWithAmount=True\n")
        else:
            with open("output_revised.txt","a") as f:
                f.write("ObtainPurchaseWithAmount=False\n")
