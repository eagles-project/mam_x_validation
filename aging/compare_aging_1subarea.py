import os, sys, importlib
import numpy as np
import numpy.linalg as lin

# Look for data in whatever directory we're running in.
sys.path.append(os.getcwd())


def usage():
    """Provides usage info."""
    print(
        "compare_particle_growth.py: compares particle cluster growth rates in Python data modules."
    )
    print("usage: python3 compare_particle_growth.py <module1.py> <module2.py>")


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

    assert "mam_" in sys.argv[2]
    assert "mam4xx_" in sys.argv[1]

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
        o1, o2 = np.array(getattr(data1.output, o_name), dtype=np.double), np.array(
            getattr(data2.output, o_name), dtype=np.double
        )
        L1, L2, Linf = norms(o1, o2)

        o1, o2 = np.squeeze(o1), np.squeeze(o2)

        p_error = 100.0 * np.max(
            np.divide(
                np.abs(np.subtract(o1, o2)),
                o2,
                out=np.zeros_like(o1),
                where=o2 != 0.0,
                casting="same_kind",
            )
        )
        print(
            "%s: L1 = %g, L2 = %g, Linf = %g, Percent Error = %g"
            % (o_name, L1, L2, Linf, p_error)
        )

    for o_name in output_names:
        o1, o2 = getattr(data1.output, o_name), getattr(data2.output, o_name)
        assert np.allclose(o1, o2)