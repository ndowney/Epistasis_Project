import numpy as np
import math
import sys
np.set_printoptions(threshold=sys.maxsize)
from collections import defaultdict

#Defunct encoding routine that can store the data in small, but inconvenient, datafiles
def genc(an_array):
    
    numel=math.ceil(len(an_array)/8)
    out_array=np.zeros(numel,dtype='uint8')
    oi=0
    for i in np.arange(0,len(an_array)-8,8):
        out_array[oi]=an_array[i]+an_array[i+1]*2+an_array[i+2]*4+an_array[i+3]*8+an_array[i+4]*16+an_array[i+5]*32+an_array[i+6]*64+an_array[i+7]*128
        oi=oi+1
    #Have to encode last value manually 
    f=1
    for i in range((len(out_array)-1)*8,len(an_array)):
        out_array[oi]=out_array[oi]+an_array[i]*f
        f=f*2
        
    return out_array


#Parse the SNP data
f=open('elife-73983-fig3-data2-v2.txt','r')
header=f.readline()
snips=defaultdict(set)
for line in f:
    parts=line.strip().split()
    env=parts[0]
    snips[env].add(int(parts[1]))
f.close()


envs=['23C','25C','27C','30C','33C','35C','37C','4NQO','cu','eth','gu','li','mann','mol','raff','sds','suloc','ynb']
for env in envs[-2:]:
    numSnips=len(snips[env])
    print("Environment {}: Number of SNPs:{}".format(env,numSnips))
    theseSnips=np.empty(shape=(100000,numSnips),dtype='uint8')
    snrow=0
    snipinds=list(snips[env])
    snipinds.sort()
    for findex in range(1,6):
        f=open('orig/geno_data_{}.txt'.format(findex))
        print("File: orig/geno_data_{}.txt                      ".format(findex))
        line=f.readline()
        while(line):
            if snrow % 100 == 0:
                print('Parsing strain {} of 100000'.format(snrow),end='\r')
            line=[float(x) for x in line.strip().split()]
            line.pop(0) #remove index in first column
            lineb=np.array([int(x+0.5) for x in line],dtype='uint8')
            sncol=0
            for i in snipinds:
                try:
                    theseSnips[snrow,sncol]=lineb[i]
                    sncol=sncol+1
                except IndexError:
                    pass
            line=f.readline()
            snrow=snrow+1
        f.close()
    np.save("Snips_{}".format(env),theseSnips)
    del theseSnips


