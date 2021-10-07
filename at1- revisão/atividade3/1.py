base = int(input())
exp = int(input())

for i in range(1,exp+1):
    if(i == 1):
        aux = base * i
    else:
        aux = aux * base
print(aux)
