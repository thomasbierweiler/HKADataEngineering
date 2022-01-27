# this script implements the map reduce algorithm in a very basic form
# no parallel processing is used
from datetime import datetime

f_map="map.hdf5"
f_shuffle="shuffle.hdf5"
f_reduce="reduce.hdf5"
######### map phase #########
print(str(datetime.now()) + ": Starting map")
# module for pattern matching
import re
# Hierarchical Data Format hdf5
import h5py
import numpy as np
inputFile="patent_claims_excerpt3.csv"
# create a hdf5-file for storing key/value pairs (hdf5 with results from map processes)
map_hdf5=h5py.File(f_map, "w")
# open the file
cnt=0
with open(inputFile,'r') as fo:
    # read a line of the file (this can be done in parallel by each map process)
    for chunk in iter(lambda: fo.readline(), ''):
        cnt+=1
        # split line into separate words
        splits=re.split("\W",chunk)
        # map part 1: for each word, generate pairs
        # [ ("word1", 1), ("word2", 1), ("word3", 1), ("wordi", 1) ,..., ("wordn", 1) ]
        pairs=[]
        for split in splits:
            if split != '':
                pairs.append((split,1))
        # map part 2: iterate over pairs and create key / values (arrays [1,1,...])
        # Key1: [1], Key2: [1], Key3: [1,1], Key4: [1], Key5: [1,1,1] ...
        wd=dict()
        for p in pairs:
            if p[0] in wd:
                wd[p[0]].append(1)
            else:
                wd[p[0]]=[1]
        # create a group for the map process
        g=map_hdf5.create_group('g'+str(cnt))
        # map process writes result to hdf5 file
        for item in wd.items():
            g[item[0]]=item[1]
# close hdf storage
map_hdf5.close()
######### shuffle phase #########
print(str(datetime.now()) + ": Starting shuffle")
# open hdf5 with results from map processes
map_hdf5=h5py.File(f_map, "r")
# create hdf5 for result of shuffle phase
shuffle_hdf5=h5py.File(f_shuffle, "w")
# iterate over map processes
for p in map_hdf5.keys():
    # iterate over words (groups in hdf5)
    for w in map_hdf5[p]:
        # add content to shuffle hdf5
        # check if word is a key in shuffle hdf5
        if w in shuffle_hdf5:
            # access list by key, and then extend list by content of map_hdf5
            s=list(shuffle_hdf5[w])
            m=list(map_hdf5[p][w])
            s.extend(m)
            # update values in hdf5
            del shuffle_hdf5[w]
            shuffle_hdf5[w]=s
        else:
            shuffle_hdf5[w]=list(map_hdf5[p][w])

# close hdf storages
map_hdf5.close()
shuffle_hdf5.close()
######### reduce phase #########
print(str(datetime.now()) + ": Starting reduce")
# open hdf5 with results from shuffle phase
shuffle_hdf5=h5py.File(f_shuffle, "r")
# create hdf5 for result of reduce phase
reduce_hdf5=h5py.File(f_reduce, "w")
# iterate over keys (words)
for p in shuffle_hdf5.keys():
    # create numpy array from hdf5 list
    vals=np.array(list(shuffle_hdf5[p]),dtype=np.uint8)
    # sum over elements
    cw=np.sum(vals)
    # store result in reduce hdf5
    reduce_hdf5[p]=[int(cw)]
# close hdf storages
shuffle_hdf5.close()
reduce_hdf5.close()
######### Content in hdf5 is not ordered #########
######### get words with most occurrences #########
print(str(datetime.now()) + ": Get words with most occurrences")
# open hdf5 with results from reduce phase
reduce_hdf5=h5py.File(f_reduce, "r")
# total length
sz=15
# create array for values and words (keys)
vals=np.zeros(0,dtype=int)
ks=[]
# iterate through hdf5
for p in reduce_hdf5.keys():
    # extract value from hdf5
    val=list(reduce_hdf5[p])[0]
    # search position in existing array (binary search)
    indx=np.searchsorted(vals,val)
    # check if arrays are smaller than sz
    # or if indx > 0
    if vals.shape[0]<sz or indx>0:
        # update both arrays (insert at indx)
        vals=np.insert(vals,indx,val)
        ks.insert(indx,p)
    # check if new #occurrences is more than lowest #occurrences
    elif indx==0 and val>vals[0]:
        # replace first elements
        vals[0]=vals
        ks[0]=p
    # truncate lists
    if vals.shape[0]>sz:
        vals=np.delete(vals,0)
        ks=ks[1:]
# print most occurrences:
for vk in zip(np.flip(vals),reversed(ks)):
    print('{}: {}.'.format(vk[0],vk[1]))
# close hdf storage
reduce_hdf5.close()

