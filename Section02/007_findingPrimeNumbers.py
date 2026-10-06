for n in range(2,10):
    for i in range(2,n):
        if n % i==0:
            print("n is  not prime : {}".format(n))
            break
    else:
        print(f"Prime {n}")
    
        