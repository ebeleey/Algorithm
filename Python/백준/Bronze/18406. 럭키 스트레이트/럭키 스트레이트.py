# 럭키 스트레이트

scores = input()

half_len = len(scores)//2
left_sum = 0
right_sum = 0

for i in range(half_len):
    left_sum += int(scores[i])
    right_sum += int(scores[-i-1])

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')