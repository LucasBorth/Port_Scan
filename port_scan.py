#Biblioteca de Teste de Rede
import socket

#Biblioteca e Comandos In-Operational System
import os

#Biblioteca de Tempo - Funcao de Espera
from time import sleep

#Biblioteca de Som - Funcao de Beep Sound, Funcao tocar sound do windows
from winsound import Beep

def retorno():
    Beep(750, 1000)
    Beep(500, 500)
    Beep(750, 1000)
    Beep(500, 500)
    op = input("Aperte ENTER para retornar ao Menu...")
    Beep(1000, 100)

def menu():
    execucao = True
    teste = False
    result = []

    while (execucao == True):
        os.system("cls")
        
        print("=================================================================")
        print("==  __________              __ ___________              __     ==")
        print("==  \______   \____________/  |\__    ___/___   _______/  |_   ==")
        print("==   |     ___/  _ \_  __ \   __\|    |_/ __ \ /  ___/\   __\  ==")
        print("==   |    |  (  <_> )  | \/|  |  |    |\  ___/ \___ \  |  |    ==")
        print("==   |____|   \____/|__|   |__|  |____| \___  >____  > |__|    ==")
        print("==                                   \/     \/ By CYB3rBoT_13  ==")
        print("=================================================================")
        print("== Opcoes =======================================================")
        print("=================================================================")
        print("== 1 - Inserir um intervalo de Testes                          ==")
        print("== 2 - Inserir portas para Teste                               ==")
        print("== 3 - Creditos                                                ==")
        if (teste == True):
            print("== 4 - Resultado                                               ==")
        print("== 0 - Sair                                                    ==")
        print("=================================================================")
        opc = str(input("-> Opcao Escolhida: "))

        if (opc == '1'):
            Beep(1000, 100)
            result = intervalo_testes()
            if (len(result) > 1):
                teste = True
        elif (opc == '2'):
            Beep(1000, 100)
            result = portas_teste()
            if (len(result) > 1):
                teste = True
        elif (opc == '3'):
            Beep(1000, 100)
            creditos()
        elif (opc == '4' and teste == True):
            Beep(1000, 100)
            resultado(result)
        elif (opc == '0'):
            os.system("cls") 
            iniciar(False)
            execucao = False
        else:
            os.system("cls")

            i = 0

            while (i < 3):
                print("=================================================================")
                print("== Opcao Invalida! ==============================================")
                print("=================================================================")

                sleep(0.5)
                if (i != 2):
                    Beep(200, 250)
                    Beep(500, 250)
                    os.system("cls")
                    sleep(0.5)
                
                i += 1

def intervalo_testes():
    os.system("cls")
    print("=================================================================")
    print("== Intervalo de Testes ==========================================")
    print("=================================================================")
    print("")
    intervalo_inicio = str(input("-> Informe uma Porta Inicial: "))
    Beep(1000, 100)
    intervalo_fim = str(input("-> Informe uma Porta Final: "))
    Beep(1000, 100)
    print("")
    print("=================================================================")
    print("")

    result = []

    if (intervalo_inicio.isnumeric() == True and intervalo_fim.isnumeric() == True):
        if (int(intervalo_fim) > int(intervalo_inicio)):
            i =  int(intervalo_inicio)
            portas = []

            while (i <= int(intervalo_fim)):
                portas.append(i)

                i += 1

            url = str(input("-> Insira uma URL: "))
            Beep(1000, 100)

            print("")
            print("=================================================================")
            print("")

            if (len(url) >= 3 and ("." in url) == True):
                listagem = str(input("-> Tambem listar portas fechadas? (1- P/ Sim | 2- P/ Nao): "))
                Beep(1000, 100)
                print("")
                print("=================================================================")
                print("")

                if (listagem.isnumeric() == True):
                    if (int(listagem) == 1 or int(listagem) == 2):
                        iniciando()
                        result = teste_portas(url, portas, listagem)
                    else:
                        print("Opcao Invalida, tente novamente!")
                        retorno()
                else:
                    print("Informacao Invalida, tente novamente!")
                    retorno()
            else:
                print("URL Invalido, tente novamente!")
                retorno()
        else:
            print("Intervalo Invalido, tente novamente!")
            retorno()
    else:
        print("Informacao Invalida, tente novamente!")
        retorno()
    
    return result
        
