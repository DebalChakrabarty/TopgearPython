def ruler(n):
    a= range(10)
    l = []
    for i in range(1,n+1):
        l.append(str(a[i%10]))
    return ''.join(l)
print(ruler(43))
