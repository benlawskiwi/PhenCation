import numpy as np
import matplotlib.pyplot as plt

height=10
width = height*1.4

fig = plt.figure(figsize=(width,height))
ax = fig.add_subplot(111)
x1,y1 = np.loadtxt('ieCurve1.dat',unpack=True)
x2,y2 = np.loadtxt('ieCurve2.dat',unpack=True)
x3,y3 = np.loadtxt('ieCurve3.dat',unpack=True)

x3 *=0.5
x2 *=0.5
x1 *=0.5


plt.plot(x1,y1,'C0',label='1 laser')
plt.plot(x2,y2,'C0')
plt.plot(x3,y3,'C2',label='1+1 REMPI')

plt.xlabel('UV wavelength (nm)',fontsize=14)
plt.ylabel('intensity (arb. u.)',fontsize=14)
plt.legend(fontsize=14)
plt.savefig('ieCurve4.pdf',dpi=300,bbbox_inches='tight')
#plt.show()
plt.plot((326,326),(60,318),'--C7',lw=0.5)
plt.plot((303,309),(240,930),'--C7',lw=0.5)
#plt.arrow(326,318,0.05,5)

#subplots
xl = ((312,331),(291,310),(266,286))
yl = ((0,155),(0,500),(0,1700))
ax = ((0.78,0.3,0.10,0.15),(0.7,0.55,0.10,0.15),(0.4,0.4,0.10,0.15))
xti = ((315,320,325,330),(295,300,305,310))
for i in (0,1):
    ax2 = fig.add_axes(ax[i])
    #ax2.figure(figsize=(4,4))
    plt.xlim(xl[i][0],xl[i][1])
    plt.ylim(yl[i][0],yl[i][1])
    ax2.plot(x1,y1,'C0',label='1 laser')
    ax2.plot(x2,y2,'C0')
    ax2.plot(x3,y3,'C2',label='1+1 REMPI')
    ax2.set_yticks([])
    ax2.set_xticks(xti[i])
    fn = 'ieCurve'+str(i)+'.pdf'
    #plt.savefig(fn,dpi=300,bbbox_inches='tight')
    #plt.show()

plt.savefig('ieCurve-insert.png',dpi=300,bbbox_inches='tight')
plt.show()
