# This file was automatically generated using the following command:
# ./merge_ensembles drydep_xactive_output_ts_100.py drydep_xactive_output_ts_300.py drydep_xactive_output_ts_300_loc2_has_snow.py drydep_xactive_output_ts_1000_loc3_over_water.py

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass

# Settings are stored here.
settings = Object()

# Input is stored here.
input = Object()
input.air_temp = [[289.37659487255456], [305.0144969240973], [260.87173391455616], [299.0846416143141]]
input.dt = [0.0, 0.0, 0.0, 0.0]
input.heff = [[215141.5904869365, 210402677778.856, 3334.148860680581], [31138.432794480996, 42992261164.98709, 874.5427866732105], [1724166.2082613558, 1163173586735.6272, 14108.669620617442], [63920.21390215724, 77625658959.18587, 1438.7290493476496]]
input.latndx = [[44], [44], [93], [40]]
input.lchnk = [[154], [154], [121], [149]]
input.mmr = [[6.271178484937343e-08, 1.2014138845000207e-09, 2.0320503567926528e-14, 1.0880757686104383e-09, 1.2558459391659479e-11, 1.0086594008945506e-10, 3.1940892782495293e-09, 7.152645497741365e-09, 7.486217981303971e-09, 7.784196342057091e-10, 4.847479758095722e-10, 3.128332812558431e-11, 5.5147189520542214e-12, 1318595535.9387484, 1.1413080936572562e-11, 2.71925248217008e-14, 4.53233557372715e-16, 2.398242228554644e-16, 129763265.88840793, 2.5267591832691925e-09, 2.3152692716090606e-10, 1.4559353768621795e-10, 2.1651076987648425e-11, 1.9841779986857723e-10, 2.2699472098193436e-10, 2.848350372129358e-13, 315117.7823035339, 5.344151423804984e-09, 7.79123973830367e-10, 3.1154062692830645e-16, 3539480907.0476513], [7.401765972028359e-08, 1.5095694152333137e-09, 1.437083810200604e-13, 4.882520142026647e-10, 9.428801539197388e-12, 5.696412174533208e-10, 1.5988276771005057e-09, 9.784054071199668e-10, 8.960610501922823e-10, 1.133232733779067e-10, 1.5945412635011166e-10, 2.580832353026427e-10, 4.3940468736615364e-11, 601956763.7256415, 4.68600673118541e-12, 1.1671207564593005e-12, 1.2831712918014743e-14, 2.1581811577464284e-15, 42612013.36660468, 3.995912764371641e-09, 2.0999007631765785e-09, 1.292165397664524e-10, 9.770203408607921e-12, 8.263598927720707e-11, 6.59994724157162e-11, 2.057695865714875e-12, 685027.6810412994, 7.695521211963893e-10, 9.653472008007726e-11, 4.790543769733047e-16, 536620237.52795863], [6.31878175050871e-08, 4.943651451985827e-13, 1.5105147989873498e-15, 2.3929747409436772e-11, 1.196060280319605e-11, 3.530495729760678e-12, 1.2045089837855326e-10, 1.116090068260501e-12, 2.181408934045187e-11, 3.3873727565054036e-13, 2.0594323836341549e-13, 5.5712505164085336e-11, 5.697049588289728e-12, 14664415.316832155, 2.1700750556507433e-12, 2.9121106173107346e-13, 5.069768003076701e-14, 4.7971767563171786e-15, 9602671.353574624, 1.6745380068208482e-12, 5.366659745808594e-10, 1.6116524678116271e-12, 2.375259118039246e-14, 7.508277763203207e-14, 5.567965615722175e-13, 2.438655414207701e-14, 47343.1834530593, 5.9195738358539685e-12, 1.975019810855811e-12, 1.5118096336947842e-16, 4300981.423482117], [7.494828175761637e-08, 3.5144206527123963e-10, 1.0323628200988572e-13, 8.44286369181045e-11, 2.442693334152247e-10, 5.25455026960957e-10, 4.950501736547859e-10, 7.193591875237255e-11, 2.4850753758340275e-10, 1.3002735609008841e-11, 3.822225476564141e-12, 2.422427484194135e-10, 5.7746124242504766e-11, 150929349.7009944, 4.238514804091934e-12, 8.5495968961051e-13, 5.387212755703674e-14, 1.0676059921284828e-14, 111874526.58189912, 8.095161942702834e-12, 1.5802572272431854e-09, 3.4506942139705336e-11, 9.009337621977126e-13, 5.3002341758649675e-12, 1.810839927029915e-11, 3.2064570142509353e-12, 295611.540023412, 1.3589200606683676e-13, 4.9222010211106097e-14, 5.634057530873181e-19, 117319.3298938223]]
input.ncdate = [[10101], [10101], [10101], [10101]]
input.ncol = [[4], [4], [4], [4]]
input.pressure_10m = [[92183.724704183], [91745.04569752615], [96786.16286910103], [100893.2400907007]]
input.pressure_sfc = [[92322.5372251751], [91883.1976448756], [96931.90585473244], [101045.1676142738]]
input.rain = [[8.114928626655756e-08], [7.898022388071367e-09], [3.498278664761428e-08], [7.184020551714546e-08]]
input.rain_threshold = [[1e-07], [1e-07], [1e-07], [1e-07]]
input.ric = [[0.2], [0.2], [0.2], [0.2]]
input.sfc_temp = [[287.4065685294889], [311.0090481072723], [265.6953630375399], [301.7874019218962]]
input.snow = [[0.0], [0.0], [0.028049198638665552], [0.0]]
input.solar_flux = [[21.097480229915508], [776.3211552917976], [0.0], [0.0]]
input.spec_hum = [[0.009777448503919612], [0.009372456162327535], [0.0013665662991613672], [0.017030176368618196]]
input.temp_highbound = [[313.15], [313.15], [313.15], [313.15]]
input.tv = [[292.2059596271606], [307.8732319253928], [261.22823243452757], [304.17810581015084]]
input.wind_speed = [[0.782837961384738], [1.4367391108154526], [7.484307925688188], [1.6739870852083936]]

# Output data is stored here.
output = Object()
output.dflx = [[0.0, 1.4642284146416144e-12, 3.930214398336464e-17, 3.918123921078378e-13, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 6.0124451333734475e-12, 3.17205991286337e-15, 9.08700831752915e-13, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 3.4251766750956416e-17, 9.936663206473441e-20, 1.5339789079344717e-13, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 7.276742582558253e-13, 2.1375467640350355e-16, 1.7800218494233934e-13, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
output.dvel = [[0.0, 0.11089026529317021, 0.1759782582514471, 0.032763950988995906, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.38364519998951385, 2.1261358751610118, 0.17927041043821795, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.005367652538324623, 0.005096415716502062, 0.49662723723979857, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.17918084184482116, 0.17918084184482116, 0.1824499962368515, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
