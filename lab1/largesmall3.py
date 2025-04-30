a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
def comp():
    if(a>b and a>c):
        if(b>c):
            print(a,"is largest and",c,"is smallest")
        else:
            print(a,"is largest and",b,"is smallest")
    if(b>a and b>c):
        if(a>c):
            print(b,"is largest and",c,"is smallest")
        else:
            print(b,"is largest and",a,"is smallest")
    if(c>b and c>a):
        if(b>a):
            print(c,"is largest and",a,"is smallest")
        else:
            print(c,"is largest and",b,"is smallest")
comp()