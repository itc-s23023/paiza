def f():
    n = int(input())  
    
    words = [input() for _ in range(n)]  
    
    result = '_'.join(words)  
    
    return result

result = f()
print(result)

