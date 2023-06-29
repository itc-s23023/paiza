def f():
    votes = [input() for _ in range(5)]
    
    count_yes = votes.count('yes')
    count_no = votes.count('no')
    
    if count_yes > count_no:
        result = 'yes'
    else:
        result = 'no'
    
    return result
result = f()
print(result)

