''' Задача 2 Рздел 1
Проверить, упорядочены ли элементы в списке по возрастанию
Пример работы алгоритма:
• входное значение: [5,3,7]
ответ: нет
• входное значение: [5,6,7]
ответ: да'''


list = [5, 6, 7]

for i in range(len(list)-1):
    if list[i] < list[i + 1]:
        answer = "Да"
    else:
        answer = "Нет"
        break

print(answer)
