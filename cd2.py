#Lê armazena os valores do arquivo1
with open("Texto1.txt") as m:
    file1 = m.readlines()
    l1 = []
    for row1 in file1:      
        l1.append(row1)

#Lê armazena os valores do arquivo2
with open("Texto2.txt") as t:
    file2 = t.readlines()
    l2 = []
    for row2 in file2:      
        l2.append(row2)


#Olha se a quantidade de valores entre arquivos é correta
length1 = len(l1)
length2 = len(l2)
if length1 == length2:
    pass
else:
    print("Quantidade ERRADA")
    i = input("Clique no ENTER para sair...")
    exit()

#Variaves de controle e cálculo
n = 0
d = 0
s = 0

#Filtra os produtos com valores diferentes e calcula a diferença entre eles
while n < length2:
    if l1[n] == l2[n]:
        n += 1
    else:
        l1n = l1[n]
        l2n = l2[n]
        rl1n = l1n.replace(",",".")
        rl2n = l2n.replace(",",".")
        diff = float(rl1n[0:-1]) - float(rl2n[0:-1])
        if n == (length2 - 1):
            diff = float(rl1n) - float(rl2n)
        s += (diff)
        print(f"\nQuantidade diferente:\n Texto 1 - {l1[n]} Texto 2 - {l2[n]} Linha:[{n + 1}]")
        print(f" Diferença: {round(diff, 2)}")
        d += 1
        n += 1


#Olha se houve diferenças entre os arquivos e se houver mostra a quantidade de valores diferentes
print("\n")
if d == 0:
    print("Não houve diferenças entre as tabelas.")
else:
    print(f"Foram encontradas [{d}] diferenças para serem consertadas.")
    print(f"Diferença total: {round(s, 2)}")


i = input("Clique no ENTER para sair...")
exit()