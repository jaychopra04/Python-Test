
# z<0 --> no access
# z between 0 to 29 access with id 200 to 300
# z between 30 to 50 access with id==name
nam = input('Who are you')
print ('Welcome', nam)

z=int(input("Your number"))
if z<0:
    print("you are not authorised to access")

elif z<30:
    b=int(input("enter your id"))
    if b>200 & b<300:
        print("access granted")
    else:
        print("sorry...no access")
elif z<50:
    c=input("Your your id")
    if c==nam:
        print("access granted")
    else:
        print("no authorisation found")
else:
    print("You can close program you neither have no. nor id")
    


