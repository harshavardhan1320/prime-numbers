def prime_check(number):
    is_prime=True
    for num in range(2,n):
        if number % num==0:
            is_prime=False
    if is_prime==True:
        print(f"{n} number is a prime number")
    else:
        print(f"{n} number is not a prime")
    
n=int(input("check the number: "))
prime_check(number=n)



    
        


