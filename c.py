def fib(number):
    if number<=0:
        print(0)
    elif number<=2:
        print(1)
    else :
        f=[0,1]
        for x in range(number):
            f= number[x-1]+ number[x-2]
            print(f)

x=[1,2,6,8,1,7,5]


fib([x])
