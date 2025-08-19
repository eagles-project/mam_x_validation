import os, sys, importlib, itertools
import numpy as np
import numpy.linalg as lin
import argparse
from textwrap import fill

# Look for data in whatever directory we're running in.
sys.path.append(os.getcwd())

def usage():
    """Provides usage info."""
    print('compare_mam4xx_mam4.py: compares values in Python data modules.')
    print('usage: python3 compare_mam4xx_mam4.py <module1.py> <module2.py> ' +
          '[check_norms (bool)] [error_tol] [--verbose_debug=(bool)] [--concise_debug=(bool)]')


def norms(x_comp, x_ref) :
    """norms(x_comp, x_ref) - Returns L1, L2, and Linf norms for x_comp - x_ref."""
    diff = np.subtract(x_comp, x_ref)
    if 1 == diff.ndim :
      axis = None
    else :
      axis = 0
    L1 = lin.norm(diff, 1, axis)
    L2 = lin.norm(diff, 2, axis)
    Linf = lin.norm(diff, np.inf, axis)
    return (L1, L2, Linf)


def print_all_errors(errvec):
  print_sep(sz=1)
  print(tabvar + f'Error in L1 norm = {errvec[0]}')
  print(tabvar + f'Error in L2 norm = {errvec[1]}')
  print(tabvar + f'Error in Linf norm = {errvec[2]}')
  print_sep(sz=1)
  print(tabvar + f'Relative Error in L1 norm = {errvec[3]}')
  print(tabvar + f'Relative Error in L2 norm = {errvec[4]}')
  print(tabvar + f'Relative Error in Linf norm = {errvec[5]}')
  print_sep(sz=1)
  print(tabvar + f'NaN in output = {errvec[6]}')
  print_sep(sz=1)


def flatten_list(list_obj):
  """
  Flattens an arbitrarily nested, potentially ragged list of lists into a
  1D numpy array.
  Source: https://www.reddit.com/r/Python/comments/181yhw2/comment/kaq15sf/
  """
  while True:
    flatter = []
    done = True
    for item in list_obj:
      if isinstance(item, list):
        flatter.extend(item)
        done = False
      else:
        flatter.append(item)
    if done:
      return np.array(list_obj)
    list_obj = flatter


# desired max width of printed messages
pwidth = 100

def print_sep(n=1, sz=2):
  """
  prints "===" or "---" separators to visually divide different outputs.
  width of separators is the same as the max-width of the text wrapping.
  Arguments:
    n: number of lines of separators to print (default n=1)
    sz = {1, 2}: controls whether separator is composed of '===' (sz=2 - default) or '---' (sz=1)
  """
  if sz == 2:
    for _ in range(n):
      print('=' * pwidth)
  elif sz == 1:
    for _ in range(n):
      print('-' * pwidth)

# define the tabs here for consistency between manual indents and textwrap.fill()
tsize = 2
tabvar = ' ' * tsize

