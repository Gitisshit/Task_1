from praktikum.burger import Burger
from data import Bun


class TestBurger:

    def test_set_bun(self, correct_bun):
        burger = Burger()
        burger.set_buns(correct_bun)
        assert burger.bun == correct_bun
