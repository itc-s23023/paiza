def f(n, m, song_lengths):
    total_length = 0  # 総再生時間
    # 曲の数だけ繰り返す
    for i in range(m): 
        # 曲の長さを総再生数に加える
        total_length += song_lengths[i] 
        # 総再生時間が制限を超えたとき
        if total_length > n * 60:  
            return i  
    return "OK"  

n = int(input())  # CDの最大長
m = int(input())  # 曲の数
song_lengths = []
for _ in range(m):
    t = int(input())  # 再生時間
    song_lengths.append(t)  # 再生時間をリストにつっこむ

result = f(n, m, song_lengths)  # resultにつっこむ 
print(result)  

