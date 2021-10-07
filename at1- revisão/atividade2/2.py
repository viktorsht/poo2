gasolina_valor = 4.53
alcool_valor = 3.45
limite = 20.00
litros = float(input("Litros: "))
combustivel = input("Combustível: ")
if(combustivel == 'a'):
    valor = litros * alcool_valor
    if(litros <= limite):
         desconto = alcool_valor * 0.03
         desconto *= litros
         valor = valor - desconto
    else:
        desconto = alcool_valor * 0.05
        desconto *= litros
        valor = valor - desconto
elif(combustivel == 'g'):
    valor = litros * gasolina_valor
    if(litros <= limite):
        desconto = gasolina_valor * 0.04
        desconto *= litros
        valor = valor - desconto
    else:
        desconto = gasolina_valor * 0.06
        desconto *= litros
        valor = valor - desconto
print("Valor: %.2f" %(valor))
