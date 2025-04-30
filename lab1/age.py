def age():
    age= int(input("enter the age:"))
    status='minor' if age<18 else 'major'
    print(status)
age()