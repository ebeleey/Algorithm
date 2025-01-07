
n = int(input())

scores = list(map(float, input().split()))

max_score = max(scores)
scores_sum = 0

for score in scores:
    new_score = score / max_score * 100
    scores_sum += new_score

print(scores_sum / n)