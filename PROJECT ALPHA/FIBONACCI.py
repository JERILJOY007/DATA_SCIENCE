num=int(input("ENTER THE NUMBER"))
a=0
b=1
print("FIRST",num,"FIBONACCI SERIES ARE")
for _ in range(num):
    print(a,end=" ")
    a,b=b,a+b
print()
