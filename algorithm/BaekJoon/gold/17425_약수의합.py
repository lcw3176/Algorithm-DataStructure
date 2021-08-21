import sys
result = [0] * 1000001

for j in range(1, len(result)):
    for i in range(j, len(result), j):
        result[i] += j
    result[j] += result[j - 1]

T = int(sys.stdin.readline())
for i in range(T): 
    print(result[int(sys.stdin.readline())])

# 케이스들을 미리 생성하는건
# 타임아웃에 안걸리는거 같다.