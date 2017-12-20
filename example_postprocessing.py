from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from ttfem_postprocessing import *
#
#An example of post processing the COMSOL surface wave data
#

#Simulation parameters 
R=5            #bending radius (m) 
k=3.0406e10    #wavenumber (2*pi/lambda) in meters
theta = 0.3358 #incidence angle (rad)

x,y,u1,u2= read_comsol_export('bent_onrowland_6.9697_arcsec.dat')

#Make the phases continuous
phase_u1 = stitch_phase(np.angle(u1))
phase_u2 = stitch_phase(np.angle(u2))

#Set the corrected phases to zero at x = 0
phase_u1 = phase_u1-phase_u1[np.argmin(x**2)]
phase_u2 = phase_u2-phase_u2[np.argmin(x**2)]

#Compute the focal spot at the Rowland circle R*sin(theta)
ksi = np.linspace(-50,50,250)*1e-6 #The detector plane coordinates (in m)
psi = fresnel_integral(ksi,x*1e-6,y*1e-6,u2,k,theta,R*np.sin(theta))

#Plot the incident and diffracted intensities on the surface
plt.figure()
plt.plot(x,np.abs(u1)**2,label='Incident',linewidth=2)
plt.plot(x,np.abs(u2)**2,label='Diffracted',linewidth=2)

plt.title('Wave intensities on the crystal surface')
plt.ylabel('Intensity (arb. units)')
plt.xlabel(u"Horizontal position (\u03bcm)")
plt.legend()

#Plot the wave phases at the surface
plt.figure()
plt.plot(x,phase_u1,label='Incident',linewidth=2)
plt.plot(x,phase_u2,label='Diffracted',linewidth=2)

plt.title('Wave phases on the crystal surface')
plt.ylabel('Phase (rad)')
plt.xlabel(u"Horizontal position (\u03bcm)")
plt.legend()

#Plot the intensity at the focus
plt.figure()
plt.plot(ksi*1e6,np.abs(psi)**2,label='Incident',linewidth=2)

plt.title('Intensity at the focal spot')
plt.ylabel('Intensity (arb. units)')
plt.xlabel(u"Position on the detector (\u03bcm)")



plt.show()
