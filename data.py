from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Bun:
    valid_bun_name = 'Флюорисцентная булка'
    invalid_bun_names = [1, 1.1, ['test_name'], {'test_name1': 'test'}, ('test_name2', 'test_name3'), None]
    empty_bun_names = ['', '    ']
    valid_price = 100.00
    invalid_price_types = [1, ['test_price'], {'test_price1': 'test'}, ('test_price2', 'test_price3'), None, 'test_price4']
    zero_below_zero_prices = [0.0, -0.0, -1.0]

class Ingredient:
    valid_ingredient_types = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
    valid_price = 100.00
    valid_ingredient_name = 'Соус Spicy-X'
    invalid_price_types = [1, ['test_price'], {'test_price1': 'test'}, ('test_price2', 'test_price3'), None, 'test_price4']
    zero_below_zero_prices = [0.0, -0.0, -1.0]
    invalid_ingredient_names = [1, 1.1, ['test_name'], {'test_name1': 'test'}, ('test_name2', 'test_name3'), None]
    empty_ingredient_names = ['', '    ']
    invalid_ingredient_type = 'test_type'