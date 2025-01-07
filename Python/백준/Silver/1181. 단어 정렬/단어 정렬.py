N = int(input())

chars=[[] for _ in range(51)]

for _ in range(N):
    char = input()
    if char not in chars[len(char)]:
        chars[len(char)].append(char)
        chars[len(char)].sort()

for element in chars:
    if type(element) == list:
        for sub_element in element:
            print(sub_element)
    elif element:
        print(element)