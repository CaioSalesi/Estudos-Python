import time
import random
from random import randint
from pwinput import pwinput

class ModoDeJogo:
  cpu = '1'
  multiplayer = '2'

class Jogos:
  jokenpo         = '1'
  imparPar        = '2'
  acerteNumero    = '3'
  verdadeiroFalso = '4'
  caraCoroa       = '5'
  superTrunfo     = '6'

class ParImpar:
  impar = False
  par   = True

def esperaDramatica(tempo = 1):
  time.sleep(1)
  for i in range(tempo):
    print('.')
    time.sleep(1)

def tratativaUmDois(numero):
  if int(numero) != 1 and int(numero) != 2:
    print("Código fora de escopo, tente novamente")
    time.sleep(2)
    return True
  return False

def sair(numero):
   if not numero:
    return True
   return False

def parImpar(numero1, numero2, opcao, nomeJogador1=None, nomeJogador2=None):
  op = int(opcao) % 2
  total = (numero1 + numero2) % 2
  if nomeJogador1 and nomeJogador2:
    jogadorVencedor = nomeJogador1 if op == total else nomeJogador2
    return print(f"Meus parabéns! {jogadorVencedor} ganhou")
  if total == op:
    return print(f"Meus parabéns! Você ganhou")
  return print("Infelizmente você perdeu")

def AdeliaGame():
      global jogo
      opçoes = ['STONE', 'PAPER', 'SCISSORS']
      pc = randint(0,2)
      rp =input("Hello dear player, my name is Patricio. Looking forward to playing with me?")
      if rp=="no" or rp == "No" or rp=="não" or rp=="Não" or rp=="fim" or rp=="Fim" or rp=="end" or rp=="End":
        acabou = True
        print("neste proga contem varios tipos de jogos diferentes qual voC~e quer jogar")
        print("1- Pedra,Papel,Tesoura/Jokenpo")
        print("2- Impar ou Par")
        print("3- Acerte o numero")
        print("4- Verdade ou falso/True and false")
        print("5- Cara ou corôa")
        print("6- Super Trunfo")
        jogo=input("Qual jogo você quer?(digite o numero)")

      else:
        acabou=False
        while acabou==False:
          print("Me too, ok, let's get started")    
          print("="*20)
          user = int(input("Choose one of the Options:\n [0] STONE\n [1] PAPER\n [2] SCISSORS"))
          print("="*20)
          print('Patricio Played {}'.format(opçoes[pc]))
          print('You Played {}'.format(opçoes[user]))
          print("="*20)

          if pc== 0:
            if user== 0:
              print("DRAW")
            elif user== 1:
              print("YOU WON!")
            elif user== 2:
              print("YOU LOSE!")
            else:
              print('INVALID')
          elif pc== 1:
            if user== 0:

              print("YOU LOSE!")
            elif user== 1:
              print("DRAW")
            elif user== 2:
              print("YOU WON!")
            else:
              print('INVALID')
          elif pc== 2:
            if user== 0:
              print("YOU WON")
            elif user== 1:
              print("YOU LOSE!")
            elif user== 2:
              print("DRAW")
          else:
            print('INVALID')  
          rp =input("Hello dear player, my name is Patricio. Looking forward to playing with me?")
          if rp=="no" or rp == "No" or rp=="não" or rp=="Não":
            acabou = True
            print("neste progama contem varios tipos de jogos diferentes qual você quer jogar")
            print("1- Pedra,Papel,Tesoura/Jokenpo")
            print("2- Impar ou Par")
            print("3- Acerte o numero")
            print("4- Verdade ou falso/True and false")
            print("5- Cara ou corôa")
            print("6- Super Trunfo")
            jogo=input("Qual jogo você quer?(digite o numero)") 

          else:
            print("Você digitou errado, reiniciando...")

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

