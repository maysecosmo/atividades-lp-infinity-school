MULTA_PERCENTUAL_DIARIA = 0.02
DIAS_CARENCIA = 5

print('Calculadora de Multas por Atraso')

try:
    valor_salario = float(input('Digite o valor do salário:  '))
    dias_atraso = int(input(f'Digite o número de dias de atraso (carência de {DIAS_CARENCIA} dias): '))

    if dias_atraso > DIAS_CARENCIA:
        dias_a_multar = dias_atraso - DIAS_CARENCIA
        multa_diaria_valor = valor_salario * MULTA_PERCENTUAL_DIARIA
        multa_total = 0.0
            
        for dia in range(dias_a_multar):
            multa_total += multa_diaria_valor

        print(multa_total)
        print(f'Salário Base: R$ {valor_salario:.2f}')
        print(f'Dias de Atraso Total: {dias_atraso} dias')
        print(f'Dias Multados: {dias_a_multar} dias')
        print(f'Multa Diária: R$ {multa_diaria_valor:.2f}')
        print(f'VALOR TOTAL DA MULTA: R$ {multa_total:.2f}')
            
        valor_total_devido = valor_salario + multa_total
        print(f'Valor Total Devido: R$ {valor_total_devido:.2f}')

    else:
        print(multa_total)
        print(f'Dias de Atraso: {dias_atraso} dias. Sem Multa.')
        print('MULTA TOTAL: R$ 0.00')

except ValueError:
    print('ERRO: Digite números válidos para salário e dias de atraso.')
except Exception as e:
    print(f'Ocorreu um erro inesperado: {e}')
