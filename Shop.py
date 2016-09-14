import sys
import unittest


class Shop():
    def __init__(self, poke_list, prices, poke_discount):
        """
        :param poke_list: list of available pokemons
        :param prices: prices of each pokemon
        :param poke_discount: discount for pokemons
        :return: nothing
        """
        self.poke_list = poke_list
        self.prices = prices
        self.cart = {}
        self.poke_discount = poke_discount

    def display_poke_products(self):
        """
        Displays available pokemon to customer
        :return: nothing
        """
        print ("id \tnames \tprices")
        for index, value in enumerate(self.poke_list):
            print "%s \t%s \t%s" % (index + 1, value, self.prices[index])
        self.user_input()

    def user_input(self):
        """
        Takes user selection of pokemon as input
        :return: nothing
        """
        selected_option = raw_input("choose your option by id or press 0 to exit ")
        if selected_option == "buy":
            self.purchase_poke()
            return
        elif selected_option == "exit":
            sys.exit(0)

        item_option = int(selected_option)
        if (item_option <= len(self.poke_list)) and item_option >= 0:
            self.add_to_cart(item_option)
        else:
            print "Please choose the correct option "

    def add_to_cart(self, item_option):
        """
        Adds the selected option to cart
        :param item_option: user selected option
        :return: nothing
        """
        pokemon = self.poke_list[item_option - 1]
        if pokemon in self.cart:
            self.cart[pokemon] += 1
        else:
            self.cart[pokemon] = 1
        print "cart: %s" % str(self.cart)

    def purchase_poke(self):
        """
        Purchases the pokemon
        :return: total final price of purchased pokemon
        """
        print "buying in progress"
        poke_sets = self.create_pokesets()
        total_pokesets_discounted_price = self.get_total_pokesets_discounted_price(poke_sets)
        without_discount_price = self.get_nondiscounted_price()
        self.cart = {}
        total_final_price = total_pokesets_discounted_price + without_discount_price
        print "The total price is: $%s" %(round(total_final_price,2))
        return round(total_final_price, 2)

    def cal_pokeset_discounted_price(self, poke_set):
        """
        Calculates the discounted price for pokemon set
        :param poke_set: a unique set of pokemons
        :return: discounted price of pokemon set
        """
        length_of_pokeset = len(poke_set)
        discount = self.poke_discount[length_of_pokeset]
        poke_set_price = self.get_pokemon_set_price(poke_set)
        discounted_price = poke_set_price * (1 - (discount / 100.0))
        return round(discounted_price, 2)

    def get_nondiscounted_price(self):
        """
        Calculates the non discounted price and returns it
        :return: total non discounted price of pokemon in cart
        """
        try:
            poke_name = self.cart.keys()[0]
            poke_count = self.cart.get(poke_name)
            total_non_discounted_price = self.get_pokemon_price(poke_name) * poke_count
            return total_non_discounted_price
        except IndexError:
            return 0

    def create_pokesets(self):
        """
        Creates unique pokemon sets
        :return: unique poke set
        """
        unique_poke_set = []
        while len(self.cart) > 1:
            temp_set = []
            del_list = []
            for key, value in self.cart.iteritems():
                temp_set.append(key)
                self.cart[key] = value - 1
                if self.cart[key] == 0:
                    del_list.append(key)
            for item in del_list:
                del self.cart[item]
            unique_poke_set.append(temp_set)
        return unique_poke_set

    def get_pokemon_price(self, poke_name):
        """
        Returns the selected pokemon price
        :param poke_name: is a name of pokemon
        :return: pokemon price of each pokemon
        """
        if poke_name in self.poke_list:
            index = self.poke_list.index(poke_name)
            poke_price = self.prices[index]
            return poke_price

    def get_pokemon_set_price(self, poke_set):
        """
        Returns unique pokemon set price
        :param poke_set: a (list)set of unique pokemon
        :return: total price of pokemon set
        """
        poke_set_price = 0
        for pokemon in poke_set:
            pokemon_price = self.get_pokemon_price(pokemon)
            poke_set_price = poke_set_price + pokemon_price

        return poke_set_price

    def get_total_pokesets_discounted_price(self, poke_sets):
        """
        Calculates discounted price of individual pokemon set
        :param poke_sets: a list of unique pokemon sets
        :return: total discounted price of pokemon sets
        """
        total_pokesets_discounted_price = 0
        for poke_set in poke_sets:
            discounted_price_poke_set = self.cal_pokeset_discounted_price(poke_set)
            total_pokesets_discounted_price = total_pokesets_discounted_price + discounted_price_poke_set
        return total_pokesets_discounted_price


def main():
    poke_list = ["Pikachu", "Squirtle", "Charmander"]
    prices = [6, 5, 5]
    poke_discount = {1: 0, 2: 10, 3: 20, 4: 40}
    shop = Shop(poke_list, prices, poke_discount)
    while True:
        shop.display_poke_products()


if __name__ == "__main__":
    main()
