#first_task
word = 'testing'
if len(word) % 2 == 0:
    print(word[int(len(word) / 2 - 1): int(len(word) / 2) + 1])
elif len(word) % 2 != 0:
    print(word[int(len(word) / 2)])

#second_task
num = 1
sum = 0

while num != 0:
    num = int(input('Введите число'))
    sum += num
else:
    print(sum)

#third_task
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    print('Идеальные пары:')
    for i in range(len(boys)):
        print(f"{sorted(boys)[i]} и {sorted(girls)[i]}")
else:
    print('Внимание, кто-то может остаться без пары!')

#fourth_task
countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
    ]
#t °С = 5/9 (t °F - 32)
print('Средняя температура в странах:')
for i in range(len(countries_temperature)):
    average = round(5/9 * (sum(countries_temperature[i][1]) - 32 * len(countries_temperature[i][1])) / len(countries_temperature[i][1]), 1)
    print(f"{countries_temperature[i][0]} - {average} C")

#fifth_task
car_ids = ['А222ВС96', 'АБ22ВВ193']
for i in range(len(car_ids)):
    if len(car_ids[i]) == 8:
        if car_ids[i][1:4].isdigit() and car_ids[i][6:].isdigit() and car_ids[i][0].isalpha() and car_ids[i][4:6].isalpha():
            print(f"Номер {car_ids[i]} валиден. Регион {car_ids[i][6:]}")
        else:
            print(f"Номер {car_ids[i]} не валиден")
    elif len(car_ids[i]) == 9:
        if car_ids[i][1:4].isdigit() and car_ids[i][6:].isdigit() and car_ids[i][0].isalpha() and car_ids[i][4:6].isalpha():
            print(f"Номер {car_ids[i]} валиден. Регион {car_ids[i][6:]}")
        else:
            print(f"Номер {car_ids[i]} не валиден")
    else:
        print(f"Номер {car_ids[i]} не валиден")

#sixth_task
