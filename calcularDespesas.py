""" total_despesas = 0
        print(f"calculando despesas (Salario R${salario:.2f})")
        for item in despesas_fixas:
            valor_gasto = float(input(f"Digite o valor gasto com {item}: "))
            total_despesas += valor_gasto
            saldo_final = salario - total_despesas
            print(f"Total de despesas: R${total_despesas:.2f}")
            print(f"Saldo restante: R${saldo_final:.2f}")"""

class CalculoDespesas:
    def __init__(cd, salario, despesas_fixas):
        cd.salario = salario
        cd.despesas_fixas = despesas_fixas
        cd.total_despesas = 0
        cd.saldo_final = salario

    def calcular(cd):
        print(f"Calculando despesas (Salário R${cd.salario:.2f})")

        for item in cd.despesas_fixas:
            valor_gasto = float(input(f"Digite o valor gasto com {item}: "))
            cd.total_despesas += valor_gasto
            cd.saldo_final = cd.salario - cd.total_despesas

            print(f"Total de despesas: R${cd.total_despesas:.2f}")
            print(f"Saldo restante: R${cd.saldo_final:.2f}")

    def mostrarSaldo(cd):
        print(f"Seu saldo é: {cd.saldo_final}R$")