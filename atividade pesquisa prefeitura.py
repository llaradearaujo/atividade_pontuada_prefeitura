import os
from dataclasses import dataclass

os.system("cls || clear")



familias = []
salario = []
filhos = []

while True:
    
    print(""" 
=====MENU====
1 - adicionar familia
2 - exibir resultados
3 - sair
""")
    opcao = int(input("digite a opção desejada: "))
    if opcao == 1:
        numero_filhos = int(input("digite o numero de filhos: "))
        filhos.append(numero_filhos)
        salario_familia = int(input("digite seu salário: "))
        salario.append(salario_familia)
        familias.append(1)
        os.system("cls || clear")

        total_familias = sum(familias)
        soma_salarios = sum(salario)
        soma_filhos = sum(filhos)
        maior_salario = max(salario)
        menor_salario = min(salario)

        media_filhos = soma_filhos / total_familias
        media_salarios = soma_salarios / total_familias
              
    elif opcao == 2:


        print(f"total de familias: {total_familias}")
        print(f"média de salário: {media_salarios}")
        print(f"média de filhos: {media_filhos}")
        print(f"maior salário: {maior_salario}")
        print(f"menor salário: {menor_salario}")
        
    elif opcao == 3:
        print("saindo do programa")
        break
    else:
        print("opção inválida")

nome_do_arquivo = "pesquisa_prefeitura.txt"

with open(nome_do_arquivo, "w") as arquivo_prefeitura:
    arquivo_prefeitura.write(f"\n total familias:{total_familias}")
    arquivo_prefeitura.write(f"\n media de salarios: {media_salarios}")
    arquivo_prefeitura.write(f"\n media de filhos: {media_filhos}")
    arquivo_prefeitura.write(f"\n maior salario: {maior_salario}")
    arquivo_prefeitura.write(f"\n menor salario: {menor_salario}")


arquivo_prefeitura.close()
print("=====DADOS SALVOS COM SUCESSO====")

with open(nome_do_arquivo,"r")as arquivo_de_origem:
    for linha in arquivo_de_origem:
       linha.strip().split("\n")
    
arquivo_prefeitura.close()

print("=====EXIBINDO DADOS======")
print(f"total familias:{total_familias}")
print(f"media de salarios: {media_salarios}")
print(f"media de filhos: {media_filhos}")
print(f"maior salario: {maior_salario}")
print(f"menor salario: {menor_salario}")


