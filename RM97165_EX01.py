ass = input("Digite qual é a sua assinatura (BASIC, SILVER, GOLD ou PLATINUM): ")
faturamento_anual = float(input("Digite o faturamento anual: "))

total = 0
if ass.upper() == "BASIC":
    total = faturamento_anual * 0.3
    print(f"O valor do bônus a pagar é de R$ {(total)}")
elif ass.upper() == "SILVER":
    total = faturamento_anual * 0.2
    print(f"O valor do bônus a pagar é de R$ {(total)}")
elif ass.upper() == "GOLD":
    total = faturamento_anual * 0.1
    print(f"O valor do bônus a pagar é de R$ {(total)}")
elif ass.upper() == "PLATINUM":
    total = faturamento_anual * 0.05
    print(f"O valor do bônus a pagar é de R$ {(total)}")

else:
    print("Assinatura inválida")
