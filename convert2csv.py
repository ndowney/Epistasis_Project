import numpy as np
import math

envs=['23C','25C','27C','30C','33C','35C','37C','4NQO','cu','eth','gu','li','mann','mol','raff','sds','suloc','ynb']

for env in envs:
    dataFile=np.load('Data_{}.npz'.format(env))
    snps=dataFile['SNPs']
    fitness=dataFile['fitness']
    
    f=open('{}.csv'.format(env),'w')
    f.write('mutated_sequence,DMS_score\n')
    for sind in range(99950):
        seqstr="".join([str(x) for x in snps[sind,:]])
        if math.isnan(fitness[sind]) is False:
            seqstr=seqstr+","+str(fitness[sind])+"\n"
            f.write(seqstr)
    f.close()
