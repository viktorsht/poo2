limite = 50.00
valor_multa = 4.00
peso = float(input())
if(peso > limite):
    excesso = peso - limite
    multa = valor_multa * excesso
    print("Excesso: %.2f Kg" %(excesso))
    print("Multa: R$ %.2f" %(multa))
