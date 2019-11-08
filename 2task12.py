words = input('Введите текст: ')
search = input('Введите слово: ')
length = len(words)

print(words.count(search, 0, length))