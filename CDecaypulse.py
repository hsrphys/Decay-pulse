# -*- coding: utf-8 -*-
"""
Created on Fri May 12 00:26:27 2017

@author: hsrag
"""

from numpy import array, arange,pi,exp,sqrt
from pylab import plot,xlabel,show
from numpy import arange,array



def cdepus(n,ga,G):
    def f(r,t):
        x=r[0]
        y=r[1]
#        n=4
#        ga=0.20
        T=3.347/(n*ga)
#        G=0.5
    
        
        fx=-((ga+G)/2.0)*x+4.0*sqrt(ga*n)*sqrt(2.0/T)*exp(-t/T)*y-2.0*sqrt(ga*n)*sqrt(2.0/T)*exp(-t/T)
        fy=-(ga+G)*y-x*sqrt(ga*n)*sqrt(2.0/T)*exp(-t/T)
        return array([fx,fy],float)
        
    #def g(t):
    #    n=10.0
    #    ga=15.0
    #    return array((4.0*n)*(exp((-t**2.0)/2.0)/sqrt(2.0*pi))/(ga+8.0*n*(exp((-t**2.0)/2.0)/sqrt(2.0*pi))),float)
    #    return (4.0*n)*(exp((-t**2.0)/2.0)/sqrt(2.0*pi))/(ga)
    a=0.0
    b=5.0
    N=30000
    h=(b-a)/N
    
    tp=arange(a,b,h)
    xp=[]
    yp=[]
    zp=[]
    r=array([0.0,0.0],float)
    
    for t in tp:
        yp.append(r[1])
    #    zp.append(g(t))
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+(2.0*k2)+(k3*2.0)+k4)/6.0
    return max(yp)    
    #plot(tp,yp,tp,zp,'r')
#    plot(tp,yp)
#    show()   