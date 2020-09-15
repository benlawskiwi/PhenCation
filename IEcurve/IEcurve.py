import numpy as np
import matplotlib.pyplot as plt
import math

#Smoothing parameters for plot 2 - currently avg over 1nm range
avg = 5
stp = 0.2

#File names
l2 = ['23a','23c','24a','24c']  
l1 = ['23b','23d','24b','24d']

ax1 = plt.subplot(1,3,1)
ax2 = plt.subplot(1,3,2)
ax3 = plt.subplot(1,3,3)

#Convert 1 laser data into one file
x1=[]
y1=[]
for i in range(0,np.size(l2)):
    x,y = np.loadtxt('nx0'+str(l1[i])+'_165.dat',usecols=(1,2),unpack=True)
    x = x[:-1]
    y = y[:-1]
    y *= -1
    for j in range (0,np.size(x)):
        x1.append(x[j])
        y1.append(y[j])
    #plt.plot(x,y,'C1')

#Smooth for plot 2
x1 = np.array(x1)
y1 = np.array(y1)
inds = x1.argsort()
x1s = x1[inds]
y1s = y1[inds]

x1a = []
y1a = []
for i in range(0,np.size(x1s)):
    subr = np.logical_and(x1s>x1s[i]-avg*stp,x1s<x1s[i]+avg*stp)
    yr = y1s[subr]
    ynew = np.mean(yr)
    y1a.append(ynew)
    x1a.append(x1s[i])
ax1.plot(x1s,y1s,'C1',label='1 laser')
ax2.plot(x1a,y1a,'C1',label='1 laser')

#scatter plot 3
#scatter step size
step = 2
x1p=[]
y1p=[]
e1p=[]
r = math.floor((x1s[-1]-x1s[0])/step)
for i in range (0,r):
    xx = x1s[0]+i*2
    subr = np.logical_and(x1s>xx-step,x1s<xx+step)
    yr = y1s[subr]
    ynew = np.mean(yr)
    std = np.std(yr)
    e1p.append(std/np.sqrt(np.size(yr)))
    x1p.append(xx)
    y1p.append(ynew)

ax3.errorbar(x1p,y1p,yerr=e1p,color='C1',marker='o',markersize='4',ls='none',label='1 laser')

#Repeat the above for 2 laser signal
x2 = []
y2 = []
for i in range(0,np.size(l2)):
    x,y = np.loadtxt('nx0'+str(l2[i])+'_165.dat',usecols=(1,2),unpack=True)
    x = x[:-1]
    y = y[:-1]
    y *= -1
    if i == 0:
        y += 26.25
    if i == 3:
        y -= 18.975
    for j in range (0,np.size(x)):
        x2.append(x[j])
        y2.append(y[j])
    #plt.plot(x,y,'C0')

x2 = np.array(x2)
y2 = np.array(y2)
inds = x2.argsort()
x2s = x2[inds]
y2s = y2[inds]

x2a = []
y2a = []

for i in range(0,np.size(x2s)):
    subr = np.logical_and(x2s>x2s[i]-avg*stp,x2s<x2s[i]+avg*stp)
    yr = y2s[subr]
    ynew = np.mean(yr)
    y2a.append(ynew)
    x2a.append(x2s[i])
ax1.plot(x2s,y2s,'C0',label='1+1 REMPI')
ax2.plot(x2a,y2a,'C0',label= '1+1 REMPI')

#scatter plot
step = 2
x2p=[]
y2p=[]
e2p=[]
r = math.floor((x2s[-1]-x2s[0])/step)
for i in range (0,r):
    xx = x2s[0]+i*2
    subr = np.logical_and(x2s>xx-step,x2s<xx+step)
    yr = y2s[subr]
    ynew = np.mean(yr)
    std = np.std(yr)
    e2p.append(std/np.sqrt(np.size(yr)))
    x2p.append(xx)
    y2p.append(ynew)

ax3.errorbar(x2p,y2p,yerr=e2p,color='C0',marker='o',ls='none',markersize='4',label='1+1 REMPI')
plt.legend()

np.savetxt('../scans/1+1d.dat',np.column_stack((x2a,y2a)))
np.savetxt('../scans/2d.dat',np.column_stack((x1a,y1a)))

plt.show()
