from __future__ import division
import numpy as np

def read_comsol_export(filename):
    A = np.loadtxt(filename,comments='%')
    x = A[:,0]
    y = A[:,1]
    u1 = A[:,2] + 1j*A[:,3]
    u2 = A[:,4] + 1j*A[:,5]

    return x,y,u1,u2


def stitch_phase(phase):
    '''
    Removes the discontinuities from the phase
    '''
    mid_ind = (phase.size-1)//2
    for i in xrange(mid_ind,phase.size-1):
        if (phase[i+1]-phase[i] > np.pi):
            phase[i+1:] = phase[i+1:]-2*np.pi
        elif (phase[i+1]-phase[i] < -np.pi):
            phase[i+1:] = phase[i+1:]+2*np.pi
    for i in xrange(mid_ind,0,-1):
        if (phase[i-1]-phase[i] > np.pi):
            phase[:i] = phase[:i]-2*np.pi
        elif (phase[i-1]-phase[i] < -np.pi):
            phase[:i] = phase[:i]+2*np.pi

    return phase
    
   
def fresnel_integral(ksi,x,y,u,k,theta,q):
    '''
    Computes the Fresnel diffraction integral for given data
    
    ksi = position on the detector plane
    x,y = coordinates of the crystal surface
    u = wave amplitude at (x,y)
    k = wavenumber
    theta = exit angle
    q = distance to the detector plane  
    '''

    xi = x*np.sin(theta) - y*np.cos(theta)
    psi=np.zeros(ksi.shape,dtype=np.complex)

    for i in range(ksi.size):
        F=u*np.exp(1j*k*(ksi[i]-xi)**2/(2*q))
        psi[i]=np.sum(F)
        
    return psi/np.sqrt(q)    
