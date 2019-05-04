"""
method to randomly create product list
method to create inventory report based on these randomly created products
"""
import random
from acme import Product


def generate_products(num_products=30):
    """
    Method to generate a parameterized number of products randomly
    Params:
        number: int, default 30
    Returns:
        list of randomly-generated products
    """
    adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
    products = {}
    for prod in range(num_products):
        name = random.choice(adjectives) + " " + random.choice(nouns)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.50000001)
        products[prod] = Product(name, price, weight, flammability)
    return products


def inventory_report(products):
    """
    Method to create a parameterized product listing
    Params:
        products: list, no default
    Returns:
        nothing

    Report has the following:

        * Number of unique product names
        * Average price, Average weight, Average flammability
    """
    names = []
    prices = []
    weights = []
    flammabilities = []

    for i in range(len(products)):
        names.append(products[i].name)
        prices.append(products[i].price)
        weights.append(products[i].weight)
        flammabilities.append(products[i].flammability)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names: ', len(set(names)))
    print('Average price: ', sum(prices) / float(len(prices)))
    print('Average weight: ', sum(weights) / float(len(weights)))
    print('Average flammability: ', sum(flammabilities) /
                                    float(len(flammabilities)))

if __name__ == '__main__':
    inventory_report(generate_products())
