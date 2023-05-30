# This file was automatically generated using the following command:
# ./merge_ensembles.py loadaer_output_ts_1400_type1.py loadaer_output_ts_1401_type1.py loadaer_output_ts_1404_type1.py loadaer_output_ts_1408_type1.py loadaer_output_ts_1409_type1.py loadaer_output_ts_1410_type1.py loadaer_output_ts_1411_type1.py loadaer_output_ts_1412_type1.py loadaer_output_ts_1413_type1.py

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass

# Settings are stored here.
settings = Object()

# Input is stored here.
input = Object()
input.cs = [[1.007234792], [1.008801927], [1.014336013], [1.02100007], [1.022277213], [1.022631545], [1.022085112], [1.021684499], [1.021979352]]
input.dt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
input.maxd_aspectype = [[14], [14], [14], [14], [14], [14], [14], [14], [14]]
input.ntot_amode = [[4], [4], [4], [4], [4], [4], [4], [4], [4]]
input.phase = [[1], [1], [1], [1], [1], [1], [1], [1], [1]]
input.state_q = [[0.00119155648, 1.382049542e-05, 1.188270466e-07, 36300142.46, 137.6758343, 2.917843023e-09, 3.945007958e-06, 115.2879204, 91.36060763, 1.044772335e-07, 8.89295341e-11, 1.72101755e-13, 7.759648519e-11, 1.129678168e-14, 9.23829513e-12, 3.739649309e-10, 1.47273999e-11, 8.291621546e-11, 4.14189261e-12, 4.019800202e-13, 3.272940926e-11, 3.126081617e-12, 80238117.34, 1.174075928e-10, 9.43523294e-12, 3.332247965e-14, 3.639686327e-15, 1912741949.0, 1.093828549e-12, 3.270052485e-10, 7.259562237e-12, 9.575720501e-14, 3.867006034e-13, 2.670223018e-12, 7.258840707e-14, 44318.66183, 8.365643101e-11, 2.308233133e-11, 1.855168371e-16, 64748635.47], [0.001139137763, 8.551209974e-06, 1.650668095e-07, 25235987.62, 198.6831253, 1.739405118e-09, 2.840625199e-06, 68.99923537, 57.36416479, 1.050070718e-07, 9.240424215e-11, 2.368258106e-13, 7.491125577e-11, 8.672617622e-15, 9.45558019e-12, 4.377844018e-10, 1.758801764e-11, 1.002201858e-10, 4.92464978e-12, 4.883771562e-13, 3.926727248e-11, 3.749813691e-12, 88598009.43, 1.180697797e-10, 9.717583725e-12, 3.488879505e-14, 3.796538514e-15, 1890706756.0, 1.312829096e-12, 3.928382422e-10, 8.830085643e-12, 1.139949838e-13, 4.627942903e-13, 3.236110834e-12, 8.762431857e-14, 53294.34994, 8.307920505e-11, 2.287386854e-11, 1.832365993e-16, 64303260.46], [0.0009990679289, 3.174831341e-06, 5.24611025e-09, 11924088.71, 1.572983817, 9.301144451e-10, 8.190166428e-07, 29.9626707, 34.53210241, 1.068043516e-07, 1.063804199e-10, 7.520428365e-13, 7.210016228e-11, 5.473930391e-15, 9.238707279e-12, 4.849614038e-10, 2.160950643e-11, 1.311689272e-10, 6.036031855e-12, 6.549227616e-13, 4.951681984e-11, 4.721640676e-12, 95412023.17, 1.117737216e-10, 1.066337526e-11, 3.815805616e-14, 4.11988338e-15, 1805831084.0, 1.644515222e-12, 4.912847494e-10, 1.065559492e-11, 1.403612312e-13, 5.883208969e-13, 4.098939478e-12, 1.096677894e-13, 67678.55612, 7.995245725e-11, 2.189767359e-11, 1.776815369e-16, 62027061.23], [0.0008811672515, 3.536023699e-06, 2.498938024e-08, 1783485.677, 2.529520147, 1.02217813e-09, 6.17258194e-07, 39.7426931, 46.62174831, 1.09193675e-07, 1.19724475e-10, 4.622985934e-13, 6.836932151e-11, 1.441130334e-14, 2.560911196e-12, 5.355695855e-10, 2.637925786e-11, 1.594786752e-10, 7.232331043e-12, 7.760279873e-13, 5.583386457e-11, 5.340630901e-12, 106294877.9, 1.03732564e-10, 1.449843791e-11, 3.935774309e-14, 4.204646649e-15, 1700019318.0, 1.868698793e-12, 5.624191988e-10, 1.30585027e-11, 1.716110898e-13, 7.400750204e-13, 5.090079641e-12, 1.323582927e-13, 76377.64092, 7.565712139e-11, 2.052007073e-11, 1.658922554e-16, 58837640.85], [0.0008949774383, 9.470781719e-06, 4.510904801e-09, 8653989.61, 1.164744661, 1.257369306e-11, 8.911411113e-07, 0.4652573116, 168.4706071, 1.097657991e-07, 1.19768478e-10, 1.660940458e-13, 7.60723193e-11, 6.380364055e-14, 1.073085367e-12, 5.216011115e-10, 2.573479311e-11, 1.537631433e-10, 7.020087207e-12, 7.303750858e-13, 5.225888639e-11, 4.979931914e-12, 106205314.5, 1.022804532e-10, 1.53469332e-11, 3.886975644e-14, 4.142012324e-15, 1692752637.0, 1.708710958e-12, 5.216118563e-10, 1.273236882e-11, 1.638546282e-13, 7.051051221e-13, 4.874291662e-12, 1.249564647e-13, 71881.86253, 7.529398429e-11, 2.034976373e-11, 1.62239691e-16, 58476565.73], [0.0009277265329, 4.056625472e-05, 1.389189748e-08, 42608072.62, 0.4164341458, 1.070303355e-09, 8.023255234e-07, 41.69768124, 170.4333386, 1.09948345e-07, 1.112848128e-10, 9.039647436e-14, 8.240873461e-11, 8.279426928e-14, 2.267531954e-12, 4.93340813e-10, 2.269503792e-11, 1.270387637e-10, 6.050200495e-12, 5.804988654e-13, 4.170424065e-11, 3.959618523e-12, 104320404.4, 1.048252185e-10, 1.340053385e-11, 3.385613211e-14, 3.605301186e-15, 1831356189.0, 1.384358838e-12, 4.300296919e-10, 1.320930645e-11, 1.65950768e-13, 7.1289336e-13, 4.550327699e-12, 1.1688693e-13, 57465.86019, 8.088488579e-11, 2.154418124e-11, 1.502247844e-16, 62013156.18], [0.0009343051239, 6.412978936e-05, 1.652242568e-08, 59302167.56, 0.6192037437, 2.274986681e-09, 1.081756701e-06, 88.27709805, 138.9016574, 1.101752254e-07, 1.019693198e-10, 9.633492779e-14, 7.455691301e-11, 8.951595387e-14, 3.31184136e-12, 4.237051266e-10, 1.99329975e-11, 1.134899369e-10, 5.316014298e-12, 5.235974172e-13, 3.716281853e-11, 3.511787044e-12, 99549715.69, 9.630597965e-11, 1.202050296e-11, 3.259038603e-14, 3.470039117e-15, 1848521218.0, 1.185710353e-12, 3.815618922e-10, 1.147489476e-11, 1.437682538e-13, 6.18230284e-13, 3.984806194e-12, 1.019766126e-13, 51104.35726, 8.06381999e-11, 2.145635456e-11, 1.501342552e-16, 61647637.53], [0.0009333181981, 7.648035879e-05, 8.549381816e-09, 62940474.96, 2.091166391, 1.659280358e-08, 1.14820623e-06, 426.0721037, 143.2222411, 1.104846003e-07, 9.371328792e-11, 7.461902752e-14, 6.538572342e-11, 9.613985218e-14, 3.978075092e-12, 3.879316272e-10, 1.842272309e-11, 1.063268638e-10, 4.922132849e-12, 4.90477286e-13, 3.406319569e-11, 3.185019234e-12, 102457505.2, 9.070977121e-11, 1.115363932e-11, 3.136031661e-14, 3.351206048e-15, 1903810172.0, 1.065339835e-12, 3.517444305e-10, 1.065658457e-11, 1.303761463e-13, 5.520941414e-13, 3.674676241e-12, 9.235618551e-14, 46931.05748, 8.136356912e-11, 2.161804823e-11, 1.47610646e-16, 61916989.71], [0.0009283755881, 9.123456387e-05, 8.351035644e-09, 64668538.59, 0.1072619875, 2.550621193e-08, 2.530932121e-06, 568.3787465, 126.9885774, 1.108325179e-07, 8.649445251e-11, 6.970792046e-14, 6.304810346e-11, 9.814998653e-14, 4.808336864e-12, 3.694008145e-10, 1.76651827e-11, 1.021373599e-10, 4.661450722e-12, 4.756275511e-13, 3.240044238e-11, 3.022761723e-12, 103516952.8, 9.092115526e-11, 1.070535395e-11, 3.011714393e-14, 3.221718019e-15, 1989310657.0, 1.031481797e-12, 3.568929097e-10, 1.094548181e-11, 1.313591702e-13, 5.546167888e-13, 3.751189802e-12, 9.494841139e-14, 44886.28713, 8.227008356e-11, 2.181546849e-11, 1.443709318e-16, 62335561.44]]

