#def pegar_numero(mensagem): # FUNÇÃO UTILIZADA PARA PEGAR FLOATS SEM ERROS DE INPUT (NÃO ESTÁ SENDO UTILIZADA NO CÓDIGO)
#    while True:
#        entrada = input(mensagem).replace(',', '.')
#        try:
#            return float(entrada)
#        except ValueError:
#            print("Valor inválido. Digite um número.")

#def calcularnota(): # CODIGO FEITO ANTERIORMENTE COMO BASE PARA A FUNÇÃO PRINCIPAL (NÃO ESTÁ SENDO UTILIZADA, SÓ ESTÁ AQUI PARA MOSTRAR MINHA LINHA DE PENSAMENTO)
#    nota = pegar_numero("Digite a nota do aluno: ")
#    if nota >= 6:
#        print(f"O aluno passsou com a nota de: {nota:.2f}")
#    elif nota < 6:
#        print(f"O aluno reprovou, pois a nota final foi: {nota:.2f}")

def notas_alunos(): #FUNÇÃO PRINCIPAL
    
    alunos = { # UTILIZEI DICIONÁRIOS PARA MOLDAR OS DADOS DA MANEIRA QUE EU QUERIA, INCLUINDO AS INFORMAÇÕES NECESSÁRIAS, COMO NOME, SOBRENOME, IDADE, MATRICULA, CAMPUS, E NOTA
        "10020030088": {
            "Nome": "Richard",
            "Sobrenome": "Grimes",
            "Idade": "26 anos",
            "Matricula": "10020030088",
            "Curso": "Análise e Desenvolvimento de Sistemas",
            "Campus": "Nova Iguaçu",
            "Nota": 6.0
        },
        "10020030089": {
            "Nome": "Larissa",
            "Sobrenome": "Souza",
            "Idade": "22 anos",
            "Matricula": "10020030089",
            "Curso": "Gastronomia",
            "Campus": "Duque de Caxias",
            "Nota": 8.5
        },
        "10020030090": {
            "Nome": "Carlos",
            "Sobrenome": "Menezes",
            "Idade": "24 anos",
            "Matricula": "10020030090",
            "Curso": "Análise e Desenvolvimento de Sistemas",
            "Campus": "Nova Iguaçu",
            "Nota": 4.3
        },
        "10020030091": {
            "Nome": "Juliana",
            "Sobrenome": "Almeida",
            "Idade": "21 anos",
            "Matricula": "10020030091",
            "Curso": "Odontologia",
            "Campus": "Nilópolis",
            "Nota": 9.2
        },
        "10020030092": {
            "Nome": "Felipe",
            "Sobrenome": "Castro",
            "Idade": "27 anos",
            "Matricula": "10020030092",
            "Curso": "Engenharia de Software",
            "Campus": "São João de Meriti",
            "Nota": 5.8
        },
        "10020030093": {
            "Nome": "Amanda",
            "Sobrenome": "Ferreira",
            "Idade": "23 anos",
            "Matricula": "10020030093",
            "Curso": "Administração",
            "Campus": "Nova Iguaçu",
            "Nota": 8.0
        }       
    }
    while True:

        while True:
            lista = input("Deseja ver a lista de alunos? (s/n)\n").lower()
            if lista == "s":
                for chave, dados in alunos.items(): # AQUI ELE FAZ A BUSCA DE TODOS OS ALUNOS, E PRINTA ELES EM UMA LISTA ORGANIZADA
                    print(f"""Aluno:
            Nome: {dados['Nome']}
            Sobrenome: {dados['Sobrenome']}
            Idade: {dados['Idade']}
            Matricula: {dados['Matricula']}
            Curso: {dados['Curso']}
            Campus: {dados['Campus']}
            Nota: {dados['Nota']}
            """)
            elif lista == "n":
                for chave, dados in alunos.items():
                    break
            else:
                print("Resposta inválida, tente novamente!")
                continue
            break
        while True:
        # AQUI EU FIZ UM LOOP, CASO A PESSOA COLOQUE UM INPUT QUE NÃO CORRESPONDA COM A MATRICULA DE QUALQUER ALUNO, ELE RETORNA AO INCIO E PRINTA UMA MENSAGEM DE ERRO
            resposta = input("Digite a matricula do aluno que deseja verificar: ")
            if resposta not in alunos:
                print("\nAluno inválido, tente novamente!\n")
                continue
            break

        selecionado = alunos[resposta]
        #AQUI EU FIZ UM PRINT, AVISANDO QUE O ALUNO FOI ENCONTRADO NO "BANCO DE DADOS", MOSTRANDO AS INFORMAÇÕES DO ALUNO
        print(f"""
        Aluno encontrado:
        Nome: {selecionado['Nome']}
        Sobrenome: {selecionado['Sobrenome']}
        Idade: {selecionado['Idade']}
        Matrícula: {selecionado['Matricula']}
        Curso: {dados['Curso']}
        Campus: {selecionado['Campus']}
        Nota: {selecionado['Nota']}""")

        while True: # NESSE LOOP A PESSOA TEM A DECISÃO DE VERIFICAR SE O ALUNO FOI APROVADO OU NÃO, SE ELA ESCREVER N, O CÓDIGO É FINALIZADO
                resposta = input("\nDeseja verificar se o aluno selecionado foi aprovado? (s/n)\n").lower()
                if resposta == "s":
                    nota = selecionado['Nota']
                    if nota >= 6:
                        print(f"O aluno passou com a nota de: {nota:.2f}")
                    else:
                        print(f"O aluno reprovou, pois a nota final foi: {nota:.2f}")
                elif resposta == "n":
                    pass
                else:
                    print("Resposta inválida, tente novamente!")
                    continue
                break
        while True:
            resposta2 = input("Deseja verificar outro aluno? (s/n)\n").lower()
            if resposta2 == "s":
                break  # reinicia o loop principal
            elif resposta2 == "n":
                input("Aperte enter para sair...")
                quit()
            else:
                print("Resposta inválida, tente novamente!")
    
notas_alunos()



# ALGUNS PRONTOS QUE EU PODERIA ADICIONAR AQUI É, QUE COM UM IMPORT DE ALGUMA BIBLIOTECA SQL, FACILMENTE DARIA PRA EXPANDIR ESSE SISTEMA, INCLUINDO INSERTS DE NOVOS ALUNOS, ATUALIZAÇÃO DE NOTA EM TEMPO REAL, LOGIN DE ALUNOS, PROFESSORES, ETC.
