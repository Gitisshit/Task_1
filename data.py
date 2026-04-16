class Bun:
    correct_bun_name = 'Флюорисцентная булка'
    invalid_bun_names = [1, 1.1, ['test_name'], {'test_name1': 'test'}, ('test_name2', 'test_name3'), None]
    empty_bun_names = ['', '    ']
    correct_price = 100.00
    invalid_prices_type = [1, ['test_price'], {'test_price1': 'test'}, ('test_price2', 'test_price3'), None, 'test_price4']
    zero_below_zero_prices = [0.0, -0.0, -1.0]