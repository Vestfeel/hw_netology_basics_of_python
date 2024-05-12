# first_task
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

setlist = []

for i in ids.values():
    setlist += i

print(set(setlist))

# second_task
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

base = []
for i in queries:
    base.append(len(i.split()))
sbase = list(set(base))
for i in range(len(sbase)):
    print(
        f' Поисковых запросов, содержащих {sbase[i]} слов(а): {round(base.count(sbase[i]) / len(base) * 100, 2)}%')

# third_task
results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}


for companies in results:
    results[companies]['ROI'] = round(
        ((results[companies]['revenue'] / results[companies]['cost']) - 1) * 100, 2)
print(results)

# fourth_task
stats = {'facebook': 55, 'yandex': 115, 'vk': 120,
         'google': 99, 'email': 42, 'ok': 98}

max_stat_int = 0
max_stat_str = ''

for i in stats:
    if stats[i] > max_stat_int:
        max_stat_int = stats[i]
        max_stat_str = i
print(f'Максимальный объем продаж на рекламном канале: {max_stat_str}')
