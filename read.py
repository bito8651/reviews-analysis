# 求清單中資料筆數
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # %用來求餘數
            print(len(data)) # print很花時間，所以會讀的比原本沒有按次print還慢很多
print('檔案讀取完了，總共有',len(data), '筆資料')

# 取留言平均長度(字元)
sum_len = 0
for d in data: # 將data清單中每一筆取出的字串(留言)稱為d變數
    sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))

# 篩選
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])