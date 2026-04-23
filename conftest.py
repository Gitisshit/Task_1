import pytest
import data
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


@pytest.fixture
def valid_bun():
    return Bun(data.Bun.valid_bun_name, data.Bun.valid_price)

@pytest.fixture
def valid_ingredient():
    return Ingredient(data.Ingredient.valid_ingredient_types[0], data.Ingredient.valid_ingredient_name, data.Ingredient.valid_price)

@pytest.fixture
def second_valid_ingredient():
    return Ingredient(data.Ingredient.valid_ingredient_types[1], data.Ingredient.valid_ingredient_name_2, data.Ingredient.valid_price)

@pytest.fixture
def valid_ingredient_parametrized(request):
    return Ingredient(request.param, data.Ingredient.valid_ingredient_name, data.Ingredient.valid_price)

@pytest.fixture
def add_multiple_ingredients(valid_ingredient, second_valid_ingredient):
    burger = Burger()
    burger.add_ingredient(valid_ingredient)
    burger.add_ingredient(second_valid_ingredient)
    return burger

@pytest.fixture
def assembled_burger(valid_bun, valid_ingredient, second_valid_ingredient):
    burger = Burger()
    burger.set_buns(valid_bun)
    burger.add_ingredient(valid_ingredient)
    burger.add_ingredient(second_valid_ingredient)
    return burger
