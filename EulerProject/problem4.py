def temp(n):
    a = list(str(n)) # turn the number into a list
    b = list(reversed(a))
    if (a == b):
        return True
    else:
        return False

def numbers(n):
    a = []
    min = 10 ** (n - 1)
    max = 10 ** n - 1
    msum = 0    

    for i in range (max, min + 1, -1):
        for j in range (i, min + 1, -1):
            sum = i * j
            if (sum > msum):
                if (temp(sum)):
                    msum = sum
                    a = []
                    a.append(i)
                    a.append(j)
                    break
    else:
        return msum

print(numbers(2))
print("answer: ", numbers(3)) 