import operator
import statistics
from collections import Counter
import time
import random
import pyodbc

def pegar_numero(mensagem):
    while True:
        entrada = input(mensagem).replace(',', '.')
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido. Digite um número.")

def pegar_desconto(mensagem):
    while True:
        entrada = input(mensagem).replace(',', '.')
        try:
            valor = float(entrada)
            if valor < 0 or valor > 100:
                print("Porcentagem inválida. Deve estar entre 0% e 100%.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Digite um número.")

def operacaomatematica():
    reais = {
        "somar": operator.add,
        "subtrair": operator.sub,
        "dividir": operator.truediv,
        "multiplicar": operator.mul,
        "media": statistics.mean
    }

    print("Escreva a operação matematica que deseja.")
    print("Somar\nSubtrair\nDividir\nMultiplicar\nMedia\n")
    while True:
        resposta = input("Digite qual operação deseja\n").lower()
        if resposta not in reais:
            print("Operação inválida, tente novamente!\n")
            continue
        break

    simbolo = reais.get(resposta)
    print(f"\nSua escolha foi: {resposta}\n")
    
    

    a = pegar_numero("Digite o primeiro número: ")
    b = pegar_numero("Digite o segundo número: ")

    if resposta == "dividir" and b == 0:
        print("Divisão por zero não é permitida. Tente novamente.\n")
        time.sleep(2)
        return operacaomatematica()

    if resposta == "media":
        resultado = simbolo([a, b])
    else:
        resultado = simbolo(a, b)
        print(f"\nO próximo número é {resultado + 1}")
        print(f"\nO número anterior é {resultado - 1}")

    print(f"\nO resultado da operação é {resultado}")

    time.sleep(2)
    continuar()

def proximoanterior():

    a = float(input("Para calcular o próximo e o anterior, digite um número\n"))

    proximo = a+1
    anterior = a-1
    print(f"O resultado da operação é {a}")
    print(f"O próximo número é {proximo}")
    print(f"O número anterior é {anterior}")
    time.sleep(2)
    continuar()

def contadorcaracteres():
    vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    concoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    texto = input("Digite uma palavra: ")

    # Conta todos os caracteres do texto
    contagem = Counter(texto)

    # Soma as ocorrências das vogais e números
    quantidadevogais = sum(contagem[vogal] for vogal in vogais)
    quantidadeconcoantes = sum(contagem[concoante] for concoante in concoantes)
    quantidadenumeros = sum(contagem[numero] for numero in numeros)
    if texto == "":
        print("Texto vazio, tente novamente!\n")
        time.sleep(1)
        vogaisnumeros()
        return
    print(f"\nA quantidade de vogais no texto {texto} é {quantidadevogais}, a quantidade de conçoantes é {quantidadeconcoantes} e a quantidade de números é {quantidadenumeros}")
    time.sleep(2)
    continuar()

def tercaparte():
    a = pegar_numero("Digite o número que deseja ver quanto vale um terço dele:\n")
    terco = a / 3
    print(f"\nUm terço de {a} é {terco}")
    continuar()

def medidas():
    metro = pegar_numero("Digite o valor em metros para converter: ")
    print(f"\nVocê digitou {metro} metros. Conversões:")
    
    unidades = {
        "Milímetros": metro * 1000,
        "Centímetros": metro * 100,
        "Decímetros": metro * 10,
        "Decâmetros": metro / 10,
        "Hectômetros": metro / 100,
        "Quilômetros": metro / 1000,
    }
    
    for unidade, valor in unidades.items():
        print(f"{unidade}: {valor}")

    continuar()

def conversao():
    valorreal = pegar_numero("Digite o valor da sua carteira em reais: R$")
    print(f"\nO valor da sua carteira em reais é de R${valorreal}\n")

    moedas = {
        "dolar": valorreal/3.45,
        "euro": valorreal/4.50,
    }
    for moeda in moedas.items():
        print(f"{moeda}")

    #print("Veja o valor atual da sua carteira em dólares")
    #valorreal = pegar_numero("Digite o valor atual da sua carteira em R$")
    #valordolar = valorreal/3.45
    #print(f"O valor da sua carteira em dólares é de: {valordolar}")
    continuar()
    
def calculodescontos():
    
    a = pegar_numero("\nDigite o valor original do produto: R$")
    b = pegar_desconto("\nDigite a porcentagem do desconto: ")
    c = a / 100 * b
    d = a - c
    print(f"\nO valor descontado é de R$ {c:.2f}")
    print(f"O valor final da compra é de R$ {d:.2f}")
    time.sleep(1)
    continuar()

def testerandom():
    a = random.randint(0,4)
    b = random.randint(0,4)
    print(f"{a}")
    print(f"{b}")
    if a == b:
        print(f"O jogo terminou em empate, com ambos times fazendo {a} gols!")
    elif a > b:
        print(f"O time da casa vence de {a} a {b}!")
    elif a < b:
        print(f"O time visitante vence o jogo de {b} a {a}!")
    time.sleep(1)
    continuar()

def sair():
    quit()

def continuar():
    while True:
        resposta = input("\nDeseja continuar? (s/n)\n").lower()
        if resposta == "s":
            definirprograma()
        elif resposta == "n":
            print("Saindo do programa...")
            quit()
        else:
            print("Resposta inválida, tente novamente!")

def definirprograma():
    programas = {
        "1": {
            "func": operacaomatematica,
            "nome": "Operações matemáticas",
            "mensagem": "\nOperações matemáticas foi selecionado\n"
        },
        "2": {
            "func": tercaparte,
            "nome": "Terceira parte",
            "mensagem": "\nTerceira parte foi selecionado\n"
        },
        "3": {
            "func": medidas,
            "nome": "Metragem",
            "mensagem": "\nConversor de medidas foi selecionado\n"
        },
        "4": {
            "func": conversao,
            "nome": "Conversão",
            "mensagem": "\nConversor de moedas foi selecionado\n"
        },
        "5": {
            "func": calculodescontos,
            "nome": "Cálculo de descontos",
            "mensagem": "\nCaluladora de descontos foi selecionada\n"
        },
        "6": {
            "func": proximoanterior,
            "nome": "Próximo e anterior",
            "mensagem": "\nProximo e anterior foi selecionado\n"
        },
        "7": {
            "func": contadorcaracteres,
            "nome": "Contador de letras e números",
            "mensagem": "\nLetras e números foi selecionado\n"
        },
        "8": {
            "func": testerandom,
            "nome": "teste random",
            "mensagem": "\nTeste randômico foi selecionado\n"
        },
        "10": {
            "func": sair,
            "nome": "Sair",
            "mensagem": "\nSaindo do programa..."
        },
    }

    while True:
        print("\nProgramas disponíveis:")
        for chave, dados in programas.items():
            print(f"{chave}: {dados['nome']}")
        resposta = input("\nDigite o número do programa que deseja executar\n")

        if resposta not in programas:
            print("\nPrograma inválido, tente novamente!\n")
            continue
        break

    selecionado = programas[resposta]
    print(selecionado["mensagem"])
    selecionado["func"]()
definirprograma()



