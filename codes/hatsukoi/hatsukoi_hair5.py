def f():
    s = int(input("文字列の合計の長さを入力してください"))
    t = int(input("+の位置を入力してください"))
    result = ''.join(['-' if i != t - 1 else '+' for i in range(s)])

    return result

result = f()
print(result)

