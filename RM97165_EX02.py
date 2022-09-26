segunda = int(input("Informe a quantia de votos para Segunda-feira: "))
terca = int(input("Informe a quantia de votos para Terça-feira: "))
quarta = int(input("Informe a quantia de votos para Quarta-feira: "))
quinta = int(input("Informe a quantia de votos para Quinta-feira: "))
sexta = int(input("Informe a quantia de votos para Sexta-feira: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia mais votado foi Segunda-feira")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O dia mais votado foi Terça-feira")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("O dia mais votado foi Quarta-feira")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("O dia mais votado foi Quinta-feira")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("O dia mais votado foi Sexta-feira")

