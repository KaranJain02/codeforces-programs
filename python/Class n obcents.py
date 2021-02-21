class Course:
    def __init__(self,Code,Fullname,Lectures,tuts,labs):
        self.Code=Code
        self.Fullname=Fullname
        self.Lectures=Lectures
        self.tuts=tuts
        self.labs=labs

class Slot:
    def __init__(self,day,start,end):
        self.day=day
        self.start=start
        self.end=end

col100=Course("Col100","intro to CS",[Slot("Fri",13,15)
,Slot("thu",14,16)],[],[Slot("Fri",14,19)])
#mtl100=...

#tt=[col100,mtl100,..]

#print(tt[0].Lectures[-1].start)

class Rational:
    def __init__(self,p,q):
        if p>0 and q<0:
            self.p=-p
            self.q=-q
        else:
            self.p=p
            self.q=q
    def __add__(self,r):
        p=self.p * r.q + self.q * r.p
        q=self.q * r.q
        return(p,q)
    def __repr__(self):
        return 'Rational({},{})'.format(self.p, self.q)
    def __str__(self):
        return '{}/{}'.format(self.p, self.q)
    
def addOne1(r):
    r.p=r.p + r.q
    return r
def addOne2(r):
    return(Rational(r.p + r.q,r.q))
a=Rational(1,2)
b=a
c=addOne2(a)
print(a)
print(b)
print(a)

    

print(Rational(1,2) + Rational(3,4))

