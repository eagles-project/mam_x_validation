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
input.moment=[[         0],]
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
output.vlc_grv=[[  0.98576884556092693E-004,  0.68360371387874395E-004,  0.82737462209148904E-001,  0.56204764206974026E-001,  0.38029434990156534E-001,  0.25635894761571666E-001,  0.31952136958814832E-001,  0.27875199263949869E-001,  0.21654395894594954E-001,  0.16517482182054129E-001,  0.12782453045737580E-001,  0.10140881238243782E-001,  0.81469999957255561E-002,  0.67131508922426645E-002,  0.55637729417729962E-002,  0.33778292408578863E-002,  0.13796372896437467E-002,  0.71965161958393502E-003,  0.54046268801650891E-003,  0.48289024648021529E-003,  0.43824992230684145E-003,  0.39354651749113175E-003,  0.36278068400338734E-003,  0.35178304505274966E-003,  0.34769812723184210E-003,  0.33533949917244267E-003,  0.31907840083547992E-003,  0.29436586337423364E-003,  0.30693735197120524E-003,  0.29953733913037976E-003,  0.30625184354582033E-003,  0.30358819792388066E-003,  0.29637676122535960E-003,  0.28674086528381347E-003,  0.27342210708798160E-003,  0.26268312140626546E-003,  0.25304987132701465E-003,  0.24320729912080517E-003,  0.23420074655073987E-003,  0.22584097220882112E-003,  0.21808934875423229E-003,  0.21127230563683914E-003,  0.20593250211297368E-003,  0.21552889141922797E-003,  0.23070109506541085E-003,  0.22296526929914612E-003,  0.28389311626759550E-003,  0.31530138053522733E-003,  0.24743960342899282E-003,  0.30510299748777540E-003,  0.37215558726361614E-003,  0.29844542275635710E-003,  0.26111620420810050E-003,  0.23877074798229204E-003,  0.22583568122748151E-003,  0.21749770975129304E-003,  0.21233895819934012E-003,  0.20869178663948364E-003,  0.20598720228718831E-003,  0.20386216403055153E-003,  0.20358447641201992E-003,  0.20290771100768890E-003,  0.20119959596046487E-003,  0.20154648240052955E-003,  0.21234528533247218E-003,  0.22736362354164574E-003,  0.22600894301709384E-003,  0.22495990673443582E-003,  0.22423349823808052E-003,  0.22068394669725339E-003,  0.21735653803917033E-003,  0.21517809609243691E-003,],]
