def selsort(l):
    
    for i in range(len(l)):
        min=i
        for k in range(i+1,len(l)):
            if l[k]<l[min]:
                min=k
        l[i],l[min]=l[min],l[i]
    return l

print (selsort([8,5,9,4]))

