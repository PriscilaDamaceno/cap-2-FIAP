impar = 0
par = 0

print("Você está digitando a nota dos alunos ÍMPARES ")
for media_impar in range(1, 51, 2):
    nota_impar = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(media_impar)))
    impar = impar + nota_impar

print("Você está digitando a nota dos alunos PARES ")
for media_par in range(2, 51, 2):
    nota_par = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(media_par)))
    par = par + nota_par

media_impar = impar / 25
print(f"A média dos alunos com números ÍMPAR é de {(media_impar)} ")

media_par = par / 25
print(f"A média dos alunos com números PAR é de {(media_par)}")

if media_impar > media_par:
    print("A maior média foi dos alunos com número ÍMPAR")

elif media_par == media_impar:
        print("Houve empate!")
else:
    print("A maior média foi dos alunos com números PAR.")