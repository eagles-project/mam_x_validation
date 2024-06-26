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

    # arg1 = module 1
    # arg2 = module 2
    # arg3 = check norms (False)
    # arg4 = error_threshold (1e-6)

    #Default check norms
    check_norms=False
    if len(sys.argv) > 3:
        check_norms=eval(sys.argv[3])

    # Default threshold error
    error_threshold=1e-6
    if len(sys.argv) > 4:
        error_threshold=float(sys.argv[4])

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
        L1, L2, Linf = norms(i1, i2)
        # max4norm = np.max((np.max(np.abs(i1)), np.max(np.abs(i2))))
        # minvalQ = np.min((np.min(np.abs(i1)), np.min(np.abs(i2))))
        # rel_error_1 = L1 / max4norm
        # rel_error_2 = L2 / max4norm
        # rel_error_inf = Linf / max4norm
        # print(f'Input error for {i_name}:')
        # print(f'max4norm = {max4norm}')
        # print(f'min val = {minvalQ}')
        # # print("L1 error", L1)
        # # print("L2 error", L2)
        # print("Linf error", Linf)
        # print("Linf rel_error", rel_error_inf)
        # if np.any(rel_error_1 > 1e-8) or np.any(rel_error_2 > 1e-8) or np.any(rel_error_inf > 1e-8):
        #   # print("i1", list(i1))
        #   # print("i2", list(i2))
        #   # print("L1 rel_error", rel_error_1)
        #   # print("L2 rel_error", rel_error_2)
        #   print(f'Input error for {i_name}:')
        #   print("Linf error", Linf)
        #   print("Linf rel_error", rel_error_inf)
          # assert(rel_error_1 < 1e-8 and rel_error_2 < 1e-8 and rel_error_inf < 1e-8)

        # if not np.allclose(i1, i2):
        #     print("Input Difference: ", i_name, ' i1: ', i1, ' i2: ', i2)
            # assert(np.allclose(i1, i2))

    # Check L1, L2, Linf norms for output data.
    output_names = [o_name for o_name in outputs1 \
                    if not o_name.startswith('_') \
                    and not o_name.endswith('_')]

    # assume that test passes.
    pass_all_tests = np.full(np.shape(output_names), True)
    for i_out, o_name in enumerate(output_names):
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
        # make arrays 1D
        o1_a = o1_a.ravel()
        o2_a = o2_a.ravel()
        L1, L2, Linf = norms(o1_a, o2_a)

        print(o_name)
        print('L1',L1)
        print('L2',L2)
        print('Linf',Linf)

        # o1a = np.array(o1_a)
        # o2a = np.array(o2_a)
        # for o1, o2 in zip(o1a, o2a):
        #   adiff = np.abs(o1 - o2)
        #   if adiff > 1e-10 and (o1 < 1e30 or o2 < 1e30):
        #     print(f'abs diff = {adiff}')
        #     print(f'o1_a = {o1}')
        #     print(f'o2_a = {o2}')

        if check_norms:
            max4norm = np.max((np.max(np.abs(o1_a)), np.max(np.abs(o2_a))))
            minvalQ = np.min((np.min(np.abs(o1_a)), np.min(np.abs(o2_a))))
            print(f'maxval = {max4norm}')
            print(f'minval = {minvalQ}')
            print("o1_a", list(o1_a))
            print("o2_a", list(o2_a))
            rel_error = L1/ max4norm
            print("L1 rel_error",rel_error)
            if rel_error > error_threshold: pass_all_tests[i_out] = False
            rel_error = L2/ max4norm
            print("L2 rel_error",rel_error)
            if rel_error > error_threshold: pass_all_tests[i_out] = False
            rel_error = Linf/ max4norm
            print("Linf rel_error",rel_error)
            if rel_error > error_threshold: pass_all_tests[i_out] = False
            if np.any(np.isnan([L1, L2, Linf])):
                print("NaN in results--failing test")
                pass_all_tests[i_out] = False
    print(f'final pass array = {pass_all_tests}')
    assert(np.all(pass_all_tests))
