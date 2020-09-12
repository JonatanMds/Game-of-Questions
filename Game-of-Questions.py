import random
import time

# Criando uma classe jogo, fazendo com que ao instânciar a classe jogo, eu consiga juntar as perguntas e repostas em um só objeto.
class Jogo:


    # Pergutas e respostas do jogo
    def __init__(self,perguntas,resposta):


        self.perguntas = perguntas
        self.resposta = resposta


# Ponto de parada do WHILE principal do jogo.
deuruim = False
primeira_pergunta = 0
# Contagem de acertos do jogador
resposta_certa=0
# Contagem de respostas puladas pelo jogador
contador_pulo = 0

pulo = 2


# Perguntas e suas respectivas respotas, criadas como estância da classe jogo.
p1=Jogo("Quem era o homem mais sedutor do mundo? \n 1 DOM JUAN \n 2 DOM ANTÔNIO \n 3 DOM MARCO \n 4 DOM CARLOS",'1')
p2=Jogo("De quantos anos é constituído um século? \n 1 50 \n 2 100 \n 3 1.000 \n 4 1.500",'2')
p3=Jogo("Qual é o coletivo de cães? \n 1 MATILHA \n 2 REBANHO \n 3 CARDUME \n 4 MANADA",'1')
p4=Jogo("Segundo a Bíblia, em que rio Jesus foi batizado por João Batista? \n 1 NO RIO NILO \n 2 NO RIO SENA \n 3 NO RIO RENO \n 4 NO RIO JORDÃO", '4')
p5=Jogo("Qual é a maior floresta do planeta? \n 1 NEGRA \n 2 DE SHERWOOD \n 3 DA TIJUCA \n 4 AMAZÔNICA",'4')
p6=Jogo("Qual é o naipe do baralho que tem o desenho de coração? \n 1 OUROS \n 2 PAUS \n 3 COPAS \n 4 ESPADAS",'3')
p7=Jogo("Qual atriz estrelou no filme: “A lagoa azul”? \n 1 ALICIA SILVERSTONE \n 2 BROOKE SHIELDS \n 3 JULIA ROBERTS \n 4 JESSICA LANGE",'2')



# Uma lista com todas as instâncias da classe jogo
pergunta=[p1,p2,p3,p4,p5,p6,p7]


# While principal do jogo, ele para se o jogar errar uma pergunta ou se todas as perguntas forem respondidas com exatidão(fazendo com que a lista pergunta
# chegue a zero)
while deuruim == False and pergunta != []:

# Se for a primeira pergunta feita ao jogador, essa será a mensagem imprimida na tela
    if primeira_pergunta == 0:
        print('Vamos para a primeira pergunta')
# Se não, essa será a mensagem
    else:
        print('Vamos para próxima pergunta')



# ""n"" recebe uma instância aleatória (perguntas que estão dentro da lista pergunta)
    n = (random.choice(pergunta))
# Um intervalo de 0.8s para que cada pergunta seja postada
    time.sleep(.8)
# Mostrando na tela a pergunta selecionada, "n" é uma das instâncias dentro da lista pergunta. EX: p1 = n, então "n.pergunta" é a instância "n" e pego apenas a pergunta
#dessa instância, logo eu mostro n.pergunta, sem mostrar a resposta
    print(n.perguntas)
# Quando a primira pergunta é feita, é somado um no primeiro if do jogo.
    primeira_pergunta = 1


# O jogodor pode pular até DOIS perguntas, caso ele pule é somado UM ao contador de pulo
    if contador_pulo <= 1:
        continuar = int(input('Deseja Continuar click 1 se deseja pular click 2. !!Atencão vocé terá apernas {} pulo(s)!!'.format(pulo)))
        if continuar != 1:
            contador_pulo = contador_pulo+1
            # A pergunta pulada é excluida da lista pergunta
            pergunta.remove(n)
            pulo-=1
# Quando não é mais possível pular, é mostrada essa mensagem, alertando o jogador
    else:

        print('!!!!!!! Não há mais a possibilidade de pular !!!!!!!')
        continuar = 1

# Se o jogador prosseguir na pergunta, sem pula-lar, ele responde a pergunta feita
    while continuar == 1:

        resposta = input(str("Qual a resposta? "))


# Acertando a pergunta somase +1 ao contador de respostas certas(respostas_certa) o código para com o break(para não ficar em um loop de: Qual a proxima pergunta)
#desta forma eu forço ele a voltar ao primeiro while do jogo, fazendo tudo de novo
        if resposta == n.resposta:
            print('Parabéns resposta certa')
            # Removo a pergunta que foi respondida da lista
            pergunta.remove(n)
            resposta_certa+=1
            break

# Se o jogador errar a pergunta e mostrada a mensagem('Não foi dessa fez que você consegui!') o deuruim virá TRUE(sinal de parada do primeiro while do jogo)
#dando então o fim de jogo e o número de acertos do jogador
        else:
            deuruim = True
            print('Não foi dessa fez que você consegui!')
            break

# Número de acertos
print('Seu total de acertos',resposta_certa)
print('fim')
