filename = 'guest_book.txt'

while True:
    guest_name = input('Здравствуйте, введите ваше имя. '
                       'Для выхода введите "q": ')
    if guest_name == 'q':
        break
    print(f"{guest_name}, добро пожаловать!")
    with open(filename, 'a', encoding='UTF-8') as file_object:
        file_object.write(guest_name + '\n')