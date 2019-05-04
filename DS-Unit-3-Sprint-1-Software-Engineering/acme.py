import random


class Product:
    """
    Product class

    Constructor params:
    name:        string, no default
    price:       int, default 10
    weight:      int, default 20
    flammability float, default 0.5
    identifier   int, auto random 1000000 - 9999999
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """
        Method to determine how stealable an item is (price / weight)
        Params:  None
        Returns: string with "stealability" of a Product
        """
        steal_score = self.price / self.weight
        if steal_score >= 1:
            return 'Very stealable!'
        elif steal_score >= .5:
            return 'Kinda stealable.'
        else:
            return 'Not so stealable...'

    def explode(self):
        """
        Method to determine how explosive an item is (flammability * weight)
        Params:  None
        Returns: string with explosiveness of a Product
        """
        explode_score = self.flammability * self.weight
        if explode_score >= 50:
            return '...BABOOM!!'
        elif explode_score >= 10:
            return '...boom!'
        else:
            return '...fizzle.'

        
class BoxingGlove(Product):
    """
    BoxingGlove class - subclass of Product

    Constructor params:
    name:        string, no default
    weight:      int, default 10

    Inherited from superclass:
    price:
    flammability
    identifier
    """
    def __init__(self, name, weight=10):
        super(BoxingGlove, self).__init__(name)
        self.weight = int(weight)

    def explode(self):
        """
        Method overrides superclass explode - returns a msg referencing the
                                    inexplosiveness(!) of boxing gloves
        Params:  None
        Returns: string "...it's a glove."
        """
        return "...it's a glove."

    def punch(self):
        """
        Subclass method to determine the effect of a punch is
                                    (depends strictly on weight)
        Params:  None
        Returns: string with appropriate response to punch
        """
        if self.weight >= 15:
            return 'OUCH!'
        elif self.weight >= 5:
            return "Hey that hurt!"
        else:
            return "That tickles."
