#condições para se estabelear TUG e TUE
perimetro = ""
print('banheiro')
print('''-->Pelo menos um ponto de tomada,
próximo ao lavatório, com uma distância
mínima de 60 cm do boxe.''')
Qtug1 = int(input('informe o numero de tomadas do banheiro:'))
if Qtug1 <= 3:
    p = Qtug1 * 600
else:
    p =(3*600) + ((Qtug1-3)*100)

print('=================================')
print('Cozinhas,copas, áreas de serviço e lavanderias')
print('''-->No mínimo um ponto de tomada para
cada 3,5 m, ou fração de perímetro,
sendo que acima da bancada da pia
devem ser previstas no mínimo duas
tomadas de corrente. ''')
Qtug2 = int(23/3.5)
print(Qtug2)
print('=================================')
print('varandas')
print('-->pelo menos um ponto de tomada')
print('=================================')

print('Salas e dormitórios')
print('''-->No mínimo um ponto de tomada
para cada 5 m, ou fração de
perímetro, devendo ser
espaçados uniformemente.
''')
print('=================================')
print('outros comodos')
print('''--> quantidade mínima de tomadas. Demais cômodos

Um ponto de tomada se a área
for igual ou inferior a 6 m2. Um
ponto de tomada para cada 5 m,
ou fração, de perímetro se a área
for superior a 6 m2.
''')
print('=================================')

#Condições para se estabelecer a potência mínima de tomadas de uso geral (TUG’s)

print('banheiros, cozinhas,copas,copas-cozinhas,áreas de serviços, lavanderias e locais semelhantes')
print('---> atribuir, no minimo 600VA por tomada até 3 tomadas')
print('---> atribuir 100VA para os excendentes.')

print('demais comodos ou dependências')
print('---> atribuir, no minimo 100VA por tomada')