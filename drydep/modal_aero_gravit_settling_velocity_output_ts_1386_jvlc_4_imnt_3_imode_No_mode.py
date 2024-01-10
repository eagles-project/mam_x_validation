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
input.moment=[[         3],]
input.ncol=[[         4],]
input.pcols=[[         4],]
input.nver=[[        72],]
input.radius_max=[[  0.50000000000000002E-004],]
input.tair=[[  0.25409818491188793E+003,  0.26672193595773729E+003,  0.26663854246703931E+003,  0.26492624140724377E+003,  0.26747272663173726E+003,  0.26931554287839930E+003,  0.26551765193221564E+003,  0.25830232966935256E+003,  0.24735237270594021E+003,  0.23986387557957525E+003,  0.23639483331155495E+003,  0.23658337818032064E+003,  0.23500756567672042E+003,  0.23131341752683281E+003,  0.22346108476896379E+003,  0.21517339306281701E+003,  0.20970894516069873E+003,  0.20606268181251448E+003,  0.20147781263116377E+003,  0.19684210205631109E+003,  0.19199532262102935E+003,  0.18917917223217995E+003,  0.18832610787738284E+003,  0.18835271989209738E+003,  0.18863011636562652E+003,  0.18894774475577390E+003,  0.18699036517696729E+003,  0.18808543222362576E+003,  0.19135330277289819E+003,  0.19499753328695681E+003,  0.19921654820972972E+003,  0.20358498310755579E+003,  0.20805987100693724E+003,  0.21246528341567426E+003,  0.21686003667886521E+003,  0.22130779526751098E+003,  0.22592830209276690E+003,  0.23065345169235218E+003,  0.23539404814973452E+003,  0.24003884416799923E+003,  0.24442860611154885E+003,  0.24829432141155272E+003,  0.25245922883269594E+003,  0.25689923846210803E+003,  0.26174577725785099E+003,  0.26567586358384250E+003,  0.26785739820887494E+003,  0.27010763882223944E+003,  0.27137937397357507E+003,  0.27319273940206648E+003,  0.27552093102729577E+003,  0.27874960096658577E+003,  0.28146479358974932E+003,  0.28393664829638817E+003,  0.28602654113290993E+003,  0.28759411006720273E+003,  0.28879494066581674E+003,  0.28975464833460353E+003,  0.29060224133975424E+003,  0.29141599731658675E+003,  0.29221003795417289E+003,  0.29288724572007095E+003,  0.29350023761046924E+003,  0.29402191174142615E+003,  0.29448972779913294E+003,  0.29502610889742260E+003,  0.29564907761563632E+003,  0.29628706696851867E+003,  0.29684417565756831E+003,  0.29656064056628139E+003,  0.29498557571239070E+003,  0.29462908511771946E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473623631657374E+005,  0.19918494910122085E+005,  0.21464768324630899E+005,  0.23142452981533017E+005,  0.24962717087195670E+005,  0.26937677995133083E+005,  0.29080482565469851E+005,  0.31405394567898205E+005,  0.33927890461241790E+005,  0.36664762957293766E+005,  0.39634231477572852E+005,  0.42856062776650258E+005,  0.46302421473722265E+005,  0.49848189262763248E+005,  0.53377157788381679E+005,  0.56818638426138627E+005,  0.60138579433274732E+005,  0.63322910446702728E+005,  0.66328782221617075E+005,  0.69114109967125667E+005,  0.71638541576819131E+005,  0.73864428387353808E+005,  0.75757758178846838E+005,  0.77317092742558816E+005,  0.78635618902024071E+005,  0.79859017156485163E+005,  0.81053362552733117E+005,  0.82216737747571591E+005,  0.83347254910099276E+005,  0.84443064164451585E+005,  0.85502355043800955E+005,  0.86523356163766643E+005,  0.87504339816024658E+005,  0.88443633673491058E+005,  0.89339632253189804E+005,  0.90190793421342401E+005,  0.91000366943135130E+005,  0.91694338299764539E+005,  0.92131652244595214E+005,],]
input.radius_part=[[  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,],]
input.density_part=[[  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,],]
input.sig_part=[[  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.81856154533613046E+000,  0.56903774215605707E+000,  0.38655337250361016E+000,  0.26221861461671014E+000,  0.17965554073077233E+000,  0.12332988044044271E+000,  0.84296275151860237E-001,  0.57806182983303075E-001,  0.40013666195630050E-001,  0.28504330379199118E-001,  0.21402938803212056E-001,  0.16998260164548685E-001,  0.14165379258700254E-001,  0.12365892010854980E-001,  0.11297976229727042E-001,  0.10684567100911653E-001,  0.10281731928668181E-001,  0.99977152853317035E-002,  0.98549363662553697E-002,  0.97984634780862202E-002,  0.98148766018714296E-002,  0.98039502687262484E-002,  0.97495182184627466E-002,  0.96781406551369291E-002,  0.96041050527863464E-002,  0.95333519122797385E-002,  0.95588575775609821E-002,  0.94651115791138194E-002,  0.92895261927140350E-002,  0.91074252292622261E-002,  0.89128092991428518E-002,  0.87224182194368238E-002,  0.85377216930581507E-002,  0.83651650272921485E-002,  0.82021425836414971E-002,  0.80450652500782954E-002,  0.78899939395583318E-002,  0.77389402088535808E-002,  0.75941221396645690E-002,  0.74579206440448867E-002,  0.73334545335120432E-002,  0.72258979594844210E-002,  0.71156416583056633E-002,  0.70036571954340586E-002,  0.68876388793283842E-002,  0.67946623699522207E-002,  0.67395268792352168E-002,  0.66853548055420446E-002,  0.66519901989772930E-002,  0.66098833288555448E-002,  0.65597177228843648E-002,  0.64948690248946223E-002,  0.64413291875863865E-002,  0.63937379529243896E-002,  0.63541660678102154E-002,  0.63246399060850819E-002,  0.63021578068742168E-002,  0.62842753874487161E-002,  0.62685418917746366E-002,  0.62535328885637573E-002,  0.62390032886155073E-002,  0.62265343071652027E-002,  0.62152383689992163E-002,  0.62055400856861004E-002,  0.61968145820268097E-002,  0.61870750150390614E-002,  0.61760418798552444E-002,  0.61648757257586635E-002,  0.61551059004200867E-002,  0.61588140867019515E-002,  0.61834233831492445E-002,  0.61887610910750738E-002,],]
