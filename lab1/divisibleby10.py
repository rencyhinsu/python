number=int(input("enter a number:"))
def divisibility():
    if(number<=0):
        print("enter valid number")
    elif(number%10==0):
        print(number,"is divisible by 10")
    else:
        print(number,"not divisible by 10")
divisibility()  