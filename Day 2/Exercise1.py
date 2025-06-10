def fibonacci(num):
    a=0
    b=1
    c=0
    result = [a,b]
    for n in range(num):
        c = a+b
        a=b
        b=c
        result.append(c)
    return result

print(fibonacci(10))