if __name__ == '__main__':
  if len(sys.argv) < 3:
    usage()
    exit(0)

  # arg1 = module 1
  # arg2 = module 2
  # arg3 = check norms (False)
  # arg4 = error_threshold (1e-6)
  # arg (optional) = verbose_debug (False)
  #   If inputs differ: prints full inputs and the entry-wise difference
  #   Always: prints full outputs
  # arg (optional) = concise_debug (False)
  #   Prints only test status and the name and error values for all failing outputs

  # NOTE: required arguments are handled as command-line args, whereas optional
  # arguments for printing debug info use argparser, which allows them to be
  # optional without interfering with the presence of the original positional
  # args (1-4, above)

  parser = argparse.ArgumentParser()
  parser.add_argument('-v', '--verbose_debug', required=False, default=True,
                      help='boolean flag controlling whether input/output'
                      + 'arrays are printed when diff is detected')
  parser.add_argument('-c', '--concise_debug', required=False, default=False,
                      help='boolean flag controlling whether output is '
                      + 'printed in a concise manner for ease in diagnosing failures')
  args = parser.parse_known_args(args=sys.argv)
  verbose_debug = args[0].verbose_debug
  concise_debug = args[0].concise_debug

  if verbose_debug and concise_debug:
    print('Error: the arguments --verbose_debug (-v) and --concise_debug (-c) '
          + 'cannot both be set to true.')
    exit(1)

  testname = sys.argv[1].replace('.py', '')
  # Import the given data modules.
  data1 = importlib.import_module(sys.argv[1].replace('.py', ''))
  data2 = importlib.import_module(sys.argv[2].replace('.py', ''))

  #Default check norms
  check_norms = True
  if len(sys.argv) > 3:
    check_norms = eval(sys.argv[3])

  # Default threshold error
  error_threshold = 1e-6
  if len(sys.argv) > 4:
    error_threshold = float(sys.argv[4])

  if not concise_debug:
    print_sep()
    print(f'Error threshold = {error_threshold}')
    print(f'Verbose debug = {verbose_debug}')
    print(f'Concise debug = {concise_debug}')
    print_sep()

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
    i1 = flatten_list(i1)
    i2 = flatten_list(i2)
    iL1, iL2, iLinf = norms(i1, i2)
    bL1, bL2, bLinf = norms(i2, np.zeros_like(i2))
    if (bL1 == 0) or (bL2 == 0) or (bLinf == 0):
      bL1, bL2, bLinf = norms(i1, np.zeros_like(i1))
    if (bL1 == 0) or (bL2 == 0) or (bLinf == 0):
      continue
    iL1_rel = iL1 / bL1
    iL2_rel = iL2 / bL2
    iLinf_rel = iLinf / bLinf
    input_diff = np.max((iL1_rel, iL2_rel, iLinf_rel))
    # 1e-12 is somewhat arbirtrary, but equality isn't expected, and the only
    # downside of a small tolerance is the potential of extra inputs being
    # flagged as differing and no effect on pass/fail of test
    if (input_diff > 1e-12) and not concise_debug:
      print("Input difference for variable: ", i_name)
      if verbose_debug:
        print_sep(sz=1)
        print(tabvar + f"Input values:")
        ntabs = 2
        prefix = tabvar * ntabs + 'i1 = [['
        subs_ind = len(prefix)
        print(fill(f"i1 = {i1}", width=pwidth, tabsize=2,
                   initial_indent=tabvar * ntabs,
                  subsequent_indent=' ' * subs_ind))
        print(fill(f"i2 = {i2}", width=pwidth, tabsize=2,
                   initial_indent=tabvar * ntabs,
                  subsequent_indent=' ' * subs_ind))
        print(fill(f"Absolute entry-wise difference = {np.abs(np.array(i1) - np.array(i2))}",
                  width=pwidth, tabsize=2, initial_indent=tabvar * ntabs,
                  subsequent_indent=' ' * subs_ind))
        print(tabvar + f'Error in L1 norm (input {i_name}) = {iL1}')
        print(tabvar + f'Error in L2 norm (input {i_name}) = {iL2}')
        print(tabvar + f'Error in Linf norm (input {i_name}) = {iLinf}')
        print_sep(sz=1)
        print(tabvar + f'Relative Error in L1 norm (input {i_name}) = {iL1_rel}')
        print(tabvar + f'Relative Error in L2 norm (input {i_name}) = {iL2_rel}')
        print(tabvar + f'Relative Error in Linf norm (input {i_name}) = {iLinf_rel}')
      assert(np.allclose(i1, i2))

  # Check L1, L2, Linf norms for output data.
  output_names = [o_name for o_name in outputs1 \
                  if not o_name.startswith('_') \
                  and not o_name.endswith('_')]

  # assume that test passes and change on failure
  pass_all_tests = np.full(np.shape(output_names), True)
  fail_tests = dict.fromkeys(output_names)
  for i_out, o_name in enumerate(output_names):
    all_zeros_print = False
    o1, o2 = getattr(data1.output, o_name), getattr(data2.output, o_name)

    # There is no requirement for the arrays in Skywalker to be regular and not
    # ragged with different length sub-lists.
    # To handle this, we recursively flatten the list into a 1D numpy array.
    # This should take care of matters for arbitrarily nested,
    # arbitrarily-patterned ragged lists, as long as the entries in the
    # compared arrays correspond when reading from left-to-right,
    # then top-to-bottom.
    # However, it is likely to fail if the arrays have a different number of
    # entries... but that would be very strange and should probably fail anyway.

    # if type(o1) is list and 0 < len(o1) and type(o1[0]) is list:
    o1_a = flatten_list(o1).astype(float)
    # if type(o2) is list and 0 < len(o2) and type(o2[0]) is list:
    o2_a = flatten_list(o2).astype(float)

    # calculate errors
    L1, L2, Linf = norms(o1_a, o2_a)
    # try to be smart about how we choose the scaling factor for rel. error
    if np.all(o2_a == 0) and not np.all(o1_a == 0):
      print('!' * pwidth)
      print(f"Warning! Reference solution for {o_name} contains all zeros.")
      print("As a result, relative error will be calculated via scaling by 1.")
      print("This will result in relative error that is equal to absolute error.")
      print("It is recommended to take a closer look at these results.")
      print('!' * pwidth)
      L1, L2, Linf = norms(o1_a, np.zeros_like(o1_a))
      L1_base = 1
      L2_base = 1
      Linf_base = 1
      all_zeros_print = True
    elif np.all(o1_a == 0) and np.all(o2_a == 0):
      pass_all_tests[i_out] = True
      print('!' * pwidth)
      print("Warning! Both the reference and calculated solutions are entirely zeros.")
      print("The test passes for this quantity, but the test may be missing something important.")
      print('!' * pwidth)
      continue
    else:
      L1_base, L2_base, Linf_base = norms(o2_a, np.zeros_like(o2_a))

    if verbose_debug:
      print_sep()
      print(f'Checking output field: {o_name}')
      print_sep()

    # check for the bit-for-bit case to exit early
    if L1 == 0 and L2 == 0 and Linf == 0:
      pass_all_tests[i_out] = True
      print('!' * pwidth)
      print("Good news--answers match to numerical precision!")
      print('!' * pwidth)
      continue

    ntabs = 1
    prefix = tabvar * ntabs + 'o1_a = ['
    subs_ind = len(prefix)
    rel_inf = False
    if check_norms:
      if verbose_debug:
        print(fill(f"o1_a = {list(o1_a)}", width=pwidth, tabsize=2,
                   initial_indent=tabvar * ntabs,
                   subsequent_indent=' ' * subs_ind))
        print(fill(f"o2_a = {list(o2_a)}", width=pwidth, tabsize=2,
                   initial_indent=tabvar * ntabs,
                   subsequent_indent=' ' * subs_ind))
        print_sep()
      L1_rel_error = L1 / L1_base
      if L1_rel_error > error_threshold: pass_all_tests[i_out] = False
      L2_rel_error = L2 / L2_base
      if L2_rel_error > error_threshold: pass_all_tests[i_out] = False
      Linf_rel_error = Linf / Linf_base
      if Linf_rel_error > error_threshold: pass_all_tests[i_out] = False
      outputNaN = np.any(np.isnan([L1, L2, Linf]))
      if outputNaN:
        pass_all_tests[i_out] = False
      if not pass_all_tests[i_out]:
        fail_tests[o_name] = (L1, L2, Linf, L1_rel_error, L2_rel_error,
                              Linf_rel_error, outputNaN)
      if all_zeros_print:
        print_sep(sz=1)
        print(f'Reference solution is all zeros - Printing error')
        print_all_errors(fail_tests[o_name])

  # We collect the errors and print at the end for easier output formatting
  if not concise_debug:
    print(f'{testname} final pass array = {pass_all_tests}')
    print_sep()
  if np.all(pass_all_tests):
    print(f'TEST STATUS for {testname}:')
    print(tabvar + f'PASS for error threshold = {error_threshold}')
  else:
    print(f'TEST STATUS for {testname}:')
    print(tabvar + f'FAIL for error threshold = {error_threshold}')
    print_sep()
    print(f'List of failing outputs:')
    for n, s in zip(output_names, pass_all_tests):
      if not s:
        print_sep(sz=1)
        print(tabvar + f'OUTPUT: {n} - FAILED')
        print_all_errors(fail_tests[n])
  print_sep(2)
  # assert pass/fail at the end so we always get informational output
  assert(np.all(pass_all_tests))
