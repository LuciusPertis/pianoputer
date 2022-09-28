#create and save sndarrays

import os
import shutil
import numpy as np

from scipy.io import wavfile as wf

path = input('MASTER_SAMPLES dir:')

l = os.listdir(path)
ll = [ (path + '/{}/'.format(x), i) for x in l for i in os.listdir(path + '/' + x)]

def exdata(s):
    data = s.split('_')
    return ( data[1], data[3], data[5], data[7] )


file = open(path + '/master_sndarr.py', 'w')

file.write(\
    'import numpy as np\n\n'+\
    'master_sndarr = dict{\\')

for i in ll:
    file.write('\n\t')
    d = exdata(i[1])
    rate, arr = wf.read(i[0]+i[1])
    file.write("('{}{}{}{}', {}),\\".format( d[0], d[1], d[2], d[3], arr.tolist()))
    print('wrote : {}'.format(i))




    
