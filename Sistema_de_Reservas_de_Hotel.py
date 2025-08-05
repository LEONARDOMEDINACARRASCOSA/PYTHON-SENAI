
import random

print("\n")

print(" ##  HOTEL MEDINA    ##")

print("\n")

nome_cliete_1 = input("DIGITE SEU NOME --- > ")
idade_cliente1 = int(input("DIGITE SUA IDADE --- > "))

print("\n")

nome_cliete_2 = input("DIGITE SEU NOME --- > ")
idade_cliente2 = int(input("DIGITE SUA IDADE --- > "))

print("\n")

nome_cliete_3 = input("DIGITE SEU NOME --- > ")
idade_cliente3 = int(input("DIGITE SUA IDADE --- > "))

print("\n")

if idade_cliente1 >= 18:
    print("-----")
else:
    print("APENAS MAIORES DE 18 PODEM FAZER O CHECK IN !!")
    print("VOLTE COM SEU RESPONSAVEL " , nome_cliete_1)
    print(exit())

if idade_cliente2 >= 18:
    print("-----")
else:
    print("APENAS MAIORES DE 18 PODEM FAZER O CHECK IN !!")
    print("VOLTE COM SEU RESPONSAVEL " , nome_cliete_2)
    print(exit())


if idade_cliente3 >= 18:
    print("-----")
else:
    print("APENAS MAIORES DE 18 PODEM FAZER O CHECK IN !!")
    print("VOLTE COM SEU RESPONSAVEL " , nome_cliete_3)
    print(exit())





print("OLÁ SEJA BEM VINDO (a) SENHOR (A)" , nome_cliete_1)
print("\n")
print("OLÁ SEJA BEM VINDO (a) SENHOR (A)" , nome_cliete_2)
print("\n")
print("OLÁ SEJA BEM VINDO (a) SENHOR (A)" , nome_cliete_3)



print("\n")

decisao = input("GOSTARIAM DE FAZER A UMA RESERVA EM NOSSO HOTEL --- > ")

print("\n")

catalogo_quartos = ["" ,"SIMPLES","DUPLO","LUXO"]
catalogo_quarto_visualizacao = "SIMPLES , DUPLO , LUXO"
precos_quarto = [0 , 100.00 , 150.00 , 250.00]

if decisao == 'sim' or decisao == 'SIM':
    print("OK , VAMOS DAR INICIO AO Check-in !!!")
    print("ESCOLHA A OPÇÃO DE QUARTO DESEJADO ! SENDO ELES " , catalogo_quarto_visualizacao)
elif decisao == 'nao' or decisao == 'NAO':
    print ("SEU CHECK IN FOI CANCELADO .... VOLTE QUANDO PRECISAR ! ")
    print(exit())


print(F'''QUAL SERIA O QUARTO DE SUA PREFERENCIA !
      
1 - {catalogo_quartos [1]} ----> {precos_quarto [1]}
2 - {catalogo_quartos [2]} ----> {precos_quarto [2]}
3 - {catalogo_quartos [3]} ----> {precos_quarto [3]}

''')

quarto_clinte_1 = [] 
quarto_clinte_2 = [] 
quarto_clinte_3 = [] 



escolha_cliente1 = int(input(nome_cliete_1 + " GOSTARIA DE SE HOSPEDAR EM QUAL QUARTO SENHOR (A) ----> "))
print("\n")
escolha_cliente2 = int(input(nome_cliete_2 + " GOSTARIA DE SE HOSPEDAR EM QUAL QUARTO SENHOR (A) ----> "))
print("\n")
escolha_cliente3 = int(input(nome_cliete_3 + " GOSTARIA DE SE HOSPEDAR EM QUAL QUARTO SENHOR (A) ----> "))


quarto_clinte_1.append(catalogo_quartos[escolha_cliente1])
quarto_clinte_2.append(catalogo_quartos[escolha_cliente2])
quarto_clinte_3.append(catalogo_quartos[escolha_cliente3])

quarto_clinte_1.append(precos_quarto[escolha_cliente1])
quarto_clinte_2.append(precos_quarto[escolha_cliente2])
quarto_clinte_3.append(precos_quarto[escolha_cliente3])