def portas_teste():
    os.system("cls")
    portas = []
    result = []

    print("=================================================================")
    print("== Portas de Teste ==============================================")
    print("=================================================================")
    print("== Insira o numero das portas desejadas linha a linha          ==")
    print("== Quando finalizado informe o digito 0 para Iniciar           ==")
    print("=================================================================")
    print("")
    
    cont = 1
    ok = True
    i = ""
    
    while (i != "0"):
        i = str(input("-> Porta n {}: ".format(cont)))
        Beep(1000, 100)

        if (i.isnumeric() == False or i == "" or i == None):
            i = "0"
            ok = False
        elif (i.isnumeric() == True):
            if (i != "0"):
                portas.append(int(i))

        cont += 1
    
    print("")
    print("=================================================================")
    print("")
    
    if (len(portas) > 0 and portas[0] != 0 and i == "0" and ok == True):
        url = str(input("-> Insira uma URL: "))
        Beep(1000, 100)

        print("")
        print("=================================================================")
        print("")

        if (len(url) >= 3 and ("." in url) == True):
            listagem = str(input("-> Tambem listar portas fechadas? (1- P/ Sim | 2- P/ Nao): "))
            Beep(1000, 100)
            print("")
            print("=================================================================")

            if (listagem.isnumeric() == True):
                if (listagem == '1' or listagem == '2'):
                    iniciando()
                    result = teste_portas(url, portas, listagem)
                else:
                    print("Opcao Invalida, tente novamente!")
                    retorno()
            else:
                print("Informacao Invalida, tente novamente!")
                retorno()
        else:
            print("URL Invalido, tente novamente!")
            retorno()
    else:
        print("Erro!, tente novamente!")
        retorno()
    
    return result

def creditos():
    os.system("cls")

    print("=================================================================")
    print("==  PortTest                                                   ==")
    print("==                                                             ==")
    print("==  Desenvolvido por CYB3rBoT_13  2020                         ==")
    print("==                                                             ==")
    print("==  - Sistema desenvolvido com a finalidade de gerar testes de ==")
    print("==    portas em WebSites, afim de encontrar falhas.            ==")
    print("=================================================================")

    Beep(500, 500)
    Beep(600, 250)
    Beep(700, 250)
    Beep(800, 250)
    sleep(0.250)
    Beep(900, 500)
    sleep(0.500)
    Beep(1000, 500)
    Beep(1080, 700)

    print("== Aperte ENTER para Retornar ao Menu                          ==")
    print("=================================================================")

    op = input("")
    Beep(1000, 100)

def resultado(result):
    os.system("cls")

    n = len(result)
    i = 0

    Beep(1500, 750)

    while (i < n):
        linha = result[i]
        print(linha)

        i += 1
    
    Beep(1000, 500)
    Beep(2000, 500)
    Beep(1000, 500)
    Beep(2000, 500)
    
    op = input("Aperte ENTER para retornar ao Menu...")
    Beep(1000, 100)

def iniciando():
    i = 17
    freq = 100
    ponto = "..."

    while (i < 65):
        os.system("cls")

        print("=================================================================")
        message = "== Iniciando{}".format(ponto)
        restante = 65 - len(message) - 3
        message = message + str(" " * restante) + " =="
                    
        print(message)
        print("=================================================================")

        Beep(freq, 100)
        sleep(0.01)

        ponto += "."
        freq += 50
        i += 1

