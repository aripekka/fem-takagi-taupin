from __future__ import division
import numpy as np

def read_comsol_export(filename):
    filu=open(filename)
    lines=filu.readlines()
    filu.close()
    
    data = []
    
    for i in range(5,len(lines)):
        #skip comments
        if lines[i][0] == '%':
            continue
        
        aux = lines[i].split()
        aux2 = []
        for j in aux:
            aux2.append(complex(j.replace('i','j')))
            
        data.append(aux2)
        
    data=np.array(data)

    #COLUMNS IN THE ARRAY (all but x and y repeated for every scan point):
    #x, y, theta2, k, u1, u2, nx, ny

    r=np.array([data[:,0],data[:,1]]).real
    n=np.array([data[:,6],data[:,7]]).real
    u=np.array([data[:,8],data[:,9]]).real    
    
    N_params = 10
    N_points = int((data.shape[1]-2)/N_params)
    
    theta = []
    k = []
    u1 = []
    u2 = []
    G = []
    scan_arcsec = []

    for i in range(N_points):
        theta.append(data[0,N_params*i+2])
        k.append(data[0,N_params*i+3])
        u1.append(data[:,N_params*i+4])
        u2.append(data[:,N_params*i+5])        
        G.append(data[0,N_params*i+10])
        scan_arcsec.append(data[0,N_params*i+11])
    
    theta = np.array(theta).real
    k = np.array(k).real    
    u1 = np.array(u1)
    u2 = np.array(u2)    
    G = np.array(G).real
    scan_arcsec = np.array(scan_arcsec).real

    
    return r,n,theta,k,u1,u2,u,G,scan_arcsec
    
