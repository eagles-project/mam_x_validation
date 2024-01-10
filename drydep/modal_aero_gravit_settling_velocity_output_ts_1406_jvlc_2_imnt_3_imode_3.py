# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1406 ] 
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
input.tair=[[  0.25435033558770152E+003,  0.26658416567070367E+003,  0.27161465885213585E+003,  0.27305969079622753E+003,  0.27224151832595254E+003,  0.26925616778151590E+003,  0.26635165683534740E+003,  0.26072780995730903E+003,  0.25153551063929930E+003,  0.24279542054437644E+003,  0.23636440233214500E+003,  0.23395470415890776E+003,  0.23218520518246595E+003,  0.22974729767387228E+003,  0.22434270552939736E+003,  0.21738764821491546E+003,  0.21026584643346985E+003,  0.20461023502760023E+003,  0.19946752148828986E+003,  0.19505257968636212E+003,  0.19073518286535349E+003,  0.18841583687591014E+003,  0.18806462515941431E+003,  0.18879792677321109E+003,  0.18999822369749231E+003,  0.19226085255536481E+003,  0.19260413418220514E+003,  0.18972449120883414E+003,  0.19104797174976594E+003,  0.19535525682088607E+003,  0.19906590137890106E+003,  0.20323923582030059E+003,  0.20782809651035029E+003,  0.21249863164057479E+003,  0.21693078725658029E+003,  0.22133492789758645E+003,  0.22600610306910096E+003,  0.23075819017782857E+003,  0.23556745536079134E+003,  0.24018267757731826E+003,  0.24472307382594502E+003,  0.24913081538966273E+003,  0.25331075011291634E+003,  0.25720073501317131E+003,  0.26104834105318724E+003,  0.26514892124293834E+003,  0.26761586708570343E+003,  0.26954547512086526E+003,  0.27119243167189433E+003,  0.27329908456006791E+003,  0.27532326908953598E+003,  0.27836308137437925E+003,  0.28116363937249344E+003,  0.28375208753045194E+003,  0.28600310197217686E+003,  0.28785124346207078E+003,  0.28920833148502106E+003,  0.29023206521350198E+003,  0.29112467266593546E+003,  0.29199643644298487E+003,  0.29275298925834494E+003,  0.29345940788283258E+003,  0.29405480897617321E+003,  0.29451529676170168E+003,  0.29458768505772565E+003,  0.29502364158678398E+003,  0.29572951515597663E+003,  0.29638024543271678E+003,  0.29700920812845578E+003,  0.29767336741838551E+003,  0.29825388939585036E+003,  0.29860278995839013E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472001195671415E+005,  0.19912820575580547E+005,  0.21454028594674601E+005,  0.23126217367895570E+005,  0.24940518517585202E+005,  0.26909009702400515E+005,  0.29044794715738790E+005,  0.31362090602785724E+005,  0.33876323120212270E+005,  0.36604229967163395E+005,  0.39563970883835282E+005,  0.42775247872845750E+005,  0.46210316735528482E+005,  0.49744469035580070E+005,  0.53261877104634288E+005,  0.56692083886690103E+005,  0.60001149186597140E+005,  0.63175048735786884E+005,  0.66171073656698005E+005,  0.68947277020995258E+005,  0.71463438910659941E+005,  0.73682033996322411E+005,  0.75569161477614034E+005,  0.77123387857471651E+005,  0.78437594692039871E+005,  0.79656985250620666E+005,  0.80847418124113727E+005,  0.82006982249399880E+005,  0.83133795980873518E+005,  0.84226015500966125E+005,  0.85281836275816924E+005,  0.86299492726177006E+005,  0.87277262800909113E+005,  0.88213479648972061E+005,  0.89106543049292231E+005,  0.89954915922264190E+005,  0.90762000938300407E+005,  0.91454058183950910E+005,  0.91890226170947557E+005,],]
input.radius_part=[[  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.15465896447944318E-005,  0.20001338385734272E-005,  0.23104628666569146E-005,  0.25998331499244585E-005,  0.28628869617956873E-005,  0.30792197851022057E-005,  0.32270676160175927E-005,  0.33370728343532789E-005,  0.33581389134597751E-005,  0.26093423221455446E-005,  0.14683539558897428E-005,  0.97255251099082411E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.86350689124726383E-006,  0.87206826726486600E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.87608199207420662E-006,  0.90440971605193409E-006,  0.91129716673366019E-006,  0.93218587013965968E-006,  0.94629158950563646E-006,  0.95171426689002104E-006,  0.94782174494058345E-006,  0.93644471655507535E-006,  0.92984063976993951E-006,  0.92468780356538203E-006,  0.91843993861922470E-006,  0.91555762858572423E-006,  0.91640513944707514E-006,  0.92152789709563453E-006,  0.93553349666193247E-006,  0.95586785032964943E-006,  0.10741840219202786E-005,  0.11863977431459806E-005,  0.11573117148007206E-005,  0.14838814154790186E-005,  0.16251750057268091E-005,  0.13621795471601232E-005,  0.15663700971875350E-005,  0.18018544622024238E-005,  0.15225659006813154E-005,  0.13436974116840589E-005,  0.12213590157355922E-005,  0.11486438631086086E-005,  0.11024097782116002E-005,  0.10799847522490052E-005,  0.10670969602491538E-005,  0.10610824995338582E-005,  0.10588732052723313E-005,  0.10716221680674954E-005,  0.10761631665489298E-005,  0.10803439406738782E-005,  0.10994259487760746E-005,  0.12078884538732269E-005,  0.13098662871884760E-005,  0.13074367273693793E-005,  0.13050002110591515E-005,  0.13038975265329032E-005,  0.12866349489083855E-005,  0.12697381569291994E-005,  0.12582736557962901E-005,],]
input.density_part=[[  0.10000000000000000E+001,  0.10000000000000000E+001,  0.17699989123180897E+004,  0.17699999997561436E+004,  0.17699999999998506E+004,  0.17699999999999986E+004,  0.17700000000000002E+004,  0.17700000000000000E+004,  0.17700000000000000E+004,  0.17700000000000002E+004,  0.17700000000000007E+004,  0.17700000000001032E+004,  0.17700000000147747E+004,  0.17700000016057738E+004,  0.17700001221646301E+004,  0.17700160834978471E+004,  0.17711579999426854E+004,  0.17874012168928105E+004,  0.18505685126498131E+004,  0.18679271603232885E+004,  0.18733851572181834E+004,  0.17536464415926912E+004,  0.16954928748531458E+004,  0.18250166067812822E+004,  0.18947465864113558E+004,  0.19173815277968074E+004,  0.19090914174251102E+004,  0.17203359363444495E+004,  0.17796006090023734E+004,  0.17911066196160766E+004,  0.18402075906743444E+004,  0.18533304155415760E+004,  0.18644546284411404E+004,  0.18848834178921284E+004,  0.18981311240980583E+004,  0.19084597923519120E+004,  0.19191323448731796E+004,  0.19285827506392939E+004,  0.19291174948151013E+004,  0.19171221946612129E+004,  0.18910766374951857E+004,  0.18387055210505741E+004,  0.17759398211515243E+004,  0.15530153883342507E+004,  0.14249324557537600E+004,  0.14746303609252298E+004,  0.12110726612054218E+004,  0.11509449343487788E+004,  0.12711349691043868E+004,  0.12219688339493587E+004,  0.11560778357987231E+004,  0.12907389692749089E+004,  0.14447496219360989E+004,  0.15959740557754219E+004,  0.17079319273777103E+004,  0.17888760122675769E+004,  0.18249141880563855E+004,  0.18423928107325842E+004,  0.18451815130247135E+004,  0.18404130621966160E+004,  0.18038116658984686E+004,  0.17896687291932053E+004,  0.17671141172894806E+004,  0.17176851112179065E+004,  0.15194517685984731E+004,  0.13994479370550994E+004,  0.13997972762214733E+004,  0.14017534735971096E+004,  0.14028275839481394E+004,  0.14192942175163791E+004,  0.14362740883680533E+004,  0.14483144908654313E+004,],]
input.sig_part=[[  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.27810793486368986E-003,  0.19291218960447849E-003,  0.23358346801028393E+000,  0.15877968760570191E+000,  0.10754007070303892E+000,  0.72603473287906214E-001,  0.91230665449056156E-001,  0.80599811414130654E-001,  0.63933242741248092E-001,  0.50563781179812091E-001,  0.41380277068196247E-001,  0.35319868296601727E-001,  0.30952319724106742E-001,  0.28082085748555519E-001,  0.25604558676225696E-001,  0.15701016381881941E-001,  0.58097901605485610E-002,  0.28722604332386157E-002,  0.21964317175782910E-002,  0.20761230599515108E-002,  0.19856036171898867E-002,  0.18769337018097500E-002,  0.17905985465147391E-002,  0.17584651273268284E-002,  0.17776586970827235E-002,  0.17487637469525601E-002,  0.17034683479784463E-002,  0.16374410289555432E-002,  0.17551862420633973E-002,  0.17384537449139023E-002,  0.18116738705430484E-002,  0.18245614445188485E-002,  0.18038657516619349E-002,  0.17619036676418825E-002,  0.16923875813353957E-002,  0.16392718288569409E-002,  0.15920698875628047E-002,  0.15421147911882610E-002,  0.14974714515330609E-002,  0.14573091395397237E-002,  0.14211653529279525E-002,  0.13921801312908103E-002,  0.13731434304706364E-002,  0.14725095498101758E-002,  0.16069439350819223E-002,  0.15587119275581205E-002,  0.20468891947218715E-002,  0.23016644536574390E-002,  0.17883645819540123E-002,  0.22380551654357312E-002,  0.27640091837712807E-002,  0.21964365547652662E-002,  0.19080212190963051E-002,  0.17348959335789173E-002,  0.16353388197456113E-002,  0.15717305710154052E-002,  0.15336216494436844E-002,  0.15073219606387364E-002,  0.14885317150091872E-002,  0.14742969401671262E-002,  0.14751371852573325E-002,  0.14720413943439827E-002,  0.14613690615615203E-002,  0.14671995589357696E-002,  0.15583560408848616E-002,  0.16792393430248827E-002,  0.16698817078824701E-002,  0.16627326460735591E-002,  0.16580190721696682E-002,  0.16309776335562045E-002,  0.16055048108274328E-002,  0.15887861393581201E-002,],]
