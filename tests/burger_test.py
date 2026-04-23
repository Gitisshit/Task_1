from praktikum.burger import Burger


class TestBurger:

    def test_set_bun(self, valid_bun):
        burger = Burger()
        burger.set_buns(valid_bun)
        assert burger.bun == valid_bun

    def test_add_ingredient(self, valid_ingredient):
        burger = Burger()
        burger.add_ingredient(valid_ingredient)
        assert burger.ingredients == [valid_ingredient]

    def test_add_multiple_ingredients(self, add_multiple_ingredients, valid_ingredient, second_valid_ingredient):
        burger_ingredients = add_multiple_ingredients
        assert burger_ingredients.ingredients == [valid_ingredient, second_valid_ingredient]

    def test_remove_ingredient(self, add_multiple_ingredients, valid_ingredient, second_valid_ingredient):
        burger_ingredients = add_multiple_ingredients
        burger_ingredients.remove_ingredient(0)
        assert burger_ingredients.ingredients == [second_valid_ingredient]

    def test_move_ingredient(self, add_multiple_ingredients, valid_ingredient, second_valid_ingredient):
        burger_ingredients = add_multiple_ingredients
        burger_ingredients.move_ingredient(0, 1)
        assert burger_ingredients.ingredients == [second_valid_ingredient, valid_ingredient]

    def test_get_price(self, assembled_burger, valid_bun, valid_ingredient, second_valid_ingredient):
        burger = assembled_burger
        assert burger.get_price() == valid_bun.get_price() * 2 + valid_ingredient.get_price() + second_valid_ingredient.get_price()

    def test_get_receipt(self, assembled_burger, valid_bun, valid_ingredient, second_valid_ingredient):
        burger = assembled_burger
        assert valid_bun.get_name() in burger.get_receipt()
        assert valid_ingredient.get_name() in burger.get_receipt()
        assert second_valid_ingredient.get_name() in burger.get_receipt()
        assert str(burger.get_price()) in burger.get_receipt()
