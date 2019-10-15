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
    
def retirar_carta(jogador):
    
    baralho = { "Ás" : 4, "Dois" : 4, "Três" : 4, "Quatro" : 4, "Cinco" : 4, "Seis" : 4, "Sete" : 4, "Oito" : 4, "Nove" : 4,
           "Dez" : 4, "Valete" : 4, "Dama" : 4, "Rei" : 4 }

    chaves = []
    valores = []
    
    global pontuação_jogador
    pontuação_jogador = 0
    
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
            if pontuação_jogador < 11:
                pontuação_jogador = pontuação_jogador + 11
            else:
                pontuação_jogador = pontuação_jogador + 1
        if sorteio_local == "Dois":
            numero_Dois = numero_Dois - 1
            pontuação_jogador = pontuação_jogador + 1
        if sorteio_local == "Três":
            numero_Tres = numero_Tres - 1
            pontuação_jogador = pontuação_jogador + 1
        if sorteio_local == "Quatro":
            numero_Quatro = numero_Quatro - 1
            pontuação_jogador = pontuação_jogador + 1
        if sorteio_local == "Cinco":
            numero_Cinco = numero_Cinco - 1
            pontuação_jogador = pontuação_jogador + 1
        if sorteio_local == "Seis":
            numero_Seis = numero_Seis - 1
            pontuação_jogador = pontuação_jogador + 1
        if sorteio_local == "Sete":
            numero_Sete = numero_Sete - 1
            pontuação_jogador = pontuação_jogador + 1
        if sorteio_local == "Oito":
            numero_Oito = numero_Oito - 1
            pontuação_jogador = pontuação_jogador + 1
        if sorteio_local == "Nove":
            numero_Nove = numero_Nove - 1
            pontuação_jogador = pontuação_jogador + 1
        if sorteio_local == "Dez":
            numero_Dez = numero_Dez - 1
            pontuação_jogador = pontuação_jogador + 1
        if sorteio_local == "Valete":
            numero_Valete = numero_Valete - 1
            pontuação_jogador = pontuação_jogador + 10
        if sorteio_local == "Dama":
            numero_Dama = numero_Dama - 1
            pontuação_jogador = pontuação_jogador + 10
        if sorteio_local == "Rei":
            numero_Rei = numero_Rei - 1
            pontuação_jogador = pontuação_jogador + 10
            
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
                if pontuação_jogador < 11:
                    pontuação_jogador = pontuação_jogador + 11
                else:
                    pontuação_jogador = pontuação_jogador + 1
        if numero_Dois > 0:
            if sorteio_local == "Dois":
                numero_Dois = numero_Dois - 1
                pontuação_jogador = pontuação_jogador + 1
        if numero_Tres > 0:
            if sorteio_local == "Três":
                numero_Tres = numero_Tres - 1
                pontuação_jogador = pontuação_jogador + 1
        if numero_Quatro > 0:
            if sorteio_local == "Quatro":
                numero_Quatro = numero_Quatro - 1
                pontuação_jogador = pontuação_jogador + 1
        if numero_Cinco > 0:
            if sorteio_local == "Cinco":
                numero_Cinco = numero_Cinco - 1
                pontuação_jogador = pontuação_jogador + 1
        if numero_Seis > 0:
            if sorteio_local == "Seis":
                numero_Seis = numero_Seis - 1
                pontuação_jogador = pontuação_jogador + 1
        if numero_Sete > 0:
            if sorteio_local == "Sete":
                numero_Sete = numero_Sete - 1
                pontuação_jogador = pontuação_jogador + 1
        if numero_Oito > 0:
            if sorteio_local == "Oito":
                numero_Oito = numero_Oito - 1
                pontuação_jogador = pontuação_jogador + 1
        if numero_Nove > 0:
            if sorteio_local == "Nove":
                numero_Nove = numero_Nove - 1
                pontuação_jogador = pontuação_jogador + 1
        if numero_Dez > 0:
            if sorteio_local == "Dez":
                numero_Dez = numero_Dez - 1
                pontuação_jogador = pontuação_jogador + 1
        if numero_Valete > 0:
            if sorteio_local == "Valete":
                numero_Valete = numero_Valete - 1
                pontuação_jogador = pontuação_jogador + 10
        if numero_Dama > 0:
            if sorteio_local == "Dama":
                numero_Dama = numero_Dama - 1
                pontuação_jogador = pontuação_jogador + 10
        if numero_Rei > 0:
            if sorteio_local == "Rei":
                numero_Rei = numero_Rei - 1
                pontuação_jogador = pontuação_jogador + 10
        
        print(baralho)
        print(lista_numeros)
    else:
        print("Ok, você decidiu parar aqui. Então vamos analisar seus pontos!")
    lista_numeros = [numero_As, numero_Dois, numero_Tres, numero_Quatro, numero_Cinco, numero_Seis, numero_Sete, numero_Oito, numero_Nove, numero_Dez, numero_Valete, numero_Dama, numero_Rei]
    print(lista_numeros)
    print(pontuação_jogador)
    return lista_numeros, pontuação_jogador


#retirar_carta(jogador_1)    
#i = 0
#while i < len(lista_numeros):
    #for a in chaves:
        #baralho_jogado[a] = lista_numeros[i]
    #i = i + 1
    
    
