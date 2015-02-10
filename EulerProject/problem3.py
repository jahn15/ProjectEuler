import math

def main(x):
    if ( x == 1 ): return False
    
    maxN = math.floor(int(math.sqrt(x)))
    for i in range(2, maxN + 1):
        if (x % i == 0):
                return False
    else:
        return True
    
def status(x):
    a = []
    i = 2
    while i <= x:
        if (x % i == 0):
            x = x / i
            if main(i):
                a.append(i)
        i += 1
    return a

print(status(13195))
print(status(600851475143))
print("answer: ", max(status(600851475143)))