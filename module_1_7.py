from itertools import count

grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5],] # исходные данные оценки
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'} # исходные данные имена
check=len(grades)-len(students) # проверка корректноси исходных данных
if check != 0:
    print('Исходные данные некорректны, количество студентов: ',len(students), ', а количество сводок успеваемости: ',len(grades)) # вывод сообщения об ошибке в исходных данных
else:
    number_of_students=len(students) # создаем переменную "кол0во Студентов"
students_list=list(students) # создаем список студениов из множества
sorted_students_list=sorted(students_list) # упорядочиваем сисок студентов по алфавиту
average_score=dict({}) # создаем пустой словарь "средний балл"
count = 0 # создаем счетчик
while count < number_of_students: # запускаем цикл по условию, что счетчик должен быть меньше кол-ва студентов
    average_score[count]={sorted_students_list[count]:grades[count]} # наполняем пустой словарь парами из списков "упорядоченные студенты" и "успеваемость"
    count=count+1 # инкрементируем счетчик
print(average_score) # выводим новый словарь на экран