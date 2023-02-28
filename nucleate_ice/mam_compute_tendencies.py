# This file was automatically generated by skywalker.

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass

# Settings are stored here.
settings = Object()
settings.function = 'compute_tendencies'
# Input is stored here.
input = Object()
input.cloud_fraction = [0.01, ]
input.dry_diameter_aitken = [5.2e-08, ]
input.pressure = [100000, ]
input.temperature = [273, ]
input.updraft_vel_ice_nucleation = [0.01, ]
input.interstitial = [[7.299469308e-10, 1.811687805e-09, 2.991980389e-09, 1.911597588e-10, 1.123090476e-10, 7.563458575e-12, 1.356030726e-12, 2.715374903e-12, 1.327543704e-11, 1.034802167e-17, 9.187966638e-18, 3.683174593e-10, 2.421325192e-11, 1.126298407e-11, 2.008344526e-12, 1.872262953e-11, 3.028730249e-11, 4.394763138e-14, 1.065451952e-09, 1.107541088e-10, 1.828532564e-17, ],]
input.interstitial_num = [[629868471.6, 47879046.89, 64725.53148, 732612090.5, ],]

# Output data is stored here.
output = Object()
output.icenuc_num_depnuc = [0, ]
output.icenuc_num_hetfrz = [0, ]
output.icenuc_num_immfrz = [0, ]
output.icenuc_num_meydep = [0, ]
