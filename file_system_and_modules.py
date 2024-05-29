# first_task
import json

with open('purchase_log.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    purchases = {}

    for line in lines:
        data = json.loads(line)
        purchases[data["user_id"]] = data["category"]
print(purchases)

# second_task

purchase_dict = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as purchase_file:
    for line in purchase_file:
        purchase = json.loads(line.strip())
        user_id = purchase['user_id']
        category = purchase['category']
        purchase_dict[user_id] = category

with open('visit_log.csv', 'r', encoding='utf-8') as visit_file, \
        open('funnel.csv', 'w', encoding='utf-8') as funnel_file:

    for line in visit_file:
        user_id, source = line.strip().split(',')

        # Проверка, есть ли user_id в словаре покупок
        if user_id in purchase_dict:
            category = purchase_dict[user_id]
            funnel_file.write(f'{user_id},{source},{category}\n')
