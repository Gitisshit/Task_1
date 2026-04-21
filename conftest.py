import pytest
import data
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def valid_bun():
    return Bun(data.Bun.valid_bun_name, data.Bun.valid_price)

@pytest.fixture
def valid_ingredient():
    return Ingredient(data.Ingredient.valid_ingredient_types[0], data.Ingredient.valid_ingredient_name, data.Ingredient.valid_price)

@pytest.fixture
def valid_ingredient_parametrized(request):
    return Ingredient(request.param, data.Ingredient.valid_ingredient_name, data.Ingredient.valid_price)