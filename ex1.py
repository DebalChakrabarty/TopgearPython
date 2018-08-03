def ruler(n):
    a= range(10)
    l = []
    j = 1
    for k in range(1,n+1):
        if k%10 == 0:
            print(j,end='')
            j+=1
        else:
            print(" ",end='')
    print("")
    for i in range(1,n+1):
        l.append(str(a[i%10]))
    return ''.join(l)
print(ruler(43))
print(ruler(5))
print(ruler(80))
print(ruler(25))
print(ruler(51))
