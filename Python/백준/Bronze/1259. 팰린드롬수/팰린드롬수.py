while(1):
    num = input()
    flag = True
    if(num == '0'):
        break
    else:
        if(len(num)%2==0):
            iRange = len(num)//2
        else:
            iRange = (len(num)-1)//2

        for i in range(iRange):
            if num[i]==num[-i-1]:
                flag = True
            else:
                flag = False
                break
        if(flag == True):
            print("yes")
        else:
            print("no")