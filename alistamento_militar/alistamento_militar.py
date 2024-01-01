# importei a biblioteca datatime para leitura do ano atual
from datetime import date

atual = date.today().year
ano = int(input('Informe o seu ano de nascimento:'))
sexo = input('Informe seu sexo (Masculino/Feminino): ')

if sexo.lower() == 'feminino':
    print('Você não precisa se alistar, o alistamento é obrigatório apenas para indivíduos do sexo masculino.')
else:
    idade = atual - ano
    print('Sua idade atual é: {}'.format(idade))

    if idade == 18:
        print('Você está no ano do seu alistamento.')
    elif idade < 18:
        a1 = 18 - idade
        print('Ainda falta {} anos para o seu alistamento.'.format(a1))
        b1 = atual + a1
        print('Seu alistamento será em: {}.'.format(b1))
    elif idade > 18:
        a2 = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(a2))
        b2 = atual - a2
        print('Seu alistamento foi em {}.'.format(b2))
