import numpy as np
import matplotlib.pyplot as plt
import math

#stictch together all 1 laser scans
#First import 630-612nm that it already smoothed
xd,yd = np.loadtxt('../scans/2d.dat',unpack=True)
xb,yb = np.loadtxt('../scans/2b.dat',unpack=True)
xa,ya = np.loadtxt('../scans/2a.dat',unpack=True)

#Now import scans one at a time, working our way towards the blue
f = ['32a','32c','31d','30c','30a','29b','41a','40b']
o = [-35,-35,-35,20,-20,140,20,-40]
xx = []
yy = []

for i in range(0,np.size(f)):
    x,y = np.loadtxt('../scans/nx0'+str(f[i])+'_165.dat',usecols=(1,2),unpack=True)
    x = x[:-1]
    y = y[:-1]
    y *=-1
    if f[i] == '32c':
        y *=1/4
        x = x[10:]
        y = y[10:]
    if f[i] == '31d':
        y *=1/4
    if f[i] == '32a':
        x = x[:-1]
        y = y[:-1]
    if f[i] == '40b':
        x=x[:-12]
        y=y[:-12]
    y += o[i]
    for j in range(0,np.size(x)):
        xx.append(x[j])
        yy.append(y[j])
    plt.plot(x,y,label=f[i])

yb -= 40
ox = [xb,xd]
oy = [yb,yd]
for i in range(0,np.size(ox)):
    x = ox[i]
    y = oy[i]
    for j in range(0,np.size(x)):
        xx.append(x[j])
        yy.append(y[j])


plt.plot(xd,yd)
plt.plot(xb,yb)
plt.plot(xa,ya)

plt.legend()
plt.show()

#Now smooth data
avg = 1
xx = np.array(xx)
yy = np.array(yy)

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

#Savefiles
np.savetxt('ieCurve1.dat',np.column_stack((xs,ys)))
np.savetxt('ieCurve2.dat',np.column_stack((xa,ya)))

plt.plot(xx,yy,'*',label='1+1 scans')
plt.plot(xs,ys,lw='2',label='averaged')
plt.plot(xa,ya)
plt.legend()
plt.show()

