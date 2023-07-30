#Faixa etária dos atletas
#Importando biblioteca
#Cabeçalho
from datetime import time, datetime
print('=' * 30)
print('{:^}'.format('Faixa etária dos atletas'))
print('=' * 30)
atual = datetime.today().year
#Inserindo variáveis
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
#Condições
if idade<14 and idade<=18:
    print('Classificação: JUNIOR')
elif idade<=9:
    print('Classifiação: MIRIM')
elif idade>9 and idade<14:
    print('Classificação: INFANTIL')
elif idade<=25 and idade>=19:
    print('Classificação: SENIOR')
else:
    print('Classificação: Master')
