a=int(input("enter a number :"))

if a%5==0 and a%11==0:
    print("its divisible")
elif a%5==0:
    print("only divisible by 5")
elif a%11==0:
    print("only divisible by 11")
else:
    print("its not divisible")
