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

good = []
for d in data:
    if 'good' in d: # 如果good有在d字串裡面
        good.append(d) # 就把該字串加進good清單
print('一共有', len(good), '筆留言提到good')
print(good[0])
# list comprehension（清單快寫法）
good = [d for d in data if 'good' in d] # line 28 to line 31
print(good)
# line 28 to line 31 的寫法是把符合條件的留言一個一個append進去list裡面
# 當把這邊的d替換成1
good = [1 for d in data if 'good' in d] # line 28 to line 31
print(good)
# 以1為例，在跑for loop時，只要符合條件，就把1裝進good清單裡面。
# 迴圈跑完後，清單裡面會有很多個1，而不是像原本的一則一則留言d。
# 適用於不需要將原本東西原封不動裝進清單的狀況
# line 35 的第一個d是指data中的每一個d，就是原本的字串(留言)原封不動裝進去good清單裡面當d裡面包含'good'時

bad = ['bad' in d for d in data]
# 'bad' in d 是True/False的運算
print(bad)