tabuada = int(input("Tabuada de: "))
begin = int(input("Começar em: "))
end = int(input("Finaliza em: "))
print("Vou montar a tabuada do %d começando de %d e termiando em %d" %(tabuada,begin,end))
for i in range(begin, end+1):
    valor = i * tabuada
    print("%d x %d = %d" %(tabuada,i,valor))
