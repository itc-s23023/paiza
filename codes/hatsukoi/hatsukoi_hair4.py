def f():
    answers = [input().split() for _ in range(5)]
    result = "OK" if sum(d == e for d, e in answers) >= 3 else "NG"
    return result

result = f()
print(result)

