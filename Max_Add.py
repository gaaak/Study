n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 제일 큰 수
second = data[n-2] # 그 다음 큰 수

count_max = (m // (k+1))
count_last = (m % (k+1))

sum = (first*k + second) * count_max + (count_last * first )

print(sum)