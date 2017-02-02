# -*- coding: utf-8 -*-
"""
AI.Lector.ru

Автор: Р.В. Шамин
"""

# класс, который реализует персептрон и его обучение
class TPerceptron:
    def __init__(self, N):
        
        # создать нулевые веса
        self.w = list()
        for i in range(N):
            self.w.append(0)
            
    # метод для вычисления значения персептрона
    def calc(self, x):
        res = 0

        for i in range(len(self.w)):
            res = res + self.w[i] * x[i]
        return res
    
    # пороговая функция активации персептрона
    def sign(self, x):
        if self.calc(x) > 0:
            return 1
        else:
            return -1
    
    # обучение на одном примере
    def learn(self, la, x, y):
        # обучаем только, когда результат неверный
        if y * self.calc(x) <= 0:
            for i in range(len(self.w)):
                self.w[i] = self.w[i] + la * y * x[i]
                
    # обучение по всем данным T - кортеж примеров
    def learning(self, la, T):
        # цикл обучения 
        for n in range(100):
            # обучение по всем набору примеров
            for t in T:
                self.learn(la, t[0], t[1])