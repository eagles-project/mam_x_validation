#!/usr/bin/env python3

# This script generates norms for cross-validating the particle nucleation
# process. To generate the data needed by the script, run Skywalker in the
# current directory, using nucleation.yaml as input. This writes a file called
# haero_skywalker.py to the directory, which is then imported as a module.
# Have another Skywalker file created previously.  If one of the
# Skywalker files in in a different directory, the -p option can
# be used to specify the directory to search in.  This script
# will compare the two and produce difference norms for all of the 
# output values.

import os, sys, importlib, argparse, itertools
import numpy as np
import numpy.linalg as lin

def norms(vals) :
    if 1 == vals.ndim :
      axis=None
    else :
      axis=0
    L1 = lin.norm(vals,1,axis)
    L2 = lin.norm(vals,2,axis)
    Linf = lin.norm(vals,np.inf,axis)
    return (L1,L2,Linf)

def check_lens(f, key, vals1, vals2) :
    warning = ("Warning: Lengths of {} are not equal:"+
       " {} vs {}. Using shorter of the two.\n")
    len1 = len(vals1)
    len2 = len(vals2)
    if len1 != len2 :
       f.write (warning.format(key, len1, len2))
    N = min(len1, len2)
    return (vals1[:N], vals2[:N])

def check_input(f, key, abs_tol, rel_tol, vals1, vals2) :
    dvals = np.subtract(vals1, vals2)
    (L1, L2, Linf) = norms(dvals)
    (N1, N2, Ninf) = norms(vals1)
    if abs_tol < L2.max() and rel_tol < (L2/N2).max():
        f.write ("Warning: Norm for difference of input.{} is:{}\n".format(key,L2))
        f.write ("     It appears that the input parameters are NOT")
        f.write (" the same for the two files.\n")
    return False

def check_output(f, key, abs_tol, rel_tol, vals1, vals2) :
    exceeds_tol = False
    dvals = np.subtract(vals1, vals2)
    (L1, L2, Linf) = norms(dvals)
    (N1, N2, Ninf) = norms(vals1)
    if isinstance(L1,(list,np.ndarray)) :
        i = 0
        for (l1,l2,linf, n1,n2,ninf) in zip(L1,L2,Linf, N1,N2,Ninf) :
            if abs_tol < np.hstack((l1, l2, linf)).max() or (0 < np.hstack((n1, n2, ninf)).max() and rel_tol < np.hstack((l1/n1, l2/n2, linf/ninf)).max()):
                exceeds_tol = True
                ind = "["+str(i)+"]"
                f.write ("Norms for difference of output.{}{}: given absolute tolerance {} and relative tolerance {}\n".format(key, ind, abs_tol, rel_tol))
                f.write ("     Absolute:  L1:{:12.6g}  L2:{:12.6g}  Linf:{:12.6g}\n".format(l1, l2, linf))
                f.write ("     Relative:  L1:{:12.6g}  L2:{:12.6g}  Linf:{:12.6g}\n".format(l1/n1, l2/n2, linf/ninf))
                i = i + 1
    else :
        if abs_tol < np.hstack((L1, L2, Linf)).max() or (0 < np.hstack((N1, N2, Ninf)).max() and rel_tol < np.hstack((L1/N1, L2/N2, Linf/Ninf)).max()):
            exceeds_tol = True
            f.write ("Norms for difference of output.{}: given absolute tolerance {} and relative tolerance {}\n".format(key, abs_tol, rel_tol))
            f.write ("     Absolute:  L1:{:12.6g}  L2:{:12.6g}  Linf:{:12.6g}\n".format(L1, L2, Linf))
            f.write ("     Relative:  L1:{:12.6g}  L2:{:12.6g}  Linf:{:12.6g}\n".format(L1/N1, L2/N2, Linf/Ninf))
    return exceeds_tol

def intersect_vars(f, data1, data2, abs_tol, rel_tol, check_vals) :
    pad_token = 0
    exceeds_tol = False
    vars1 = vars(data1)
    vars2 = vars(data2)

    keys1 = list(vars1)
    keys2 = list(vars2)
    keys = [key for key in keys1 if key in keys2]
    for key in keys :
        o1 = vars1[key];
        o2 = vars2[key];
        # There is no requirement for the arrays in Skywalker to be regular. They could
        # be ragged with each line a different length. But numpy arrays are made of
        # regular lists. So find a command from Stackoverflow that will fill out
        # irregular lists and padd with 0's.
        if type(o1) is list and 0 < len(o1) and type(o1[0]) is list :
            o1 = [list(i) for i in zip(*itertools.zip_longest(*o1, fillvalue=pad_token))]
        if type(o2) is list and 0 < len(o2) and type(o2[0]) is list :
            o2 = [list(i) for i in zip(*itertools.zip_longest(*o2, fillvalue=pad_token))]

        vals1 = np.array(o1)
        vals2 = np.array(o2)
        (vals1, vals2) = check_lens(f, key, vals1, vals2)
        # check_vals is either the check_input or check_output function
        exceeds_tol = exceeds_tol or check_vals(f, key, abs_tol, rel_tol, vals1, vals2)
    return exceeds_tol
          
def parse_args () :
    description = ('Skywalker output difference tool: '+
        'Generates L1, L2, Linf diff norms for two Skywalker files.')
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-p', metavar='path1:path2:...', 
        help='Search paths for the input module files seperated by ":".')
    parser.add_argument('-o', metavar='file.txt', 
        help='Output file to write results to. Default:stdout')
    parser.add_argument('-a', metavar='abs_tolerance', default=0.00001,
                        help='Absolute tolerance to test norms against. Default: 0.00001')
    parser.add_argument('-r', metavar='rel_tolerance', default=0.00001,
                        help='Relative tolerance to test norms against. Default: 0.00001')
    parser.add_argument('file1')
    parser.add_argument('file2')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    abs_tol = float(args.a)
    rel_tol = float(args.r)

    # Look for data in whatever directory we're running in.
    sys.path.append(os.getcwd())
    if args.p :
        for p in args.p.split(':') :
            sys.path.append(p)

    f = sys.stdout
    if args.o :
       f = open(args.o, "w")

    data1 = importlib.import_module(args.file1) 
    data2 = importlib.import_module(args.file2) 
   
    intersect_vars(f, data1.input,  data2.input,  abs_tol, rel_tol, check_input)
    exceeds_tol = intersect_vars(f, data1.output, data2.output, abs_tol, rel_tol, check_output)

    f.close()
    if exceeds_tol : sys.exit(1)
    else           : sys.exit(0)
