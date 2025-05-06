import operator
import statistics
from collections import Counter
import time

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
    
    print(f"Para {resposta} informe o primeiro e o segundo valor respectivamente\n")
    a = float(input("Digite o primeiro número\n").replace(",", "."))
    print()
    b = float(input("Digite o segundo número\n").replace(",", "."))
    print()
    if resposta == "dividir" and b == 0:
        print("Um dos números digitados é 0, o que não é permitido, tente novamente!\n")
        operacaomatematica()
        time.sleep(2)
        return
    if resposta == "media":
        c = simbolo([a, b])
        print(f"O resultado da operação é {c}")
    else:
        c = simbolo(a, b)
        proximo = c+1
        anterior = c-1
        print(f"O resultado da operação é {c}")
        print(f"O próximo número é {proximo}")
        print(f"O número anterior é {anterior}")
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

def vogaisnumeros():
    vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    texto = input("Digite uma palavra: ")

    # Conta todos os caracteres do texto
    contagem = Counter(texto)

    # Soma as ocorrências das vogais e números
    quantidadevogais = sum(contagem[vogal] for vogal in vogais)
    quantidadenumeros = sum(contagem[numero] for numero in numeros)
    if texto == "":
        print("Texto vazio, tente novamente!\n")
        time.sleep(1)
        vogaisnumeros()
        return
    print(f"\nA quantidade de vogais no texto {texto} é {quantidadevogais}, e a quantidade de números é {quantidadenumeros}")
    time.sleep(2)
    continuar()

def continuar():
    resposta = input("\nDeseja continuar? (s/n)\n").lower()
    if resposta == "s":
        definirprograma()
    elif resposta == "n":
        print("Saindo do programa...")
        quit()
    else:
        print("Resposta inválida, tente novamente!")
        continuar()
def sair():
    quit()

def definirprograma():
    tipoPrograma = {
        "1": operacaomatematica,
        #"2": tercaparte,
        #"3": metragem,
        #"4": conversao,
        #"5": calculodescontos,
        "6": proximoanterior,
        "7": vogaisnumeros,
        "10": sair,
    }
    nomesPrograma = {
        "1": "Operações matemáticas",
        #"2": "Terceira parte",
        #"3": "Metragem",
        #"4": "Conversão",
        #"5": "Cálculo de descontos",
        "6": "Próximo e anterior",
        "7": "Vogais e números",
        "10": "Sair",
    }
    mensagemExibicao = {
        "1": "\nOperações matemáticas foi selecionado\n",
        "6": "\nProximo e anterior foi selecionado\n",
        "7": "\nVogais e números foi selecionado\n",
        "10": "\nSaindo do programa...",
    }
    while True:
        print("\nProgramas disponíveis:")
        for chave, nome in nomesPrograma.items():
            print(f"{chave}: {nome}")
        resposta = input("\nDigite o número do programa que deseja executar\n")
        if resposta not in tipoPrograma:
            print("\nPrograma inválido, tente novamente!\n")
            continue
        break
    programa = tipoPrograma.get(resposta)
    resposta = mensagemExibicao.get(resposta, "ERRO: mensagem não encontrada")
    print(resposta)
    programa()
definirprograma()

#palavra = input("digite sua palavra: ")

#for letra in palavra:
#    print(letra)


