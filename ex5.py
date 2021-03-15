prices = []
price_string = ''

# Собираем цены в список цен

if not (chose_list := input('Если хотите использовать шаблонный список ничего не вводите: ')):
    prices = [15.0, 20.0, 0.2, 6.45, 0.4, 0.15, 54.0, 2.3, 5.7, 4.0, 4.0]
else:
    print('ВНИМАНИЕ! Введённые значения будут очищены от нецифровых символов и лишних точек!')
    while len(prices) <= 20:
        _price = '0'
        _dot_enabled = True
        if len(prices) < 10:
            string = input(f'Введите цену №{len(prices) + 1}: ')
        else:
            string = input(f'Введите цену №{len(prices) + 1} или не вводите для завершения: ')
            if not string:
                break
        for digit in string:
            if digit.isdigit():
                _price += digit
            elif digit == '.' and _dot_enabled:
                _price += digit
                _dot_enabled = False
        _price = round(float(_price), 2)
        if _price:
            prices.append(_price)

print(f'\nID и содержимое списка:\n{id(prices)} {prices}\n')

print('Задача A:')

for i, price in enumerate(prices):
    _price = str(price).split('.')
    price_string += f'{_price[0]} руб. {_price[1]:0>2} коп.'
    if i + 1 < len(prices):
        price_string += ', '

print(f'Список цен: {price_string}')
print(f'ID и содержимое списка:\n{id(prices)} {prices}\n')

print('Задача B:')

price_string = ''
prices.sort()
for i, price in enumerate(prices):
    _price = str(price).split('.')
    price_string += f'{_price[0]} руб. {_price[1]:0>2} коп.'
    if i + 1 < len(prices):
        price_string += ', '

print(f'Цены по возрастанию: {price_string}')
print(f'ID и содержимое списка:\n{id(prices)} {prices}\n')

print('Задача C:')

price_string = ''
desc_prices = list(sorted(prices, reverse=True))
for i, price in enumerate(desc_prices):
    _price = str(price).split('.')
    price_string += f'{_price[0]} руб. {_price[1]:0>2} коп.'
    if i + 1 < len(desc_prices):
        price_string += ', '

print(f'Цены по убыванию: {price_string}')
print(f'ID и содержимое списка 1:\n{id(prices)} {prices}')
print(f'ID и содержимое списка 2:\n{id(desc_prices)} {desc_prices}\n')

print('Задача D:')

price_string = ''
for i, price in enumerate(sorted(desc_prices)[:5:-1]):
    _price = str(price).split('.')
    price_string += f'{_price[0]} руб. {_price[1]:0>2} коп.'
    if i + 1 < 5:
        price_string += ', '

print(f'5 самых высоких цен: {price_string}')
print(f'ID и содержимое списка 1:\n{id(prices)} {prices}')
print(f'ID и содержимое списка 2:\n{id(desc_prices)} {desc_prices}\n')