def RodrigoGame():
  while True:
    def criaLista(tamanho):
        if tamanho > 2:
            n = random.randint(0, (tamanho - 1))
            for i in range(0, tamanho):
                if n == i:
                    lista.append(True)
                else:
                    lista.append(False)
            global tentativas
            tentativas = 5
            return True
        else:
            return False

    def jogoA(posicao):
        global ganhou
        ganhou = lista[posicao]
        return lista[posicao]

    def tentativaDecremento():
        global tentativas
        tentativas = tentativas - 1

    def testaTentativa():
        global tentativas
        return tentativas > 0

    def salvar():
        global jogador
        global tentativas
        global ganhou
        log = open('log.txt', 'a')
        log.write("Player: " + jogador + "\n")
        log.write("List Size: " + str(len(lista)) + "\n")
        log.write("List Created: " + str(lista) + "\n")
        log.write("Attempts used: " + str(3 - tentativas) + "\n")
        if ganhou:
            log.write("Situation: You won the game!\n----------\n")
        else:
            log.write("Situation: Lost the game!\n----------\n")
        log.close()
        print("File saved successfully.")

    lista = list()
    tentativas = 0
    ganhou = False
    print("---------------------\nO jogo")
    print("Created by Rodrigo and the group 100% Favela\n---------------------")
    print()
    resp = 'a'
    while resp != 'x':
        jogador = input("Type your name:")
        if criaLista(int(input("Enter list size, for more fun minimum size is 2"))):
            print("You have "+ str(tentativas) + " attempts")
            while (testaTentativa()) and (not jogoA(int(input("Enter a number")))) :
                tentativaDecremento()
                print("You have " + str(tentativas) + "  attempts")
        else:
            print("list was not created, try again by setting a value above 2")

        if ganhou:
            print("Congratulations you won the game.\nSaving the game ...")
        else:
            print("It wasn't this time, try again later.\nSaving the game ...")
        salvar()
        resp = input("Type x to quit the game and any other keys to play again.")
    #variáveis globais
    #lista -> lista de valores
    #jogador -> nome do jogador
    #tentativas -> qtd de tentativas
    #ganhou -> controle de ganhar ou perder o jogo
    #resp -> controle de loop do jogo
  
def CarlosGame():
    global jogo
    print("Nome do Jogo: Set the Number")
    print('')
    print("Objetivo: Adivinhar um número aleatório de 0 a 100 com 10 tentativas.")
    print('')
    print("Dos criadores de 'COMO SOBREVIVER NO IFRO' e ' O JOGO'")
    print('')
    cn = (random.randint(0,100))
    tent = 10
    print()
    carlosR=input('Você que jogar?se não digite fim para terminar o jogo ')
    print()
    if carlosR=="fim" or carlosR == "Fim" or carlosR=="end" or carlosR=="End":
      final = True
      print("neste progama contem varios tipos de jogos diferentes qual você quer jogar")
      print("1- Pedra,Papel,Tesoura/Jokenpo")
      print("2- Impar ou Par")
      print("3- Acerte o Numero")
      print("4- Verdade ou falso/True and false")
      print("5- Cara ou corôa")
      print("6- Super Trunfo")
      jogo=input("Qual jogo você quer?(digite o numero)")

    else:
      final=False
      while final==False:
        print("Tente adivinhar o número secreto de 0 a 100! Você terá 10 tentativas!")
        while tent > 0:
            tent = tent - 1
            un = int(input('Número: '))
            print()
            if un > cn:
                print('O número secreto é menor!')
                print('Número de tentativas: %d' % tent)
                print()
            elif un < cn:
                print('O número secreto é maior!')
                print('Número de tentativas = %d' % tent)
                print()
            else:
                print('Parabéns! Você acertou! O número secreto é: %d' % cn)
                tent = -1
                print()
                carlosR=input('Você que jogar?se não digite fim para terminar o jogo ')
                print()
                if carlosR=="fim" or carlosR == "Fim" or carlosR=="end" or carlosR=="End":
                  final = True
                  print("neste progama contem varios tipos de jogos diferentes qual você quer jogar")
                  print("1- Pedra,Papel,Tesoura/Jokenpo")
                  print("2- Impar ou Par")
                  print("3- Acerte o Numero")
                  print("4- Verdade ou falso/True and false")
                  print("5- Cara ou corôa")
                  jogo=input("Qual jogo você quer?(digite o numero)")
        if tent == 0:
            print()
            print('Que pena! Você perdeu! Mais sorte da próxima vez!')
            print('O número secreto é: %d' % cn)
            input()
            print()
            carlosR=input('Você que jogar?se não digite fim para terminar o jogo ')
            print()
            if carlosR=="fim" or carlosR == "Fim" or carlosR=="end" or carlosR=="End":
              final = True
              print("neste progama contem varios tipos de jogos diferentes qual você quer jogar")
              print("1- Pedra,Papel,Tesoura/Jokenpo")
              print("2- Impar ou Par")
              print("3- Acerte o Numero")
              print("4- Verdade ou falso/True and false")
              print("5- Cara ou corôa")
              print("6- Super Trunfo")
              jogo=input("Qual jogo você quer?(digite o numero)")
        elif tent == -1:
            input()
            print()
            carlosR=input('Você que jogar?se não digite fim para terminar o jogo ')
            print()
            if carlosR=="fim" or carlosR == "Fim" or carlosR=="end" or carlosR=="End":
              final = True
              print("neste progama contem varios tipos de jogos diferentes qual você quer jogar")
              print("1- Pedra,Papel,Tesoura/Jokenpo")
              print("2- Impar ou Par")
              print("3- Acerte o Numero")
              print("4- Verdade ou falso/True and false")
              print("5- Cara ou corôa")
              print("6- Super Trunfo")
              jogo=input("Qual jogo você quer?(digite o numero)")
  