diaria_clinte_1 = []
diaria_clinte_2 = []
diaria_clinte_3 = []

print("\n")

diaria_clinte_1 = int(input(nome_cliete_1  + " QUANTOS DIAS GOSTARIA DE RESERVAR ---->  " ))
print("\n")
diaria_clinte_2 = int(input(nome_cliete_2  + " QUANTOS DIAS GOSTARIA DE RESERVAR ---->  " ))
print("\n")
diaria_clinte_3 = int(input(nome_cliete_3  + " QUANTOS DIAS GOSTARIA DE RESERVAR ---->  " ))

soma_clinte_1 = diaria_clinte_1 * precos_quarto[escolha_cliente1]
soma_clinte_2 = diaria_clinte_2 * precos_quarto[escolha_cliente2]
soma_clinte_3 = diaria_clinte_3 * precos_quarto[escolha_cliente3]



print(F'''

NOME DO CLINTE : { nome_cliete_1}
TIPO DE QUARTO E VALOR DA DIARIA : { quarto_clinte_1 }
QUANTIDADE DE DIARIAS : { diaria_clinte_1 }
SOMA TODAS DOS DIAS R$ : { soma_clinte_1 }

''')


print(F'''

NOME DO CLINTE : { nome_cliete_2}
TIPO DE QUARTO E VALOR DA DIARIA : { quarto_clinte_2 }
QUANTIDADE DE DIARIAS : { diaria_clinte_2 }
SOMA TODAS DOS DIAS R$ : { soma_clinte_2 }

''')

print(F'''

NOME DO CLINTE : { nome_cliete_3 }
TIPO DE QUARTO E VALOR DA DIARIA : { quarto_clinte_3 }
QUANTIDADE DE DIARIAS : { diaria_clinte_3 }
SOMA TODAS DOS DIAS R$ : { soma_clinte_3 }

''')


confirmacao_clinte_1 = input(nome_cliete_1 + " ESTÁ DE ACORDO COM A ESTADIA ? ---->  " )
print("\n")
confirmacao_clinte_2 = input(nome_cliete_2 + " ESTÁ DE ACORDO COM A ESTADIA ? ---->  " )
print("\n")
confirmacao_clinte_3 = input(nome_cliete_3 + " ESTÁ DE ACORDO COM A ESTADIA ? ---->  " )

print("\n")

if confirmacao_clinte_1 == 'sim' or confirmacao_clinte_1 == 'SIM':
    print("SEJA BEM VINDO SENHOR (A) " , nome_cliete_1)

elif confirmacao_clinte_1 == 'nao' or confirmacao_clinte_1 == 'NAO':
    print(nome_cliete_1 , " SEU CHECK IN FOI CANCELADO .... VOLTE QUANDO PRECISAR ! ")
    
print("\n")

if confirmacao_clinte_2 == 'sim' or confirmacao_clinte_2 == 'SIM':
    print("SEJA BEM VINDO SENHOR (A) " , nome_cliete_2)

elif confirmacao_clinte_2 == 'nao' or confirmacao_clinte_2 == 'NAO':
    print(nome_cliete_2 , " SEU CHECK IN FOI CANCELADO .... VOLTE QUANDO PRECISAR ! ")

print("\n")

if confirmacao_clinte_3 == 'sim' or confirmacao_clinte_3 == 'SIM':
    print("SEJA BEM VINDO SENHOR (A) " , nome_cliete_3)

elif confirmacao_clinte_3 == 'nao' or confirmacao_clinte_3 == 'NAO':
    print(nome_cliete_3 , " SEU CHECK IN FOI CANCELADO .... VOLTE QUANDO PRECISAR ! ")

print("\n")      

print(F'''

Bem-vindo ao Hotel Medina! Esperamos que você tenha uma estadia incrível conosco. O café da manhã é servido das 7h às 10h30 no nosso restaurante !
Venha se deliciar com uma variedade de opções frescas e deliciosas para começar o dia com energia !
Estamos ansiosos para atendê-lo.

''')
