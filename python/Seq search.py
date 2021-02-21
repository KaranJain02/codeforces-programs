def seqsearch(left,right,l,x):
    u=left
    found=False
    
    while(not found and u<right):
        if l[u]== x:
            found = True
        else: 
            u=u+1
    print (found)

seqsearch(0,2,[2,5,4,6,7,8,4],4)