def SabrinaGame():
    global jogo
    
    dormir=input("Opa, hoje iremos jogar cara ou corôa, você quer jogar?Se não digite'fim'")
    if dormir=="fim" or dormir == "Fim" or dormir =="end" or dormir =="End":
      finalJ = True
      print("neste progama contem varios tipos de jogos diferentes qual você quer jogar")         
      print("1- Pedra,Papel,Tesoura/Jokenpo")
      print("2- Impar ou Par")
      print("3- Acerte o Numero")
      print("4- Verdade ou falso/True and false")
      print("5- Cara ou corôa")
      print("6- Super Trunfo")
      jogo=input("Qual jogo você quer?(digite o numero)") 
    
    else:
      finalJ=False
      while finalJ==False:
        vezes = int(input("Computador - Quantas vezes vamos brincar?\n"))
        vencer = []
        moedas = []
        for i in range(0, vezes):
          moedas.append(random.randint(0,1))
        #print(moedas) --> gabarito das moedas

        for i in range(0, vezes):
          sorteio= int(input("Computador - Escolha [0]Cara\t [1] Coroa\n"))
          if sorteio == 1:
            print("Computador - Irei apostar em cara então")
          else:
            print("Computador - Irei apostar em coroa então")
          print("Computador - Vamos começar o lançamento da moeda")
          if moedas[i] == sorteio:
            print("Computador - Você ganhou!!! Mas isso ainda não acabou!!")
            vencer.append(1)
          else:
            print("Computador - Hahaha Você perdeu! Esperado já!!")

        if len(vencer) > (vezes - len(vencer)):
          print("Computador - PARABÉNS!! Você ganhou o jogo!")
        elif len(vencer) == (vezes - len(vencer)):
          print("Computador - iiih alá empatamos!")
        else:
          print("Computador - HAHAHAHA!! Que pena,você perdeu o jogo, mais sorte da próxima vez!")
        dormir=input("Opa, hoje iremos jogar cara ou corôa, você quer jogar?Se não digite'fim'")
        if dormir=="fim" or dormir == "Fim" or dormir =="end" or dormir =="End":
          finalJ = True
          print("neste progama contem varios tipos de jogos diferentes qual você quer jogar")         
          print("1- Pedra,Papel,Tesoura/Jokenpo")
          print("2- Impar ou Par")
          print("3- Acerte o Numero")
          print("4- Verdade ou falso/True and false")
          print("5- Cara ou corôa")
          jogo=input("Qual jogo você quer?(digite o numero)")

