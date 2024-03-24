a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))

if a == b != c and c == a != b and b == a != c:
    print("É um triângulo isósceles")
elif a != b != c and b != a != c and c != a != b:
    print("É um triângulo escaleno.")
elif a == b == c and b == a == c and c == a == b:
    print("É um triângulo equilátero.")
else: 
    print("Não é um triângulo.")
