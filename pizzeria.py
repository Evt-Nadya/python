d = {}
d['name'] = input("Введите имя: ")
d['password'] = input("Введите пароль: ")
print("Наше меню")
f = open('пиццы.txt')
print(f.read())
f.close()
f = open('напитки.txt')
print(f.read())
f.close()
f = open('закуски.txt')
print(f.read())
f.close()
if d['name'] == 'Администратор' and d['password'] == 'admin':
    print("Хотите расширить меню? Да/Нет")
    choice = input()
    if choice == 'Да':
        print("Пицца/Напиток/Закуска")
        choice = input()
        if choice == 'Пицца':
            pizza = input("Добавить пиццу: ")
            f = open("пиццы.txt", 'a')
            f.write('\n' + pizza)
            f.close()
        if choice == 'Напиток':
            drink = input("Добавить напиток: ")
            f = open("напитки.txt", 'a')
            f.write('\n' + drink)
            f.close()
        if choice == 'Закуска':
            snack = input("Добавить закуску: ")
            f = open("закуски.txt", 'a')
            f.write('\n' + snack)
            f.close()
if d['name'] == 'Пользователь' and d['password'] == 'user':
    name = input("Введите ваше имя: ")
    order = input("Введите ваш заказ: ")
    f = open(name, 'w')
    f.write(order)
    f.close()
    f = open("пиццы.txt")
    text = f.read()
    f.close()
    c = text.count(order)
    while c > 0:
        print(order)
        c -= 1
    f = open("напитки.txt")
    text = f.read()
    f.close()
    c = text.count(order)
    while c > 0:
        print(order)
        c -= 1
    f = open("закуски.txt")
    text = f.read()
    f.close()
    c = text.count(order)
    while c > 0:
        print(order)
        c -= 1