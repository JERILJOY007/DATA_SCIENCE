a=int(input("ENTER THE LIMIT"))
for i in range(2,a+1):
    for j in range(2,i):
        if i%j==0:
            print(i)
            break