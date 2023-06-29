def f(M, N):
    if M - N >= 0:
        result = M - N
    else:
        result = 0
    return result

M, N = map(int, input().split())

result = f(M, N)
print(result)

#def f(M, N):
#    result = M - N if M - N >= 0 else 0
#    return result

