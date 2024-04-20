saldo = 0.0
LIMITE = 500.0
extrato = f'Saldo inicial: R$ {saldo}\n'
numero_saques = 0
LIMITE_SAQUES = 3

print('Bem-vindo ao Python Bank!')

while True:
  escolha = input('''
  Escolha uma opção:
  [D] Depósito.
  [S] Saque.
  [E] Extrato.
  [0] Sair.
  ''')

  if escolha.upper() == 'D':
    deposito = float(input('Indique o valor a ser depositado:'))
    saldo = saldo + deposito
    extrato = extrato + f'+ R$ {deposito}\n'
    print(f'Você depositou R$ {deposito}.')

  elif escolha.upper() == 'S':
    saque = float(input('Indique o valor a ser sacado:'))
    if numero_saques == LIMITE_SAQUES:
      print('Você já atingiu o limite diário de saques (3 saques).')
    elif saque > saldo:
      print('Você não possui saldo suficiente para realizar este saque.')
    elif saque <= LIMITE:
      saldo = saldo - saque
      numero_saques = numero_saques + 1
      extrato = extrato + f'- R$ {saque}\n'
      print(f'Você sacou R$ {saque}.')
    else:
      print('O valor do seu saque é maior do que o permitido (R$ 500.00).')

  elif escolha.upper() == 'E':
    if extrato == f'Saldo inicial: R$ {saldo}\n':
      print('Não foram realizadas movimentações.')
    else:
      print(extrato + f'Saldo atual: R$ {saldo}')

  elif escolha == '0':
    break

  else:
    print('Escolha inválida.')
