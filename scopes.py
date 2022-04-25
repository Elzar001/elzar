# Области видимости и пространство имен

# Области видимости:
# 1. Built - ins(Встроенная) - print, len, max, int ...
# 2. Global(Глобальная)
# 3. Enclosed (Нелокальная, nonlocal)
# 4. Local(Локальная)

# оператор global -> позволяет менять значение глобальной переменной, 
# находясь в локальной области видимости. Нужен для неизменяемых типов данных

# nonlocal -> позволяет менять значение нелокальной переменной находясь в локальной области.  


# a = 10 # Global
# print # Built - ins
# def hello(): # Global
#     global a
#     print(a)
#     a = 'hello world' # Local
#     print(a, 'local inside function')

# hello()
# print(a, 'global')

# print(dir(__builtins__))


# x = 'Global'
# print(x, '1')
# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')

# enclosed()
# print(x, '5')

# local -> enclosed -> global -> built-ins (LEGB) 
# *** enclosed - появляется в определенных случаях


# a = 10 # global
# def encklosed():
#     # Started enclosed scope

#     def local():
#         # Started locak scope
#         # End local scope
    
#     # End enclosed scope

# print(a)


# def my_func(a, b):
#     global c
#     a, b = b, a
#     c = 'hello world' # так делать не рекомендуется!!
#     d = 'John'
#     print({'a':a, 'b':b, 'c':c, 'd':d}, 'Local scope!!')

# a = 1
# b = 10
# c = 'c is global'
# d = 'Snow'
# my_func(a,b)
# print({'a':a, 'b':b, 'c':c, 'd':d}, 'Global scope!!')


# def counter():
#     num = 0
#     def incrementer():
#         nonlocal num
#         num += 1
#         return num
#     return incrementer

# c = counter()
# print(c)
# print(c())
# print(c())
# print(c())
# c = counter()
# print(c())

# print('\n\n\n\n\n\n\n')
# print(globals())
# print('\n\n\n\n\n\n\n')
# print(locals())

#---------------------------------------------------
# TASKS

# ls = [[1,2,3], [3,3,5], [5,6,5]]
# ls1 = max([sum(x) for x in ls])
# print(ls1)

# dict1 = {
#     'John': {'history': 99, 'fizik': 95, 'literature': 91}, 
#     'Jerry': {'history': 92, 'math': 96, 'literature': 81},
#     'Larry': {'history': 84, 'math': 85, 'literature': 87},
# }

# new_dict = {inner_key: other_key for inner_key, 
# inner_value in dict1.items() for other_key in inner_value.keys()
# if max(inner_value.values()) == inner_value[other_key]}

# print(new_dict)

# new_dict = {key: max(value, key = value.get) for key, value in dict1.items()}

# print(new_dict)




# a = [4, 15, 38]
# b = [5, 10, 50]

# cb = 0
# ca = 0
# res = []

# for x in range(0,3):
#     if a[x] > b[1]:
#         ca += 1
#     elif b[1] > a[x]:
#         cb += 1


# print(res)

# def compareTriplets(a, b):
#     bob = 0
#     alice = 0
#     for i in range(0,3):
#         if a[i] > b[1]:
#             alice += 1
#         elif b[i] > a[i]:
#             bob += 1
#         else:
#             pass
#     return [alice, bob]

# a = [4, 15, 38]
# b = [5, 10, 50]

# print(compareTriplets(a,b))


# a = 'pythonist'
# dict_ = {x: a.count(x) for x in a}
# print(dict_)




# balance = 0

# def get_salary(amount):
#     global balance
#     balance = balance + amount

#     def pay_bills(amount, log_name):
#         balance = balance - amount, 'Вы потратили {amount} сомов на {log_name}'
#         pay_bills(amount, log_name)

# amount = 10000
# log_name = 'Кабельное тв'
# get_salary(amount)
# print(balance)


