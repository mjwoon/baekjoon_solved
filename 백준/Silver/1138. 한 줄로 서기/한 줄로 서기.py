import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = [0] * n

# 1. 키 작은 사람부터 결과 넣기
for i, a in enumerate(arr):
    count = 0  # 앞에 키큰 사람 넣은 횟수
    for j, res in enumerate(result):
        # 2. 아직 아무도 안 채워지고, 앞에 키큰 사람으로 더 채워야하는 경우: count 늘리기
        if res == 0 and count < a:
            count += 1
         # 3. 아직 아무도 안 채워지고, count 와 a가 동일한 경우: 현재 학생 넣기
        elif res == 0 and count == a:
            result[j] = i + 1
            break
print(*result)