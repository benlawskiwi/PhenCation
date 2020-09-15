import numpy as np
import matplotlib.pyplot as plt

f = ['a','b','c','d']
width = 3.33
height = width/1.4
one_col=(4*width,4*height)
fig = plt.figure(constrained_layout=True,figsize=one_col)
gs = fig.add_gridspec(2,3)
ax1 = fig.add_subplot(gs[:,:-1])
ax2 = fig.add_subplot(gs[1,2])
ax3 = fig.add_subplot(gs[0,2])

for i in range(0,np.size(f)):
    x,y = np.loadtxt('../scans/1+1'+str(f[i])+'.dat',unpack=True)
    x *=0.5
    if i == 0:
        ax1.plot(x,y,'C0',label="1+1' REMPI (320nm)")
    if i != 0:
        ax1.plot(x,y,'C0')

f = ['a','b','d']

for i in range(0,np.size(f)):
    x,y = np.loadtxt('../scans/2'+str(f[i])+'.dat',unpack=True)
    x *=0.5
    if i == 0:
        ax1.plot(x,y,'C1',label='1 laser')
    if i != 0:
        ax1.plot(x,y,'C1')

ax1.legend()
ax1.set_xlabel('wavelength of ionisation laser (nm)')


x1,y1 = np.loadtxt('../scans/1+1d.dat',unpack=True)
x2,y2 = np.loadtxt('../scans/2d.dat',unpack=True)
x1 *=0.5
x2 *=0.5

ax2.plot(x1,y1,'C0',label='1+1 REMPI')
ax2.plot(x2,y2,'C1',label='1 laser')
ax2.legend()

x3,y3 = np.loadtxt('../scans/nx026c_165.dat',usecols=(1,2),unpack=True)
x3 = x3[:-1]
y3 = y3[:-1]
y3 *=-1
x3 *=0.5

ax3.plot(x3,y3,'C1',label='1 laser')
ax3.legend()

plt.savefig('IEcurve.png', dpi= 400, bbox_inches='tight')





plt.show()





#fig = plt.figure(constrained_layout=True)
#gs = fig.add_gridspec(2,3)
#ax1 = fig.add_subplot(gs[:,:-1])
#ax2 = fig.add_subplot(gs[1,2])
#ax3 = fig.add_subplot(gs[0,2])

#plt.show()
