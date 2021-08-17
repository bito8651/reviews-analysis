data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # %用來求餘數
            print(len(data)) # print很花時間，所以會讀的比原本沒有按次print還慢很多
print(len(data))

print(data[0])
print('--------------')
print(data[1])