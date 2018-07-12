import numpy as num
import time
import pandas as pd
import matplotlib.pyplot as plt


res = pd.DataFrame(columns=["res1","res2","res3"])
fig = plt.figure()

def AddList(N,M):
    return [[int(x%2)*(x+1) for x in range(N*i,N*i+N)] for i in range(M)]

def AddMas(a):
    return num.array(*[a],dtype = "int32")

def ListNZ(a,N,M):
    return [[i,i2] for i in range(M) for i2 in range(N) if not a[i][i2] == 0]

def NumArrNZ(b):
    return num.transpose(num.nonzero(b))

temp = []
temp2 = []
temp3 = []

for i in range(10,120,50):
    a = AddList(i,i)
    b = AddMas(a)
    

    for z in range(50):
        start = time.time()
        ListNZ(a,i,i)
        temp.append(time.time() - start)
    for z in range(50):
        start = time.time()
        ListNZ(b,i,i)
        temp2.append(time.time() - start)
    for z in range(50):
        start = time.time()
        NumArrNZ(b)
        temp3.append(time.time() - start)
    
    res = pd.DataFrame({'res1': temp,
                        'res2': temp2,
                        'res3': temp3})
    
#print(res)
def showw(a):
    plt.grid(True)
    plt.plot(a)
    plt.legend(["list & list func","numpy & list func","numpy & numpy func"],loc=2)
    plt.show()

showw(res[res.index<50])
showw(res[(res.index>=50)&(res.index<100)])
showw(res[(res.index>=100)&(res.index<150)])