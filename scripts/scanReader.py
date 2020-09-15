import numpy as np
import matplotlib.pyplot as plt

f = input('Enter scan name (022a):')
m = 165

fn = '../scans/nx'+str(f)+'_'+str(m)+'.dat'

x,y = np.loadtxt(fn,usecols=(1,2),unpack=True)
x = x[:-1]
y = y[:-1]
y = y*-1

plt.plot(x,y)
plt.show()

s = input('Plot second scan? (Y/N):')

if s == 'Y':
    f = input('Enter scan name (022a):')
    fn = '../scans/nx'+str(f)+'_'+str(m)+'.dat'
    x2,y2 = np.loadtxt(fn,usecols=(1,2),unpack=True)
    x2 = x2[:-1]
    y2 = y2[:-1]
    y2 = y2*-1
    plt.plot(x,y)
    plt.plot(x2,y2)
    plt.show()
