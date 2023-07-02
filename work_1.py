
# Задача №1
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
#
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

def tup_pathfile (text:str) -> tuple:
    tuple_result = text.partition('test')
    return tuple_result

print(tup_pathfile('c:/Users/Vladislav/Desktop/deep_to_python/test.txt'))

# Задача №2
# Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и
# суммой премии в качестве значения. Сумма рассчитывается как ставка
# умноженная на процент премии (решение задачи "не в одну строку" есть на 4 семинаре(5 задача))
names = ['Vlad', 'Den', 'Alex']
cash = [1000, 2000, 3000]
percent = ['10.25%', '15%', '20%']
dict_variable = {name: money / 100 * perc
            for name, money, perc in zip(names, cash, (float(i[:-1]) for i in percent))}
print(dict_variable)

#Задача №3
# Создайте функцию генератор чисел Фибоначчи
def gener_fib(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(gener_fib(int(input('n= ')))))