def superTrunfo():
  global jogo
  print("Vamos jogar um jogo chamado super Trunfo ")
  pergunta=input("Você quer jogar?ou digite 'fim' para terminar o jogo ")
  if pergunta=="fim" or pergunta == "Fim" or pergunta=="end" or pergunta=="End":
    fim = True
    print("neste progama contem varios tipos de jogos diferentes qual você quer jogar")
    print("1- Pedra,Papel,Tesoura/Jokenpo")
    print("2- Impar ou Par")
    print("3- Acerte o Numero")
    print("4- Verdade ou falso/True and false")
    print("5- Cara ou corôa")
    print("6- Super Trunfo")
    jogo=input("Qual jogo você quer?(digite o numero)")
  
  else:
    fim=False
    while fim==False:
      nick=input("Qual é o seu nome? ")
      #criando classe
      class EDF:
          #inicio da classe
          #construtor         #parâmetros ou argumentos
          def __init__(self,numero,nome,atacar,defesa,titulos,AnoFund,preço):
              #atributos
              self._numero=numero
              self._nome=nome
              self._atacar=atacar
              self._defesa=defesa
              self._titulos=titulos
              self._AnoFund=AnoFund
              self._preco=preço 

          #métodos
          def mostrarcartaP(self):
            print("esta é a sua carta")
            print("-"*50)
            print("numero:",self._numero)
            print("-"*50)
            print("nombre: ",self._nome)
            print("-"*50)
            print("atacar: ", self._atacar)   
            print("-"*50)                  
            print("defensa:", self._defesa)
            print("-"*50)
            print("titulos:",self._titulos)
            print("-"*50)
            print("ano de fundacion",self._AnoFund)
            print("-"*50)
            print("precio de elquipo",self._preco)
            print("*"*50)

          def mostrarcartaBot(self):
            print("esta é a carta do BOT")
            print("-"*50)
            print("numero:",self._numero)
            print("-"*50)
            print("nome: ",self._nome)
            print("-"*50)
            print("atacar: ", self._atacar)   
            print("-"*50)                  
            print("defesa:", self._defesa)
            print("-"*50)
            print("titulos:",self._titulos)
            print("-"*50)
            print("ano de fundacion",self._AnoFund)
            print("-"*50)
            print("precio de elquipo",self._preco)
            print("*"*50)

        
          def compararCartas(self, carta, jogador):

            

            atributo = input('''qual atributo você quer comparar? 
            1-ataque
            2-defesa
            3-titulos
            4-Ano de fundacion
            5-Preço do time ''')
            if atributo == "1" or atributo=="ataque":
              print('o atributo ataque será comparado')
              if self._atacar > carta._atacar:
                  print(f'jogador',jogador,'ganhou essa partida!')
                  carta.mostrarcartaBot()
              else:
                  print('o computador ganhou')
                  carta.mostrarcartaBot()
            
            elif atributo=="2" or atributo=="defesa":
              print('o atributo defesa será comparado')
              if self._defesa > carta._defesa:
                  print(f'jogador',jogador,'ganhou essa partida!')
                  carta.mostrarcartaBot()
              else:
                  print('o computador ganhou')
                  carta.mostrarcartaBot()
            
            elif atributo == "3" or atributo=="titulos":
              print('o atributo titulos será comparado')
              if self._titulos > carta._titulos:
                  print(f'jogador',jogador,'ganhou essa partida!')
                  carta.mostrarcartaBot()
              else:
                  print('o computador ganhou')
                  carta.mostrarcartaBot()                      
            
            elif atributo == "4" or atributo=="Ano de fundacion":
              print('o atributo Ano de fundacion será comparado')
              if self._AnoFund < carta._AnoFund:
                  print(f'jogador',jogador,'ganhou essa partida!')
                  carta.mostrarcartaBot()
              else:
                  print('o computador ganhou')
                  carta.mostrarcartaBot()
            
            elif atributo == "5" or atributo=="preço do time":
              print('o atributo preço de time será comparado')
              if self._preco > carta._preco:
                  print(f'jogador',jogador,'ganhou essa partida!')
                  carta.mostrarcartaBot()
              else:
                  print('o computador ganhou')
                  carta.mostrarcartaBot()

      #fim da classe

      #instanciando objetos
      #nome do objeto = nome da classe ()
      ERealM=EDF("E1","Real Madrid",85,86,91,1902,1080.000)
      EFcB=EDF("E2","FC Barcelona",94,88,93,1899,1060.000)
      EAtleM=EDF("E3","Atletico de Madrid",81,82,31,1903,870.000)
      EValeCF=EDF("E4","Valencia CF",81,81,25,1919,524.000)
      EGetaCF=EDF("E5","Getafe CF",50,78,11,1983,200.000)
      ERealS=EDF("E6","Real Sociedad",80,76,14,1909,390.000)
      EAthB=EDF("E7","Athletic de Bilão",79,80,50,1898,250.000)
      ESeviFC=EDF("E8","Sevilla FC",79,80,22,1890,370.000)
      EGraFC=EDF("E9","Granada FC",76,75,21,1931,60.000)
      EOsasu=EDF("E10","Osasuna",73,73,13,1920,70.000)
      TIMES=[ERealM,EFcB,EAtleM,EValeCF,EGetaCF,ERealS,EAthB,ESeviFC,EGraFC,EOsasu]
      #invocando métodos : objeto.metodo()
      a = random.choice(TIMES)
      a.mostrarcartaP()
      a.compararCartas(random.choice(TIMES),nick)
      pergunta=input("Você quer jogar?ou digite 'fim' para terminar o jogo ")

      if pergunta=="fim" or pergunta=="Fim" or pergunta=="end" or pergunta=="End":
        fim = True
        print("neste progama contem varios tipos de jogos diferentes qual você quer jogar")
        print("1- Pedra,Papel,Tesoura/Jokenpo")
        print("2- Impar ou Par")
        print("3- Acerte o Numero")
        print("4- Verdade ou falso/True and false")
        print("5- Cara ou corôa")
        print("6- Super Trunfo")
        jogo=input("Qual jogo você quer?(digite o numero)") 

