documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

# first_task


def find_owner_by_number(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            return f"Владелец документа: {doc['name']}"
    return "Документ не найден в базе"

# second_task


def find_shelf_by_number(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return f"Документ хранится на полке: {shelf}"
    return "Документ не найден в базе"

# third_task


def list_all_documents():
    result = []
    for doc in documents:
        shelf = find_shelf_by_number(doc['number'])
        result.append(
            f"№: {doc['number']}, тип: {doc['type']}, владелец: {doc['name']}, полка хранения: {shelf.split(': ')[1]}")
    return "\n".join(result)

# fourth_task


def add_shelf(shelf_number):
    if shelf_number in directories:
        return f"Такая полка уже существует. Текущий перечень полок: {', '.join(directories.keys())}."
    directories[shelf_number] = []
    return f"Полка добавлена. Текущий перечень полок: {', '.join(directories.keys())}."

# fifth_task


def delete_shelf(shelf_number):
    if shelf_number not in directories:
        return f"Такой полки не существует. Текущий перечень полок: {', '.join(directories.keys())}."
    if directories[shelf_number]:
        return f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {', '.join(directories.keys())}."
    del directories[shelf_number]
    return f"Полка удалена. Текущий перечень полок: {', '.join(directories.keys())}."


def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'p':
            doc_number = input("Введите номер документа: ")
            print(find_owner_by_number(doc_number))
        elif command == 's':
            doc_number = input("Введите номер документа: ")
            print(find_shelf_by_number(doc_number))
        elif command == 'l':
            print(list_all_documents())
        elif command == 'ads':
            shelf_number = input("Введите номер полки: ")
            print(add_shelf(shelf_number))
        elif command == 'ds':
            shelf_number = input("Введите номер полки: ")
            print(delete_shelf(shelf_number))
        else:
            print("Неизвестная команда. Попробуйте снова.")


main()
