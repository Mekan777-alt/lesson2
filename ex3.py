name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(f'\nID и содержимое исходного списка:\n{id(name)} {name}')



for member in name:
    name = member.split()[-1].title()
    print(f'Привет, {name}!')

print(f'\nID и содержимое списка:\n{id(name)} {name}')




