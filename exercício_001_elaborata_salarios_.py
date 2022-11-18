faixa_20 = 1.2
faixa_15 = 1.15
faixa_10 = 1.10
faixa_05 = 1.05

salario = int(input("Informe seu salário R$ "))

if salario <= 1280:
    print("Seu salário atual é: R$", salario)
    print("Seu salário foi reajustado em: 20%")
    print("seu reajuste é de: R$ ", (salario * faixa_20) - salario)
    print("Seu salário atual é de: R$", salario * faixa_20)
    
elif salario > 1280 and salario <=1700:
    print("Seu salário atual é: R$", salario )
    print("Seu salário foi reajustado em: 15%")
    print("seu reajuste é de: R$ ", (salario * faixa_15) - salario)
    print("Seu salário atual é de: R$", salario * faixa_15)
    
elif salario > 1700 and salario <= 2500:
    print("Seu salário atual é: R$", salario )
    print("Seu salário foi reajustado em: 10%")
    print("seu reajuste é de: R$ ", (salario * faixa_10) - salario)
    print("Seu salário atual é de: R$", (salario * faixa_10))
    
elif salario > 2500:
    print("\n Seu salário atual é: R$", salario )
    print("   Seu salário foi reajustado em: 5%")
    print("\n seu reajuste é de: R$ ", (salario * faixa_05) - salario)
    print("   Seu salário atual é de: R$", salario * faixa_05)