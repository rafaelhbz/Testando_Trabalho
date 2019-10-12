# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:30:37 2019

@author: RafaelzZ
"""

numero_baralhos = int(input('Digite o numero de baralhos que seráo utilizados: '))

baralho = { "Ás" : 4, "Dois" : 4, "Três" : 4, "Quatro" : 4, "Cinco" : 4, "Seis" : 4, "Sete" : 4, "Oito" : 4, "Nove" : 4,
           "Dez" : 4, "Valete" : 4, "Dama" : 4, "Rei" : 4 }


cartas = []
numero = []

for key in baralho.keys():
    cartas.append(key)
    
for values in baralho.values():
    numero.append(values)
    

baralho_novo = {}

i = 0
while i < len(cartas):
    baralho_novo[cartas[i]] = 4 * numero_baralhos
    i+=1
    
print(baralho_novo)

lista = ["fandangos_de_presunto"]
    

    