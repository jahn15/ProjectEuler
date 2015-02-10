def temp(x):
    f   = [1]
    a,b = 1,2
    while b < x:
        f.append(b)
        a,b =b,a+b
    else:
        return f

def even(x):
    f   = []
    a,b = 1,2
    while b < x:
        if ( b%2 == 0 ): f.append(b)
        a,b = b,a+b
    else:
        return f
      
def fib(x):
    sum = 0
    a,b = 1,2
    while b < x:
        if ( b%2 == 0 ): sum += b
        a,b =b,a+b
    else:
        return sum

print(temp(10))
print(sum(temp(10)))
print(sum(even(4000000)))
print("answer: ", fib(4000000))    