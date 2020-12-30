coin = [500, 100, 50, 10]
n = int(input())

count = 0

for i in coin :
    count += n // i
    n %= i

print(count)