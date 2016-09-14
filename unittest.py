import unittest

from Shop import Shop


# 1.Pikachu
# 2.Squirtle
# 3.Charmander
class ShopTesting(unittest.TestCase):
    # create a shop
    poke_list = ["Pikachu", "Squirtle", "Charmander"]
    prices = [6, 5, 5]
    poke_discount = {1: 0, 2: 10, 3: 20, 4: 40}
    shop = Shop(poke_list, prices, poke_discount)

    # Purchased 1 Pikachu
    def test_purchased_one_pikachu(self):
        # add a pikachu to the cart
        self.shop.add_to_cart(1)
        # buy
        actual = self.shop.purchase_poke()
        self.assertEqual(actual, 6)

    def test_purchased_two_pikachu(self):
        self.shop.add_to_cart(1)
        self.shop.add_to_cart(1)
        actual = self.shop.purchase_poke()
        self.assertEqual(actual, 12)

    def test_purchased_one_pikachu_and_squirtle(self):
        self.shop.add_to_cart(1) #pikachu
        self.shop.add_to_cart(2) #squirtle
        actual = self.shop.purchase_poke()
        self.assertEqual(actual, 9.90)

    def test_purchased_two_pikachu_and_two_squirtle(self):
        self.shop.add_to_cart(1) #pikachu
        self.shop.add_to_cart(1) #pikachu
        self.shop.add_to_cart(2) #squirtle
        self.shop.add_to_cart(2) #squirtle
        actual = self.shop.purchase_poke()
        self.assertEqual(actual, 19.80)

    def test_purchased_three_pikachu_and_three_squirtle(self):
        self.shop.add_to_cart(1) #pikachu
        self.shop.add_to_cart(1) #pikachu
        self.shop.add_to_cart(1) #pikachu
        self.shop.add_to_cart(2) #squirtle
        self.shop.add_to_cart(2) #squirtle
        self.shop.add_to_cart(2) #squirtle
        actual = self.shop.purchase_poke()
        self.assertEqual(actual, 29.70)

    def test_purchased_two_pikachu_and_one_squirtle(self):
        self.shop.add_to_cart(1) #pikachu
        self.shop.add_to_cart(1) #pikachu
        self.shop.add_to_cart(2) #squirtle
        actual = self.shop.purchase_poke()
        self.assertEqual(actual, 15.90)

    def test_purchased_three_pokemon(self):
        self.shop.add_to_cart(1) #pikachu
        self.shop.add_to_cart(2) #squirtle
        self.shop.add_to_cart(3) #charmander
        actual = self.shop.purchase_poke()
        self.assertEqual(actual, 12.80)

    def test_purchased_two_pikachu_one_squirtle_one_charmander(self):
        self.shop.add_to_cart(1) #pikachu
        self.shop.add_to_cart(1) #pikachu
        self.shop.add_to_cart(2) #squirtle
        self.shop.add_to_cart(3) #charmander
        actual = self.shop.purchase_poke()
        self.assertEqual(actual, 18.80)




if __name__ == '__main__':
    unittest.main()
