# This file was automatically generated using the following command:
# ./merge_ensembles.py lin_strat_chem_solve_output_ts_1400.py lin_strat_chem_solve_output_ts_1401.py lin_strat_chem_solve_output_ts_1402.py lin_strat_chem_solve_output_ts_1403.py lin_strat_chem_solve_output_ts_1404.py lin_strat_chem_solve_output_ts_1405.py lin_strat_chem_solve_output_ts_1406.py lin_strat_chem_solve_output_ts_1407.py lin_strat_chem_solve_output_ts_1408.py lin_strat_chem_solve_output_ts_1409.py lin_strat_chem_solve_output_ts_1410.py lin_strat_chem_solve_output_ts_1411.py lin_strat_chem_solve_output_ts_1412.py lin_strat_chem_solve_output_ts_1413.py lin_strat_chem_solve_output_ts_1414.py lin_strat_chem_solve_output_ts_1415.py lin_strat_chem_solve_output_ts_1416.py

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass

# Settings are stored here.
settings = Object()

# Input is stored here.
input = Object()
input.chlorine_loading = [[3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975], [3.286483673640975]]
input.chlorine_loading_bgnd = [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]]
input.delta_t = [[3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0], [3600.0]]
input.do_lin_stratchem = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
input.dt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
input.lchnk = [[137], [137], [137], [137], [137], [137], [137], [137], [137], [137], [137], [137], [137], [137], [137], [137], [137]]
input.linoz_PmL_clim = [[-4.3710734454775926e-16], [-4.3671889839468485e-16], [-4.3633045224161034e-16], [-4.3594200608745065e-16], [-4.355535599343761e-16], [-4.351651137813017e-16], [-4.347766676271418e-16], [-4.343882214740674e-16], [-4.339997753209929e-16], [-4.3361132916683313e-16], [-4.332228830137586e-16], [-4.3283443686068416e-16], [-4.3244599070652433e-16], [-4.3205754455344996e-16], [-4.3166909840037545e-16], [-4.3128065224621557e-16], [-4.3089220609314116e-16]]
input.linoz_cariolle_psc = [[2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08], [2.850688065360013e-08]]
input.linoz_dPmL_dO3 = [[-1.0731396993844996e-08], [-1.0733540283126868e-08], [-1.073568357240874e-08], [-1.07378268616966e-08], [-1.0739970150978472e-08], [-1.0742113440260344e-08], [-1.0744256729548206e-08], [-1.0746400018830076e-08], [-1.0748543308111951e-08], [-1.075068659739981e-08], [-1.0752829886681683e-08], [-1.0754973175963555e-08], [-1.0757116465251414e-08], [-1.0759259754533287e-08], [-1.0761403043815159e-08], [-1.0763546333103021e-08], [-1.0765689622384893e-08]]
input.linoz_dPmL_dO3col = [[-6.177487197835175e-18], [-6.1822888418064245e-18], [-6.1870904857776745e-18], [-6.1918921297623405e-18], [-6.196693773733591e-18], [-6.201495417704841e-18], [-6.2062970616895065e-18], [-6.211098705660757e-18], [-6.2159003496320065e-18], [-6.220701993616671e-18], [-6.225503637587922e-18], [-6.230305281559171e-18], [-6.235106925543837e-18], [-6.239908569515087e-18], [-6.244710213486336e-18], [-6.249511857471003e-18], [-6.254313501442252e-18]]
input.linoz_dPmL_dT = [[-1.0488834189953105e-16], [-1.0490414172947188e-16], [-1.0491994155941269e-16], [-1.0493574138939765e-16], [-1.0495154121933845e-16], [-1.0496734104927928e-16], [-1.0498314087926421e-16], [-1.0499894070920505e-16], [-1.0501474053914587e-16], [-1.0503054036913081e-16], [-1.0504634019907161e-16], [-1.0506214002901246e-16], [-1.050779398589974e-16], [-1.0509373968893823e-16], [-1.0510953951887903e-16], [-1.0512533934886399e-16], [-1.0514113917880482e-16]]
input.linoz_o3_clim = [[4.87394178365753e-07], [4.874380444271754e-07], [4.874819104885978e-07], [4.875257765501428e-07], [4.875696426115653e-07], [4.876135086729879e-07], [4.876573747345329e-07], [4.877012407959554e-07], [4.877451068573779e-07], [4.877889729189229e-07], [4.878328389803455e-07], [4.878767050417679e-07], [4.87920571103313e-07], [4.879644371647355e-07], [4.880083032261581e-07], [4.880521692877031e-07], [4.880960353491255e-07]]
input.linoz_o3col_clim = [[281.20955787337635], [281.2152378205057], [281.22091776763506], [281.2265977147803], [281.23227766190973], [281.2379576090392], [281.2436375561844], [281.24931750331376], [281.25499745044317], [281.2606773975883], [281.26635734471773], [281.2720372918472], [281.2777172389924], [281.2833971861218], [281.28907713325117], [281.29475708039644], [281.30043702752585]]
input.linoz_t_clim = [[215.6189679371539], [215.618116836083], [215.6172657350121], [215.6164146339388], [215.61556353286787], [215.614712431797], [215.6138613307237], [215.61301022965276], [215.6121591285819], [215.61130802750856], [215.61045692643768], [215.60960582536674], [215.60875472429348], [215.6079036232226], [215.60705252215163], [215.60620142107837], [215.60535032000743]]
input.ltrop = [[35], [35], [35], [35], [35], [35], [35], [35], [35], [35], [35], [35], [35], [35], [35], [35], [35]]
input.ncol = [[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]]
input.o3_vmr = [[3.6131057477260656e-07], [3.6754011905336104e-07], [3.742683962104681e-07], [3.812981484819422e-07], [3.884858295237155e-07], [3.957012173140577e-07], [4.02790392624839e-07], [4.0971127919164477e-07], [4.1645626446331364e-07], [4.2308576213010997e-07], [4.296107289749614e-07], [4.361158824232673e-07], [4.429034830261133e-07], [4.501588573961729e-07], [4.5800250246748714e-07], [4.665055822143839e-07], [4.754998415658963e-07]]
input.o3col = [[6.533824914561677e+18], [6.550658283025804e+18], [6.567584535731167e+18], [6.582072368941644e+18], [6.59279146665358e+18], [6.601756624882512e+18], [6.611385902056144e+18], [6.619684338975109e+18], [6.624671586416773e+18], [6.6270973421633e+18], [6.633906241160484e+18], [6.649549097027608e+18], [6.670225523569519e+18], [6.692003494632107e+18], [6.709674653333317e+18], [6.7185510358317e+18], [6.722016771600141e+18]]
input.pcols = [[4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4]]
input.pmid = [[13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061], [13368.21799321061]]
input.psc_T = [[197.5], [197.5], [197.5], [197.5], [197.5], [197.5], [197.5], [197.5], [197.5], [197.5], [197.5], [197.5], [197.5], [197.5], [197.5], [197.5], [197.5]]
input.pver = [[72], [72], [72], [72], [72], [72], [72], [72], [72], [72], [72], [72], [72], [72], [72], [72], [72]]
input.radians_to_degrees = [[57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232], [57.29577951308232]]
input.rlats = [[0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859], [0.6851812346816859]]
input.sza = [[2.480681028060327], [2.323980538248946], [2.138927044982115], [1.9408210412260345], [1.7382960129593912], [1.5373556188063418], [1.3436591879596256], [1.1641959987219652], [1.0089632990416006], [0.8923396615179606], [0.831734594775256], [0.8397907060754546], [0.9146361032952149], [1.0415247701075736], [1.203308952645417], [1.3866436444354977], [1.58235141094111]]
input.temp = [[213.90805888207677], [213.96448912056178], [214.01014542123983], [214.06275419250366], [214.10297521297488], [214.1566294584853], [214.22651293069538], [214.30896904562968], [214.3836861165352], [214.44707801769744], [214.51731727510202], [214.63749906583735], [214.7676887999674], [214.913959212621], [215.0220927391554], [215.0583321554533], [215.04211323339763]]

