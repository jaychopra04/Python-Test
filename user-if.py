x= input('Enter your favourite number')
x= int(x)
if x < 10:
    print('Low')
elif x<20 :
    print('Medium')
elif x<50 :
    print('High')
elif x<100 :
    print('V- high')
elif x<500 :
    print('Extreme')
else:
    print('Number is greater than 500')
    x=x-2
    print(x)


print('ALL DONE JAY!!')