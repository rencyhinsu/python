#print("Hello world")
#input("enter the number ")
#age=15#
#if(age<18):#
 #   print("minor")
#elif(age>=18 and age<40):
#    print("adult")
#else:
#    print("senior citizen")
#for i in range(10):
#    print(i)
#for i in range(2,10):
#    print(i)
#for i in range(2,10,2):
#    print(i)
#for i in range(10,0,-1):
#    print(i)
#    print(" "*(4-i),"* "*i)
#for i in range(1,5):
#
#for i in range(3,0,-1):
#     print(" "*(4-i),"* "*i)

lst = [1,3,5,4]
print(len(lst))
lst.append(5)
print(lst)
lst.extend([6,7])
print(lst)
print(lst.count(5))
lst.insert(2,10)
print(lst)

print(lst[2])
print(lst[2:6]) #print upto n-1
print(lst[2:10000]) #automatically take last index

lst.sort()
print(lst)
lst.sort(reverse=True)

print(lst)

lst.remove(5)
print(lst)


