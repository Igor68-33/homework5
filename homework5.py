# Неизменяемые и изменяемые объекты. Кортежи
immutable_var = (1, [11, 22], 'String1', True, 2.5)
print('Immutable tuple: ', immutable_var)
#  Кортежи значения не изменяют.
# immutable_var[1] = 100        # будет сообщение об ощибке
immutable_var[1][0] = 33  # допустимо изменить только список
print('Immutable tuple: ', immutable_var)

# Создание изменяемых структур данных
mutable_list = [1, 2, 3, True]  # список с разными типами
mutable_list = mutable_list + [5, 7, 9, True]  # в конец добавили 4 элемента списка
print('Mutable list: ', mutable_list)
mutable_list[1] = mutable_list[1] + 10  # увеличили элемент списка 1 на 10
mutable_list[len(mutable_list) - 1] = False  # последний элемент списка будет False
mutable_list.remove(9)  # удалили элемент со значением 9
mutable_list.append('Finis') # добавили элемент в конец "Finis"
print('Mutable list: ', mutable_list)
