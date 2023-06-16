# This file was automatically generated by skywalker.

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass

# Settings are stored here.
settings = Object()
settings.function = 'compute_massflux'
# Input is stored here.
input = Object()
input.dt = [0, ]
input.icol = [2, ]
input.ii = [1, ]
input.kbot = [71, ]
input.ktop = [48, ]
input.xx_mfup_max = [0, ]
input.dpdry_i = [[4.765070038e-12, 7.035664904e-12, 1.038821682e-11, 1.533828715e-11, 2.264710651e-11, 3.343863818e-11, 4.937242326e-11, 7.289878786e-11, 1.076356587e-10, 1.589249343e-10, 2.08797421e-10, 2.729924357e-10, 3.46282674e-10, 4.257457076e-10, 5.067320514e-10, 5.829370958e-10, 6.467709753e-10, 7.078321953e-10, 7.531472877e-10, 7.745217206e-10, 7.665986208e-10, 7.256396525e-10, 6.501465518e-10, 6.680386871e-10, 7.248126163e-10, 7.86411856e-10, 8.532455119e-10, 9.257589768e-10, 1.004434976e-09, 1.089795461e-09, 1.182409649e-09, 1.282897822e-09, 1.391925535e-09, 1.49890914e-09, 1.621599841e-09, 1.759360886e-09, 1.908817141e-09, 2.070921566e-09, 2.246679744e-09, 2.437159724e-09, 2.643389839e-09, 2.866642561e-09, 3.108248017e-09, 3.369612514e-09, 3.652397152e-09, 3.850919299e-09, 3.859307795e-09, 3.805533186e-09, 3.666455103e-09, 3.543544734e-09, 3.372297809e-09, 3.152991638e-09, 2.889401869e-09, 2.583581065e-09, 2.238811208e-09, 1.859872616e-09, 1.513253436e-09, 1.337291223e-09, 1.306377665e-09, 1.273368575e-09, 1.238298367e-09, 1.201247665e-09, 1.162285659e-09, 1.121415683e-09, 1.078592861e-09, 1.033926141e-09, 9.876006995e-10, 9.398629986e-10, 8.90691834e-10, 8.398955378e-10, 6.299115581e-10, 2.926118545e-10, ],]
input.du = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5.931125871e-08, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],]
input.ed = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.531137436e-06, 4.534876034e-07, 4.879672565e-07, 5.220609019e-07, 5.550373995e-07, 5.862523151e-07, 6.151461032e-07, 6.408613414e-07, 6.627918769e-07, 6.817792654e-07, 6.998151165e-07, 7.178477132e-07, 7.357271401e-07, 7.534460469e-07, 7.709790395e-07, 7.882504605e-07, 8.052376209e-07, 8.219192611e-07, 8.381202301e-07, 8.537614331e-07, 8.68116321e-07, 8.804490271e-07, -6.198410683e-06, 0, ],]
input.eu = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3.362508108e-07, 2.990082413e-07, 2.691476474e-07, 2.447379402e-07, 2.24876483e-07, 2.088854006e-07, 1.962457107e-07, 1.864566676e-07, 1.789683946e-07, 1.729816846e-07, 1.677020882e-07, 1.627919613e-07, 1.582058164e-07, 1.539344168e-07, 1.499645185e-07, 1.46274332e-07, 1.428539136e-07, 1.396938622e-07, 1.367604949e-07, 1.340399171e-07, 1.314232504e-07, 1.288147024e-07, 2.224467111e-07, 0, ],]

# Output data is stored here.
output = Object()
output.xx_mfup_max = [8.519885612e-15, ]
output.md_i = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1.661321197e-14, -1.822016558e-14, -1.986573649e-14, -2.151179015e-14, -2.311551625e-14, -2.463014663e-14, -2.600734262e-14, -2.719926308e-14, -2.820223517e-14, -2.911397259e-14, -3.002819543e-14, -3.094228015e-14, -3.185332987e-14, -3.275840517e-14, -3.365450305e-14, -3.453845948e-14, -3.540698303e-14, -3.625678684e-14, -3.708451497e-14, -3.788693375e-14, -3.866015787e-14, -3.939964307e-14, 0, 0, ],]
output.mu_i = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],]