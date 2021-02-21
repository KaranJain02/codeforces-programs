def clean(l):
    b=l[0:1]
    for i in range(1,len(l)):
        if l[i] != l[i-1]:
            b.append(l[i])
    return b

print(clean[1,1,2,2,3,5,8,9,9])