import matplotlib.pyplot as plt

# Задаем метки для каждого сектора
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

# Задаем размеры (доли) для каждого сектора
sizes = [15, 30, 45, 10]

# Создаем новую фигуру и оси
fig1, ax1 = plt.subplots()

# Создаем круговую диаграмму, используя заданные размеры и метки, и добавляем проценты
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.show()  # Отображаем круговую диаграмму
