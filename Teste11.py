n1=float(input("Digite o primeiro valor:"))
n2=float(input("Digite o segundo valor:"))
op=input("Digite a operação:")
match op:
    case "+":
        print(n1+n2)
    case "-":
        print(n1-n2)
    case "*":
        print(n1*n2)
    case "/":
        print(n1/n2)

