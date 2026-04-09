from calcularDespesas import CalculoDespesas


salario = float(input("Digite seu salario mensal: "))
despesas_fixas = ["comida", "transporte", "moradia"]
opcao = 1
while(opcao != 0):
    print("1-Calcular despesa: ")
    print("2-mostrar saldo")
    print("3 faça isso")
    opcao = int(input("0-Sair do programa: "))
    c = CalculoDespesas(salario, despesas_fixas)
    if(opcao == 1):      
       c.calcular()

    if(opcao == 2):
        c.mostrarSaldo()
            





























