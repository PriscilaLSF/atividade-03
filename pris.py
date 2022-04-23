primeironome=input("Insira seu primeiro nome: ")
print("Digite seu salário do mes de abril: ")
salarioreais=input("Reais: ")
salariocentavos=input("Centavos: ")
salarioformatado= salarioreais +","+ salariocentavos
primeiraletra=primeironome[0:1].upper()
restantenome = primeironome[1:].lower()
primeironomeformatado=primeiraletra+restantenome
mensagem="O salário de " + primeironomeformatado + " no mês de Abril foi de R$ " + salarioformatado + "."
print(mensagem)