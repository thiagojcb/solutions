#! /usr/bin/python

# simulacao para verificar probabilidade do problema das caixas com bolas coloridas (3o problema):
# https://www1.folha.uol.com.br/colunas/marceloviana/2021/12/desafios-matematicos-para-a-familia-no-reveillon.shtml
# https://outline.com/CtGjFw

import random as rnd
import math

caixas = [['branco','branco'],['branco','preto']]  #caixa com duas bolas pretas eh irrelevante

jogadas         = 100000
n_branco        = 0
n_branco_branco = 0

for i in range (0,jogadas):

    icaixa = rnd.randint(0,1)             #escolha aleatoria entre caixa 1 ou 2
    c_selecionada = caixas[icaixa]
    
    bola = rnd.randint(0,1)               #escolha aleatoria entre bola 1 ou 2

    if c_selecionada[bola] == 'branco':   #tirei bola branca?
        n_branco +=1
        
        if icaixa == 0:                   #segunda bola sera branca?
            n_branco_branco += 1

razao = 100. * float(n_branco_branco) / float(n_branco)
erro  = 100. * math.sqrt(float(n_branco_branco)) / float(n_branco)  #incerteza estatistica (otimista? soh considerando numerador, fadiga de propagar se tiver que considerar denominador...)

print('Probabilidade da segunda bola ser branca, se tirei uma branca primeiro (%i simulacoes):'%jogadas)
print('(%.1f'%razao + " +/- " + '%.1f'%erro + ')%')
