# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:34:40 2019

@author: RafaelzZ
"""

jogo_10começa = 0

dinheiro = int(input("Quanto dinheiro você quer apostar"))

if dinheiro < 0:
    print("Você está maluco?!?")
elif dinheiro == 0:
    print("Vai se fude")
else:
    jogo_começa = True
    
if jogo_começa == True:
    print("O jogo vai começar!")
    
while jogo_começa == True:
    if dinheiro > 0:
        dinheiro = 0
    elif dinheiro == 0:
        jogo_começa = False
