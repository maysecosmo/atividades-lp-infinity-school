def calcular_ferias_proporcionais():
    print('--- Calculadora de Férias Proporcionais ---')

    while True:
        try:
            salario_mensal = float(input('Digite o Salário Mensal: '))
            if salario_mensal > 0:
                break
            else:
                print('O salário deve ser um valor positivo.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')

    while True:
        try:
            meses_trabalhados = int(input('Digite o número de meses trabalhados (1 a 11): '))
            if 1 <= meses_trabalhados <= 11:
                break
            else:
                print('O número de meses deve estar entre 1 e 11 para ser proporcional.')
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')

    valor_por_mes = salario_mensal / 12
    
    ferias_proporcionais = 0
    for _ in range(meses_trabalhados):
        ferias_proporcionais += valor_por_mes

    print('\n--- Resultado do Cálculo ---')
    print(f'Salário Mensal: R$ {salario_mensal:,.2f}')
    print(f'Meses Trabalhados: {meses_trabalhados}')
    print(f'Valor por 1/12: R$ {valor_por_mes:,.2f}')
    print(f'Férias Proporcionais: R$ {ferias_proporcionais:,.2f}')
    print('----------------------------')

calcular_ferias_proporcionais()