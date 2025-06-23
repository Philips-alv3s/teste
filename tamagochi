import random
dias = 0
fome = random.randint(1, 100)
felicidade = random.randint(1, 100)
saude = random.randint(1, 100)
while True:
    print("==== TAMAGOTCHI ===")
    if dias == 0:
        print(f"Tamagotchi nasceu! e tem {dias} dias de vida")
    else:
        print(f"Tamagotchi tem {dias} dias de vida")
    print("\n1. Alimentar \n2. Brincar \n3. Dormir \n4. Sair\n")
    print("= " * 20)
    print(f"Status do Tamagotchi: \n1. Fome: {fome} \n2. Felicidade: {felicidade} \n3. Saúde: {saude}")
    print("= " * 20)
    opcao = int(input("Escolha uma opção entre 1 a 4: "))
    if opcao == 1:
        fome -= 10
        felicidade += 5
        print("Você alimentou o Tamagochi. \n")
    elif opcao == 2:
        felicidade += 15
        fome += 15
        print("Você brincou com o Tamagochi. \n")
    elif opcao == 3:
        saude += 10
        felicidade -= 15
        print("Você fez o Tamagochi dormir. \n")
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
        continue
    fome = max(0, min(fome, 100))
    felicidade = max(0, min(felicidade, 100))
    saude = max(0, min(saude, 100))
    if fome >= 100:
        print("Seu Tamagotchi morreu de fome.")
        break
    elif felicidade <= 0:
        print("Seu Tamagotchi ficou triste e não quer mais brincar.")
        break
    elif saude <= 0:
        print("Seu Tamagotchi ficou doente e não quer mais brincar.")
        break
    
    dias +=1
