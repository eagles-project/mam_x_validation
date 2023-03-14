# This file was automatically generated using the following command:
# ./merge_ensembles.py nucleate_ice_cam_calc_output_ts_1402.py nucleate_ice_cam_calc_output_ts_1403.py nucleate_ice_cam_calc_output_ts_1404.py nucleate_ice_cam_calc_output_ts_1406.py nucleate_ice_cam_calc_output_ts_1410.py

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass

# Settings are stored here.
settings = Object()

# Input is stored here.
input = Object()
input.alnsg_amode = [[0.5877866649, 0.4700036292, 0.5877866649, 0.4700036441], [0.5877866649, 0.4700036292, 0.5877866649, 0.4700036441], [0.5877866649, 0.4700036292, 0.5877866649, 0.4700036441], [0.5877866649, 0.4700036292, 0.5877866649, 0.4700036441], [0.5877866649, 0.4700036292, 0.5877866649, 0.4700036441]]
input.ast = [[0.999], [0.999], [0.7120661434], [0.331647452], [0.999]]
input.dgnum = [[1.117680669e-07, 4.731958792e-08, 1.752052657e-06, 1.000000012e-07], [1.04259823e-07, 4.110350268e-08, 1.768073929e-06, 1.000000012e-07], [1.535284746e-07, 5.157700473e-08, 1.085711795e-06, 1.000000012e-07], [1.537122098e-07, 5.183740215e-08, 1.083050841e-06, 1.000000012e-07], [1.614176541e-07, 4.13050011e-08, 1.133878851e-06, 1.000000012e-07]]
input.dt = [0.0, 0.0, 0.0, 0.0, 0.0]
input.lchnk = [[136], [136], [137], [137], [114]]
input.lptr_bc_a_amode = [[19, -999888777, 32, 38], [19, -999888777, 32, 38], [19, -999888777, 32, 38], [19, -999888777, 32, 38], [19, -999888777, 32, 38]]
input.lptr_dust_a_amode = [[20, -999888777, 29, -999888777], [20, -999888777, 29, -999888777], [20, -999888777, 29, -999888777], [20, -999888777, 29, -999888777], [20, -999888777, 29, -999888777]]
input.lptr_mom_a_amode = [[22, 27, 35, 39], [22, 27, 35, 39], [22, 27, 35, 39], [22, 27, 35, 39], [22, 27, 35, 39]]
input.lptr_nacl_a_amode = [[21, 26, 30, -999888777], [21, 26, 30, -999888777], [21, 26, 30, -999888777], [21, 26, 30, -999888777], [21, 26, 30, -999888777]]
input.lptr_pom_a_amode = [[17, -999888777, 33, 37], [17, -999888777, 33, 37], [17, -999888777, 33, 37], [17, -999888777, 33, 37], [17, -999888777, 33, 37]]
input.lptr_so4_a_amode = [[16, 24, 31, -999888777], [16, 24, 31, -999888777], [16, 24, 31, -999888777], [16, 24, 31, -999888777], [16, 24, 31, -999888777]]
input.lptr_soa_a_amode = [[18, 25, 34, -999888777], [18, 25, 34, -999888777], [18, 25, 34, -999888777], [18, 25, 34, -999888777], [18, 25, 34, -999888777]]
input.mincld = [[0.0001], [0.0001], [0.0001], [0.0001], [0.0001]]
input.modeptr_accum = [[1], [1], [1], [1], [1]]
input.modeptr_aitken = [[2], [2], [2], [2], [2]]
input.modeptr_coarse = [[3], [3], [3], [3], [3]]
input.ncol = [[4], [4], [4], [4], [4]]
input.nucleate_ice_subgrid = [[1.2], [1.2], [1.2], [1.2], [1.2]]
input.numptr_amode = [[23, 28, 36, 40], [23, 28, 36, 40], [23, 28, 36, 40], [23, 28, 36, 40], [23, 28, 36, 40]]
input.pmid = [[93776.24033], [91349.0301], [23463.78114], [23457.38215], [36912.36844]]
input.rho = [[1.373572514], [1.342996745], [0.3784315403], [0.3779369685], [0.5416944083]]
input.so4_sz_thresh_icenuc = [[8e-08], [8e-08], [8e-08], [8e-08], [8e-08]]
input.state_q = [[0.0001691718148, 0.0, 4.443171907e-07, 11720342.8, 3270.620347, 8.316984984e-10, 6.631901851e-07, 2.480873558, 168.7830519, 6.904267833e-08, 3.300307612e-12, 1.125502939e-11, 7.739043283e-10, 5.014807362e-14, 2.245458505e-10, 8.980692555e-10, 2.152539857e-11, 3.673798005e-10, 2.560705195e-11, 1.555588133e-12, 2.678551644e-12, 2.149558887e-13, 262046430.7, 3.400487059e-11, 3.202989633e-11, 5.554260656e-16, 1.49750634e-17, 343423565.8, 1.807667558e-11, 1.477547096e-10, 1.442160446e-12, 3.471642529e-14, 1.280343677e-13, 2.151641601e-12, 1.392372471e-14, 6474.282102, 1.406416528e-11, 4.860795442e-11, 3.498445013e-18, 26614752.05], [0.000157451874, 0.0, 2.565947387e-07, 6667282.612, 1698.008622, 1.260423295e-10, 5.532751428e-07, 3.549101072e-05, 150.8081514, 7.045423049e-08, 2.67247341e-12, 7.979591941e-12, 8.670358027e-10, 3.071821211e-14, 2.816240408e-10, 7.503232305e-10, 1.512049091e-11, 2.793011578e-10, 1.797026176e-11, 1.580261346e-12, 3.750734597e-12, 3.117463531e-13, 263655476.6, 2.955123203e-11, 3.708819015e-11, 9.928075154e-16, 3.318015033e-17, 561455398.9, 1.765536078e-11, 2.06922605e-10, 1.340000928e-12, 2.979398565e-14, 1.073741743e-13, 2.851027568e-12, 1.512587896e-14, 8335.727486, 1.009279414e-11, 3.760472749e-11, 3.409702664e-18, 20411478.21], [5.358551952e-05, 0.0, 7.120661434e-08, 1e-12, 1741.268529, 1.955696397e-36, 4.001799617e-08, 1e-12, 67.33069705, 2.481598003e-07, 3.18985873e-11, 1.278242821e-13, 6.103334787e-12, 3.286959794e-14, 2.012488102e-13, 4.655832298e-10, 2.163261387e-10, 1.001552296e-09, 3.11036846e-11, 1.137495554e-11, 4.830967451e-11, 7.120776735e-12, 170667559.1, 3.438936835e-12, 1.384926291e-11, 9.124319767e-15, 1.267984471e-15, 80752839.78, 3.355188613e-11, 2.39236645e-10, 7.140888871e-12, 4.600833561e-13, 3.133189682e-12, 9.886571818e-12, 2.012124248e-13, 49442.03727, 2.138529354e-11, 3.277399375e-12, 4.323308942e-17, 16419619.68], [5.640225907e-05, 0.0, 3.31647452e-08, 1e-12, 665.3378641, 8.824855477e-38, 2.794080647e-08, 1e-12, 48.3953706, 2.4373097e-07, 3.141816848e-11, 7.455563181e-14, 5.846735159e-12, 4.532826351e-14, 1.195270102e-13, 4.58264191e-10, 2.16594351e-10, 1.004313892e-09, 3.112204703e-11, 1.130403847e-11, 4.968333405e-11, 7.297406409e-12, 169987532.4, 3.373643823e-12, 1.376530034e-11, 9.793079067e-15, 1.35570667e-15, 78858489.6, 3.299128659e-11, 2.465366391e-10, 7.070463899e-12, 4.470653077e-13, 3.034930944e-12, 9.690032381e-12, 2.027867934e-13, 50934.10939, 2.100893833e-11, 3.213787599e-12, 4.422679947e-17, 16123566.49], [0.000347797344, 7.888609052e-31, 2.77458974e-05, 126479.4392, 1079042.573, 4.947354719e-14, 7.405924404e-07, 0.002898065787, 261.730618, 1.392340411e-07, 1.765735847e-10, 5.596693426e-14, 1.126966307e-11, 9.369351809e-14, 7.312325862e-12, 1.384232074e-09, 2.138048213e-10, 9.736906186e-10, 3.830768034e-11, 1.2994074e-11, 7.834467259e-11, 1.210422482e-11, 198348144.6, 1.625256023e-11, 1.586678953e-11, 3.997451398e-14, 5.885590259e-15, 241864361.8, 1.991821069e-10, 4.744548529e-10, 2.50584518e-11, 1.115722975e-12, 6.402175108e-12, 1.650528854e-11, 2.947887252e-13, 103355.9575, 1.086172984e-10, 2.282653662e-11, 9.755330896e-17, 81174406.25]]
input.temperature = [[237.8457014], [236.9643763], [216.0054731], [216.2291542], [237.3950401]]
input.wsubi = [[0.2], [0.2], [0.2], [0.2], [0.2]]

# Output data is stored here.
output = Object()
output.naai = [[13977.85118], [0.0], [0.0], [1396028.04], [28473.41106]]
output.naai_hom = [[219964.2654], [0.0], [0.0], [1396028.04], [0.0]]
output.nidep = [[0.0], [0.0], [0.0], [0.0], [0.0]]
output.nihf = [[302136.869], [0.0], [0.0], [527610.6053], [0.0]]
output.niimm = [[947.8315467], [863.3937165], [0.0], [0.0], [15423.88755]]
output.nimey = [[0.0], [0.0], [0.0], [0.0], [0.0]]
