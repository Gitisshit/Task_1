import data
import pytest

from conftest import valid_ingredient_parametrized
from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_price_valid_price(self, valid_ingredient):
        ingredient = valid_ingredient
        assert ingredient.get_price() == data.Ingredient.valid_price

    @pytest.mark.parametrize("invalid_price_type", data.Ingredient.invalid_price_types)
    def test_get_price_invalid_price_error(self, invalid_price_type):
        ingredient = Ingredient(data.Ingredient.valid_ingredient_types[0], data.Ingredient.valid_ingredient_name, invalid_price_type)
        assert isinstance(ingredient.get_price(), float), \
            f'Класс Ingredient.get_price() принял невалидный тип данных {type(invalid_price_type)}. Ожидалась TypeError'

    @pytest.mark.parametrize("zero_below_zero_price", data.Ingredient.zero_below_zero_prices)
    def test_get_price_zero_and_below_zero_price_error(self, zero_below_zero_price):
        ingredient = Ingredient(data.Ingredient.valid_ingredient_types[0], data.Ingredient.valid_ingredient_name, zero_below_zero_price)
        assert ingredient.get_price() > 0.0, \
            f'Класс Ingredient.get_price() принял нулевое или отрицательное значение. Ожидалась ValueError'

    def test_get_name_valid_name(self, valid_ingredient):
        ingredient = valid_ingredient
        assert ingredient.get_name() == data.Ingredient.valid_ingredient_name

    @pytest.mark.parametrize("invalid_ingredient_name", data.Ingredient.invalid_ingredient_names)
    def test_get_name_invalid_name(self, invalid_ingredient_name):
        ingredient = Ingredient(data.Ingredient.valid_ingredient_types[0], invalid_ingredient_name, data.Ingredient.valid_price)
        assert isinstance(ingredient.get_name(), str), \
            f'Класс Ingredient.get_name() принял невалидный тип данных {type(invalid_ingredient_name)}. Ожидалась TypeError'

    @pytest.mark.parametrize("empty_ingredient_name", data.Ingredient.empty_ingredient_names)
    def test_get_name_empty_name_error(self, empty_ingredient_name):
        ingredient = Ingredient(data.Ingredient.valid_ingredient_types[0], empty_ingredient_name.strip(), data.Ingredient.valid_price)
        assert len(ingredient.get_name()) > 0, f'Класс Ingredient.get_name() принял пустую строку. Ожидалась ValueError'

    @pytest.mark.parametrize('valid_ingredient_parametrized', data.Ingredient.valid_ingredient_types, indirect=True)
    def test_get_type_valid_type(self, valid_ingredient_parametrized):
        ingredient = valid_ingredient_parametrized
        assert ingredient.get_type() in data.Ingredient.valid_ingredient_types

    def test_get_type_valid_type_error(self):
        ingredient = Ingredient(data.Ingredient.invalid_ingredient_type, data.Ingredient.valid_ingredient_name, data.Ingredient.valid_price)
        assert ingredient.get_type() in data.Ingredient.valid_ingredient_types, \
            f'Класс Ingredient.get_type() принял значение, отсутствующее в списке. Ожидалась ValueError'