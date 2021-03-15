list_one = ['В', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

string = ''
i = 0
while i < len(list_one):
    str_1 = ''
    if list_one[i][0] == '+' or list_one[i][0] == '-':
        str_1 = list_one[i][0]
        list_one[i] = list_one[i][1:]

    elif list_one[i].isdigit():
            list_one[i] = f'{str_1}{list_one[i]:0>2}'
            list_one.insert(i + 1, '"')
            list_one.insert(i, '"')
            string = f"{string}{''.join(list_one[i:i + 3])} "
            i += 3
    else:
            list_one[i] = f'{str_1}{list_one[i]}'
            string = f'{string}{list_one[i]} '
            i += 1

    print(id(list_one), list_one)
    print(string)