def teste_portas(url, portas, listagem):
    display = [
    "=================================================================",
    "==          PORTA            ====            STATUS            ==",
    "=================================================================",
    ]
    resultado = False
    total = len(portas)
    contagem = 1
    result = []

    for i in portas:
        os.system("cls")

        print("=================================================================")

        porcentagem = round((contagem * 100) / total)

        linha_porta = "== Porta Atual: {} ====== Progresso: {}% ".format(i, porcentagem)
        restante = 65 - int(len(linha_porta))

        linha_porta = linha_porta + str("=" * restante)
        print(linha_porta)

        contador = 0
        n = len(display)

        while (contador < n):
            linha = display[contador]

            print(linha)

            contador += 1
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        cod = client.connect_ex((url, i))

        if (cod == 0):
            resultado = True

            message_a = "==          {}".format(i)
            restante = 31 - len(message_a) - 2
            message_a = message_a + str(" " * restante) + "=="

            message_b = "==            {}".format("Aberta")
            restante = 34 - len(message_b) - 2
            message_b = message_b + str(" " * restante) + "=="

            message = message_a + message_b

            display.append(message)
            print(message)
            Beep(2000, 500)
        if (cod != 0 and listagem == '1'):
            message_a = "==          {}".format(i)
            restante = 31 - len(message_a) - 2
            message_a = message_a + str(" " * restante) + "=="

            message_b = "==            {}".format("Fechada")
            restante = 34 - len(message_b) - 2
            message_b = message_b + str(" " * restante) + "=="

            message = message_a + message_b

            display.append(message)
            Beep(100, 50)
            print(message)
        
        contagem += 1
        
    if (resultado != True):
        print("==                                                             ==")
        print("== Nenhuma Porta Aberta Encontrada... ===========================")
    
    display.append("=================================================================")
    print("=================================================================")

    result = display

    Beep(1000, 500)
    Beep(2000, 500)
    Beep(1000, 500)
    Beep(2000, 500)

    op = input("Teste Finalizado, Aperte ENTER para retornar ao Menu...")
    Beep(1000, 100)

    return result

