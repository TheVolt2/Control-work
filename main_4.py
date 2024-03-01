import numpy as np
from matplotlib import pyplot as plt

# Задаем индексы для каждой категории
index = np.arange(5)

# Значения FPS для каждой категории
Intel = [145, 120, 180, 150, 210]
Nvidia = [180, 140, 200, 170, 230]
AMD = [160, 130, 190, 160, 220]

bw = 0.3  # Ширина каждого столбца

# Задаем пределы осей
plt.axis([0, 5, 0, 300])

# Заголовок диаграммы
plt.title('Тест FPS в играх', fontsize=20)

# Создаем столбчатую диаграмму для каждой категории, смещая каждую влево на 0.3, чтобы они не перекрывали друг друга
plt.bar(index, Intel, bw, color='b')
plt.bar(index + bw, Nvidia, bw, color='g')
plt.bar(index + 2 * bw, AMD, bw, color='r')

# Устанавливаем подписи для оси X
plt.xticks(index + 1.5 * bw, ['Cyberpunk', 'RDR 2', 'CS 2', 'Doom', 'GTA 5'])

plt.show()  # Отображаем диаграмму