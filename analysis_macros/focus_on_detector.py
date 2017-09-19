from __future__ import division
from scipy.interpolate import interp1d
import numpy as np

def focus_fresnel_kirchhoff(xi,r,n,u2,q,theta,k,u,G):
    
    def s(x,y,xi):
        s_squared = x**2 + y**2 - 2*x*(q*np.cos(theta)+xi*np.sin(theta)) \
                    - 2*y*(q*np.sin(theta)-xi*np.cos(theta)) + q**2 + xi**2
        return np.sqrt(s_squared)
    
    def zeta(x,y,nx,ny,xi):
        return nx*(x-q*np.cos(theta)-xi*np.sin(theta)) \
               + ny*(y-q*np.cos(theta)+xi*np.cos(theta))

    psi=[]
    
    for pos in xi:
        #factors of integrand
        S = s(r[0],r[1],pos)
        F1 = u2/S
        F2 = 1j*k/S*zeta(r[0],r[1],n[0],n[1],pos) \
             - 1j*k*(n[0]*np.cos(theta) + n[1]*np.sin(theta))
        F3 = np.exp(1j*(k*S + k*np.cos(theta)*r[0] + k*np.sin(theta)*r[1]-G*u[1]))
              
        #line integral over the surface        
        psi.append(np.trapz(F1*F2*F3*np.sqrt(1+(n[0]/n[1])**2),r[0]))
        
    return np.array(psi)
    

def focus_fresnel_projection(x,r,n,u2,q,theta,k,u,G):

    xi = r[0]*np.sin(theta) - r[1]*np.cos(theta)

    psi=np.zeros(x.shape,dtype=np.complex128)

    for i in range(len(x)):
        F=u2*np.exp(-1j*G*u[1]+1j*k*(x[i]-xi)**2/(2*q))
        psi[i]=np.trapz(F,xi)
        
    return psi
