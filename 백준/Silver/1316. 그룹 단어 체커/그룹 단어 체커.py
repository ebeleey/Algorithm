N = int(input()) #단어의 개수 
word = []
count = 0
history = []

for i in range(N):
  word.append(input()) #단어 입력받기

result = 0 #그룹단어 개수

for i in range(N):
  presWord = word[i] #현재 단어
  history=[] #한 단어 내에서 나온 소문자 체크
  history.append(presWord[0]) #맨 첫 글자 추가
  temp = 0 
    
  if(len(presWord)==1): #한 글자 단어라면 그냥 중복문자
    result+=1
  else:
    for j in range(len(presWord)-1): 
      if(presWord[j]!=presWord[j+1]): #앞글자와 뒷글자가 다르고
        if(presWord[j+1] not in history): #뒷글자가 history 리스트에 없다면
          history.append(presWord[j+1]) #뒷글자를 history에 추가
        else: #앞글자와 뒷글자가 다른데, 뒷글자가 history리스트에 있다면 그룹단어가 아니므로 break
          break
      temp+=1 #반복문 한 번 돌때마다 temp++
      if(temp == len(presWord)-1): #break되지 않고 한 단어 끝까지 반복문이 돌면 그룹단어임
        result+=1

print(result)
