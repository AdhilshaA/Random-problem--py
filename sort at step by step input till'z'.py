inp = None
list1=[]
while inp is None:
    inp1 = input('Enter the number:')
    if inp1 != 'z':
        list1.append(int(inp1))
        for i in range(len(list1)-1,0,-1):
            ##print('Checking for i =',i) 
            if i != 0 and list1[i] < list1[i-1]:
                ##print('swap')
                list1[i-1],list1[i] = list1[i],list1[i-1]
            else:
                break
        print(list1)
    else:
        break

print('Final result:',list1)
