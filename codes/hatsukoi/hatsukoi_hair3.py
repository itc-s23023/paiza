def f():
    n = int(input("数字を入力してください："))
    result = "lucky" if n % 7 == 0 else "unlucky"
    return result

result = f()
print(result)

