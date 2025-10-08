horas_trabalhadas = float(input('Digite o total de horas trabalhadas na semana: '))
valor_hora_normal = float(input('Digite o valor da sua hora de trabalho (R$): '))

jornada_padrao = 44

if horas_trabalhadas > jornada_padrao:
    horas_extras = horas_trabalhadas - jornada_padrao
    valor_hora_extra = valor_hora_normal * 1.5
    total_hora_extra = horas_extras * valor_hora_extra
    print(f'Total: {horas_extras} horas extras a R$ {valor_hora_extra} cada, totalizando R$ {total_hora_extra:.2f}')

else:
       print('Jornada de trabalho cumprida corretamente.')