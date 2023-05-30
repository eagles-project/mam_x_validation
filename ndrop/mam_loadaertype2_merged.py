# This file was automatically generated using the following command:
# ./merge_ensembles.py loadaer_output_ts_1400_type2.py loadaer_output_ts_1401_type2.py loadaer_output_ts_1402_type2.py loadaer_output_ts_1403_type2.py loadaer_output_ts_1404_type2.py loadaer_output_ts_1405_type2.py loadaer_output_ts_1406_type2.py loadaer_output_ts_1410_type2.py loadaer_output_ts_1415_type2.py loadaer_output_ts_1416_type2.py loadaer_output_ts_1417_type2.py

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass

# Settings are stored here.
settings = Object()

# Input is stored here.
input = Object()
input.cs = [[1.030692652], [1.032159141], [1.033546461], [1.035312219], [1.037253451], [1.039222683], [1.041186977], [1.047065413], [1.04659439], [1.047398848], [1.048157802]]
input.dt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
input.maxd_aspectype = [[14], [14], [14], [14], [14], [14], [14], [14], [14], [14], [14]]
input.ntot_amode = [[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]]
input.phase = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
input.state_q = [[0.001347764225, 2.200183448e-06, 5.570331565e-08, 22780616.18, 82.55142931, 4.359672869e-08, 9.528269887e-06, 77.11107237, 217.2470562, 1.014992581e-07, 7.694744225e-11, 5.549296734e-13, 1.576310354e-10, 9.703320227e-15, 1.131734002e-11, 4.620771575e-10, 1.708558285e-11, 9.276521418e-11, 4.76665851e-12, 4.25356095e-13, 3.492385296e-11, 3.324955239e-12, 90246433.22, 1.199745915e-10, 9.740991782e-12, 3.23236844e-14, 3.541688412e-15, 1935357826.0, 1.256356999e-12, 3.666340574e-10, 9.438032138e-12, 1.23149536e-13, 5.016389773e-13, 3.299803435e-12, 8.930978233e-14, 47723.18704, 8.562448323e-11, 2.344574669e-11, 1.813647193e-16, 66174948.7], [0.001292658147, 1.581498237e-06, 6.554884071e-08, 13533972.07, 84.59266597, 7.913847771e-08, 1.121829736e-05, 48.21904542, 214.8659635, 1.019777078e-07, 8.064875694e-11, 7.723184276e-13, 1.524330398e-10, 6.929221556e-15, 1.141078069e-11, 5.040663168e-10, 1.925924035e-11, 1.057438259e-10, 5.304242754e-12, 4.891774689e-13, 3.999964303e-11, 3.812369885e-12, 97039011.47, 1.204333345e-10, 9.860709929e-12, 3.355974451e-14, 3.649294483e-15, 1914686978.0, 1.382999304e-12, 4.090780247e-10, 1.034580799e-11, 1.308109226e-13, 5.339054505e-13, 3.615967915e-12, 9.702162443e-14, 54527.86661, 8.493954546e-11, 2.322441587e-11, 1.784184683e-16, 65682356.61], [0.001232152635, 1.296331498e-06, 7.695843099e-08, 9475099.886, 94.16632878, 1.406648126e-08, 9.119620384e-06, 31.56777064, 205.8707735, 1.025455892e-07, 8.484697543e-11, 8.787697303e-13, 1.465076507e-10, 4.921074132e-15, 1.019036492e-11, 5.64304116e-10, 2.238030861e-11, 1.219722645e-10, 6.182047328e-12, 5.571644753e-13, 4.579150221e-11, 4.380475592e-12, 103756203.7, 1.211806133e-10, 1.054366372e-11, 3.45579966e-14, 3.737451804e-15, 1884506783.0, 1.544250828e-12, 4.589902246e-10, 1.220088669e-11, 1.657214067e-13, 6.943660843e-13, 4.327809992e-12, 1.164900136e-13, 62228.35077, 8.38298023e-11, 2.28941907e-11, 1.757609596e-16, 64888770.28], [0.001168203909, 1.202332293e-06, 9.326108022e-08, 10047350.23, 116.2241752, 6.076375284e-08, 5.169500814e-06, 45.35284949, 211.8594123, 1.032083466e-07, 8.966854792e-11, 1.132528795e-12, 1.390282742e-10, 3.279392398e-15, 1.024833728e-11, 5.622019815e-10, 2.283339208e-11, 1.296874555e-10, 6.346334468e-12, 6.026340958e-13, 4.868518473e-11, 4.660027089e-12, 103752502.1, 1.188600164e-10, 1.05744262e-11, 3.569509047e-14, 3.854201201e-15, 1854715929.0, 1.602914424e-12, 4.849453425e-10, 1.229573547e-11, 1.650027706e-13, 6.957407282e-13, 4.461555038e-12, 1.193867995e-13, 66319.49271, 8.267595778e-11, 2.25638428e-11, 1.743323051e-16, 64074384.58], [0.001112068929, 1.187819716e-06, 6.569603171e-08, 9755251.866, 107.339199, 1.021769348e-08, 5.253433912e-06, 47.32221313, 199.8473372, 1.038778604e-07, 9.453307775e-11, 1.349976885e-12, 1.319455965e-10, 1.952666873e-15, 1.037043818e-11, 5.386788444e-10, 2.209424929e-11, 1.32922839e-10, 6.211805507e-12, 6.303622147e-13, 5.009203194e-11, 4.765400546e-12, 102108453.6, 1.158871909e-10, 1.07808807e-11, 3.672782593e-14, 3.957537541e-15, 1823103585.0, 1.612430895e-12, 5.007667529e-10, 1.189062161e-11, 1.563237147e-13, 6.598083047e-13, 4.393880977e-12, 1.168910506e-13, 68452.59681, 8.118180833e-11, 2.213405201e-11, 1.728342814e-16, 62992296.1], [0.001063543225, 1.236294199e-06, 2.398198251e-08, 3615080.053, 45.17088175, 1.000869305e-07, 6.042408163e-06, 35.40073178, 185.199816, 1.045053509e-07, 9.923757133e-11, 4.288846046e-13, 1.263271603e-10, 2.890654307e-16, 3.540479905e-12, 5.529467433e-10, 2.503946201e-11, 1.475191623e-10, 6.96721348e-12, 6.890498622e-13, 5.302524278e-11, 5.059667302e-12, 108331721.1, 1.115992629e-10, 1.425380169e-11, 3.672148011e-14, 3.950271172e-15, 1783305765.0, 1.753723332e-12, 5.367617128e-10, 1.252753094e-11, 1.672130526e-13, 7.150515768e-13, 4.806920317e-12, 1.263271095e-13, 72553.95491, 7.911166854e-11, 2.152300659e-11, 1.690772149e-16, 61398279.72], [0.001022443867, 1.266724358e-06, 9.324144244e-09, 4692775.565, 27.29863538, 1.094382882e-07, 6.766154091e-06, 20.31649309, 177.5940084, 1.050820289e-07, 1.037717093e-10, 6.370838459e-13, 1.23503728e-10, 2.3129522e-16, 3.135011391e-12, 5.598365653e-10, 2.61553932e-11, 1.54871316e-10, 7.238984135e-12, 7.340834892e-13, 5.52911814e-11, 5.268823475e-12, 109215031.7, 1.101693284e-10, 1.414990618e-11, 3.725882703e-14, 3.998950415e-15, 1761731225.0, 1.775576892e-12, 5.415974389e-10, 1.267772715e-11, 1.687070372e-13, 7.28650031e-13, 4.877577479e-12, 1.282424524e-13, 75363.04269, 7.843557104e-11, 2.128727373e-11, 1.66534167e-16, 60888618.08], [0.001030673301, 2.715388807e-05, 2.744945455e-09, 67492443.53, 0.433993174, 1.626383802e-08, 3.675437871e-06, 143.6142771, 186.6501764, 1.058897498e-07, 8.647548579e-11, 1.86161031e-13, 1.573716842e-10, 3.842292165e-14, 3.886228852e-12, 3.944514529e-10, 1.767561246e-11, 9.442570314e-11, 4.665958428e-12, 4.113709775e-13, 3.007240593e-11, 2.860116652e-12, 93135823.1, 9.639442464e-11, 1.231077591e-11, 2.834258989e-14, 3.014218553e-15, 1944806887.0, 1.036362302e-12, 3.235186388e-10, 1.145180369e-11, 1.441122742e-13, 6.283684581e-13, 3.729649156e-12, 9.660348796e-14, 41422.02831, 8.631324596e-11, 2.275639121e-11, 1.384254943e-16, 65659980.48], [0.001043607208, 2.155084611e-05, 9.749213472e-08, 78842144.13, 149.9720187, 2.090644277e-08, 3.902457359e-06, 515.7101596, 153.7778294, 1.082588882e-07, 6.174820425e-11, 1.387465895e-13, 1.247869677e-10, 8.533257448e-14, 7.24077582e-12, 3.463664836e-10, 1.607495828e-11, 7.791387994e-11, 4.190535863e-12, 3.32232536e-13, 2.218313525e-11, 2.150767857e-12, 99721052.95, 1.068014089e-10, 1.080916368e-11, 2.464315264e-14, 2.678948171e-15, 2395373414.0, 7.880637918e-13, 2.410135948e-10, 1.051839887e-11, 1.259447434e-13, 5.22372956e-13, 3.199501594e-12, 8.245241692e-14, 29992.66195, 9.064818922e-11, 2.362975794e-11, 1.243126796e-16, 67417966.97], [0.0009996066652, 2.385987962e-06, 1.012241901e-07, 52655484.2, 151.4828855, 5.065837406e-08, 2.636563513e-06, 229.6455463, 151.2399567, 1.097141014e-07, 7.301567999e-11, 6.058113958e-13, 1.212617621e-10, 5.644135838e-14, 7.682015324e-12, 4.942037376e-10, 2.395922412e-11, 1.17288632e-10, 6.206361995e-12, 5.133102812e-13, 3.53377308e-11, 3.366641536e-12, 115503099.8, 1.105778665e-10, 1.210273114e-11, 3.21875551e-14, 3.475163474e-15, 2231626371.0, 1.137220964e-12, 3.617833603e-10, 1.440271346e-11, 1.755236768e-13, 7.285093598e-13, 4.462628225e-12, 1.124571612e-13, 47938.52267, 8.38309519e-11, 2.205118955e-11, 1.387386657e-16, 62807250.56], [0.0009478862997, 5.634240744e-07, 1.296258346e-07, 21890391.51, 232.0278, 5.091960165e-08, 2.46918329e-06, 69.14249445, 142.9793516, 1.111300976e-07, 8.364112932e-11, 9.827753385e-13, 1.092688126e-10, 3.624747464e-14, 8.216262053e-12, 6.877391164e-10, 3.470532538e-11, 1.84167739e-10, 9.116027503e-12, 8.647180989e-13, 5.536950978e-11, 5.249979257e-12, 141703757.6, 1.120604185e-10, 1.272429355e-11, 3.891812619e-14, 4.202360855e-15, 2070770335.0, 1.909459342e-12, 5.908412801e-10, 2.035121652e-11, 2.551159946e-13, 1.066117543e-12, 6.84774107e-12, 1.710388912e-13, 76587.56188, 7.785386849e-11, 2.068069907e-11, 1.511463747e-16, 58924190.35]]

