# 1 - Perguntar para o usuário o tipo de operação
# 2 - Perguntar o primeiro número
# 3 - Perguntar o segundo número
# 4 - Apresentar o resultado
# 5 - Sair do programa
print('=====================================')
print('============ Calculadora ============')
print('=====================================')
while True:

    operacao = input("Qual a operação você deseja realizar? (+, -, *, /). Para sair digite 'q'.")
    if operacao == 'q' or operacao == 'Q':
        print('Sistema finalizado! ')
        break
    else:
        num1 = int(input('Informe o primeiro número:'))
        num2 = int(input('Informe o segundo número:'))

        if operacao == '+':
            total = num1 + num2
            print(f'{num1} + {num2}  = {total} ')
        elif operacao == '-':
            total = num1 - num2
            print(f'{num1} - {num2} = {total}')
        elif operacao == '*':
            total = num1 * num2
            print(f'{num1} + {num2} = {total}')
        elif operacao == '/':
            total = num1 / num2
            print(f'{num1} / {num2} = {total}')
        else:
            print('Deve ser informado da segunte forma. (+, -, *, /) ou (q) para sair do sistema. ')

