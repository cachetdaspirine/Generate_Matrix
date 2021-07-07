import numpy as np
import sys
import os

from Functions import *

#sys.path.append('/home/hleroy/Simulation/Extra_Module_py')
sys.path.append('/home/hugo/Extra_Module_py')
import RandomParticleFunctions_v4 as RPF
import MeasurePoisson as MP

file = open('Matrix.data','ab')
Nstat = 10
for i in range(Nstat):

    Mc,rho0,e1,e2,seed = RPF.RandomParticle()

    l4mu = MP.GetL4MU(Mc,rho0)
    lamb = MP.GetLambda(Mc,rho0)
    val,vect = np.linalg.eigh(Mc)


    data = np.array([np.sqrt(0.5*(l4mu+lamb)/(2*val[0])),MeasureL(Mc,rho0),seed])

    np.savetxt(file,data[np.newaxis,:])
file.close()
