saldo = 0
extrato = []
gerenciador = [extrato]
while True:
    print(" === GERENCIADOR DE FINANÇAS === ")
    print(f"Saldo Atual: {saldo} \n")
    print("1. Adicionar Receita \n2. Adicionar Despesa \n3. Ver Extrato \n4. Sair \n")
    Tudo = int(input(">>> "))
    if Tudo == 1:
        print("1. Salário \n2. Investimento \n3. Freelance \n4. Presente \n")
        escolha = int(input("Escolha um dos numeros: "))
        if escolha == 1:
            valor = int(input("Digite o valor: ")) 
            descricao = str(input("Digite a descrição: "))
            extrato.append({"Valor": valor, "Descrição": descricao})
            saldo += valor
        elif escolha == 2:
            valor = int(input("Digite o valor: ")) 
            descricao = str(input("Digite a descrição: "))
            extrato.append({"Valor": valor, "Descrição": descricao})
            saldo += valor
        elif escolha == 3:
            valor = int(input("Digite o valor: ")) 
            descricao = str(input("Digite a descrição: "))
            extrato.append({"Valor": valor, "Descrição": descricao})
            saldo += valor
        elif escolha == 4:
            valor = int(input("Digite o valor: ")) 
            descricao = str(input("Digite a descrição: "))
            extrato.append({"Valor": valor, "Descrição": descricao})
            saldo += valor
        else:
            print("numero errado")
            continue
    elif Tudo == 2:
        print("1. Alimento \n2. Saude \n3. Moradia \n4. Diversão")
        escolha = int(input("Digite uma opção: "))
        if escolha == 1:
            valor = int(input("Digite o valor: ")) 
            descricao = str(input("Digite a descrição: "))
            extrato.append({"Valor": valor, "Descrição": descricao})
            saldo -= valor
        elif escolha == 2:
            valor = int(input("Digite o valor: ")) 
            descricao = str(input("Digite a descrição: "))
            extrato.append({"Valor": valor, "Descrição": descricao})
            saldo -= valor
        elif escolha == 3:
            valor = int(input("Digite o valor: ")) 
            descricao = str(input("Digite a descrição: "))
            extrato.append({"Valor": valor, "Descrição": descricao})
            saldo -= valor
        elif escolha == 4:
            valor = int(input("Digite o valor: ")) 
            descricao = str(input("Digite a descrição: "))
            extrato.append({"Valor": valor, "Descrição": descricao})
            saldo -= valor
        else:
            print("numero errado")
    elif Tudo == 3:
        print("=== EXTRATO ===")
        if not extrato:
            print("O extrato está vazio")
        else:
            print("Extrato:")
            for i, item in enumerate(extrato, 1):
                print(f"{i}. {item['Descrição']} - Valor:{item['Valor']}")
    elif Tudo == 4:
        print("Saindo...")
        break
    else:
        print("essa opção não existe...")
