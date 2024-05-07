import re
 
some_text = '''
Эталонной реализацией Python является интерпретатор CPython, 
поддерживающий большинство активно используемых платформ. 
Он распространяется под свободной лицензией Python Software Foundation License, 
позволяющей использовать его без ограничений в любых приложениях, включая проприетарные.
'''

def vowel_cons(some_text: str) -> list:
    vowels = len(re.findall(r'\b[aeiouAEIOUауоиэыяюеёАУОИЭЫЯЮЕЁ]', some_text))
    cons = len(re.findall(r'\b[^aeiouAEIOUауоиэыяюеёАУОИЭЫЯЮЕЁ\s\W]', some_text))
    return [vowels, cons]
 
print('Слов на гласные буквы:', vowel_cons(some_text)[0], '\nСлов на согласные буквы:', vowel_cons(some_text)[1])