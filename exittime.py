###Find first frame when the ligand reached the surface####
###if maximum coordination number was above 550###
import pandas as pd
import numpy as np
import os

###Read and combine *colvars.traj file for each run####
for x in range(0,20):
    x0 = 'run'+str(x)+'/md00.colvars.traj'
    PATH = 'run'+str(x)+'/COM.dat' 
    X0 = pd.read_csv(str(x0),delimiter='\t',comment='#',header=None,names=['CV1'])
    if os.path.isfile('run'+str(x)+'/md01.colvars.traj') == True:
        x1 = 'run'+str(x)+'/md01.colvars.traj'
        X1 = pd.read_csv(str(x1),delimiter='\t',comment='#',header=None,names=['CV1']) 
        COM = pd.concat([X0,X1]).reset_index(drop=True)
        COM.to_csv(str(PATH),sep='\t',index=False,header=False) 
    else:
        X0.to_csv(str(PATH),sep='\t',index=False,header=False)

###list the combined files###
FILE = []
for i in range(0,20):
    fname='run'+str(i)+'/COM.dat'
    FILE.append(fname) 

###Get the frame number from run0 to run19
EXIT = []
OUT = []
CN =[]
for f in FILE: 
    d = pd.read_csv(str(f),delimiter='\s+',comment='#',header=None,names=['time','CV1'])
    minvalue = d['CV1'].min()
    if minvalue < 25: 
        out = 'Y'
        exit = d[d['CV1'] < 25].index[0]
    elif minvalue < 20:
        out = 'Y'
        exit = d[d['CV1'] < 20].index[0]
    else:
        exit = 99999
        out = 'N'
    EXIT.append(exit)
    OUT.append(out) 
    cn = d['CV1'].max()
    CN.append(cn) 

data = pd.DataFrame({'OUT': OUT, 'Exitframe' : EXIT, 'MAXCN0' : CN})
data['MAXCN'] = np.where(data['MAXCN0'] > 550,True,False)
data = data.drop(['MAXCN0'],axis=1)
data.to_csv('exittime.dat',sep='\t',header=False)

 
