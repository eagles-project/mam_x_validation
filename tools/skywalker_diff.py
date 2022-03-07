# This script generates norms for cross-validating the particle nucleation
# process. To generate the data needed by the script, run skywalker in the
# current directory, using nucleation.yaml as input. This writes a file called
# haero_skywalker.py to the directory, which is then imported as a module.

import os, sys, importlib
import numpy as np
import numpy.linalg as lin
import math 

# Look for data in whatever directory we're running in.
sys.path.append(os.getcwd())

def norms(vals) :
    L1 = lin.norm(vals,1)
    L2 = lin.norm(vals)            
    Linf = lin.norm(vals,np.inf)            
    return (L1,L2,Linf)

def check_lens(vals1, vals2) :
    len1 = len(vals1)
    len2 = len(vals2)
    if len1 != len2 :
       print ("Lengths of values are not equal: %s vs %s. Using shorter of the two"%(len1,len2))
    N = min(len1, len2)
    return (vals1[:N], vals2[:N])

def usage():
    print('skywalker_diff.py: generates L1, L2, Linf diff norms for two skywalker output files.')
    print('usage: python3 skywalker_diff.py filename1 filename2')
    print('where filename1.py and filename2.py are skywalker files')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()

    file1 = sys.argv[1];
    file2 = sys.argv[2];

    # Should we append a remote file path to the system path so the module
    # is found?  Or make the user copy or link the file into the current dir?
    base1 = os.path.basename(file1)
    dir1  = os.path.dirname(file1)
    base2 = os.path.basename(file2)
    dir2  = os.path.dirname(file2)
    if dir1 : 
      sys.path.append(dir1)
      file1 = base1
    if dir2 : 
      sys.path.append(dir2)
      file2 = base2

    data1 = importlib.import_module(file1) 
    data2 = importlib.import_module(file2) 
   
    vars1 = vars(data1.output)
    vars2 = vars(data2.output)
 
    keys1 = list(vars1)
    keys2 = list(vars2)

    for key1 in keys1 :
        for key2 in keys2 :
           if key1 == key2 :
              vals1 = np.array(vars1[key1])
              vals2 = np.array(vars2[key2])
              (vals1, vals2) = check_lens(vals1, vals2)
              dvals = np.subtract(vals1, vals2)
              (L1, L2, Linf) = norms(dvals)
              (N1, N2, Ninf) = norms(vals1)
              print ("Norms for difference of output.{}:".format(key1))
              print ("     Absolute:  L1:{:12.6g}  L2:{:12.6g}  Linf:{:12.6g}".format(L1, L2, Linf))
              print ("     Relative:  L1:{:12.6g}  L2:{:12.6g}  Linf:{:12.6g}".format(L1/N1, L2/N2, Linf/Ninf))
          
