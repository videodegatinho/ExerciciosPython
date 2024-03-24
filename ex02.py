media1 = float(input("Digite a média do primeiro semestre: "))
media2 = float(input("Digite a média do segundo semestre: "))

soma = (media1 + media2)/2

print("Sua média é: ", soma)

if soma <=4:
    print("Você está reprovado.")
elif soma >4 and soma<6:
    print("Você está de exame.")
elif soma >6:
    print("Você está aprovado. Parabéns!")
