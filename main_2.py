import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# Генерируем равномерно распределенные значения времени от 0 до 20
t = np.linspace(0, 20, 100)

# Генерируем значения x, y, z для анимации
x = np.sin(np.pi/5 * t)
y = np.sin(np.pi/3 * t)
z = np.linspace(0, 100, 100)

# Создаем массив с данными
dataSet = np.array([x, y, z])
numDataPoints = len(t)  # Количество временных точек

# Функция для анимации
def animate_func(num):
    ax.clear()  # Очистка осей

    # Построение траектории в 3D и добавление точек
    ax.plot3D(dataSet[0, :num+1], dataSet[1, :num+1], dataSet[2, :num+1], c='blue')
    ax.scatter(dataSet[0, num], dataSet[1, num], dataSet[2, num], c='blue', marker='o')

    # Установка пределов осей
    ax.set_xlim3d([-1, 1])
    ax.set_ylim3d([-1, 1])
    ax.set_zlim3d([0, 100])

    # Установка заголовка и меток осей
    ax.set_title('Траектория \nВремя = ' + str(np.round(t[num], decimals=2)) + ' сек')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

# Создаем фигуру и оси 3D
fig = plt.figure()
ax = plt.axes(projection='3d')

# Создаем анимацию с помощью функции animate_func
line_ani = animation.FuncAnimation(fig, animate_func, interval=100, frames=numDataPoints)

plt.show()  # Отображаем анимацию
