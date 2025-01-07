# FizzBuzz
# 1 2 Fizz 4 Buzz Fizz 7 8  Fizz Buzz 11 Fizz 13 14 FizzBuzz 순서
inputs = [0, 0, 0]

inputs[0] = input()
inputs[1] = input()
inputs[2] = input()

fizzbuzz = {0: 'FizzBuzz',
            1: '1',
            2: '2',
            3: 'Fizz',
            4: '4',
            5: 'Buzz',
            6: 'Fizz',
            7: '7',
            8: '8',
            9: 'Fizz',
            10: 'Buzz',
            11: '11',
            12: 'Fizz',
            13: '13',
            14: '14',
            15: 'FizzBuzz'
            }


num = 0 
for i in range(3):
    if inputs[i].isdecimal():
        num = int(inputs[i])//15
        inputs[i] = int(inputs[i])%15        
        break

# 답
index = (int(inputs[i]) + 3 - i)%15
if fizzbuzz[index].isdecimal():
    print(num*15 + int(inputs[i]) + 3 - i)
else: 
    print(fizzbuzz[index])