# Output data is stored here.
output = Object()
output.hygro = [[0.423205831, 0.46102861, 1.120039181, 1.140473606e-07], [0.4211891837, 0.4606938169, 1.12079626, 1.131229966e-07], [0.4190711761, 0.4581741794, 1.118467193, 1.129317356e-07], [0.4162435263, 0.4572300019, 1.119873699, 1.135870944e-07], [0.4137402143, 0.4552801476, 1.121990243, 1.146984343e-07], [0.4068998845, 0.4394997153, 1.121857515, 1.151752242e-07], [0.4045796589, 0.4391958268, 1.121687452, 1.144597052e-07], [0.4072215679, 0.4394863719, 1.108495088, 8.682254547e-08], [0.4055447766, 0.4513651612, 1.099963986, 7.436904777e-08], [0.4039892109, 0.4475923891, 1.104300108, 8.962006572e-08], [0.398014273, 0.4457640263, 1.109245004, 1.049749674e-07]]
output.naerosol = [[93016335.61, 1994759090.0, 49187.93823, 72422019.42], [100159702.7, 1976261666.0, 56281.43596, 71930414.74], [107236857.1, 1947725316.0, 64315.89171, 71074540.87], [107416233.2, 1920210065.0, 68661.38119, 70209462.43], [105912345.9, 1891020485.0, 71002.69228, 69060386.58], [112580781.9, 1853251802.0, 75399.71571, 67406966.87], [113713268.7, 1834291608.0, 78467.01859, 66934798.73], [97519299.06, 2036340026.0, 43371.57317, 73782062.7], [104367494.6, 2506984377.0, 31390.15175, 77335498.1], [120977813.7, 2337402891.0, 50210.75343, 71660878.07], [148527899.0, 2170494082.0, 80275.85049, 66687660.11]]
output.vaerosol = [[4.064398645e-13, 7.992245563e-14, 2.089321159e-13, 1.024675594e-13], [4.505666449e-13, 8.042799153e-14, 2.332356151e-13, 1.01772004e-13], [5.104232535e-13, 8.167891329e-14, 2.627826205e-13, 1.005610559e-13], [5.203981188e-13, 8.049363264e-14, 2.775947101e-13, 9.933708454e-14], [5.109433858e-13, 7.911720427e-14, 2.864044891e-13, 9.77112945e-14], [5.408007116e-13, 8.035896144e-14, 3.075658641e-13, 9.537192472e-14], [5.562548706e-13, 7.956185752e-14, 3.109841459e-13, 9.470386938e-14], [3.722026284e-13, 6.993109349e-14, 1.901938234e-13, 1.043918404e-13], [3.195123362e-13, 7.447940998e-14, 1.43323169e-13, 1.094194806e-13], [4.661017862e-13, 7.813094065e-14, 2.140374654e-13, 1.013906453e-13], [6.766301198e-13, 7.972117651e-14, 3.473302771e-13, 9.4354201e-14]]