Saldo = 0
Limite = 500
Extrato = ""
numero_saque = 0
limite_saque = 3

while True:
   menu = "Digite uma opção:\n-> 0 - Extrato\n-> 1 - Depositar\n-> 2 - Sacar\n-> 3 - Sair\n "
   opção = input(menu)

   if opção == "1":
         print("-> Depósito <-")
         valor_deposito = float(input("Quanto você quer depositar? "))
         if valor_deposito > 0:
            Saldo += valor_deposito
            # print(f"Saldo atualizado: R${Saldo:.2f}")
            Extrato += f"+ Depósito: R${valor_deposito:.2f}\n Saldo atual: R${Saldo:.2f}\n"
         else:
            print("Valor incorreto, tente novamente.")
   elif opção == "2":
         print("-> Saque <-")
         valor_saque = float(input("Quanto você quer sacar? "))
         if valor_saque > Saldo:
            print("Valor excede seu saldo da conta")
         elif valor_saque > Limite:
            print("Valor excede o seu limite de saque")
         elif numero_saque >= limite_saque:
            print("Você já atingiu o limite de saques diários")
         elif valor_saque > 0:
            Saldo -= valor_saque
            numero_saque += 1
            Extrato += f"- Saque: R${valor_saque:.2f}\n Saldo atual: R${Saldo:.2f}\n"
         else:
            print("Tente Novamente")
          
   elif opção == "0":
        print("-> Extrato <-")
        if Extrato == "":
            print("Não foram realizadas movimentações")
        else:
            print(f"{Extrato}")
   elif opção == "3":
       break
   else:
       print("Operação inválida, tente novamente")