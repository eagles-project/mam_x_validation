# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1393 ] 
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
input.tair=[[  0.25099811071426365E+003,  0.25690840140799361E+003,  0.26271240014273371E+003,  0.26209340122796732E+003,  0.26424405255904759E+003,  0.26585421780125336E+003,  0.26518153355391001E+003,  0.26118483991427655E+003,  0.25209004995557666E+003,  0.24239280021237829E+003,  0.23562888628560935E+003,  0.23415368080773339E+003,  0.23266852778572024E+003,  0.23007870252630357E+003,  0.22380258897076416E+003,  0.21627726476106562E+003,  0.21041217757760174E+003,  0.20642079866960674E+003,  0.20194165370260652E+003,  0.19775601344699675E+003,  0.19306867696005006E+003,  0.18979102361654378E+003,  0.18847191639887731E+003,  0.18848039303234515E+003,  0.18876639684447326E+003,  0.18909199380015809E+003,  0.18663245715574365E+003,  0.18780882481449081E+003,  0.19134614440805581E+003,  0.19524369705800947E+003,  0.19927212055518856E+003,  0.20320246503715913E+003,  0.20745805342164530E+003,  0.21191569625313261E+003,  0.21647794766308144E+003,  0.22107784801150066E+003,  0.22558621463351270E+003,  0.23025934797726586E+003,  0.23485197598403812E+003,  0.23929367132002042E+003,  0.24381993277956590E+003,  0.24833497593939890E+003,  0.25287210235564780E+003,  0.25733498403665556E+003,  0.26099699767856140E+003,  0.26448583831892029E+003,  0.26746544338018612E+003,  0.26964574070168965E+003,  0.27080566093393310E+003,  0.27278522317422670E+003,  0.27509140822100363E+003,  0.27801488895578962E+003,  0.28137650136091679E+003,  0.28391187880138853E+003,  0.28581370796996111E+003,  0.28738966625382000E+003,  0.28861544194063981E+003,  0.28958347125797121E+003,  0.29042318731873667E+003,  0.29118536779032894E+003,  0.29189008614879646E+003,  0.29256197651271634E+003,  0.29319091676620695E+003,  0.29367286315424303E+003,  0.29404680245489925E+003,  0.29442362804462999E+003,  0.29469650708125607E+003,  0.29453070815427458E+003,  0.29378284787509136E+003,  0.29230166107637768E+003,  0.29233280895606572E+003,  0.29249907840859208E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472622178629732E+005,  0.19914992411684136E+005,  0.21458139197088178E+005,  0.23132431504831562E+005,  0.24949014959692227E+005,  0.26919982413425765E+005,  0.29058454143102124E+005,  0.31378665077584737E+005,  0.33896060379655508E+005,  0.36627398804400786E+005,  0.39590862934880541E+005,  0.42806179557346535E+005,  0.46245569573417510E+005,  0.49784167670269293E+005,  0.53306000472612737E+005,  0.56740522292257388E+005,  0.60053750239509107E+005,  0.63231642403247766E+005,  0.66231436180731311E+005,  0.69011131877106032E+005,  0.71530458979606439E+005,  0.73751844953119988E+005,  0.75641346351762171E+005,  0.77197527875088592E+005,  0.78513387919506495E+005,  0.79734312412778905E+005,  0.80926242793708821E+005,  0.82087265595494653E+005,  0.83215496805125673E+005,  0.84309090286237042E+005,  0.85366239234141103E+005,  0.86385175847690523E+005,  0.87364175910475213E+005,  0.88301570475513523E+005,  0.89195757307753025E+005,  0.90045197393117283E+005,  0.90853234877959563E+005,  0.91546024744378155E+005,  0.91982631343617162E+005,],]
input.radius_part=[[  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.14607910135531538E-005,  0.18969746085708365E-005,  0.22443965942907709E-005,  0.25948731865183434E-005,  0.28767949636010408E-005,  0.30726964699865368E-005,  0.32026723359874180E-005,  0.33181644318947231E-005,  0.33581389134597751E-005,  0.27222922008278022E-005,  0.14759820831270516E-005,  0.10021752735817991E-005,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.85726636033965670E-006,  0.84232233569924718E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.84863595187960092E-006,  0.88639359182990376E-006,  0.90406052415651031E-006,  0.91865999611853795E-006,  0.92379673491322811E-006,  0.93727392676688688E-006,  0.95205682761932449E-006,  0.96124540339395657E-006,  0.96290006797057149E-006,  0.96326262963549686E-006,  0.96351876926461264E-006,  0.95907475052654103E-006,  0.95285250462555256E-006,  0.94207174768733076E-006,  0.93536397804661843E-006,  0.92970918273646669E-006,  0.93204915835359163E-006,  0.94564117055872109E-006,  0.95993747761000773E-006,  0.97052251898083727E-006,  0.15277249040938243E-005,  0.15673788811868421E-005,  0.16492727603221964E-005,  0.27084511896535815E-005,  0.24245232516425295E-005,  0.15688638397885412E-005,  0.12463032400752067E-005,  0.11643044186638315E-005,  0.11171834417047194E-005,  0.10935882537769535E-005,  0.10909462903690429E-005,  0.10950271143107383E-005,  0.10991691978486435E-005,  0.11029073243481148E-005,  0.11070673475171274E-005,  0.11146337307384682E-005,  0.11300505559507605E-005,  0.11400223244742264E-005,  0.11475443148375723E-005,  0.11753513778228128E-005,  0.12463030949926312E-005,  0.13951799166341172E-005,  0.16048107615082950E-005,  0.27450851874118074E-005,  0.26603718163934902E-005,  0.27459791423930453E-005,],]
input.density_part=[[  0.10000000000000000E+001,  0.17699985936180055E+004,  0.17699999806633773E+004,  0.17699999999103043E+004,  0.17699999999997474E+004,  0.17699999999999980E+004,  0.17700000000000000E+004,  0.17700000000000000E+004,  0.17700000000000002E+004,  0.17700000000000000E+004,  0.17700000000000000E+004,  0.17700000000000448E+004,  0.17700000000062564E+004,  0.17700000009369030E+004,  0.17700001490957472E+004,  0.17700214659062283E+004,  0.17712490028208194E+004,  0.17862623281342374E+004,  0.18442562326297771E+004,  0.18667815436711578E+004,  0.18812498652234631E+004,  0.18584929299443729E+004,  0.17206094749106069E+004,  0.18635401308316345E+004,  0.19387031726769649E+004,  0.19135791269018657E+004,  0.17915160719734956E+004,  0.17587604701528517E+004,  0.17910514127177960E+004,  0.18191461489739877E+004,  0.18241108953889225E+004,  0.18317239665294667E+004,  0.18460630900758949E+004,  0.18537042685622441E+004,  0.18577993447669469E+004,  0.18629325614973286E+004,  0.18636722952047228E+004,  0.18751236746811039E+004,  0.18842492124626635E+004,  0.18921782830799475E+004,  0.19032749688239601E+004,  0.19178027252207510E+004,  0.19174732996172199E+004,  0.18932968844386735E+004,  0.18595747745205365E+004,  0.18450491650236092E+004,  0.12127318010479858E+004,  0.11856690138634626E+004,  0.11623877973144872E+004,  0.10441491317869602E+004,  0.10716715239312557E+004,  0.12754832734682973E+004,  0.15482422769682419E+004,  0.16630734936373915E+004,  0.17366221103895118E+004,  0.17676394463082240E+004,  0.17608930937045895E+004,  0.17477922107040122E+004,  0.17403335796077324E+004,  0.17315829114485807E+004,  0.17221931603374067E+004,  0.17099479645056722E+004,  0.16817748166554888E+004,  0.16568161749050689E+004,  0.16410547459041215E+004,  0.15929907735213844E+004,  0.14833374678537184E+004,  0.13373375257211962E+004,  0.12207104275394124E+004,  0.10359322664272270E+004,  0.10393757407536038E+004,  0.10358062271696238E+004,],]
input.sig_part=[[  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.97925789788462557E-004,  0.11878476524664497E+000,  0.81373108335312125E-001,  0.55067980345672944E-001,  0.37469161220978021E-001,  0.25474493875012657E-001,  0.30102799848587925E-001,  0.26441211838268225E-001,  0.21041975651438810E-001,  0.16472512496129764E-001,  0.12833181160173420E-001,  0.10119883136240699E-001,  0.80796471173331125E-002,  0.66679154127406133E-002,  0.55627512767869192E-002,  0.35726289831198668E-002,  0.13887836719627530E-002,  0.74711363065904049E-003,  0.53998668728077895E-003,  0.48357376368159241E-003,  0.44055604804081654E-003,  0.40171627779953754E-003,  0.35957543312448203E-003,  0.36089521541265160E-003,  0.35593827239126534E-003,  0.33526582408656191E-003,  0.30563621922261253E-003,  0.30695370077237156E-003,  0.30861013093086089E-003,  0.30811518721997658E-003,  0.29917412457994221E-003,  0.29550083129890404E-003,  0.29380592099354544E-003,  0.28884144769878296E-003,  0.28038367896009739E-003,  0.27198750388993120E-003,  0.26339061554986749E-003,  0.25452148633773512E-003,  0.24503440309231299E-003,  0.23399221987988031E-003,  0.22552444214993432E-003,  0.21828510634297886E-003,  0.21291690140238327E-003,  0.20964753842409950E-003,  0.20608394043774536E-003,  0.20352370364686121E-003,  0.30015588298293447E-003,  0.30342613492240352E-003,  0.32385116084891372E-003,  0.74114133884676961E-003,  0.60862950458895196E-003,  0.31229018523937154E-003,  0.24293396945914371E-003,  0.22747257026614037E-003,  0.21812589307268812E-003,  0.21190926182701702E-003,  0.20900688380460356E-003,  0.20798064826249731E-003,  0.20774370605638787E-003,  0.20725925247986536E-003,  0.20688466888126668E-003,  0.20737458912596407E-003,  0.20863434242661668E-003,  0.20840382718490384E-003,  0.20850616229456520E-003,  0.21124475276062171E-003,  0.21925649298427466E-003,  0.24456673454258284E-003,  0.29170259121466790E-003,  0.69993566715511148E-003,  0.66037454587768889E-003,  0.69949823719700423E-003,],]
