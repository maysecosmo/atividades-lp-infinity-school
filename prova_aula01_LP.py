tempo_servico=int(input("Digite o tempo de serviço em anos: "))
fgts=float(input("Digite o valor do FGTS: "))

if tempo_servico>=1:
    multa=fgts*0.4

    print(f"A multa será de R$ {multa:.2f} (40% do FGTS).")

else:
    print("O funcionário não tem direito à multa rescisória.")