while True:
  time.sleep(0.3)
  print("Neste programa contem varios tipos de jogos diferentes qual você quer jogar")
  print("1 - Pedra, Papel, Tesoura/Jokenpo")
  print("2 - Ímpar ou Par")
  print("3 - Acerte o Número")
  print("4 - Verdade ou falso/True and false")
  print("5 - Cara ou corôa")
  print("6 - Super Trunfo")
  jogo = input("Qual jogo você quer? (digite o número): ")
  match jogo:
    case Jogos.jokenpo:
      AdeliaGame()
    case Jogos.imparPar:
      ImparOuParGame()
    case Jogos.acerteNumero:
      CarlosGame()
    case Jogos.verdadeiroFalso:           #BEM PROVAVEL Q VC(PROFESSORA) ESTÁ LENDO ISSO NA HORA DA APRESENTAÇÃO, E DEVE ESTAR DANDO UMA BRONCA TIPO "AH PQ O JOGO DO RODRIGO NÃO ESTÁ EM FUNÇÃO, AÍ EU TE RESPONDO ,MEIO Q O DOUGLAS DO PASSADO Q ESTÁ ESCREVENDO ISSO AGR AS 2 DA MANHA(COF COF BEM RENPONSAVEL) ESTÁ PESQUISANDO UMA FORMA DE COLOCAR UMA FUNÇÃO EM OUTRA E MEIO NÃO CONSEGUI :/, POR ISSO Q EU FIZ ESTÁ GAMBIARRA FOI MAL E NÃO TIRA PONTO DO GRUPO PLEASE, ESSA FOI A UNICA MANEIRA DE FAZER O PROGAMA LER, SE TEVE ALGUM ERRO DE PORTUGUES FOI MAL EU TO DESDE DAS 9 FAZENDO ISSO E AINDA FALTA MUITA COISA :( ASS:DOUGLAS (KAKAKAKAKAK DOUGLAS DO PRESENTE E FUTURO DESTE DOUGLAS 03/04/2020 ESTA RINDO MUITO DE SI MESMO DO PASSADO KAKAKKAKAKA)
      RodrigoGame()
    case Jogos.caraCoroa:
      SabrinaGame()
    case Jogos.superTrunfo:
      superTrunfo()
    case _:
      print("Digitaste algo errado")