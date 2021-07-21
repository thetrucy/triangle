h= int(input('Enter height: '))
for i in range(2*h-1,0,-1):
    print(' * ',end=' ')
print()
for i in range(h-1,0,-1):
    for n in range(2*h-1):
        if n == h+i-2 or n == h-i :
            print(' * ',end=' ')
        else: 
            print('  ',end='  ')
    print()
