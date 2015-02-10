def temp(n1, n2):
    if ( n1 == n2 ): 
            return n1;

    while (n2 != 0):
        r  = n1 % n2
        n1 = n2
        n2 = r
    else:
        return n1

def lcm(n1,n2):
    return int( n1 * n2 / temp(n1,n2) )

t = 1
for i in range(2, 21):
    t = lcm(i, t)
print("answer: ", t)