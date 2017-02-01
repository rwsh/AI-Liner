# -*- coding: utf-8 -*-
"""
AI.Lector.ru

Автор: Р.В. Шамин
"""

import TPerceptron



perceptron = TPerceptron.TPerceptron(2)

la = 0.1

T = list()

T.append([[2,1], 1])
T.append([[3,2], 1])
T.append([[4,1], 1])

T.append([[1,2], -1])
T.append([[2,3], -1])
T.append([[5,7], -1])

perceptron.learning(la, T)

print(perceptron.w)

print(perceptron.sign([1.5, 2]))

print(perceptron.sign([3, 1.5]))

print(perceptron.sign([5,1]))

print(perceptron.sign([5,10]))


