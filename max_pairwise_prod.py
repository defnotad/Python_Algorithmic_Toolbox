n = int(input())
arr = []
arr = list(map(int, input().split()))
max1 = -1
for i in range(n):
    if(max1 < arr[i]):
        max1 = arr[i]
arr.remove(max1)
max2 = -1
for i in range(n-1):
    if(max2 < arr[i]):
        max2 = arr[i]
print(max2*max1)
