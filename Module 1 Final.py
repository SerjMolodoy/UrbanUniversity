grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # Список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # Множество
students_list = sorted(students)  # Отсортировали по алфавиту
print(students_list)
grades_average_list = [(sum(grades[0]) / len(grades[0])),(sum(grades[1]) / len(grades[1])),
                       (sum(grades[2]) / len(grades[2])),(sum(grades[3]) / len(grades[3])),
                       (sum(grades[4]) / len(grades[4])),]  # Посчитали средний балл
print(grades_average_list)
average_grades_student = dict(zip(students_list, grades_average_list))  # сопоставили
print(average_grades_student)
print()
print('Всё!')
