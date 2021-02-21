#s="1235"
#By default input is string
#n=(input("Please enter a number"))
#print(type(n))

#txt=input("any line with commas")
#print(txt.split(","))

#numinpu=input("enter some numbers with any spaces")
#L=numinpu.split(",")
#L1=[int(x) for x in L]
#print(L1)

print('IIt Delhi\n damn')

import time
for i in reversed(range(4)):
    if i > 0:
        print(i, end='>>>',flush=True)
        time.sleep(1)
    else:
        print('Start')


#(def dp(A):
 #   m=len(A)
  #  n=len(A[0])
   ###       return A[0][0] + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
#)#