def iniciar(sentido):
    i = 0

    if (sentido == True):
        i = 18
        titulo = "Carregando"
        freq = 100
        ponto = "..."
    else:
        i = 64
        titulo = "Finalizando"
        freq = 3000
        ponto = "..............................................."

    while (i < 65):
        os.system("cls")

        print("=================================================================")
        if (i < 18):
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
        elif (i < 21):
            print("==  __________                                                 ==")
            print("==  \______   \                                                ==")
            print("==   |     ___/                                                ==")
            print("==   |    |                                                    ==")
            print("==   |____|                                                    ==")
            print("==                                                             ==")
        elif (i < 24):
            print("==  __________                                                 ==")
            print("==  \______   \____                                            ==")
            print("==   |     ___/  _ \                                           ==")
            print("==   |    |  (  <_> )                                          ==")
            print("==   |____|   \____/                                           ==")
            print("==                                                             ==")
        elif (i < 27):
            print("==  __________                                                 ==")
            print("==  \______   \___________                                     ==")
            print("==   |     ___/  _ \_  __ \                                    ==")
            print("==   |    |  (  <_> )  | \/                                    ==")
            print("==   |____|   \____/|__|                                       ==")
            print("==                                                             ==")
        elif (i < 31):
            print("==  __________              __                                 ==")
            print("==  \______   \____________/  |                                ==")
            print("==   |     ___/  _ \_  __ \   __\                              ==")
            print("==   |    |  (  <_> )  | \/|  |                                ==")
            print("==   |____|   \____/|__|   |__|                                ==")
            print("==                                                             ==")
        elif (i < 35):
            print("==  __________              __ ___________                     ==")
            print("==  \______   \____________/  |\__    ___/                     ==")
            print("==   |     ___/  _ \_  __ \   __\|    |                        ==")
            print("==   |    |  (  <_> )  | \/|  |  |    |                        ==")
            print("==   |____|   \____/|__|   |__|  |____|                        ==")
            print("==                                   \/                        ==")
        elif (i< 39):
            print("==  __________              __ ___________                     ==")
            print("==  \______   \____________/  |\__    ___/___                  ==")
            print("==   |     ___/  _ \_  __ \   __\|    |_/ __ \                 ==")
            print("==   |    |  (  <_> )  | \/|  |  |    |\  ___/                 ==")
            print("==   |____|   \____/|__|   |__|  |____| \___  >                ==")
            print("==                                   \/     \/                 ==")
        elif (i < 43):
            print("==  __________              __ ___________                     ==")
            print("==  \______   \____________/  |\__    ___/___   ______         ==")
            print("==   |     ___/  _ \_  __ \   __\|    |_/ __ \ /  ___/         ==")
            print("==   |    |  (  <_> )  | \/|  |  |    |\  ___/ \___ \          ==")
            print("==   |____|   \____/|__|   |__|  |____| \___  >____  >         ==")
            print("==                                   \/     \/                 ==")
        elif (i < 46):
            print("==  __________              __ ___________              __     ==")
            print("==  \______   \____________/  |\__    ___/___   _______/  |_   ==")
            print("==   |     ___/  _ \_  __ \   __\|    |_/ __ \ /  ___/\   __\  ==")
            print("==   |    |  (  <_> )  | \/|  |  |    |\  ___/ \___ \  |  |    ==")
            print("==   |____|   \____/|__|   |__|  |____| \___  >____  > |__|    ==")
            print("==                                   \/     \/                 ==")
        elif (i < 50):
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
        elif (i < 54):
            print("==  __________              __ ___________              __     ==")
            print("==  \______   \____________/  |\__    ___/___   _______/  |_   ==")
            print("==   |     ___/  _ \_  __ \   __\|    |_/ __ \ /  ___/\   __\  ==")
            print("==   |    |  (  <_> )  | \/|  |  |    |\  ___/ \___ \  |  |    ==")
            print("==   |____|   \____/|__|   |__|  |____| \___  >____  > |__|    ==")
            print("==                                   \/     \/                 ==")
        elif (i < 57):
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
        elif (i < 62):
            print("==  __________              __ ___________              __     ==")
            print("==  \______   \____________/  |\__    ___/___   _______/  |_   ==")
            print("==   |     ___/  _ \_  __ \   __\|    |_/ __ \ /  ___/\   __\  ==")
            print("==   |    |  (  <_> )  | \/|  |  |    |\  ___/ \___ \  |  |    ==")
            print("==   |____|   \____/|__|   |__|  |____| \___  >____  > |__|    ==")
            print("==                                   \/     \/                 ==")
        elif (i < 65):
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                                             ==")

        print("=================================================================")
        message = "== {}{}".format(titulo, ponto)
        restante = 65 - len(message) - 3
        message = message + str(" " * restante) + " =="
                        
        print(message)
        print("=================================================================")

        Beep(freq, 100)
        sleep(0.01)

        if (sentido == False and i < 12):
            i = 999999

            os.system("cls")

            print("=================================================================")
            print("==  Sistema Encerrado                                          ==")
            print("==                                                             ==")
            print("==  Ate Logo...                                                ==")
            print("==                                                             ==")
            print("==                                                             ==")
            print("==                                             By CYB3rBoT_13  ==")
            print("=================================================================")

            Beep(200, 3000)

        if (sentido == True):
            i += 1
            ponto += "."
            freq += 50
        else:
            i = i - 1
            n = len(ponto)
            novo_ponto = ""
            temp_i = 0

            while (temp_i < n - 1):
                novo_ponto += ponto[temp_i]

                temp_i += 1

            ponto = novo_ponto
            freq -= 50

    if (sentido == True):
        menu()

#Inicio de Execucao
iniciar(True)