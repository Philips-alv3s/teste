import math
print("=== CALCULADORA CIENTÍFICA ===")
print("Faça uma operação matemática com os números e operadores a seguir:")
print("Escolha o operador exemplos: 5+3, 10-3, 1*3, 2/5, 5**7, 3^, sin, cos, tan: \n")
while True:
    conta = input(">>> ")
    if conta == "":
        continue
    elif conta == "sair":
        print("Saindo...")
        break
    elif len(conta) > 2:
        if conta == "sin":
            numero = int(input("Digite o número: "))
            resultado = math.sin(math.radians(numero))
            print("Seno de", conta, "graus é:", resultado)
        elif conta == "cos":
            numero = int(input("Digite o número: "))
            resultado = math.cos(math.radians(numero))
            print("Cosseno de", conta, "graus é:", resultado)
        elif  conta =="tan":
            numero = int(input("Digite o número: "))
            resultado = math.tan(math.radians(numero))
            print("Tangente de", conta, "graus é:", resultado)
        elif conta == "sqrt":
            numero = int(input("Digite o número: "))
            if conta >= 0:
                print(f"Resultado: {numero ** 0.5}")
            else:
                print("Raiz quadrada de número negativo não é permitida.")
    elif conta in ["+", "-", "*", "/", "**"]:
        print(eval(conta))
    else:
        print("Operação incorreta.")
        continue