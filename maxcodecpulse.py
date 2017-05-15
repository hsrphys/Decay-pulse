# -*- coding: utf-8 -*-
"""
Created on Fri May 12 00:42:26 2017

@author: hsrag
"""

from scipy.optimize import curve_fit
from matplotlib.pylab import legend
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from pylab import plot,ylim,figure
from numpy import array, arange,pi,exp,sqrt,log,savetxt
#def fit_func(N,ga, a, b, c, d):
#    return 1+a*sqrt(ga/N)+(b*ga)/N+c*sqrt(ga/N**3.0)+d/N**2.0
def CDP():
    
    GG=[0.40]
    G=0.3
#    G=arange(0.10,2.0,0.1)
#    N=arange(1,30,1)
    m=len(GG)
#    n=50
#    ga=0.1
    for i in range(m):
        ga=GG[i]
        N=arange(100,360,1)
        mx=[]
        mxa=[]
    
        
        for n in N:
            mx.append(cdepus(n,ga,G))
            mxa.append(cdecayappro(n,ga,G))
        plot(N,mx)
        plot(N,mxa,'r')
#        plot(N,fit_func(N,ga,-3.2,25.6,-6,7),'.')
#        params = curve_fit(fit_func, N, mx)
#        [a, b,c,d] = params[0]
#        print params[0]
        savetxt('cdma1.dat', zip(N, mx), fmt="%i %f")
        savetxt('cdma2.dat', zip(N, mxa), fmt="%i %f")
    plt.show()      

if __name__ == "__main__":
    CDP() 