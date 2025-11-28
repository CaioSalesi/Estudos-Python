import time
import random
from random import randint
from pwinput import pwinput

def ImparOuParGame():
  print("Vamos jogar um jogo de ímpar ou par!")
  while True:

    modo = input("Você quer jogar contra a '1 - CPU' ou '2 - Multiplayer' ? Digite o número: ")

    if sair(modo): break
    if tratativaUmDois(modo): continue 

    time.sleep(0.5)
    match modo:
      case ModoDeJogo.cpu:
        while True:
          imparPar = input("Você quer '1 - Ímpar' ou '2 - Par' ? Digite o número da escolha: ")
          if sair(imparPar): break
          if tratativaUmDois(imparPar): continue    

          time.sleep(0.2)

          try:
            num1 = int(input("Digite o número para o jogo: "))
          except ValueError:
            print("Valor inválido, recomeçando...")
            break

          num2 = random.randint(0,99)

          esperaDramatica(3)

          print(f'{num1} (Seu número) + {num2} (Número do computador) = {num1 + num2}')
          parImpar(num1, num2, imparPar)

      case ModoDeJogo.multiplayer:
        while True:
          nomeJogador1 = input("Jogador 1, digite o seu nome: ")
          if sair(nomeJogador1): break
          nomeJogador2 = input("Jogador 2, digite o seu nome: ")
          if sair(nomeJogador2): break

          jogadorEscolhido = random.choice([nomeJogador1, nomeJogador2])
          print(f'O jogador sorteado para escolher é: {jogadorEscolhido}')

          imparPar = input(f"{jogadorEscolhido}, você quer '1 - Ímpar' ou '2 - Par' ? Digite o número da escolha: ")
          if sair(imparPar): break
          if tratativaUmDois(imparPar): continue    

          time.sleep(0.2)

          try:
            num1 = int(pwinput(prompt=f"{nomeJogador1}, Digite o número para o jogo: ", mask="*"))
            num2 = int(pwinput(prompt=f"{nomeJogador2}, Digite o número para o jogo: ", mask="*"))
          except ValueError:
            print("Valor inválido, recomeçando...")
            break

          esperaDramatica(3)

          print(f'{num1} ({nomeJogador1}) + {num2} ({nomeJogador2}) = {num1 + num2}')
          if jogadorEscolhido == nomeJogador1: parImpar(num1, num2, imparPar, nomeJogador1, nomeJogador2)
          else:                                parImpar(num1, num2, imparPar, nomeJogador2, nomeJogador1)
