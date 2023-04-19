import time

print("Olá! Insira o ticket do estacionamento para realizarmos o pagamento.")
tempo = float(input("Agora, insira o tempo de estacionamento em minutos: "))

if tempo <= 10:
  print("O valor a ser pago é de R$8.00")
elif tempo <= 20:
  print("O valor a ser pago é de R$15.00")
elif tempo <= 25:
  print("O valor a ser pago é de R$18.00")
elif tempo <= 35 or tempo <= 40:
  print("O valor a ser pago é de R$25.00")
else:
  print("O valor a ser pago é de R$35.00")

forma_pagamento = input("Qual será a forma de pagamento? ")
if forma_pagamento == "cartão" or forma_pagamento == "Cartão":
  print("Insira seu cartão.")
  time.sleep(1)
  print("Processando pagamento...")
  time.sleep(3)
elif forma_pagamento == "dinheiro" or forma_pagamento == "Dinheiro":
  print("Insira as cédulas.")
  print("Processando pagamento...")
  time.sleep(3)

print("Pagamento aprovado e finalizado no {}!".format(forma_pagamento))
print("Obrigado! Volte sempre.")

