# This file was automatically generated using the following command:
# ./merge_ensembles calculate_resistance_rgsx_and_rsmx_output_ts_100.py calculate_resistance_rgsx_and_rsmx_output_ts_300.py calculate_resistance_rgsx_and_rsmx_output_ts_300_loc2_has_snow.py calculate_resistance_rgsx_and_rsmx_output_ts_1000_loc3_over_water.py

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass

# Settings are stored here.
settings = Object()

# Input is stored here.
input = Object()
input.beglt = [[1], [1], [1], [1]]
input.crs = [[98.11184398337988], [5.2624099864930916], [1e+36], [4917097.63112848]]
input.drat = [[1.3740328303634228, 2.3332297194282963, 1.8857345177418792], [1.3740328303634228, 2.3332297194282963, 1.8857345177418792], [1.3740328303634228, 2.3332297194282963, 1.8857345177418792], [1.3740328303634228, 2.3332297194282963, 1.8857345177418792]]
input.dt = [0.0, 0.0, 0.0, 0.0]
input.endlt = [[11], [11], [11], [11]]
input.foxd = [[1.0, 1e-36, 1e-36], [1.0, 1e-36, 1e-36], [1.0, 1e-36, 1e-36], [1.0, 1e-36, 1e-36]]
input.fr_lnduse = [[1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
input.has_dew = [[0], [0], [0], [0]]
input.has_rain = [[0], [0], [0], [0]]
input.heff = [[215141.5904869365, 210402677778.856, 3334.148860680581], [31138.432794480996, 42992261164.98709, 874.5427866732105], [1724166.2082613558, 1163173586735.6272, 14108.669620617442], [63920.21390215724, 77625658959.18587, 1438.7290493476496]]
input.index_season = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
input.ncol = [[4], [4], [4], [4]]
input.rgso = [[300.0, 300.0, 300.0, 600.0, 300.0, 150.0, 150.0, 150.0, 3500.0, 150.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 300.0, 300.0, 300.0, 3500.0, 300.0, 2000.0, 2000.0, 2000.0, 2000.0, 2000.0, 400.0, 400.0, 400.0, 400.0, 400.0, 1000.0, 800.0, 1000.0, 3500.0, 1000.0, 180.0, 180.0, 180.0, 3500.0, 180.0, 200.0, 200.0, 200.0, 3500.0, 200.0], [300.0, 300.0, 300.0, 600.0, 300.0, 150.0, 150.0, 150.0, 3500.0, 150.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 300.0, 300.0, 300.0, 3500.0, 300.0, 2000.0, 2000.0, 2000.0, 2000.0, 2000.0, 400.0, 400.0, 400.0, 400.0, 400.0, 1000.0, 800.0, 1000.0, 3500.0, 1000.0, 180.0, 180.0, 180.0, 3500.0, 180.0, 200.0, 200.0, 200.0, 3500.0, 200.0], [300.0, 300.0, 300.0, 600.0, 300.0, 150.0, 150.0, 150.0, 3500.0, 150.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 300.0, 300.0, 300.0, 3500.0, 300.0, 2000.0, 2000.0, 2000.0, 2000.0, 2000.0, 400.0, 400.0, 400.0, 400.0, 400.0, 1000.0, 800.0, 1000.0, 3500.0, 1000.0, 180.0, 180.0, 180.0, 3500.0, 180.0, 200.0, 200.0, 200.0, 3500.0, 200.0], [300.0, 300.0, 300.0, 600.0, 300.0, 150.0, 150.0, 150.0, 3500.0, 150.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 200.0, 200.0, 200.0, 3500.0, 200.0, 300.0, 300.0, 300.0, 3500.0, 300.0, 2000.0, 2000.0, 2000.0, 2000.0, 2000.0, 400.0, 400.0, 400.0, 400.0, 400.0, 1000.0, 800.0, 1000.0, 3500.0, 1000.0, 180.0, 180.0, 180.0, 3500.0, 180.0, 200.0, 200.0, 200.0, 3500.0, 200.0]]
input.rgss = [[400.0, 400.0, 400.0, 100.0, 500.0, 150.0, 200.0, 150.0, 100.0, 150.0, 350.0, 350.0, 350.0, 100.0, 350.0, 500.0, 500.0, 500.0, 100.0, 500.0, 500.0, 500.0, 500.0, 100.0, 500.0, 100.0, 100.0, 200.0, 100.0, 200.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1.0, 1.0, 1.0, 100.0, 1.0, 220.0, 300.0, 200.0, 100.0, 250.0, 400.0, 400.0, 400.0, 50.0, 400.0], [400.0, 400.0, 400.0, 100.0, 500.0, 150.0, 200.0, 150.0, 100.0, 150.0, 350.0, 350.0, 350.0, 100.0, 350.0, 500.0, 500.0, 500.0, 100.0, 500.0, 500.0, 500.0, 500.0, 100.0, 500.0, 100.0, 100.0, 200.0, 100.0, 200.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1.0, 1.0, 1.0, 100.0, 1.0, 220.0, 300.0, 200.0, 100.0, 250.0, 400.0, 400.0, 400.0, 50.0, 400.0], [400.0, 400.0, 400.0, 100.0, 500.0, 150.0, 200.0, 150.0, 100.0, 150.0, 350.0, 350.0, 350.0, 100.0, 350.0, 500.0, 500.0, 500.0, 100.0, 500.0, 500.0, 500.0, 500.0, 100.0, 500.0, 100.0, 100.0, 200.0, 100.0, 200.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1.0, 1.0, 1.0, 100.0, 1.0, 220.0, 300.0, 200.0, 100.0, 250.0, 400.0, 400.0, 400.0, 50.0, 400.0], [400.0, 400.0, 400.0, 100.0, 500.0, 150.0, 200.0, 150.0, 100.0, 150.0, 350.0, 350.0, 350.0, 100.0, 350.0, 500.0, 500.0, 500.0, 100.0, 500.0, 500.0, 500.0, 500.0, 100.0, 500.0, 100.0, 100.0, 200.0, 100.0, 200.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1.0, 1.0, 1.0, 100.0, 1.0, 220.0, 300.0, 200.0, 100.0, 250.0, 400.0, 400.0, 400.0, 50.0, 400.0]]
input.ri = [[1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 60.0, 1e+36, 1e+36, 1e+36, 120.0, 120.0, 1e+36, 1e+36, 1e+36, 240.0, 70.0, 1e+36, 1e+36, 1e+36, 140.0, 130.0, 250.0, 250.0, 400.0, 250.0, 100.0, 500.0, 500.0, 800.0, 190.0, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 80.0, 1e+36, 1e+36, 1e+36, 160.0, 100.0, 1e+36, 1e+36, 1e+36, 200.0, 150.0, 1e+36, 1e+36, 1e+36, 300.0], [1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 60.0, 1e+36, 1e+36, 1e+36, 120.0, 120.0, 1e+36, 1e+36, 1e+36, 240.0, 70.0, 1e+36, 1e+36, 1e+36, 140.0, 130.0, 250.0, 250.0, 400.0, 250.0, 100.0, 500.0, 500.0, 800.0, 190.0, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 80.0, 1e+36, 1e+36, 1e+36, 160.0, 100.0, 1e+36, 1e+36, 1e+36, 200.0, 150.0, 1e+36, 1e+36, 1e+36, 300.0], [1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 60.0, 1e+36, 1e+36, 1e+36, 120.0, 120.0, 1e+36, 1e+36, 1e+36, 240.0, 70.0, 1e+36, 1e+36, 1e+36, 140.0, 130.0, 250.0, 250.0, 400.0, 250.0, 100.0, 500.0, 500.0, 800.0, 190.0, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 80.0, 1e+36, 1e+36, 1e+36, 160.0, 100.0, 1e+36, 1e+36, 1e+36, 200.0, 150.0, 1e+36, 1e+36, 1e+36, 300.0], [1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 60.0, 1e+36, 1e+36, 1e+36, 120.0, 120.0, 1e+36, 1e+36, 1e+36, 240.0, 70.0, 1e+36, 1e+36, 1e+36, 140.0, 130.0, 250.0, 250.0, 400.0, 250.0, 100.0, 500.0, 500.0, 800.0, 190.0, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 1e+36, 80.0, 1e+36, 1e+36, 1e+36, 160.0, 100.0, 1e+36, 1e+36, 1e+36, 200.0, 150.0, 1e+36, 1e+36, 1e+36, 300.0]]
input.tc = [[14.256568529488902], [37.859048107272315], [-7.454636962460086], [28.63740192189624]]

# Output data is stored here.
output = Object()
output.cts = [[1.1783465351983004e-05], [6.619823179947983e-16], [31646.79762100325], [6.695090342077937e-12]]
output.rgsx = [[4e-323, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 114.78588952033941, 47.59766456177039, 89.71103171424595, 107.49416200051469, 0.0, 40.24552165726385, 0.4647139578101744, 214.98831221756402, 0.0, 0.0, 96.3526801660342, 0.00020189511422577755, 8.307533367965595e-05, 0.00017813115811655324, 0.0002494230264442262, 6.3e-322, 5.931137757043164e-05, 1.225874447416749e-05, 0.00048706258753646937, 2.55353205e-316, 0.0, 0.00020189511422577755, 11997.064831449325, 4498.899319158162, 10497.43172899109, 14996.331036365787, 5e-324, 2999.26621669993, 29.99267383263, 29992.662060948107, 2.557282e-316, 2.55727924e-316, 11997.064831449325, 2.1219957915e-314, 1.52783696999e-312, 1.379297264127e-312, 1.379297264127e-312, 5.534e-321, 6.95330017126863e-310, 152.20805829584512, -5.014678465409588, 4.065621094068465e-13, -3.38471956326502e-12, -8.527744784470749e-14, 1.7447702100078245e-12, 1.4737956027007786e-12, 2.3734615321908107e-12, 7.916344945588239e-13, 2.2585065378261688e-13, -2.128522194805841e-12, 2.3741481279417595e-13, 1.0781330718339566e-12, 8.1870733949291e-14, 6.802663577155428e-13, 5.110159957873353e-13, 3.4585895573944554e-13, 2.6609687445963605e-13, 2.5023364342016957e-13, 1.9751387030780293e-13, 1.4817332536313836e-13, 1.0187843186901367e-13, 7.458286730753171e-14, 5.596402671609349e-14, 3.9637378462939066e-14, 3.2789407986686884e-14, 2.5682537900908687e-14, 1.83166335584043e-14, 1.370521791717662e-14, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.2988683910746797e-06, 1.2468131172059757e-06, 1.319155766549619e-06, 1.6420749426997249e-06, 2.1728849124682084e-06, 2.7778937804812507e-06, 3.7657663855589206e-06, 5.202316137314534e-06, 6.924221370756175e-06, 7.997514557703512e-06, 9.22807247230208e-06, 9.85841238062485e-06, 1.1447316003090827e-05, 1.1235289017118301e-05, 9.652064545014544e-06, 8.066629007727339e-06, 7.060791800098882e-06, 6.3830154456025535e-06, 6.1135736625513725e-06, 5.986746449676146e-06, 5.731918609145046e-06, 5.06761674117661e-06, 4.248315437412058e-06, 2.7446648162148194e-06, 1.7613459355069838e-06, 1.0552972139957866e-06, 6.264731673759783e-07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.07882068279926872, 0.1382680713366278, 0.22741972106360456, 0.3802693972396921, 0.6721723322098154, 1.228400657160581, 2.3224473793667726, 4.5478748446906625, 9.031824331339873, 17.01972025678621, 29.408248887963655, 47.368589492997124, 72.30296967107526, 103.0961658139371, 135.27585778608236, 164.38846372855986, 186.9756982005852, 202.91077272149323, 213.88829521506085, 221.31730069932786, 226.40567885219028, 229.50769515843407, 231.3024161556944, 232.44298344287887, 233.41687394060594, 234.22079929732908, 234.84818991389122, 6.95330017106784e-310, 0.0, 8e-323, 6.95330017106705e-310, 0.0, 0.0, 0.0, 6.95330017113227e-310, 5e-324, 6.95330017114927e-310, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.5e-323, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.921154106e-315, 0.0, 0.0, 0.0, 0.0, 5.30498949e-315], [4e-323, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 243.20283621758637, 114.38294388882828, 169.78881388360426, 177.84832725645595, 0.0, 155.1066552167215, 3.206316927142799, 355.6966545129119, 0.0, 0.0, 173.0564645454977, 0.0009304000049340152, 0.00034890000185066944, 0.0008141000043173462, 0.0011630000061673535, 6.3e-322, 0.00023260000123400028, 2.3260000129953657e-06, 0.0023260000123340448, 2.55353205e-316, 0.0, 0.0009304000049340152, 45738.18526611067, 17151.8194747915, 40020.91210784684, 57172.731582638335, 5e-324, 11434.546316527667, 114.34546316527667, 114345.46316527667, 2.557282e-316, 2.55727924e-316, 45738.18526611067, 2.1219957915e-314, 1.52783696999e-312, 1.379297264127e-312, 1.379297264127e-312, 5.534e-321, 6.95255411391753e-310, 62.02107913618143, -5.014678465409588, -6.909047323321609e-13, 1.0850693650396838e-12, -7.343000050252622e-13, -3.817701871176664e-12, -2.0182898769718506e-12, 1.8684029837180208e-13, -2.1774597201249455e-13, -1.4939889298086499e-12, -1.8486584250608642e-12, -2.8453152994455443e-13, 6.250370431965454e-13, 3.844401749504042e-13, 6.456217598614008e-13, 1.333123763676968e-13, 1.9627621232628284e-13, 3.6765817033957444e-13, 3.1064854610779045e-13, 2.093536713102242e-13, 1.4297923129837366e-13, 9.967085271067897e-14, 7.432585032601352e-14, 5.5835494934160636e-14, 3.9744847307026e-14, 3.3640410601867793e-14, 2.6402409230023312e-14, 1.8765853535267337e-14, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.3755340767869276e-06, 1.3249874687400424e-06, 1.4763191809824818e-06, 1.8326449707221823e-06, 2.280001671662378e-06, 2.8148400518803504e-06, 3.8096880381675763e-06, 5.532534065366021e-06, 6.913918592433149e-06, 8.197345752992368e-06, 9.477971800212332e-06, 1.036208072725024e-05, 1.1417625962991e-05, 1.0411256479701439e-05, 9.078085406820054e-06, 8.42960886487163e-06, 7.73304328415471e-06, 6.776950556106167e-06, 6.205414993454727e-06, 6.035750037981995e-06, 5.757832234841089e-06, 5.037548415984126e-06, 4.185623907622909e-06, 2.684857059543647e-06, 1.6857901380348347e-06, 9.7209839578603e-07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.07941151462125182, 0.14197513456031674, 0.2392767428770046, 0.4122016219865682, 0.7296108646177153, 1.30587868739152, 2.4198977714561534, 4.7669063013912005, 9.350002913398992, 17.489814807604347, 30.332153483998557, 48.94045841553294, 74.2567193045072, 105.50270981182703, 138.4864962065624, 166.61291109290286, 187.0077813420151, 202.26777072596352, 214.0516317148001, 222.45858558944758, 227.89799165431415, 231.01375667515327, 232.79181795680964, 233.83514312679438, 234.5879865308505, 235.0924827974101, 0.0, 6.95255411371674e-310, 0.0, 8e-323, 6.95255411371595e-310, 0.0, 0.0, 0.0, 6.95255411378117e-310, 5e-324, 6.95255411379816e-310, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.5e-323, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.81130837e-315, 0.0, 0.0, 0.0, 0.0, 5.30498949e-315], [0.0, 2.5539597e-316, 0.0, 0.0, 0.0, 2.121995793e-314, 5.14e-322, 2.7068617e-317, 2.7068617e-317, 2e-323, 1.0247818939112543e-13, 31652.541997815075, 2.0379961995413878e-13, 31652.587930667287, 31652.587930667287, 31652.587930667287, 31652.587930667287, 31646.855618370122, 31697.451917273505, 1.3192086291674388e-15, 8.368632827925962e-16, 31649.6951726526, 31646.79762960042, 2.8869057181237034e-18, 31646.79762960042, 31646.79762960042, 31646.79762960042, 31646.79762960042, 31646.797621089223, 31646.79770697494, 0.0, 0.0, 31646.797625301835, 32355.58167144176, 0.0, 32355.58167144176, 32355.58167144176, 32355.58167144176, 32355.58167144176, 31653.885461507634, 38734.63812538836, 2.55347394e-316, 1.84121634e-315, 32001.189646222505, 5e-324, 5e-324, 5.304990144e-315, 2.095e-321, 0.0, 5e-324, 4.4e-323, 6e-323, 2e-323, 8.4879831644e-314, 8.4879831644e-314, 6e-322, 6e-322, 2e-323, 6.952967802376e-310, 171.74628076612774, 28.030651794945495, -2.4932490039301624e-12, -6.472829809513685e-12, -5.559307442174373e-13, 1.1950906911597058e-12, 2.1804710349455868e-12, 2.704703518438622e-12, 2.0445326681466914e-12, -8.18192284791655e-13, 1.2830346868802415e-12, 4.00259123267243e-12, 3.100228870826819e-12, 1.7356230210947587e-12, 5.927876465383952e-13, 1.9553991217520857e-14, -8.69402099848155e-14, 6.19472715524528e-15, 2.844824480371503e-14, 2.695433398521059e-14, 2.062739013310298e-14, 1.6118700620713804e-14, 1.409180981211985e-14, 1.1360585029645472e-14, 8.208171953092623e-15, 7.362688421563762e-15, 6.087532962107606e-15, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.3196017714743082e-06, 1.2532569296889278e-06, 1.4391077082108355e-06, 1.7861095148116623e-06, 2.1956330759871326e-06, 2.7778906037894957e-06, 3.697779165355077e-06, 5.031632190335419e-06, 6.535123706925271e-06, 7.58417841459639e-06, 7.898970982375378e-06, 7.865566398400178e-06, 7.775925548082531e-06, 7.252832971441521e-06, 6.1012608625871675e-06, 4.961003032160898e-06, 3.908376744925838e-06, 3.112305841198175e-06, 2.447375561995744e-06, 2.019465278439708e-06, 1.75475216344168e-06, 1.5309629827821778e-06, 1.3581168313966212e-06, 1.19182531549273e-06, 1.0090909159103785e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.09087754742219116, 0.15170111905293934, 0.2465787857921806, 0.41327629861470067, 0.7151534966944065, 1.2706199300536842, 2.341611022425952, 4.510332495602906, 8.694483563397716, 15.713204091129876, 25.611157049469625, 38.40233426745192, 55.04069702651373, 76.57646798172277, 101.87237130691577, 126.34946088032649, 146.37566939487056, 162.0574003527004, 174.11378621851992, 182.9162576472429, 188.86020185742788, 192.48259357203915, 194.59922183049886, 195.9318725487784, 196.9836290642034, 0.0, 0.0, 0.0, 1.841203534e-315, 6.952967774051e-310, 0.0, 0.0, 0.0, 0.0, 2.55588854e-316, 5e-324, 5e-324, 2.7049995e-317, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.3e-322, 0.0, 0.0, 0.0], [6.95305563632265e-310, 0.0, 0.0, 0.0, 0.0, 2.55588854e-316, 5e-324, 5e-324, 2.7049995e-317, 2.7049995e-317, 1.9012918503958164e-14, 2.492132007895469e-14, 2.1410880775245914e-14, 1.6070256657719513e-14, 1.2338272892562704e-14, 1.2060806026106815e-14, 1.2244129663648431e-14, 1.5632275382630234, 1.5802610728901954e-14, 5.653531931448514e-15, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.2882405257696816e-06, 0.0, 0.0, 6.3e-322, 0.0, 0.0, 0.0, 0.0, 1e-323, 0.0, 0.0, 69.50579057630883, 2.55333995e-316, 0.0, 0.0, 0.0, 2e-323, 1.6e-322, 2.095e-321, 0.0, 1.794503974e-315, 5e-324, 5e-324, 6.95305563633174e-310, 6.95305563679023e-310, 8.4879831644e-314, 8.4879831644e-314, 6.9530556651324e-310, 6.952931408677e-310, 2e-323, 6.9530556363333e-310, 3.250579e-317, 106.08760599181598, 82.05885901129312, 2.0156193222240007e-12, 2.8800964685705983e-12, 3.923936669668549e-12, 2.2408269891276036e-12, 4.354338584187931e-13, -4.566780353488228e-13, -9.881106760910154e-13, -1.204188179566234e-12, -9.886168319373314e-13, -5.610373663887889e-13, -2.603417464982596e-13, -1.1138620695843192e-13, -5.150303145209256e-14, -2.733313213955023e-14, -1.6917790616711342e-14, -1.1181427236698205e-14, -7.579958744661286e-15, -5.656749923246827e-15, -4.2371983085469985e-15, -3.4425994967450878e-15, -2.9313356026425097e-15, -2.55073590608209e-15, -2.2109301302466695e-15, -1.9807489879025453e-15, -1.754087173845299e-15, -1.5269130069311621e-15, -1.3436551288952972e-15, -1.2000367656921232e-15, -1.0420399269531246e-15, -8.624366091492269e-16, -7.451784479410265e-16, -6.269827280365956e-16, -4.99736985549959e-16, -3.963623582726124e-16, -3.1881732246837684e-16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.4606132768710702e-06, 1.6206040564281532e-06, 1.93142450096824e-06, 2.2192122247057387e-06, 2.2219890257381744e-06, 1.9851073347964176e-06, 1.3570565958886526e-06, 7.063115805677492e-07, 5.161651186832177e-07, 8.064456580684689e-07, 1.2431324614423688e-06, 1.4457101732565925e-06, 1.4302393559864444e-06, 1.2440006719824484e-06, 9.386220854413378e-07, 4.844632018218862e-07, -1.6664643933043838e-07, -7.510485360809539e-07, -1.45531443435841e-06, -2.0896579991993736e-06, -2.5583038113902705e-06, -2.828472696814885e-06, -3.05737887522672e-06, -2.984470431378898e-06, -2.8767994208986513e-06, -2.7140559806247795e-06, -2.511306386824718e-06, -2.286791517758443e-06, -2.0061503554755374e-06, -1.6578261410552838e-06, -1.4305968342378749e-06, -1.1674773227072432e-06, -8.632170681893105e-07, -6.061208029288725e-07, -4.351037783412064e-07, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1993771157310847, 0.2640409765399239, 0.3701921900875957, 0.5489864174433137, 0.8455593348158814, 1.3353145009620542, 2.1605903905612704, 3.7027962872210733, 6.802216640823551, 12.635040538201881, 21.491052859767596, 32.86889022306396, 46.521152856869556, 62.4345429951801, 81.09660771841989, 102.79966492474867, 126.66960060138774, 151.19928486299455, 175.07822128294876, 197.41214283431853, 217.7689336713879, 235.67857666825515, 250.59297101249774, 263.47899202849294, 275.8324050859562, 288.07352055142053, 300.3451402253696, 2.729788e-317, 325.68005527375414, 0.0, 2.5539597e-316, 0.0, 0.0, 0.0, 2.121995793e-314, 5.04e-322, 2.7068617e-317, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
output.rsmx = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.3480889468065804e+38, 8088.539504481088, 16177.07318532057, 9436.62845128767, 0.0, 13480.89529170741, 1e+36, 1.3480889468065804e+38, 0.0, 0.0, 20221.340025740312, 2.2891747020993425e+38, 13735.048212610312, 27470.096425206364, 16024.222914709655, 0.0, 22891.74702100768, 1e+36, 2.2891747020993425e+38, 0.0, 0.0, 34337.6205315044, 1.8501289079876537e+38, 11100.773447925922, 22201.546895851843, 12950.902355913575, 0.0, 18501.289079876533, 1e+36, 1.8501289079876537e+38, 0.0, 0.0, 27751.933619814805, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.3054244165713655e-11, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 201144393.25530648, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973751821934684e-20, 3.9738361331658894e-20, 3.973851066228068e-20, 3.9738667281020877e-20, 3.973875232300916e-20, 3.9738776496582195e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 5.313570847349009e-13, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.2897023476531803e-12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.230724088273845e+36, 433.85250495155634, 867.695950247987, 506.1597458342948, 0.0, 723.0814684825102, 1e+36, 7.230724088273845e+36, 0.0, 0.0, 1084.6176728962025, 1.2278411376301942e+37, 736.7046826478963, 1473.4093652260128, 859.4887964109158, 0.0, 1227.841137699974, 1e+36, 1.2278411376301942e+37, 0.0, 0.0, 1841.7617065150712, 9.923508158039599e+36, 595.4104894823759, 1190.8209789647517, 694.645571062772, 0.0, 992.3508158039599, 1e+36, 9.923508158039599e+36, 0.0, 0.0, 1488.5262237059399, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.374032830363423e+72, 0.0, 1.374032830363423e+72, 1.374032830363423e+72, 5.496131321453691e+38, 1.0992262642907382e+39, 1e+36, 1.374032830363423e+72, 1.3541376656490356e-19, 3.1506308065925074e-16, 1.374032830363423e+72, 2.3332297194282967e+72, 6.682684020166113e-12, 2.3332297194282967e+72, 2.3332297194282967e+72, 9.332918877713184e+38, 1.866583775542637e+39, 1e+36, 2.3332297194282967e+72, 2.9487705309549965e-11, 1.0312216226983986e-11, 2.3332297194282967e+72, 1.8857345177418793e+72, 8.843309821888388e-13, 1.8857345177418793e+72, 1.8857345177418793e+72, 7.542938070967517e+38, 1.5085876141935034e+39, 1e+36, 1.8857345177418793e+72, 0.0, 0.0, 1.8857345177418793e+72, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.6931595146166563e-25, 1.9714067721341002e-20, 4.58667893245726e-17, 3.815007843562859e-15, 1.3921484844310666e-13, 9.68714844660424e-13, 3.864881396379508e-12, 9.51340864800185e-12, 2.40744907289726e-11, 1.917267490367454e-11, 8.188428299490632e-12, 6.0596960569271354e-12, 4.272273036785121e-12, 1.4960506979219372e-12, 3.3552371176346573e-13, 1.7397570911384673e-13, 1.2831730754265703e-13, 8.149610038989255e-14, 3.9827549065884387e-14, 9.132743678296737e-15, 2.814732245730266e-16, 1.0191955463830787e-20, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.4852294053894506e-07, 0.052162321086869586, 121.12324195904142, 10034.552158803814, 361826.75324365916, 1830456.8503942718, 5324556.762437612, 10761603.91806009, 24428571.930085637, 18356361.14276072, 7226033.4859422445, 4908341.16699889, 3191883.6921437685, 1044525.7397918138, 232075.64256414765, 118657.42483380911, 86494.34755428357, 54467.08234451991, 26485.688365350376, 6057.668632504534, 186.35717269912246, 0.006736932541893869, 0.0, 0.0, 0.0, 0.0, 0.0, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973868372235913e-20, 3.973877649658219e-20, 3.973877649658219e-20, 4.6549009718343216e-18, 3.859854950593086e-16, 9.491519593777038e-14, 2.095647365333526e-13, 5.274687822860608e-13, 1.2248382999272443e-12, 2.2230042409304316e-12, 1.5856748689253336e-12, 2.986308879681332e-13, 2.5297471258914595e-13, 1.8423200352495718e-13, 2.975389143059539e-14, 6.581263172421055e-15, 3.3250818293770133e-15, 2.3954091888755247e-15, 1.4944326920350955e-15, 7.225550910961561e-16, 1.6475901494642049e-16, 5.057597233496967e-18, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.4164522142192302e-26, 1.6470283195954824e-21, 3.8233852160957835e-18, 3.165672743377337e-16, 1.1349545321174175e-14, 5.396630678932404e-14, 1.4054967405276845e-13, 2.5310752006492617e-13, 5.334278885541342e-13, 3.8167425980358807e-13, 1.4543873580228022e-13, 8.42464706858016e-14, 4.610642692947302e-14, 1.3881042311282745e-14, 3.0466706059942343e-15, 1.5265883390010592e-15, 1.093223231608677e-15, 6.793385483883779e-16, 3.277351881365476e-16, 7.464807850976453e-17, 2.289704170216312e-18, 8.25577125576468e-23, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e+36, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.4001611747623015e-11, 2.318698488517908e-11, 1.5891830010339967e-11, 1e+36, 8.99899633864847e-12, 8.83238703890929e-12, 8.822013950106652e-12, 1.1578550000561507e-11, 1.0861867422512949e-11, 3.899900811752553e-12, 0.0, 0.0, 0.0, 0.0, 1e+36, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.9038664037905087e-12, 1.7497054127412344e-12, 1.1332704126089945e-12, 7.650689208287668e-13, 6.584569244428603e-13, 6.394718356742869e-13, 6.376013889829739e-13, 7.695802056013853e-13, 7.206145538117388e-13, 2.5899230282308075e-13, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 15501750.67562341, 21700753.717402272, 15774611.516333867, 10832799.53832957, 10741596.31424237, 11455746.578967938, 12630319.229283582, 17950604.573040597, 17171954.176874727, 5926039.068543816, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973867813951805e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 2.586533623325721e-13, 6.606120432985727e-13, 5.977892660425569e-13, 8.352846321009373e-13, 2.2062033754795882e-12, 3.800507871614362e-12, 3.4844123929967313e-12, 1.5404889596562234e-12, 1.0268788835177453e-12, 3.0646400964978394e-13, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.9738776496582183e-20, 3.973877649658219e-20, 3.973877649658219e-20, 3.9738776496582195e-20, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.565514700034655e-13, 1.3551425705240672e-12, 9.134057451162883e-13, 7.280222836874268e-13, 5.374326083067656e-13, 4.0575054224058625e-13, 4.1053596612205894e-13, 7.630967123550852e-13, 8.775955913507705e-13, 2.7821782276794223e-13, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]