def dealer():
    baralho = { "Ás" : 4, "Dois" : 4, "Três" : 4, "Quatro" : 4, "Cinco" : 4, "Seis" : 4, "Sete" : 4, "Oito" : 4, "Nove" : 4,
           "Dez" : 4, "Valete" : 4, "Dama" : 4, "Rei" : 4 }

    chaves = []
    valores = []

    pontuação = 0
    
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
            if pontuação < 11:
                pontuação = pontuação + 11
            else:
                pontuação = pontuação + 1
        if sorteio_local == "Dois":
            numero_Dois = numero_Dois - 1
            pontuação = pontuação + 1
        if sorteio_local == "Três":
            numero_Tres = numero_Tres - 1
            pontuação = pontuação + 1
        if sorteio_local == "Quatro":
            numero_Quatro = numero_Quatro - 1
            pontuação = pontuação + 1
        if sorteio_local == "Cinco":
            numero_Cinco = numero_Cinco - 1
            pontuação = pontuação + 1
        if sorteio_local == "Seis":
            numero_Seis = numero_Seis - 1
            pontuação = pontuação + 1
        if sorteio_local == "Sete":
            numero_Sete = numero_Sete - 1
            pontuação = pontuação + 1
        if sorteio_local == "Oito":
            numero_Oito = numero_Oito - 1
            pontuação = pontuação + 1
        if sorteio_local == "Nove":
            numero_Nove = numero_Nove - 1
            pontuação = pontuação + 1
        if sorteio_local == "Dez":
            numero_Dez = numero_Dez - 1
            pontuação = pontuação + 1
        if sorteio_local == "Valete":
            numero_Valete = numero_Valete - 1
            pontuação = pontuação + 10
        if sorteio_local == "Dama":
            numero_Dama = numero_Dama - 1
            pontuação = pontuação + 10
        if sorteio_local == "Rei":
            numero_Rei = numero_Rei - 1
            pontuação = pontuação + 10
            
        primeira_rodada = primeira_rodada + 1
        
    while pontuação < 17 and pontuação < pontuação_jogador + 1:
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
            if pontuação < 11:
                pontuação = pontuação + 11
            else:
                pontuação = pontuação + 1
        if sorteio_local == "Dois":
            numero_Dois = numero_Dois - 1
            pontuação = pontuação + 1
        if sorteio_local == "Três":
            numero_Tres = numero_Tres - 1
            pontuação = pontuação + 1
        if sorteio_local == "Quatro":
            numero_Quatro = numero_Quatro - 1
            pontuação = pontuação + 1
        if sorteio_local == "Cinco":
            numero_Cinco = numero_Cinco - 1
            pontuação = pontuação + 1
        if sorteio_local == "Seis":
            numero_Seis = numero_Seis - 1
            pontuação = pontuação + 1
        if sorteio_local == "Sete":
            numero_Sete = numero_Sete - 1
            pontuação = pontuação + 1
        if sorteio_local == "Oito":
            numero_Oito = numero_Oito - 1
            pontuação = pontuação + 1
        if sorteio_local == "Nove":
            numero_Nove = numero_Nove - 1
            pontuação = pontuação + 1
        if sorteio_local == "Dez":
            numero_Dez = numero_Dez - 1
            pontuação = pontuação + 1
        if sorteio_local == "Valete":
            numero_Valete = numero_Valete - 1
            pontuação = pontuação + 10
        if sorteio_local == "Dama":
            numero_Dama = numero_Dama - 1
            pontuação = pontuação + 10
        if sorteio_local == "Rei":
            numero_Rei = numero_Rei - 1
            pontuação = pontuação + 10
        
        
        
            
    lista_numeros = [numero_As, numero_Dois, numero_Tres, numero_Quatro, numero_Cinco, numero_Seis, numero_Sete, numero_Oito, numero_Nove, numero_Dez, numero_Valete, numero_Dama, numero_Rei]
    print(lista_numeros)
    print(pontuação)
    return lista_numeros, pontuação

numero_jogadores = int(input("Digite qual é o número de jogadores. Obs: NO MÁXIMO 7: "))
if numero_jogadores >= 1:
    jogador_1 = str(input("Por favor, digite qual é o nome do primeiro jogador: "))
    if retirar_carta(jogador_1)[1] > dealer()[1]:
        print("Jogador, você ganhou")
    else:
        print("Jogador, você perdeu!")
    if numero_jogadores >= 2:
        jogador_2 = str(input("Por favor, digite qual o nome do segundo jogador: "))
        if retirar_carta(jogador_2)[1] > dealer()[1]:
            print("Jogador, você ganhou!")
        else:
            print("Jogador, você perdeu!")
        if numero_jogadores >= 3:
            jogador_3 = str(input("Por favor, digite qual o nome do terceiro jogador: "))
            if retirar_carta(jogador_3)[1] > dealer()[1]:
                print("Jogador, você ganhou!")
            else:
                print("Jogador, você perdeu!")
            if numero_jogadores >= 4:
                jogador_4 = str(input("Por favor, digite qual o nome do quarto jogador: "))
                if retirar_carta(jogador_4)[1] > dealer()[1]:
                    print("Jogador, você ganhou!")
                else:
                    print("Jogador, você perdeu!")
                if numero_jogadores >= 5:
                    jogador_5 = str(input("Por favor, qual o nome do quinto jogador: "))
                    if retirar_carta(jogador_5)[1] > dealer()[1]:
                        print("Jogador, você ganhou")
                    else:
                        print("Jogador, você ganhou!")
                    if numero_jogadores >= 6:
                        jogador_6 = str(input("Por favor, qual o nome do sexto jogador: "))
                        if retirar_carta(jogador_6)[1] > dealer()[1]:
                            print("Jogador, você perdeu!")
                        if numero_jogadores >= 7:
                            jogador_7 = str(input("Por favor, qual o nome do setimo jogador: "))
                            if retirar_carta(jogador_7)[1] > dealer()[1]:
                                print("Jogador, você ganhou")
                            else:
                                print("Jogador, você perdeu!")
