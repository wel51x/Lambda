"""
Unit testing for Acme products and product reporting
"""
import unittest
from acme import Product
from acme import BoxingGlove
import acme_report


class AcmeProductTests(unittest.TestCase):
    """
    Making sure Acme products are the tops!
    """

    def test_default_product_price(self):
        """
        Test default product price == 10.
        """
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """
        Test default product weight == 20.
        """
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_boxing_glove_weight(self):
        """
        Test default Boxing Glove weight == 10.
        """
        glove = BoxingGlove('Test Boxing Glove')
        self.assertEqual(glove.weight, 10)

    def test_product_stealability_and_explode(self):
        """
        Test product stealability and explosiveness
        """
        prod = Product('Test Product', weight=200, flammability=5.0)
        stealable = prod.stealability()
        explodable = prod.explode()
        self.assertEqual(stealable, 'Not so stealable...')
        self.assertEqual(explodable, '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    """
    Making sure Acme reporting is the tops!
    """

    def test_default_num_products(self):
        """
        Check that default number of items == 30 in report
        """
        products = acme_report.generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """
        Test for legal product names
        """
        adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
        products = acme_report.generate_products()
        for prod in range(len(products)):
            prod_name = products[prod].name
            name_split = prod_name.split()
            self.assertIn(name_split[0], adjectives)
            self.assertIn(name_split[1], nouns)

if __name__ == '__main__':
    unittest.main()
