def temp(x):
    sum=0
    for i in range(1,x):
        if (i%3 == 0) or (i%5 == 0):
            sum += i
    else:
        return sum

print(temp(10)) 
print("answer: ", temp(1000))