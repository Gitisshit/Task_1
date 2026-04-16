import pytest
from praktikum.bun import Bun
import data


class TestBun:

    def test_get_bun_name_return_correct_name(self):
        bun = Bun(data.Bun.correct_bun_name, data.Bun.correct_price)
        assert bun.get_name() == data.Bun.correct_bun_name

    @pytest.mark.parametrize("not_str_bun_name", data.Bun.invalid_bun_names)
    def test_get_bun_name_invalid_name_error(self, not_str_bun_name):
        bun = Bun(not_str_bun_name, data.Bun.correct_price)
        assert isinstance(bun.get_name(), str), f'Класс Bun.get_name() принял невалидный тип данных {type(not_str_bun_name)}. Ожидалась TypeError'

    @pytest.mark.parametrize("empty_bun_name", data.Bun.empty_bun_names)
    def test_get_bun_name_empty_name_error(self, empty_bun_name):
        bun = Bun(empty_bun_name.strip(), data.Bun.correct_price)
        assert len(bun.get_name()) > 0, f'Класс Bun.get_name() принял пустую строку. Ожидалась ValueError'

    def test_get_price_return_correct_price(self):
        bun = Bun(data.Bun.correct_bun_name, data.Bun.correct_price)
        assert bun.get_price() == data.Bun.correct_price

    @pytest.mark.parametrize("invalid_price_type", data.Bun.invalid_prices_type)
    def test_get_price_invalid_price_error(self, invalid_price_type):
        bun = Bun(data.Bun.correct_bun_name, invalid_price_type)
        assert isinstance(bun.get_price(), float), f'Класс Bun.get_price() принял невалидный тип данных {type(invalid_price_type)}. Ожидалась TypeError'

    @pytest.mark.parametrize('zero_below_zero_price',data.Bun.zero_below_zero_prices)
    def test_get_price_zero_and_below_zero_price_error(self, zero_below_zero_price):
        bun = Bun(data.Bun.correct_bun_name, zero_below_zero_price)
        assert bun.get_price() > 0.0, f'Класс Bun.get_price() принял нулевое или отрицательное значение. Ожидалась ValueError'
