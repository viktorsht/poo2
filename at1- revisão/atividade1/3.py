taxa_ir = 0.11
taxa_inss = 0.08
taxa_sindicato = 0.05
salario = float(input())
imposto_renda = (salario * taxa_ir)
inss = (salario * taxa_inss)
sindicato = (salario * taxa_sindicato)
print("Salário: R$ %.2f" %(salario))
print("IR (11%%): R$ %.2f" %(imposto_renda))
print("INSS (8%%): R$ %.2f" %(inss))
print("Sindicato (5%%): R$ %.2f" %(sindicato))
print("Salário líquido: R$ %.2f" %(salario - imposto_renda - inss - sindicato))