# Output data is stored here.
output = Object()
output.hygro = [[0.4200725253, 0.4614486187, 1.124273333, 1.192714206e-07], [0.4182897233, 0.4604913313, 1.123981733, 1.186599978e-07], [0.4086758444, 0.4541606919, 1.124254174, 1.196490158e-07], [0.3997946928, 0.4344082797, 1.121764572, 1.182128845e-07], [0.3989883144, 0.4301771352, 1.120438246, 1.162256095e-07], [0.4047241976, 0.4394474984, 1.113647048, 1.003926732e-07], [0.4025701415, 0.440766634, 1.114456023, 1.00652889e-07], [0.4006672852, 0.441581641, 1.114483262, 9.810050335e-08], [0.3998442794, 0.4438777004, 1.11427283, 9.491894519e-08]]
output.naerosol = [[80818623.44, 1926580239.0, 44639.29814, 69220518.14], [89377842.61, 1907348618.0, 53763.4429, 68829221.25], [96779851.15, 1831719502.0, 68648.79677, 66553523.66], [108527077.8, 1735719843.0, 77981.57676, 63306385.81], [108571273.0, 1730462448.0, 73483.1901, 63050813.85], [106681336.3, 1872802610.0, 58766.40142, 67621450.16], [101748282.3, 1889346016.0, 52233.00269, 67369793.35], [104679244.8, 1945093341.0, 47948.73394, 67935862.1], [105792188.4, 2033034416.0, 45872.85865, 68694137.27]]
output.vaerosol = [[3.330853319e-13, 7.633532114e-14, 1.810895016e-13, 9.793785943e-14], [3.94681516e-13, 7.711726592e-14, 2.179731889e-13, 9.738422619e-14], [4.661696543e-13, 7.489352691e-14, 2.739334723e-13, 9.416441569e-14], [5.367544991e-13, 7.466343499e-14, 3.166328427e-13, 8.957014598e-14], [5.205572522e-13, 7.478524653e-14, 2.945559017e-13, 8.920854552e-14], [4.669974282e-13, 7.428793558e-14, 2.451867481e-13, 9.567539015e-14], [4.066730367e-13, 6.791753646e-14, 2.172057437e-13, 9.531932913e-14], [3.748779132e-13, 6.377425776e-14, 2.001686433e-13, 9.612024139e-14], [3.580703351e-13, 6.345582393e-14, 2.032322118e-13, 9.719310026e-14]]