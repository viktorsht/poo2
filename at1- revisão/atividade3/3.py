while True:
    n = int(input())
    if(n < 0):
        exit()
    if(n > 16):
        n = int(input())
    else:
        fat = 1
        x = 1
        while(x<= n):
            fat*=x
            x+=1
        print("Fatorial: %d" %(fat))
