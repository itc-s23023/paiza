def f(p):
    points = p // 100  
    if p >= 1000:
        points += 10
    return points

p = int(input())

result = f(p)
print(result)


#def f(p):
#    points = p // 100
#    points += 10 if p >= 1000 else 0
#    return points

