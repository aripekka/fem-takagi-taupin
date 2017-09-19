from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


datapath = '../data/'

data = {}

data['xop'] = np.loadtxt(datapath + 'xop_xinpro_si111_8keV.dat',comments='%')
data['unbent'] = np.loadtxt(datapath +'unbent_1_75um_grid_rocking_curve.dat',comments='%')
data['unbent with boundary'] = np.loadtxt(datapath +'unbent_1_75um_grid_boundary_rocking_curve.dat',comments='%')
data['bent'] = np.loadtxt(datapath +'bent_1um_grid_onrowland_rocking_curve.dat',comments='%')


x = data['xop'][:,0]
y = data['xop'][:,1] 
plt.plot(x,y,label='XOP',linewidth=2)

x = data['unbent'][:,0]
y = data['unbent'][:,2]/data['unbent'][:,1]
plt.plot(x,y,label='Unbent',linewidth=2)

x = data['unbent with boundary'][:,0]
y = data['unbent with boundary'][:,2]/data['unbent with boundary'][:,1] 
plt.plot(x,y,label='Unbent\nw/ boundary',linewidth=2)

x = data['bent'][:,0]
y = data['bent'][:,2]/data['bent'][:,1]
plt.plot(x,y,label='Bent\n(5 m radius)',linewidth=2)


plt.ylabel('Reflectivity',fontsize = 16)
plt.xlabel("Incident angle relative to Bragg's angle (arc sec)",fontsize = 16)
plt.title('Rocking curves of Si(111)',fontsize = 18, fontweight = 'bold')

plt.tick_params(axis='both', which='major', labelsize=15, pad = 5)
plt.xlim([-5,20])
plt.legend()

plt.show()
