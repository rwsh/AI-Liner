# -*- coding: utf-8 -*-
"""
AI.Lector.ru

Автор: Р.В. Шамин
"""

class TPerceptron:
    def __init__(self, N):
        self.w = list()
        for i in range(N):
            self.w.append(0)
            
    def calc(self, x):
        res = 0

        for i in range(len(self.w)):
            res = res + self.w[i] * x[i]
        return res
        
    def sign(self, x):
        if self.calc(x) > 0:
            return 1
        else:
            return -1
    
    def learn(self, la, x, y):
        if y * self.calc(x) <= 0:
            for i in range(len(self.w)):
                self.w[i] = self.w[i] + la * y * x[i]
                
    def learning(self, la, T):
        for n in range(100):
            for t in T:
                self.learn(la, t[0], t[1])