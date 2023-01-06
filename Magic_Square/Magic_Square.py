def Magic(n):
    magicSquare=[[0 for a in range(n)] for b in range(n)]
    i=n/2
    j=n-1
    num=1
    while num<=(n**2):
        if i==-1 and j==n:
            j=n-2
            i=0
        else:
            if j==n:
                j=0
            if i<0:
                i=n-1
        if magicSquare[int(i)][int(j)]:
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[int(i)][int(j)]=num
            num=num+1
        j=j+1
        i=i-1
    for a in range(0,n):
        for b in range(0,n):
            print(magicSquare[a][b],end=" ")
            if b == n -1:
                print()
    print("The magic number of ",n," is ",(((n**2)+1)*n)/2,"\n")

size = int(input("Enter the size of the magic square you want to create: "))
Magic(size)