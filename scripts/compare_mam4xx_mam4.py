import os, sys, importlib, itertools
import numpy as np
import numpy.linalg as lin

# Look for data in whatever directory we're running in.
sys.path.append(os.getcwd())

def usage():
    """Provides usage info."""
    print('compare_mam4xx_mam4.py: compares values in Python data modules.')
    print('usage: python3 compare_mam4xx_mam4.py <module1.py> <module2.py>')


def norms(x_comp, x_ref) :
    """norms(x_comp, x_ref) - Returns L1, L2, and Linf norms for x_comp - x_ref."""
    diff = np.subtract(x_comp, x_ref)
    if 1 == diff.ndim :
      axis=None
    else :
      axis=0
    L1 = lin.norm(diff,1,axis)
    L2 = lin.norm(diff,2,axis)
    Linf = lin.norm(diff,np.inf,axis)
    return (L1, L2, Linf)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        exit(0)

    # Import the given data modules.
    data1 = importlib.import_module(sys.argv[1].replace('.py', ''))
    data2 = importlib.import_module(sys.argv[2].replace('.py', ''))
    # Threshold error
    L1_max=1e-6
    L2_max=1e-6
    Linf_max=1e-6

    # Make sure that the input and output names are identical.
    inputs1 = dir(data1.input)
    inputs1.sort()
    inputs2 = dir(data2.input)
    inputs2.sort()
    assert(inputs1 == inputs2)

    outputs1 = dir(data1.output)
    outputs1.sort()
    outputs2 = dir(data2.output)
    outputs2.sort()
    assert(outputs1 == outputs2)

    # Check that the input data is identical for data1 and data2.
    input_names = [i_name for i_name in inputs1 \
                   if not i_name.startswith('_') \
                   and not i_name.endswith('_')]
    for i_name in input_names:
        i1, i2 = getattr(data1.input, i_name), getattr(data2.input, i_name)
        assert(i1 == i2)

    # Check L1, L2, Linf norms for output data.
    output_names = [o_name for o_name in outputs1 \
                    if not o_name.startswith('_') \
                    and not o_name.endswith('_')]

    for o_name in output_names:
        pad_token = 0
        o1, o2 = getattr(data1.output, o_name), getattr(data2.output, o_name)

        # There is no requirement for the arrays in Skywalker to be regular. They could
        # be ragged with each line a different length. But numpy arrays are made of
        # regular lists. So find a command from Stackoverflow that will fill out
        # irregular lists and padd with 0's.
        if type(o1) is list and 0 < len(o1) and type(o1[0]) is list : 
            o1 = [list(i) for i in zip(*itertools.zip_longest(*o1, fillvalue=pad_token))]
        if type(o2) is list and 0 < len(o2) and type(o2[0]) is list : 
            o2 = [list(i) for i in zip(*itertools.zip_longest(*o2, fillvalue=pad_token))]

        o1_a= np.array(o1)
        o2_a= np.array(o2)
        L1, L2, Linf = norms(o1_a, o2_a)
        print(o_name)
        print('L1',L1)
        print('L2',L2)
        print('Linf',Linf) 
        #assert(L1.max() < L1_max)
        #assert(L2.max() < L2_max)
        #assert(Linf.max() < Linf_max)   
