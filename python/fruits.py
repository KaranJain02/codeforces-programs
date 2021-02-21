def stringProblem(A,B):
    n=len(A)
    m=len(B)
    def consvow(A): # Checks if the character is a vowel or not
        if A == 'a' or A == 'e' or A == 'i' or A == 'o' or A == 'u':
            return True
        else:
            return False 
    def conrow (Ai,Bs): # Finds minimum no. of steps req to convert an alphabet(Ai) into req string(Bs)
        if Ai in Bs: # If Ai already exists in Bs we just have to insert rest of the elements(i.e len(Bs)-1 elements) 
            return len(Bs)-1
        elif consvow(Ai) == True: # if alphabet Ai is a vowel
            q = 0
            for p in Bs: 
                q+=consvow(p) # Checks no. of vowels in string Bs
            if q==0: # if there are no vowels in string Bs
                return(1+len(Bs)) #  2 steps to convert vowel Ai into any consonant in Bs and inserting rest of the elements
            else: # if a vowel exists in Bs
                return(len(Bs)) # 1 step to convert vowel Ai to any of the vowel in Bs and inserting rest of the elements
        else: # Ai doesnt exist in Bs and is a consonant
            return len(Bs) # 1 step to convert Ai into any element in Bs and inserting rest of the elements
    def concom (As,Bi): # Finds minimum no. of steps to convert a string As into alphabet Bi
        if Bi in As:
            return len(As)-1
        elif consvow(Bi) == False:
            q=0
            for p in As:
                q+=consvow(p)
            if q==len(As):
                return(1+len(As))
            else:
                return(len(As))
        else:
            return(len(As))
    
    grid=[[0 for i in range(m)] for i in range(n)]
    for i in range (m):
        grid[0][i]=conrow(A[0],B[:i+1])
    for i in range (1,n):
        grid[i][0]=concom(A[:i+1],B[0])
    for i in range (1,n):
        for j in range (1,m):
            grid[i][j]=min(grid[i-1][j]+1,grid[i][j-1]+1,grid[i-1][j-1]+conrow(A[i],B[j]))
    return grid[n-1][m-1]

print(stringProblem("bplpcd","apple"))