num = int(input('Digite um número inteiro:'))
print('-~~-'*13)
print('''Escolha uma das bases para conversão:
\033[1;36m[1]\033[m \033[1;36m Converte para Binário\033[m
\033[1;35m[2]\033[m \033[1;35m Converte para Octal\033[m
\033[1;32m[3]\033[m \033[1;32m Converte para Hexadecimal\033[m''')
print('-~~-'*13)
opcao = int(input('Qual a sua opção:'))
if opcao == 1:
    print('{} Convertido para Binário é igual a \033[1;36m{}\033[m'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} Convertido para Octal é igual a \033[1;35m{}\033[m'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para Hexadecimal é igual a \033[1;32m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('\33[1;31mOpção inválida tente novamente!\33[m')
