import pandas as pd
import numpy as np
import matplotlib as mpl
import random
import scipy as sp
from scipy.stats import ks_2samp, kstest
from statsmodels.distributions.empirical_distribution import ECDF
from sklearn.utils import resample
from scipy.optimize import curve_fit
from scipy.stats import (norm,gamma,sem)
from scipy import stats

import warnings
warnings.filterwarnings('ignore',category=RuntimeWarning)

#get list of unbiased dissociation times
FILE = []
for i in range(0,20):
    fname='../run'+str(i)+'/CN'
    FILE.append(fname) 

data = []
for f in FILE: 
    d = pd.read_csv(str(f),delimiter='\s+',comment='#',header=None,names=['time','CV1','bias','rct','acc'])
    d = d[:d[d['CV1']<25].index[0]+1] 
    x = d['time'].tolist()
    y = d['acc'].tolist()
    time = x[-1]*y[-1]/10**11
    rt = np.round(time,6)
    data.append(rt)

np.savetxt('cn25.dat',data)

#fitting unbiased dissociation times using EDF to get tau 
print('')
print('###Approximated residence time (tau)###')
def func(x,tau):
    return 1-np.exp(-x/tau)

#seconds to mins 
DATA = np.divide(data,60) 
ecdf = ECDF(DATA)
x1 = np.logspace(-8,1,180)
y1 = ecdf(x1)
popt,pcov = curve_fit(func,x1,y1)
tau1=popt[0]
yfit=func(x1,tau1)
x2 = np.random.exponential(tau1,10000)
st,p = ks_2samp(DATA,x2)
print('###Rough tau value###')
print(f'tau = {tau1:1.6f} min , D = {st:1.3f} , p-value = {p:1.3f}')
print('')

#bootstrapped resampling
mean = []
P = []
for i in range(1000):
    x = np.random.choice(DATA,size=len(DATA),replace=True)
    ecdf = ECDF(x)
    x1 = np.logspace(-8,1,180)
    y1 = ecdf(x1)
    popt,pcov = curve_fit(func,x1,y1,maxfev=1000)
    tau1=popt[0]
    x2 = np.random.exponential(tau1,10000)
    st,p = ks_2samp(x,x2)
    mean.append(tau1)
    P.append(p)

COM = pd.concat([pd.DataFrame(P,columns=['P']),pd.DataFrame(mean,columns=['Tau'])],axis=1)
COM = COM.drop(COM[COM['P']<0.05].index)
COM = COM[['P','Tau']]
print('###From bootstrapping###')
print('Number of successful bootstrapping trials (P-value >= 0.05): ', len(COM))
print('Calculated average residence times (min): ', np.round(np.mean(COM['Tau']),6),np.round(sem(COM['Tau']),6),np.round(np.std(COM['Tau']),6))
print('Average P-value from the successful trials: ', np.round(np.mean(COM['P']),2))
print('')
#jackknife resampling
mean = []
P = []
for i in range(1000):
    x = np.random.choice(DATA,size=len(DATA)-1,replace=False)
    ecdf = ECDF(x)
    x1 = np.logspace(-8,1,180)
    y1 = ecdf(x1)
    popt,pcov = curve_fit(func,x1,y1,maxfev=1000)
    tau1=popt[0]
    x2 = np.random.exponential(tau1,10000)
    st,p = ks_2samp(x,x2)
    mean.append(tau1)
    P.append(p)

COM = pd.concat([pd.DataFrame(P,columns=['P']),pd.DataFrame(mean,columns=['Tau'])],axis=1)
COM = COM.drop(COM[COM['P']<0.05].index)
COM = COM[['P','Tau']]
print('###From jackknife###')
print('Number of successful jackknife trials (P-value >= 0.05): ', len(COM))
print('Calculated average residence times (min): ', np.round(np.mean(COM['Tau']),6),np.round(sem(COM['Tau']),6),np.round(np.std(COM['Tau']),6))
print('Average P-value from the successful trials: ', np.round(np.mean(COM['P']),2))

 
