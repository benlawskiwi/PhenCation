import numpy as np
import matplotlib.pyplot as plt
import math

#stictch together all 1+1 scans
#First import 630-612nm that it already smoothed
xd,yd = np.loadtxt('../scans/1+1d.dat',unpack=True)
xc,yc = np.loadtxt('../scans/1+1c.dat',unpack=True)
xb,yb = np.loadtxt('../scans/1+1b.dat',unpack=True)
xa,ya = np.loadtxt('../scans/1+1a.dat',unpack=True)
#import nx031e scan
ye1 = np.loadtxt('../scans/nx031e_165.dat',unpack=True)
yeb = np.loadtxt('../scans/nx031e_baseline.dat',unpack=True)
ye = yeb-ye1
ye *= 1/4    #Account for the change in soure!
ye -= 20
ye = ye[9:]
xe = np.arange(610,604.9,-0.2)
xe = xe[9:]

#Now import scans one at a time, working our way towards the blue
f = ['32b','31c','31b','31a','30b','29c','41b','40d','40a','28a']
o = [-20,-40,-300,80,150,100,-80,-280,-580,550]
xx = []
yy = []

for i in range(0,np.size(f)):
    x,y = np.loadtxt('../scans/nx0'+str(f[i])+'_165.dat',usecols=(1,2),unpack=True)
    x = x[:-1]
    y = y[:-1]
    y *=-1
    if f[i] == '31c':
        y *= 1/4.0     #Account for the change in source!
    if f[i] == '32b':
        y *= 1/4
        y = y[9:]
        x = x[9:]
    if f[i] == '31a':
        y *=1/4
        y = y[:-5]
        x = x[:-5]
    if f[i] == '40a':
        y = y[:-26]
        x = x[:-26]
    if f[i] == '28a':
        y = y[18:]
        x = x[18:]
    y += o[i]
    for j in range(0,np.size(x)):
        xx.append(x[j])
        yy.append(y[j])
    plt.plot(x,y,label=f[i])

plt.plot(xe,ye,label='eee')

yc += 100
yb += 400
ya += 420

ox = [xa,xb,xc,xd]
oy = [ya,yb,yc,yd]
for i in range(0,np.size(ox)):
    x = ox[i]
    y = oy[i]
    for j in range(0,np.size(x)):
        xx.append(x[j])
        yy.append(y[j])


plt.plot(xd,yd)
plt.plot(xc,yc)
plt.plot(xb,yb)
plt.plot(xa,ya)
plt.legend()
plt.show()

xx = np.array(xx)
yy = np.array(yy)

#Now smooth data
avg = 2
xi = min(xx)
xf = max(xx)
xr = np.arange(xi,xf,0.2)
ys = []
xs = []
for i in range(0,np.size(xr)):
    subr = np.logical_and(xx>xr[i]-avg,xx<xr[i]+avg)
    #print('range = '+str(xr[i]-avg)+' - '+str(xr[i]+avg))
    yr = yy[subr]
    ynew = np.mean(yr)
    ys.append(ynew)
    xs.append(xr[i])

np.savetxt('ieCurve3.dat',np.column_stack((xs,ys)))

plt.plot(xx,yy,'*',label='1+1 scans')
plt.plot(xs,ys,lw='2',label='averaged')
plt.legend()
plt.show()
