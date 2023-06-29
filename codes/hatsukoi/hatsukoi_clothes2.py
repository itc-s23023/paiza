def f(n, m):
    if m % n == 0:
        return "ok"
    else:
        return "ng"

n, m = map(int, input().split())

result = f(n, m)
print(result)


#def f(n ,m):
#    return "ok" if m % n == 0 else "ng"
