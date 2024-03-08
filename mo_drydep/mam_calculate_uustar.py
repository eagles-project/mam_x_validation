# This file was automatically generated using the following command:
# ./merge_ensembles calculate_uustar_output_ts_100.py calculate_uustar_output_ts_300.py calculate_uustar_output_ts_300_loc2_has_snow.py calculate_uustar_output_ts_1000_loc3_over_water.py

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass

# Settings are stored here.
settings = Object()

# Input is stored here.
input = Object()
input.dt = [0.0, 0.0, 0.0, 0.0]
input.fr_lnduse = [[1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
input.index_season = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
input.lcl_frc_landuse = [[0.002091889806526504, 0.10112323792561469, 0.19104123086831826, 0.5670317901050222, 0.0, 0.04201923774885866, 0.08569376122393312, 0.006623429475491744, 0.0, 0.0, 0.004375422846234795], [0.002091889806526504, 0.10112323792561469, 0.19104123086831826, 0.5670317901050222, 0.0, 0.04201923774885866, 0.08569376122393312, 0.006623429475491744, 0.0, 0.0, 0.004375422846234795], [4.540810641666117e-06, 0.0, 0.12627596166595084, 0.0020540615542248117, 0.041079126949484526, 0.009342282077117719, 0.4689810916273251, 0.05037459228308989, 0.0, 0.0, 0.3018883430321654], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]]
input.ncol = [[4], [4], [4], [4]]
input.ribn = [[0.2], [-1.2100418490932332], [-0.035697676249964824], [-0.39727170786113664]]
input.unstable = [[0], [1], [1], [1]]
input.va = [[0.782837961384738], [1.4367391108154526], [7.484307925688188], [1.6739870852083936]]
input.z0 = [[1.0, 1.0, 1.0, 1.0, 1.0, 0.25, 0.1, 0.005, 0.001, 0.03, 0.05, 0.05, 0.05, 0.001, 0.02, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.002, 0.002, 0.002, 0.002, 0.002, 0.15, 0.1, 0.1, 0.001, 0.01, 0.1, 0.08, 0.02, 0.001, 0.03, 0.1, 0.08, 0.06, 0.04, 0.06], [1.0, 1.0, 1.0, 1.0, 1.0, 0.25, 0.1, 0.005, 0.001, 0.03, 0.05, 0.05, 0.05, 0.001, 0.02, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.002, 0.002, 0.002, 0.002, 0.002, 0.15, 0.1, 0.1, 0.001, 0.01, 0.1, 0.08, 0.02, 0.001, 0.03, 0.1, 0.08, 0.06, 0.04, 0.06], [1.0, 1.0, 1.0, 1.0, 1.0, 0.25, 0.1, 0.005, 0.001, 0.03, 0.05, 0.05, 0.05, 0.001, 0.02, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.002, 0.002, 0.002, 0.002, 0.002, 0.15, 0.1, 0.1, 0.001, 0.01, 0.1, 0.08, 0.02, 0.001, 0.03, 0.1, 0.08, 0.06, 0.04, 0.06], [1.0, 1.0, 1.0, 1.0, 1.0, 0.25, 0.1, 0.005, 0.001, 0.03, 0.05, 0.05, 0.05, 0.001, 0.02, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.002, 0.002, 0.002, 0.002, 0.002, 0.15, 0.1, 0.1, 0.001, 0.01, 0.1, 0.08, 0.02, 0.001, 0.03, 0.1, 0.08, 0.06, 0.04, 0.06]]
input.zl = [[12.816427027976749], [13.505708784823883], [11.495025186520767], [13.304651089489907]]

# Output data is stored here.
output = Object()
output.uustar = [[0.03198781076259495], [0.3395594415377216], [2.9335023410482277], [0.12901879149872647]]
