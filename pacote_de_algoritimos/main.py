import operator
import statistics
from collections import Counter
import time
import random
import sys

def main():
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
            "mensagem": "\nCalculadora de descontos foi selecionada\n"
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
            "nome": "Teste random",
            "mensagem": "\nTeste randômico foi selecionado\n"
        },
        "10": {
            "func": sys.exit,
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

        selecionado = programas[resposta]
        print(selecionado["mensagem"])
        selecionado["func"]()

        # Loop para continuar ou sair
        while True:
            continuar = input("\nDeseja continuar? (s/n)\n").lower()
            if continuar == "n":
                print("Saindo do programa...")
                sys.exit()
            elif continuar == "s":
                break
            else:
                print("Resposta inválida, tente novamente!")
 

def pegar_numero(mensagem):
    while True:
        entrada = input(mensagem).replace(',', '.')
        try:
            return float(entrada)
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
    
    
    while True:
        a = pegar_numero("Digite o primeiro número: ")
        b = pegar_numero("Digite o segundo número: ")
        if resposta == "dividir" and b == 0:
            print("Divisão por zero não é permitida. Tente novamente.\n")
            continue
        if resposta == "media":
            resultado = simbolo([a, b])
        else:
            resultado = simbolo(a, b)
            print(f"\nO próximo número é {resultado + 1}")
            print(f"\nO número anterior é {resultado - 1}")
        break
    print(f"\nO resultado da operação é {resultado}")
    time.sleep(1)
    

def proximoanterior():

    a = float(input("Para calcular o próximo e o anterior, digite um número\n"))

    proximo = a+1
    anterior = a-1
    print(f"O resultado da operação é {a}")
    print(f"O próximo número é {proximo}")
    print(f"O número anterior é {anterior}")
    time.sleep(2)
    

def contadorcaracteres():
    vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while True:
        texto = input("Digite uma palavra: ")
        if texto == "":
            print("Texto vazio, tente novamente!\n")
            time.sleep(1)
            continue
        break

    # Conta todos os caracteres do texto
    contagem = Counter(texto)
    # Soma as ocorrências das vogais, consoantes e números
    quantidadevogais = sum(contagem[vogal] for vogal in vogais)
    quantidadeconsoantes = sum(contagem[consoantes] for consoantes in consoantes)
    quantidadenumeros = sum(contagem[numero] for numero in numeros)
    print(f"\nA quantidade de vogais no texto é {quantidadevogais}, a quantidade de consoantes é {quantidadeconsoantes} e a quantidade de números é {quantidadenumeros}")
    time.sleep(2)
    

def tercaparte():
    a = pegar_numero("Digite o número que deseja ver quanto vale um terço dele:\n")
    terco = a / 3
    print(f"\nUm terço de {a} é {terco}")
    time.sleep(2)
    

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
    time.sleep(2)
    

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
    time.sleep(2)
    
    
def calculodescontos():
    
    a = pegar_numero("\nDigite o valor original do produto: R$")
    while True:
        b = pegar_numero("\nDigite a porcentagem do desconto: ")
        if b < 0 or b > 100:
                print("Porcentagem inválida. Deve estar entre 0% e 100%.")
        else:
            break
    c = a / 100 * b
    d = a - c
    print(f"\nO valor descontado é de R$ {c:.2f}")
    print(f"O valor final da compra é de R$ {d:.2f}")
    time.sleep(1)
    

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
    

def sair():
    quit()

# Início do programa
main()



