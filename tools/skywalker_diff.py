# This script generates norms for cross-validating the particle nucleation
# process. To generate the data needed by the script, run skywalker in the
# current directory, using nucleation.yaml as input. This writes a file called
# haero_skywalker.py to the directory, which is then imported as a module.
# Have another haero_skywalker.py created previously.  This script
# will compare the two and produce difference norms for all of the 
# output values.

import os, sys, importlib, argparse
import numpy as np
import numpy.linalg as lin

def norms(vals) :
    L1 = lin.norm(vals,1)
    L2 = lin.norm(vals)            
    Linf = lin.norm(vals,np.inf)            
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

def check_input(f, key, vals1, vals2) :
    dvals = np.subtract(vals1, vals2)
    (L1, L2, Linf) = norms(dvals)
    if .0000001 < L2 :
        f.write ("Warning: Norm for difference of input.{} is:{}\n".format(key,L2))
        f.write ("     It appears that the input parameters are NOT the same for the two files.\n")

def check_output(f, key, vals1, vals2) :
    dvals = np.subtract(vals1, vals2)
    (L1, L2, Linf) = norms(dvals)
    (N1, N2, Ninf) = norms(vals1)
    f.write ("Norms for difference of output.{}:\n".format(key))
    f.write ("     Absolute:  L1:{:12.6g}  L2:{:12.6g}  Linf:{:12.6g}\n".format(L1, L2, Linf))
    f.write ("     Relative:  L1:{:12.6g}  L2:{:12.6g}  Linf:{:12.6g}\n".format(L1/N1, L2/N2, Linf/Ninf))

def intersect_vars(f, data1, data2, check_vals) :
    vars1 = vars(data1)
    vars2 = vars(data2)
    keys1 = list(vars1)
    keys2 = list(vars2)
    keys = [key for key in keys1 if key in keys2]
    for key in keys :
        vals1 = np.array(vars1[key])
        vals2 = np.array(vars2[key])
        (vals1, vals2) = check_lens(f, key, vals1, vals2)
        # check_vals is either the check_input or check_output function
        check_vals(f, key, vals1, vals2)
          
def parse_args () :
    description = ('Skywalker output difference tool: '+
        'Generates L1, L2, Linf diff norms for two skywalker files.')
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-p', metavar='path1:path2:...', 
        help='Search paths for the input module files seperated by ":".')
    parser.add_argument('-o', metavar='file.txt', 
        help='Output file to write results to. Default:stdout')
    parser.add_argument('file1')
    parser.add_argument('file2')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

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
   
    intersect_vars(f, data1.input,  data2.input,  check_input)
    intersect_vars(f, data1.output, data2.output, check_output)

    f.close()

