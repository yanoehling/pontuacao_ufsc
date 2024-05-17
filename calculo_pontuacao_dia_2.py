def somatorio(num, lista, recado):
    num_original = num
    while True:
        if num == 0:
            break
        for n in range(6, -1, -1):
            if num >= 2**n:
                lista[n] = 1
                num -= 2**n

    xx = str(lista).replace('1', 'X')
    xx = xx.replace("0", "_")
    print(f"{recado}{xx} ({num_original})")


a = open("gabaritos_oficiais\gabarito_d2_violeta.txt")
# a = open("gabaritos_oficiais\gabarito_d2_amarela.txt")
gab = a.readlines()
b = open("gabaritos_pessoais\yan_d2_violeta.txt")
# b = open("gabaritos_pessoais\lucas_d2_amarela.txt")
rsp = b.readlines()
cont = 0
pontos = []
pont_total, humanas, fisica, quimica  = 0, 0, 0, 0,

while True:

    lst = gab[cont].split()

    if lst[1] == "A":
        np = 0
    else:
        np = int(lst[1])

    questao = int(lst[0])
    gab_soma = int(lst[2])
    gabarito = []
    resp_soma = int(rsp[cont])
    resposta = []
    cont += 1

    if np != 0:
        for c in range(np):
            gabarito.append(0)
            resposta.append(0)
        somatorio(gab_soma, gabarito, f"Gabarito {questao}:  ")
        somatorio(resp_soma, resposta, "Sua resposta: ")
        for c in range(np):
            if resposta[c] != gabarito[c]:
                if resposta[c] == 1:
                    resposta[c] = 2
    else:
        print(f"QST ABERTA:   ({gab_soma})")
        print(f"Sua resposta: ({resp_soma})")

    ntpc = gabarito.count(1)
    npc = resposta.count(1)
    npi = resposta.count(2)

    if np == 0:
        if gab_soma == resp_soma:
            pontuacao = 1
        else:
            pontuacao = 0
    elif npc > npi:
        pontuacao = (np - (ntpc - (npc - npi))) / np
        pontuacao = pontuacao.__round__(2)
    else:
        pontuacao = 0

    print(f"Pontuação: {pontuacao}")
    print()
    pontos.append(pontuacao)

    if cont == 40:
        break

for c, v in enumerate(pontos):
    pont_total += v
    if c <= 19:
        humanas += v
    elif c <= 29:
        fisica += v
    else:
        quimica += v

print(f"Pontuação Humanas: {humanas.__round__(2)}")
print(f"Pontuação Física: {fisica.__round__(2)}")
print(f"Pontuação Química: {quimica.__round__(2)}")
print(f"Pontuação total Dia 2: {pont_total.__round__(2)}")
