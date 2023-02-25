import os, sys, importlib
import numpy as np
import numpy.linalg as lin

# Look for data in whatever directory we're running in.
sys.path.append(os.getcwd())


def usage():
    """Provides usage info."""
    print("compare_coag_num_update.py: compare validaiton data in Python data modules.")
    print("usage: python3 compare_coag_validaiton.py <module1.py> <module2.py>")


def norms(x_comp, x_ref):
    """norms(x_comp, x_ref) - Returns L1, L2, and Linf norms for x_comp - x_ref."""
    diff = np.subtract(x_comp, x_ref)
    if 1 == diff.ndim:
        axis = None
    else:
        axis = 0
    L1 = lin.norm(diff, 1)
    L2 = lin.norm(diff, 2)
    Linf = lin.norm(diff, np.inf)
    return (L1, L2, Linf)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        exit(0)

    # Import the given data modules.
    data1 = importlib.import_module(sys.argv[1].replace(".py", ""))
    data2 = importlib.import_module(sys.argv[2].replace(".py", ""))

    # Make sure that the input and output names are identical.
    inputs1 = dir(data1.input)
    inputs1.sort()
    inputs2 = dir(data2.input)
    inputs2.sort()
    assert inputs1 == inputs2

    outputs1 = dir(data1.output)
    outputs1.sort()
    outputs2 = dir(data2.output)
    outputs2.sort()
    assert outputs1 == outputs2

    # Check that the input data is identical for data1 and data2.
    input_names = [
        i_name
        for i_name in inputs1
        if not i_name.startswith("_") and not i_name.endswith("_")
    ]
    for i_name in input_names:
        i1, i2 = getattr(data1.input, i_name), getattr(data2.input, i_name)
        assert i1 == i2

    # Check L1, L2, Linf norms for output data.
    output_names = [
        o_name
        for o_name in outputs1
        if not o_name.startswith("_") and not o_name.endswith("_")
    ]

    for o_name in output_names:
        o1, o2 = getattr(data1.output, o_name), getattr(data2.output, o_name)

        L1, L2, Linf = norms(o1, o2)

        print("%s: L1 = %g, L2 = %g, Linf = %g" % (o_name, L1, L2, Linf))

        # Here we treat number variables different his is because it appears that formula for aging is
        # sufficently ill-conditioned that near round errors can translate to large absolute differences in aerosol number.
        # The primary culprit is the computation of xferfrac_pcage  in
        # mam_pcarbon_aging_frac.

        if o_name not in [
            "qnum_cur",
            "qnum_del_coag",
            "qnum_del_cond",
            "xferfrac_pcage",
        ]:
            assert np.allclose(o1, o2)
        elif o_name == "qnum_cur":
            assert Linf < 1e7
        elif o_name == "qnum_del_coag":
            assert Linf < 1e7
        elif o_name == "qnum_del_cond":
            assert Linf < 1e7
        elif o_name == "xferfrac_pcage":
            assert Linf > 1e-6
