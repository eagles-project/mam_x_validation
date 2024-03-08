# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1386 ] 
# This file was generated by E3SM.

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass
# Settings are stored here.
settings = Object()
# Input is stored here.
input = Object()
input.dt = [    0.00, ]
input.moment=[[         0],]
input.ncol=[[         4],]
input.pcols=[[         4],]
input.nver=[[        72],]
input.radius_max=[[  0.50000000000000002E-004],]
input.tair=[[  0.25409818491188793E+003,  0.26672193595773729E+003,  0.26663854246703931E+003,  0.26492624140724377E+003,  0.26747272663173726E+003,  0.26931554287839930E+003,  0.26551765193221564E+003,  0.25830232966935256E+003,  0.24735237270594021E+003,  0.23986387557957525E+003,  0.23639483331155495E+003,  0.23658337818032064E+003,  0.23500756567672042E+003,  0.23131341752683281E+003,  0.22346108476896379E+003,  0.21517339306281701E+003,  0.20970894516069873E+003,  0.20606268181251448E+003,  0.20147781263116377E+003,  0.19684210205631109E+003,  0.19199532262102935E+003,  0.18917917223217995E+003,  0.18832610787738284E+003,  0.18835271989209738E+003,  0.18863011636562652E+003,  0.18894774475577390E+003,  0.18699036517696729E+003,  0.18808543222362576E+003,  0.19135330277289819E+003,  0.19499753328695681E+003,  0.19921654820972972E+003,  0.20358498310755579E+003,  0.20805987100693724E+003,  0.21246528341567426E+003,  0.21686003667886521E+003,  0.22130779526751098E+003,  0.22592830209276690E+003,  0.23065345169235218E+003,  0.23539404814973452E+003,  0.24003884416799923E+003,  0.24442860611154885E+003,  0.24829432141155272E+003,  0.25245922883269594E+003,  0.25689923846210803E+003,  0.26174577725785099E+003,  0.26567586358384250E+003,  0.26785739820887494E+003,  0.27010763882223944E+003,  0.27137937397357507E+003,  0.27319273940206648E+003,  0.27552093102729577E+003,  0.27874960096658577E+003,  0.28146479358974932E+003,  0.28393664829638817E+003,  0.28602654113290993E+003,  0.28759411006720273E+003,  0.28879494066581674E+003,  0.28975464833460353E+003,  0.29060224133975424E+003,  0.29141599731658675E+003,  0.29221003795417289E+003,  0.29288724572007095E+003,  0.29350023761046924E+003,  0.29402191174142615E+003,  0.29448972779913294E+003,  0.29502610889742260E+003,  0.29564907761563632E+003,  0.29628706696851867E+003,  0.29684417565756831E+003,  0.29656064056628139E+003,  0.29498557571239070E+003,  0.29462908511771946E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473623631657374E+005,  0.19918494910122085E+005,  0.21464768324630899E+005,  0.23142452981533017E+005,  0.24962717087195670E+005,  0.26937677995133083E+005,  0.29080482565469851E+005,  0.31405394567898205E+005,  0.33927890461241790E+005,  0.36664762957293766E+005,  0.39634231477572852E+005,  0.42856062776650258E+005,  0.46302421473722265E+005,  0.49848189262763248E+005,  0.53377157788381679E+005,  0.56818638426138627E+005,  0.60138579433274732E+005,  0.63322910446702728E+005,  0.66328782221617075E+005,  0.69114109967125667E+005,  0.71638541576819131E+005,  0.73864428387353808E+005,  0.75757758178846838E+005,  0.77317092742558816E+005,  0.78635618902024071E+005,  0.79859017156485163E+005,  0.81053362552733117E+005,  0.82216737747571591E+005,  0.83347254910099276E+005,  0.84443064164451585E+005,  0.85502355043800955E+005,  0.86523356163766643E+005,  0.87504339816024658E+005,  0.88443633673491058E+005,  0.89339632253189804E+005,  0.90190793421342401E+005,  0.91000366943135130E+005,  0.91694338299764539E+005,  0.92131652244595214E+005,],]
input.radius_part=[[  0.13795799520252484E-007,  0.13537106393414173E-007,  0.17222271326230819E-007,  0.19573999292016736E-007,  0.19832365766533046E-007,  0.23872359037803377E-007,  0.27305821880406180E-007,  0.29733854462359810E-007,  0.32676112721107858E-007,  0.34373070656099805E-007,  0.35631755409166527E-007,  0.36290995914152565E-007,  0.37002086538125289E-007,  0.37988745465172844E-007,  0.37908741253226276E-007,  0.37263173060844501E-007,  0.38206147459385118E-007,  0.40061261425868106E-007,  0.39127384106217052E-007,  0.33123323169008119E-007,  0.29543003653946665E-007,  0.27865918349069451E-007,  0.27660718940259479E-007,  0.27382667177544079E-007,  0.26280840147932598E-007,  0.19842373472526683E-007,  0.14049365453455241E-007,  0.14737470878178841E-007,  0.16111571357921343E-007,  0.18297107920710562E-007,  0.19954197188869542E-007,  0.21395607067328077E-007,  0.22208945938345792E-007,  0.23632554812615564E-007,  0.25800753213617006E-007,  0.27507486204900769E-007,  0.29095557729271901E-007,  0.30946949055976470E-007,  0.32274765457085776E-007,  0.32860121733363442E-007,  0.33445873034307385E-007,  0.33092739776300631E-007,  0.32024011866605089E-007,  0.31914598091488759E-007,  0.35134695915554897E-007,  0.36387001808723623E-007,  0.40352704815634325E-007,  0.42433334651509289E-007,  0.43750526080277594E-007,  0.44031354581742466E-007,  0.43785219485899621E-007,  0.37338809529114552E-007,  0.33265945381082334E-007,  0.31582752669305542E-007,  0.29776078298312606E-007,  0.27137358627884664E-007,  0.23754863460261156E-007,  0.22293723398322764E-007,  0.21754610098988247E-007,  0.21484235904573074E-007,  0.21272261704841474E-007,  0.21157526635882120E-007,  0.20952111526809912E-007,  0.21245816354349485E-007,  0.22738076988954644E-007,  0.24058604517582209E-007,  0.25224782139434467E-007,  0.26863632254772909E-007,  0.27364282546282081E-007,  0.29165923583808277E-007,  0.36035108706191617E-007,  0.38599185079320635E-007,],]
input.density_part=[[  0.17711406965478964E+004,  0.17716708968599710E+004,  0.17718367398162152E+004,  0.17718833338786019E+004,  0.17718683736942762E+004,  0.17718359569584597E+004,  0.17715398478432376E+004,  0.16963836571417391E+004,  0.15870846762681779E+004,  0.15639796751395645E+004,  0.15499525500881900E+004,  0.15454644716940654E+004,  0.15394107795534849E+004,  0.15342679206769351E+004,  0.15173478534987012E+004,  0.14559099260679407E+004,  0.13527971567285188E+004,  0.12628004644899113E+004,  0.12192704373495064E+004,  0.11918592336477500E+004,  0.11839598843259425E+004,  0.11704340658236995E+004,  0.11515074707630165E+004,  0.11500915348589740E+004,  0.11502362292183543E+004,  0.11672117848562523E+004,  0.12113040440484208E+004,  0.11727037728334549E+004,  0.11567342649287125E+004,  0.11468502474291124E+004,  0.11379311437896170E+004,  0.11035788959268252E+004,  0.10796073271628532E+004,  0.10664803654241362E+004,  0.10485051691101407E+004,  0.10335901076196369E+004,  0.10241377612716542E+004,  0.10184007678844346E+004,  0.10186561113415229E+004,  0.10197214412074070E+004,  0.10235000238830476E+004,  0.10406116332241754E+004,  0.10564987827402670E+004,  0.10614926825181972E+004,  0.10493445442301841E+004,  0.10525131962283365E+004,  0.10412201660178569E+004,  0.10390235703545357E+004,  0.10499397650734354E+004,  0.10581999212162300E+004,  0.10769985463596786E+004,  0.11502577072534982E+004,  0.12084888679710336E+004,  0.12535452024119722E+004,  0.12868362514827822E+004,  0.13105728111950839E+004,  0.13483059356216206E+004,  0.13851118158366355E+004,  0.14092124058068714E+004,  0.14408906766648208E+004,  0.14616051997410898E+004,  0.14822010994310206E+004,  0.15065123747218422E+004,  0.15004326217959674E+004,  0.14361716306659036E+004,  0.13821838990997389E+004,  0.13536888506440735E+004,  0.13594660776988635E+004,  0.13686332809681007E+004,  0.12894081481534738E+004,  0.11552167781447683E+004,  0.11271665690564034E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.26934234958667608E-002,  0.18344568746920936E-002,  0.15805669570459569E-002,  0.12127866987801806E-002,  0.83622641782472114E-003,  0.68408141375570506E-003,  0.52614061398287629E-003,  0.36651763671198621E-003,  0.24979520206528722E-003,  0.17274439789589791E-003,  0.12194753861249135E-003,  0.88306592000548861E-004,  0.65302602843246438E-004,  0.49645825278475614E-004,  0.36967266732661112E-004,  0.26921789538872973E-004,  0.20426929835312185E-004,  0.16355163899607297E-004,  0.12834743188842647E-004,  0.89958980435617653E-005,  0.68818631334167547E-005,  0.56811595388781304E-005,  0.50366820004002065E-005,  0.45846428438134208E-005,  0.40614202945545727E-005,  0.28620985882361778E-005,  0.19228075541060266E-005,  0.18073444375432967E-005,  0.18150736314403086E-005,  0.19064611326281653E-005,  0.19263529634241454E-005,  0.18707802245013090E-005,  0.17734598556693964E-005,  0.17458327315339530E-005,  0.17623074634647307E-005,  0.17422498515287291E-005,  0.17173217820506270E-005,  0.17086376905764559E-005,  0.16751056505190847E-005,  0.16020814943597917E-005,  0.15347070793855002E-005,  0.14438672221322389E-005,  0.13252984690195549E-005,  0.12419867887160635E-005,  0.12738393962391521E-005,  0.12421861239942268E-005,  0.12886633281841409E-005,  0.12812408533034343E-005,  0.12685741760715713E-005,  0.12273569026122024E-005,  0.11896632896987627E-005,  0.10254499551137805E-005,  0.91751147269639979E-006,  0.87325543086258232E-006,  0.81984193874755714E-006,  0.73917010272845788E-006,  0.64755091254653570E-006,  0.61261294927705911E-006,  0.59922293874743744E-006,  0.59694387058155012E-006,  0.59190585150349845E-006,  0.58980836521257659E-006,  0.58659596362085111E-006,  0.58659367041949702E-006,  0.59773127787708808E-006,  0.60555814299973929E-006,  0.61877972507887353E-006,  0.66007588971523106E-006,  0.67279673376851516E-006,  0.67426558101943160E-006,  0.75875267871551416E-006,  0.79697162288188034E-006,],]