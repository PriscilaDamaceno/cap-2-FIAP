minutos = int(input("Informe os minutos do horário atual: "))

count = 1
resultado = 1

while count <= minutos:
    resultado = resultado * count
    count = count + 1

print(f"A senha é: LIBERDADE{resultado}")