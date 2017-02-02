# -*- coding: utf-8 -*-
"""
AI.Lector.ru

Автор: Р.В. Шамин
"""

import TPerceptron

# создаем класс двумерного персептрона
perceptron = TPerceptron.TPerceptron(2)

la = 0.1 # константа обучения

# создаем примеры
T = list()

T.append([[2,1], 1])
T.append([[3,2], 1])
T.append([[4,1], 1])

T.append([[1,2], -1])
T.append([[2,3], -1])
T.append([[5,7], -1])

perceptron.learning(la, T) # обучение персептрона

print(perceptron.w) # печатаем веса

# проверим работу на тестовых примерах
print(perceptron.sign([1.5, 2])) 
print(perceptron.sign([3, 1.5]))
print(perceptron.sign([5,1]))
print(perceptron.sign([5,10]))
