import os, sys, importlib

# Look for data in whatever directory we're running in.
sys.path.append(os.getcwd())

def usage():
    print('compare_nucleation_rate.py: compares nucleation rates in Python data modules.')
    print('usage: python3 compare_nucleation_rate.py <module1.py> <module2.py>')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        exit(0)

    # Import the given data modules.
    data1 = importlib.import_module(sys.argv[1].replace('.py', ''))
    data2 = importlib.import_module(sys.argv[2].replace('.py', ''))

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

    # FIXME: quantitative comparisons go here!
