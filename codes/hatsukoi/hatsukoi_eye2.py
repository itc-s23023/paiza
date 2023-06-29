def f():
    a, b = map(int, input("空白区切りで２つの文字を入力してください：").split())
    if a >= b:
        result = "OK"
    else:
        result = "NO"
    return result

result = f()
print(result)



#def f():
#    a, b = map(int, input("空白区切りで２つの文字を入力してください：").split())
#    result = "OK" a >= b else "NO"
#    return result
