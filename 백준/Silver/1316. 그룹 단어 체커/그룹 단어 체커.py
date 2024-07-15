N = int(input())
word = []
count = 0
history = []

for i in range(N):
  word.append(input())

result = 0

for i in range(N):
  presWord = word[i]
  history=[]
  history.append(presWord[0])
  temp = 0
  if(len(presWord)==1):
    result+=1
  else:

    for j in range(len(presWord)-1):
      if(presWord[j]!=presWord[j+1]):
        if(presWord[j+1] not in history):
          history.append(presWord[j+1])
        else:
          break
      temp+=1
      if(temp == len(presWord)-1):
        result+=1


print(result)