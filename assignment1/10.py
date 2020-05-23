min = int(input('min value:'))
max = int(input('max value:'))
sum = 0
for i in range(min, max + 1):
    if(i % 2 != 0):
        sum = sum + i

print('Sum of odd numbers from', min,'-', max,'is:', sum)