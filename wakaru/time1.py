import time
old1 = time.time()
s = ''
for i in range(1000000):
    s += '根菜町１丁目２番地　人参n'
print(time.time() - old1, '秒')


old2 = time.time()
s = '根菜町１丁目２番地　人参n' * 1000000
print(time.time() - old2, '秒')