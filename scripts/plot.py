import numpy as np
import matplotlib.pyplot as plt
import math

#filenames
l2 = ['22a','23a','23c','24a','24c','25c','26a','27b','27c','28a']
l1 = ['22b','23b','23d','24b','24d','25a','25d','26b','27d','27c']
avg = 10
stp= 0.2
xx = []
yy = []

for i in range(0,np.size(l2)):
    x,y = np.loadtxt('../scans/nx0'+str(l2[i])+'_165.dat',usecols=(1,2),unpack=True)
    x = x[:-1]
    y = y[:-1]
    y *=-1
    if l2[i] == '26a':
        #y *= 1220/883
        y *= 1210/823
        x = x[20:]
        y = y[20:]
    if l2[i] == '27c':
        #y *= 857/522
        y *= 1210/567
        x = x[10:]
        y = y[10:]
    if l2[i] == '27b':
        y *= 1210/810
        x = x[10:]
        y = y[10:]
    if l2[i] == '28a':
        x = x[20:]
        y = y[20:]
    plt.plot(x,y,label=l2[i])
    s0 = x[0]
    s1 = x[-1]
    print(l2[i],s0,s1)
    subr0 = np.logical_and(x>s0-2,x<s0)
    yr0 = y[subr0]
    ym0 = round(np.mean(yr0))
    subr1 = np.logical_and(x>s1,x<s1+2)
    yr1 = y[subr1]
    ym1 = round(np.mean(yr1))
    print(ym0,ym1)
    ym = round(np.mean(y))
    print(ym)
    print(' ')
    xs = []
    ys = []
    for j in range(0,np.size(x)):
        subr = np.logical_and(x>x[j]-avg*stp,x<x[i]+avg*stp)
        yr = y[subr]
        ynew = np.mean(yr)
        xs.append(x[j])
        ys.append(ynew)
    #plt.plot(xs,ys,'o')
    if l2[i] in ('25c','26a','27c','27b'):
        for k in range(0,np.size(x)):
            xx.append(x[k])
            yy.append(y[k])

xx = np.array(xx)
yy = np.array(yy)
inds = xx.argsort()
x1 = xx[inds]
y1 = yy[inds]
#plt.plot(x1,y1,'--')
x1s = []
y1s = []

avg = 10
stp = 0.2
for i in range(0,np.size(x1)):
    subr = np.logical_and(x1>x1[i]-avg*stp,x1<x1[i]+avg*stp)
    yr = y1[subr]
    ynew = np.mean(yr)
    y1s.append(ynew)
    x1s.append(x1[i])

plt.plot(x1s,y1s)
np.savetxt('../scans/1+1a.dat',np.column_stack((x1s,y1s)))

x1,y1 = np.loadtxt('../scans/nx022a_165.dat',usecols=(1,2),unpack=True)
x1 = x1[:-1]
y1 = y1[:-1]
y1 *=-1

x1s = []
y1s = []
for i in range(0,np.size(x1)):
    subr = np.logical_and(x1>x1[i]-avg*stp,x1<x1[i]+avg*stp)
    yr = y1[subr]
    ynew = np.mean(yr)
    y1s.append(ynew)
    x1s.append(x1[i])

plt.plot(x1s,y1s,'--')
np.savetxt('../scans/1+1c.dat',np.column_stack((x1s,y1s)))

x1,y1 = np.loadtxt('../scans/nx028a_165.dat',usecols=(1,2),unpack=True)
x1 = x1[:-1]
y1 = y1[:-1]
x1 = x1[20:]
y1 = y1[20:]
y1 *=-1
y1 += 200

x1s = []
y1s = []
for i in range(0,np.size(x1)):
    subr = np.logical_and(x1>x1[i]-avg*stp,x1<x1[i]+avg*stp)
    yr = y1[subr]
    ynew = np.mean(yr)
    y1s.append(ynew)
    x1s.append(x1[i])

plt.plot(x1s,y1s,'--')
np.savetxt('../scans/1+1b.dat',np.column_stack((x1s,y1s)))



plt.legend()
plt.show()








#Now try smoothing first
#avg = 5
#stp = 0.2

#for i in range(0,np.size(l2)):
#    x,y = np.loadtxt('../scans/nx0'+str(l2[i])+'_165.dat',usecols=(1,2),unpack=True)
#    x = x[:-1]
#    y = y[:-1]
#    y *=-1
#    xs = []
#    ys = []
#    for j in range(0,np.size(x)):
#        subr = np.logical_and(x>x[j]-avg*stp,x<x[i]+avg*stp)
#        yr = y[subr]
#        ynew = np.mean(yr)
#        xs.append(x[j])
#        ys.append(ynew)
#    plt.plot(xs,ys)

#plt.show()
