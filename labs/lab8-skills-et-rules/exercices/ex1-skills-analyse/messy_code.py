def calc(a,b,c):
    x=a+b
    y=x*c
    z=y/2
    return z

def process(data):
    result=[]
    for i in range(len(data)):
        if data[i]>0:
            result.append(data[i]*2)
    return result

class User:
    def __init__(self,n,e,a):
        self.n=n
        self.e=e
        self.a=a
    def get_info(self):
        return self.n+' '+self.e+' '+str(self.a)

# Made with Bob
