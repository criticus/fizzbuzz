for x in range(1,101):
    print("Fizz"*(x%3<1)+"Buzz"*(x%5<1) or x)
    
