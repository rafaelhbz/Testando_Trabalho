# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:34:40 2019

@author: RafaelzZ
"""

import random
import math

baralho_jogado = {}

valor = 0
    
sorteio = str(random.choice(chaves))
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
        sorteio = str(random.choice(chaves))
        
        if sorteio == "Ás":
            numero_As == numero_As - 1
        elif sorteio == "Dois":
            numero_Dois = numero_Dois - 1
        elif sorteio == "Três":
            numero_Tres = numero_Tres - 1
        elif sorteio == "Quatro":
            numero_Quatro = numero_Quatro - 1
        elif sorteio == "Cinco":
            numero_Cinco = numero_Cinco - 1
        elif sorteio == "Seis":
            numero_Seis = numero_Seis - 1
        elif sorteio == "Sete":
            numero_Sete = numero_Sete - 1
        elif sorteio == "Oito":
            numero_Oito = numero_Oito - 1
        elif sorteio == "Nove":
            numero_Nove = numero_Nove - 1
        elif sorteio == "Dez":
            numero_Dez = numero_Dez - 1
        elif sorteio == "Valete":
            numero_Valete = numero_Valete - 1
        elif sorteio == "Dama":
            numero_Dama = numero_Dama - 1
        elif sorteio == "Rei":
            numero_Rei = numero_Rei - 1
            
        primeira_rodada = primeira_rodada + 1
    
    sorteio_local = str(random.choice(chaves))
    deseja_retirar = str(input("Você quer retirar mais uma carta? "))
    
    while deseja_retirar == "Sim" or deseja_retirar == "sim":
        if numero_As == 0:
            del chaves[0]
        if numero_Dois == 0:
            del chaves[1]
        if numero_Tres == 0:
            del chaves[2]
        if numero_Quatro == 0:
            del chaves[3]
        if numero_Cinco == 0:
            del chaves[4]
        if numero_Seis == 0:
            del chaves[5]
        if numero_Sete == 0:
            del chaves[6]
        if numero_Oito == 0:
            del chaves[7]
        if numero_Nove == 0:
            del chaves[8]
        if numero_Dez == 0:
            del chaves[9]
        if numero_Valete == 0:
            del chaves[10]
        if numero_Dama == 0:
            del chaves[11]
        if numero_Rei == 0:
            del chaves[12]
            
        sorteio_local
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
        deseja_retirar = str(input("Você quer retirar mais uma carta? "))
        
    else:
        print("Ok, você decidiu parar aqui. Então vamos analisar seus pontos!")
        
    lista_numeros = [numero_As, numero_Dois, numero_Tres, numero_Quatro, numero_Cinco, numero_Seis, numero_Sete, numero_Oito, numero_Nove, numero_Dez, numero_Valete, numero_Dama, numero_Rei]
    print(lista_numeros)
    print(chaves)
    return lista_numeros

retirar_carta()        
#i = 0
#while i < len(lista_numeros):
    #for a in chaves:
        #baralho_jogado[a] = lista_numeros[i]
    #i = i + 1
    
