nota1 = float(input('digite sua nota do 1° bimestre: '))
nota2 = float(input('digite sua nota do 2° bimestre: '))
nota3 = float(input('digite sua nota do 3° bimestre: '))
nota4 = float(input('digite sua nota do 4° bimestre: '))
media = (nota1+nota2+nota3+nota4)/4
if media >= 7: situacao = 'aprovado'
elif media < 7: situacao = 'reprovado'
print('sua média é',media,'\nVocê está',situacao)