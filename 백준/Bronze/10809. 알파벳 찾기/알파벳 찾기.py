chars = input()

locate = [-1]*26
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in set(chars):
    if char in alphabet:
        locate[ord(char)-97] = chars.find(char)
    
for item in locate:
    print(item, end=' ')