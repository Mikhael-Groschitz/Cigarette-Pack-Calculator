# Solicitar informações ao usuário
anos_fumando = float(input("Quantos anos você fuma? "))
valor_maco = float(input("Qual é o valor atual do maço? R$ "))
maços_por_dia = float(input("Quantos maços você fuma por dia? "))

# Calcular o montante gasto
montante_gasto = anos_fumando * 365 * maços_por_dia * valor_maco

# Exibir mensagem de acordo com o critério
if montante_gasto < 20000:
    print(f"Com o valor R$ {montante_gasto:.2f}, você poderia ter dado entrada em um carro.")
elif 20000 <= montante_gasto <= 50000:
    print(f"Com o valor R$ {montante_gasto:.2f}, você poderia ter comprado um carro popular usado.")
else:
    print(f"Com o valor R$ {montante_gasto:.2f}, você poderia ter comprado um carro zero.")
