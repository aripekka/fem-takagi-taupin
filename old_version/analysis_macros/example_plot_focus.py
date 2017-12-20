from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from read_comsol_export import *
from focus_on_detector import *

datapath = '../data/'

def compute_focus(xi, pythonfk,R_bend=5,det_dist=None,relative_shift=0):

    r,n,theta,k,u1,u2,u,G,scan_arcsec = read_comsol_export(pythonfk)

    if det_dist == None:
        det_dist = (np.sin(theta[0])*R_bend+relative_shift)*1e6

    #focus
    dh2 = focus_fresnel_projection(xi,r,n,u2[0],det_dist,theta[0],k[0],u,G[0])
    return dh2

#The detector coordinates
xi=np.linspace(-10,10,250)

dh = compute_focus(xi,datapath + 'diffracted_intensity_onrowland_5arcsec.dat')
y=np.abs(dh)**2
y=y/np.trapz(y,xi)

dh = compute_focus(xi,datapath + 'diffracted_intensity_onrowland_5arcsec.dat',relative_shift = 0.1)
y2=np.abs(dh)**2
y2=y2/np.trapz(y2,xi)

dh = compute_focus(xi,datapath + 'diffracted_intensity_onrowland_5arcsec.dat',relative_shift = -0.1)
y3=np.abs(dh)**2
y3=y3/np.trapz(y3,xi)

plt.plot(xi,y,label='Detector in focus',linewidth=2)
plt.plot(xi,y2,label='Offset +10 cm',linewidth=2)
plt.plot(xi,y3,label='Offset -10 cm',linewidth=2)

plt.xlabel('Position on the detector (um)',fontsize = 16)
plt.ylabel('Intensity (arb. units)',fontsize = 16)
plt.title('Focal spot of bent Si(111)')
plt.legend(loc=2)

plt.legend()
plt.show()

