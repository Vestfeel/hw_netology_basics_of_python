#first_task
import re

def acronym(some_words):
    return ''.join(word[0].upper() for word in some_words.split())

print(acronym('Информационные технологии'))
print(acronym('Near Field Communication'))

#second_task
import re

emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']

def counting(emails: list) -> dict:
    dic = {}
    for email in emails:
        domain = re.findall(r'@(\w+\.\w+)', email)[0]
        dic[domain] = dic.get(domain, 0) + 1
    return dic

for k, v in counting(emails).items():
    print(k, v)

#third_task
