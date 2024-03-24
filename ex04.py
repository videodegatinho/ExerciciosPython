cargo = input("Qual o seu cargo?")
salario = float(input("Qual o seu salário atual?"))
reajuste = float(input("Qual é a porcentagem do reajuste?"))

print("Calculando o reajuste")

percentual_reajuste = salario * (reajuste/100)

if cargo == 'analista jr': 
    percentual_bonus = salario * 0.02
elif cargo == 'analista pleno':
    percentual_bonus = salario * 0.025
elif cargo == 'analista sênior':
    percentual_bonus = salario * 0.03
elif cargo == 'arquiteto':
    percentual_bonus = salario * 0.04
elif cargo == 'gerente':
    percentual_bonus = salario * 0.045

resultado = salario + percentual_reajuste + percentual_bonus
print("Salário reajustado: ", resultado)