# Output data is stored here.
output = Object()
output.do3_linoz = [[1.3303986286721102e-15], [1.2550272643301464e-15], [1.1753764711676566e-15], [1.0922847837628872e-15], [1.0096294301524459e-15], [9.25635529951668e-16], [8.411048968028906e-16], [7.573344397781181e-16], [6.769982759334571e-16], [5.996532875231924e-16], [5.216664228910383e-16], [4.3656499669368104e-16], [3.461686593433417e-16], [2.487533898359725e-16], [1.4992723215779917e-16], [5.356344286370151e-17], [-4.1353889761829604e-17]]
output.do3_linoz_psc = [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]]
output.o3_vmr = [[3.613153642076698e-07], [3.6754463715151265e-07], [3.742726275657643e-07], [3.8130208070716375e-07], [3.8848946418966404e-07], [3.957045496019655e-07], [4.027934206024675e-07], [4.0971400559562796e-07], [4.16458701657107e-07], [4.2308792088194504e-07], [4.296126069740838e-07], [4.361174540572554e-07], [4.4290472923328693e-07], [4.5015975290837635e-07], [4.5800304220552293e-07], [4.665057750427782e-07], [4.754996926918932e-07]]
output.o3clim_linoz_diag = [[4.87394178365753e-07], [4.874380444271754e-07], [4.874819104885978e-07], [4.875257765501428e-07], [4.875696426115653e-07], [4.876135086729879e-07], [4.876573747345329e-07], [4.877012407959554e-07], [4.877451068573779e-07], [4.877889729189229e-07], [4.878328389803455e-07], [4.878767050417679e-07], [4.87920571103313e-07], [4.879644371647355e-07], [4.880083032261581e-07], [4.880521692877031e-07], [4.880960353491255e-07]]
output.o3col_du_diag = [[243.16430645931064], [243.79078090903624], [244.42071215970103], [244.9598946386916], [245.35881900459918], [245.69246836183518], [246.05083371999046], [246.35967022609262], [246.5452767553693], [246.63555423011908], [246.88895575587955], [247.47112381941224], [248.2406223881473], [249.0511162870155], [249.70877012777507], [250.03911558733532], [250.1680971939018]]
output.ss_o3 = [[4.852855174818073e-07], [4.844681296606997e-07], [4.837536634160933e-07], [4.830231911507378e-07], [4.824943727680801e-07], [4.8187173051174e-07], [4.810760465108042e-07], [4.801859579733875e-07], [4.794426017513999e-07], [4.788649801547288e-07], [4.781260059166508e-07], [4.767085869373488e-07], [4.75084538544363e-07], [4.7327924049559025e-07], [4.7193471332657156e-07], [4.7148205362737493e-07], [4.716584999906512e-07]]
