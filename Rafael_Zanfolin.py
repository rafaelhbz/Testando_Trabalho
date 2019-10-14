# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:34:40 2019

@author: RafaelzZ
"""

import random
import math

baralho_jogado = {}

valor = 0

#if baralho_jogado[sorteio] == 0:
    #del baralho_jogado[sorteio]
    #print("Deu ruim")
    
def retirar_carta():
    
    baralho = { "Ás" : 4, "Dois" : 4, "Três" : 4, "Quatro" : 4, "Cinco" : 4, "Seis" : 4, "Sete" : 4, "Oito" : 4, "Nove" : 4,
           "Dez" : 4, "Valete" : 4, "Dama" : 4, "Rei" : 4 }

    chaves = []
    valores = []

    for keys in baralho.keys():
        chaves.append(keys)
    
    for values in baralho.values():
        valores.append(values)
    
    numero_As = 4
    numero_Dois = 4
    numero_Tres = 4
    numero_Quatro = 4
    numero_Cinco = 4
    numero_Seis = 4
    numero_Sete = 4
    numero_Oito = 4
    numero_Nove = 4
    numero_Dez = 4
    numero_Valete = 4
    numero_Dama = 4
    numero_Rei = 4
    
    # Aqui é iniciada a primera rodada
    primeira_rodada = 0
    while primeira_rodada < 2:   
        sorteio_local = str(random.choice(list(baralho.keys())))
        
        if sorteio_local == "Ás":
            if numero_As == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Dois":
            if numero_Dois == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Três":
            if numero_Tres == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Quatro":
            if numero_Quatro == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Cinco":
            if numero_Cinco == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Seis":
            if numero_Seis == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Sete":
            if numero_Sete == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Oito":
            if numero_Oito == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Nove":
            if numero_Nove == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Dez":
            if numero_Dez == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Valete":
            if numero_Valete == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Dama":
            if numero_Dama == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Rei":
            if numero_Rei == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        
        if sorteio_local == "Ás":
            numero_As = numero_As - 1
        if sorteio_local == "Dois":
            numero_Dois = numero_Dois - 1
        if sorteio_local == "Três":
            numero_Tres = numero_Tres - 1
        if sorteio_local == "Quatro":
            numero_Quatro = numero_Quatro - 1
        if sorteio_local == "Cinco":
            numero_Cinco = numero_Cinco - 1
        if sorteio_local == "Seis":
            numero_Seis = numero_Seis - 1
        if sorteio_local == "Sete":
            numero_Sete = numero_Sete - 1
        if sorteio_local == "Oito":
            numero_Oito = numero_Oito - 1
        if sorteio_local == "Nove":
            numero_Nove = numero_Nove - 1
        if sorteio_local == "Dez":
            numero_Dez = numero_Dez - 1
        if sorteio_local == "Valete":
            numero_Valete = numero_Valete - 1
        if sorteio_local == "Dama":
            numero_Dama = numero_Dama - 1
        if sorteio_local == "Rei":
            numero_Rei = numero_Rei - 1
            
        primeira_rodada = primeira_rodada + 1
    
    deseja_retirar = str(input("Você quer retirar mais uma carta? "))
    
    while deseja_retirar == "Sim" or deseja_retirar == "sim":
        deseja_retirar = str(input("Você quer retirar mais uma carta? "))
        lista_numeros = [numero_As, numero_Dois, numero_Tres, numero_Quatro, numero_Cinco, numero_Seis, numero_Sete, numero_Oito, numero_Nove, numero_Dez, numero_Valete, numero_Dama, numero_Rei]
        sorteio_local = str(random.choice(list(baralho.keys())))
            
        if sorteio_local == "Ás":
            if numero_As == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Dois":
            if numero_Dois == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Três":
            if numero_Tres == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Quatro":
            if numero_Quatro == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Cinco":
            if numero_Cinco == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Seis":
            if numero_Seis == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Sete":
            if numero_Sete == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Oito":
            if numero_Oito == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Nove":
            if numero_Nove == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Dez":
            if numero_Dez == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Valete":
            if numero_Valete == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Dama":
            if numero_Dama == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
        if sorteio_local == "Rei":
            if numero_Rei == 0:
                sorteio_local = str(random.choice(list(baralho.keys())))
            
        if numero_As == 0:
            if baralho["Ás"] in baralho:
                del baralho["Ás"]
        if numero_Dois == 0:
            if baralho["Dois"] in baralho:
                del baralho["Dois"]
        if numero_Tres == 0:
            if baralho["Três"] in baralho:
                del baralho["Três"]
        if numero_Quatro == 0:
            if baralho["Quatro"] in baralho:
                del baralho["Quatro"]
        if numero_Cinco == 0:
            if baralho["Cinco"] in baralho:
                del baralho["Cinco"]
        if numero_Seis == 0:
           if baralho["Seis"] in baralho:
                del baralho["Seis"]
        if numero_Sete == 0:
            if baralho["Sete"] in baralho:
                del baralho["Sete"]
        if numero_Oito == 0:
            if baralho["Oito"] in baralho:
                del baralho["Oito"]
        if numero_Nove == 0:
            if baralho["Nove"] in baralho:
                del baralho["Nove"]
        if numero_Dez == 0:
            if baralho["Dez"] in baralho:
                del baralho["Dez"]
        if numero_Valete == 0:
            if baralho["Valete"] in baralho:
                del baralho["Valete"]
        if numero_Dama == 0:
            if baralho["Dama"] in baralho:
                del baralho["Dama"]
        if numero_Rei == 0:
            if baralho["Rei"] in baralho:
                del baralho["Rei"]
                
            
        if numero_As > 0:
            if sorteio_local == "Ás":
                numero_As = numero_As - 1
        if numero_Dois > 0:
            if sorteio_local == "Dois":
                numero_Dois = numero_Dois - 1
        if numero_Tres > 0:
            if sorteio_local == "Três":
                numero_Tres = numero_Tres - 1
        if numero_Quatro > 0:
            if sorteio_local == "Quatro":
                numero_Quatro = numero_Quatro - 1
        if numero_Cinco > 0:
            if sorteio_local == "Cinco":
                numero_Cinco = numero_Cinco - 1
        if numero_Seis > 0:
            if sorteio_local == "Seis":
                numero_Seis = numero_Seis - 1
        if numero_Sete > 0:
            if sorteio_local == "Sete":
                numero_Sete = numero_Sete - 1
        if numero_Oito > 0:
            if sorteio_local == "Oito":
                numero_Oito = numero_Oito - 1
        if numero_Nove > 0:
            if sorteio_local == "Nove":
                numero_Nove = numero_Nove - 1
        if numero_Dez > 0:
            if sorteio_local == "Dez":
                numero_Dez = numero_Dez - 1
        if numero_Valete > 0:
            if sorteio_local == "Valete":
                numero_Valete = numero_Valete - 1
        if numero_Dama > 0:
            if sorteio_local == "Dama":
                numero_Dama = numero_Dama - 1
        if numero_Rei > 0:
            if sorteio_local == "Rei":
                numero_Rei = numero_Rei - 1
        
        print(baralho)
        print(lista_numeros)
    else:
        print("Ok, você decidiu parar aqui. Então vamos analisar seus pontos!")
        
    lista_numeros = [numero_As, numero_Dois, numero_Tres, numero_Quatro, numero_Cinco, numero_Seis, numero_Sete, numero_Oito, numero_Nove, numero_Dez, numero_Valete, numero_Dama, numero_Rei]
    print(lista_numeros)
    return lista_numeros

retirar_carta()        
#i = 0
#while i < len(lista_numeros):
    #for a in chaves:
        #baralho_jogado[a] = lista_numeros[i]
    #i = i + 1
    
