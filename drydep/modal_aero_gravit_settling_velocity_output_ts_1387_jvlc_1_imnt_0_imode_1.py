# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1387 ] 
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
input.tair=[[  0.25380286507550383E+003,  0.26559286328696550E+003,  0.26654114167743057E+003,  0.26432509187855811E+003,  0.26649320064326594E+003,  0.26851164433049865E+003,  0.26543752170102857E+003,  0.25884339701677783E+003,  0.24799969696738719E+003,  0.24003276542698575E+003,  0.23620550837266208E+003,  0.23631615129131328E+003,  0.23489264776931489E+003,  0.23146604551131543E+003,  0.22385409393710302E+003,  0.21555438498332001E+003,  0.20989872021099740E+003,  0.20613924584186910E+003,  0.20155103148046982E+003,  0.19694755207694260E+003,  0.19206907339197079E+003,  0.18917086806155805E+003,  0.18827775025728064E+003,  0.18832315057245481E+003,  0.18859275319023340E+003,  0.18887799265033570E+003,  0.18687435511189815E+003,  0.18805362938672536E+003,  0.19133598553232792E+003,  0.19503652776819146E+003,  0.19926538074274598E+003,  0.20357903138847252E+003,  0.20802272590494422E+003,  0.21244740540906346E+003,  0.21678493570712871E+003,  0.22126579673393226E+003,  0.22592583622491861E+003,  0.23063149604229378E+003,  0.23530539253859556E+003,  0.23993285335263747E+003,  0.24444050069413825E+003,  0.24835097427573726E+003,  0.25247111616315834E+003,  0.25694314100927221E+003,  0.26178581247196024E+003,  0.26571558971871337E+003,  0.26794784678854029E+003,  0.27035140683862784E+003,  0.27148124316106765E+003,  0.27325855153458866E+003,  0.27551679093417971E+003,  0.27888653406970388E+003,  0.28156956122931217E+003,  0.28398644708582805E+003,  0.28605263217399676E+003,  0.28763044762568808E+003,  0.28883872607163357E+003,  0.28979902895419974E+003,  0.29064114417689768E+003,  0.29143913283674215E+003,  0.29223280220628442E+003,  0.29291965387420254E+003,  0.29352143186162186E+003,  0.29404665575657577E+003,  0.29450847416357692E+003,  0.29499382508488605E+003,  0.29555422223443418E+003,  0.29615156544709157E+003,  0.29672456958416916E+003,  0.29578434355073830E+003,  0.29440022320242161E+003,  0.29378430925960083E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18474011939809378E+005,  0.19919852985496855E+005,  0.21467338734020504E+005,  0.23146338756492863E+005,  0.24968030015173819E+005,  0.26944539364005825E+005,  0.29089023970553302E+005,  0.31415758787388386E+005,  0.33940232408210541E+005,  0.36679250711347668E+005,  0.39651047402237375E+005,  0.42875404732956842E+005,  0.46324465499488644E+005,  0.49873013299021957E+005,  0.53404748663864622E+005,  0.56848927546798048E+005,  0.60171471507648443E+005,  0.63358299151227708E+005,  0.66366527637725216E+005,  0.69154039180706866E+005,  0.71680450036256414E+005,  0.73908082022708390E+005,  0.75802896253423227E+005,  0.77363453391985473E+005,  0.78683013323558334E+005,  0.79907370765928543E+005,  0.81102652571682804E+005,  0.82266939894573079E+005,  0.83398343423330996E+005,  0.84495011832120595E+005,  0.85555133234138819E+005,  0.86576934855624961E+005,  0.87558687634283779E+005,  0.88498717932414409E+005,  0.89395419007675475E+005,  0.90247247516640404E+005,  0.91057416628693652E+005,  0.91751846101947318E+005,  0.92189434316316299E+005,],]
input.radius_part=[[  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.40895565189818464E-007,  0.40997593941880924E-007,  0.43024147265405485E-007,  0.47288892750122114E-007,  0.49911332725626215E-007,  0.53889181943510571E-007,  0.58856269846142151E-007,  0.64920357443953936E-007,  0.72177613884870463E-007,  0.83857429317345237E-007,  0.10021128803962450E-006,  0.11630871350146750E-006,  0.12455835761366332E-006,  0.12605587397670050E-006,  0.12669651423691601E-006,  0.12758701002776135E-006,  0.12657131554873138E-006,  0.12543573932264043E-006,  0.12520970048159272E-006,  0.12547163175482141E-006,  0.12300714231117060E-006,  0.12170975066373249E-006,  0.12160815468846270E-006,  0.12269591157515093E-006,  0.12324517397582728E-006,  0.12297336744384339E-006,  0.12309525618637582E-006,  0.12362824239645187E-006,  0.12417731336567165E-006,  0.12469416012589299E-006,  0.12462251974629126E-006,  0.12370567046380785E-006,  0.12192606368640111E-006,  0.11651530173040350E-006,  0.11587856435667273E-006,  0.11738123350538023E-006,  0.12002443923004512E-006,  0.13457407098633978E-006,  0.13957302801343211E-006,  0.15489246200985344E-006,  0.15667374498244812E-006,  0.16132471903114494E-006,  0.18440153689341454E-006,  0.17709993530318927E-006,  0.14711893294421669E-006,  0.13662430425429484E-006,  0.13171071475327728E-006,  0.12934261763083857E-006,  0.12878359309059031E-006,  0.12865201112753261E-006,  0.12838595038447241E-006,  0.12813589105540522E-006,  0.12788706692727234E-006,  0.12761593619668598E-006,  0.12760503059748006E-006,  0.12742453298009366E-006,  0.12750947529474153E-006,  0.12763866945247241E-006,  0.13054180129122255E-006,  0.13222574167352396E-006,  0.13161911661136848E-006,  0.12958850634038230E-006,  0.13934596489964037E-006,  0.16589708274571785E-006,  0.21894144764406229E-006,],]
input.density_part=[[  0.16384365317248362E+004,  0.16551513057154752E+004,  0.16801076328047350E+004,  0.16923623205258791E+004,  0.17042746862659112E+004,  0.17067972337138140E+004,  0.17143448146439298E+004,  0.16731332741701212E+004,  0.15755342676242055E+004,  0.15660075681347341E+004,  0.15539413868220524E+004,  0.15387009812747428E+004,  0.15178469977600080E+004,  0.15126066510062333E+004,  0.15495437836285778E+004,  0.15410859506899119E+004,  0.14146669101374559E+004,  0.13314894148288799E+004,  0.13383328771251286E+004,  0.12937403014051743E+004,  0.12589498972792483E+004,  0.12280568282428574E+004,  0.12127918231256938E+004,  0.12110734787303800E+004,  0.12026670989078623E+004,  0.11882299129302014E+004,  0.11792036665947280E+004,  0.11955287743833082E+004,  0.12101634512325090E+004,  0.11937741676784203E+004,  0.11741700752063011E+004,  0.11616668881809746E+004,  0.11492451187014933E+004,  0.11425923098885792E+004,  0.11381101045776916E+004,  0.11334911621656809E+004,  0.11277602392365507E+004,  0.11222474376691307E+004,  0.11190338166421093E+004,  0.11155589000377099E+004,  0.11182398920685271E+004,  0.11222468936464629E+004,  0.11270775576872959E+004,  0.11285400875450332E+004,  0.10965477416757381E+004,  0.10982918050038738E+004,  0.10734357332952613E+004,  0.10713829238180615E+004,  0.10715136948133786E+004,  0.10507381603115189E+004,  0.10600282789570542E+004,  0.11048937722155376E+004,  0.11305218180882121E+004,  0.11457186753511612E+004,  0.11525091578910483E+004,  0.11515491562077100E+004,  0.11498199593747697E+004,  0.11497189643928746E+004,  0.11497503910318801E+004,  0.11493922972826867E+004,  0.11484069050196570E+004,  0.11461202171934883E+004,  0.11454765631608354E+004,  0.11448184141329766E+004,  0.11437216091792873E+004,  0.11339544455265989E+004,  0.11295436018770004E+004,  0.11320937419688028E+004,  0.11394650994687606E+004,  0.11141330402569679E+004,  0.10696289518045612E+004,  0.10307866290075087E+004,],]
input.sig_part=[[  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.86284774056742519E-002,  0.60390662267657182E-002,  0.41592311394521046E-002,  0.28257220491055089E-002,  0.19352013819746619E-002,  0.13176176380916185E-002,  0.89124728186244968E-003,  0.52972396569933328E-003,  0.33156482465323498E-003,  0.23050418719002994E-003,  0.17263842944260574E-003,  0.12864390239680963E-003,  0.99819853078647003E-004,  0.80798726866735551E-004,  0.68982541305143244E-004,  0.58985058477198783E-004,  0.50207892152341399E-004,  0.46373229546509423E-004,  0.45306721519148731E-004,  0.40042302270384470E-004,  0.34269364567262846E-004,  0.29907680299458836E-004,  0.27121690521350969E-004,  0.24819217184338365E-004,  0.22629406379639009E-004,  0.20694434827671498E-004,  0.19007045909407724E-004,  0.17541983868179683E-004,  0.16399617951647460E-004,  0.15114963740865167E-004,  0.14055571846014836E-004,  0.13087831566532364E-004,  0.12101289560477197E-004,  0.11313843476181731E-004,  0.10669791634090268E-004,  0.10071422070617596E-004,  0.94947424715105740E-005,  0.89036427932824189E-005,  0.82995681623160598E-005,  0.76696244264886047E-005,  0.68736191371748081E-005,  0.64532556640685163E-005,  0.61972856699648547E-005,  0.60056154354786972E-005,  0.63243172399778217E-005,  0.62636917631728376E-005,  0.66257123269691556E-005,  0.64030219253949132E-005,  0.63801090824819167E-005,  0.72333598093978559E-005,  0.66845146653116245E-005,  0.52569180446309881E-005,  0.47449802750913915E-005,  0.44744132742180419E-005,  0.43066026115515614E-005,  0.42077170200287795E-005,  0.41399798446615788E-005,  0.40828004819919921E-005,  0.40314811224745250E-005,  0.39811215302092221E-005,  0.39299357981394351E-005,  0.38871515412379173E-005,  0.38450061580984880E-005,  0.38154933341724397E-005,  0.37880831277445247E-005,  0.38445653957221874E-005,  0.38711803944751915E-005,  0.38313223727205492E-005,  0.37527106112225089E-005,  0.40336223470061288E-005,  0.49431310147011648E-005,  0.72060819838331703E-005,],]
