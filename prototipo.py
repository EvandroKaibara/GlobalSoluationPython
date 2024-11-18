# Função que calcula a produção de energia em 1 dia__________________________________________________________________________________________________________________________________
def calcularDiaria(paineis, horaSol):
    return paineis * horaSol * 300

# Função que calcula o total da produção_____________________________________________________________________________________________________________________________________________
def calcularProducao(paineis, horaSolMensal):
    total = 0
    for horaSolMensal in horaSolMensal:
        total += calcularDiaria(paineis, inputHoras)
    return total

# Interface de boas-vindas___________________________________________________________________________________________________________________________________________________________
print(f"{'*' * 57}")
print(f"*{' ' * 55}*")
print(f"* BEM-VINDO A CALCULADORA DE PRODUÇÃO DE ENERGIA SOLAR! *")
print(f"*{' ' * 55}*")
print(f"{'*' * 57}")

# Loop principal que serve como input de seletores das opções________________________________________________________________________________________________________________________
while True:
    opcao = input("Deseja calcular a produção em:\n"
                  "[M]ês (30 dias)\n"
                  "[S]emana (7 dias)\n"
                  "[P]eríodo personalizado (em dias)\n"
                  "[0] Sair\n"
                  "Opção: ")
    if opcao == '0':
        break

    paineis = int(input("Quantos painéis solares você possui? "))
    listaHoras = []

    # Tomadas de decisões dentro das opções__________________________________________________________________________________________________________________________________________
    if opcao == 'M' or opcao == 'm':
        aux = 'mensal'
        dias = 30
    elif opcao == 'S' or opcao == 's':
        aux = 'semanal'
        dias = 7
    elif opcao == 'p':  
        aux = 'dias'
        dias = int(input("Quantos dias você deseja calcular? "))
    else:
        print(f"Opção {opcao} inválida!")

    # For responsavel por fazer a contagem de horas diarias__________________________________________________________________________________________________________________________
    for i in range(dias):
        inputHoras = int(input(f"Quantas horas de sol no dia {i+1}º? "))
        listaHoras.append(inputHoras)

    producao = calcularProducao(paineis, listaHoras)
    producaoKWH = producao / 1000

    # Output com a produção total e a produção de kw/h_______________________________________________________________________________________________________________________________
    print(f"\nA produção de energia solar total {aux} é de: {producao:.2f} watts.")
    print(f"A produção de energia solar em kw/h é de: {producaoKWH:.2f} kw/h")
    print(f"Para finalizar a aplicação digite (0)!\n")

# Interface de finalização___________________________________________________________________________________________________________________________________________________________
print(f"{'*' * 34}")
print(f"*{' ' * 32}*")
print(f"* OBRIGADO POR USAR A APLICAÇÃO! *")
print(f"*{' ' * 32}*")
print(f"{'*' * 34}")