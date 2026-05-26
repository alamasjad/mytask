def fizzbuzz(st,en):
    for i in range(st,en+1):
        if i%3==0:
            print("Fizz",end=" ")
        elif i%5==0:
            print("Buzz",end=" ")
        else:
            print(i,end=" ")

# fizzbuzz(10,15)

def primechecker(n):
    for i in range(2,int(n**0.5)):
        if n%i==0:
            print(f"{n} is not a Prime")
            return
    else:
        print(f"{n} is a Prime")

primechecker(int(input("Enter The number for prime checking:")))