# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1383 ] 
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
input.tair=[[  0.25510328965988165E+003,  0.26686810170356648E+003,  0.26463392351803714E+003,  0.26597114087528786E+003,  0.26952527592395001E+003,  0.27169224066457485E+003,  0.26735578263082698E+003,  0.25924406973390296E+003,  0.24821786483051022E+003,  0.24120475397828366E+003,  0.23772323309034653E+003,  0.23733304418918746E+003,  0.23475163538327706E+003,  0.22998135870514304E+003,  0.22155413713624301E+003,  0.21377410019496250E+003,  0.20923972292649043E+003,  0.20609893763697860E+003,  0.20163335709674442E+003,  0.19699844701918718E+003,  0.19227212364025422E+003,  0.18958183324837887E+003,  0.18872653726566685E+003,  0.18867922187673889E+003,  0.18896037439740633E+003,  0.18940876330628836E+003,  0.18757911704747528E+003,  0.18828191300349857E+003,  0.19150617381618434E+003,  0.19498043524885517E+003,  0.19901269143825118E+003,  0.20348303201996853E+003,  0.20799894299938396E+003,  0.21260393143144444E+003,  0.21707556035929946E+003,  0.22153443110984989E+003,  0.22595303051464646E+003,  0.23062201553724896E+003,  0.23548646494913200E+003,  0.24020364273073929E+003,  0.24466950683302633E+003,  0.24858442523100248E+003,  0.25260245450856399E+003,  0.25682656297867084E+003,  0.26146687508476452E+003,  0.26578159564733716E+003,  0.26815549560883528E+003,  0.27041943031946249E+003,  0.27145154868262676E+003,  0.27311217462476895E+003,  0.27549627099659688E+003,  0.27826849230061111E+003,  0.28114492094654963E+003,  0.28377601660506656E+003,  0.28593930565832670E+003,  0.28749146148679824E+003,  0.28868767127337389E+003,  0.28965416748368057E+003,  0.29052800903473280E+003,  0.29137573029138508E+003,  0.29216184848156837E+003,  0.29284155680861744E+003,  0.29349502646539270E+003,  0.29396006862131361E+003,  0.29447299050579630E+003,  0.29516038302699707E+003,  0.29590975220214528E+003,  0.29663809489533509E+003,  0.29721681019487647E+003,  0.29731067909318972E+003,  0.29738982202367316E+003,  0.29756333070907738E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472306995733034E+005,  0.19913890085790783E+005,  0.21456052840999764E+005,  0.23129277489646869E+005,  0.24944702549505993E+005,  0.26914413161002241E+005,  0.29051521234837965E+005,  0.31370252622929675E+005,  0.33886042638394036E+005,  0.36615639349272729E+005,  0.39577213744620029E+005,  0.42790480031634688E+005,  0.46227676825454160E+005,  0.49764018436689308E+005,  0.53283605444302739E+005,  0.56715937145799384E+005,  0.60027052321306794E+005,  0.63202918014267030E+005,  0.66200798890412741E+005,  0.68978722036791252E+005,  0.71496442620244925E+005,  0.73716412065163808E+005,  0.75604708570600706E+005,  0.77159897751426091E+005,  0.78474918701208138E+005,  0.79695064638526688E+005,  0.80886234952331652E+005,  0.82046517395822040E+005,  0.83174029157575031E+005,  0.84266925278142051E+005,  0.85323400105404580E+005,  0.86341686965950546E+005,  0.87320062742364535E+005,  0.88256859551469592E+005,  0.89150476180417943E+005,  0.89999374596983253E+005,  0.90806928651687413E+005,  0.91499346672900312E+005,  0.91935730652379425E+005,],]
input.radius_part=[[  0.21833246906473015E-007,  0.22433166062522575E-007,  0.26478792811957116E-007,  0.29640218002107642E-007,  0.30824561241801386E-007,  0.35172937823295467E-007,  0.40093833030451024E-007,  0.42807748179739744E-007,  0.44843507854190686E-007,  0.46431557050996005E-007,  0.48084066293661423E-007,  0.49784940703340147E-007,  0.51145891458134480E-007,  0.52318734415656439E-007,  0.55048614176602930E-007,  0.59923307545308180E-007,  0.64394417352835880E-007,  0.66895132582458004E-007,  0.68037863232542979E-007,  0.69212829122087558E-007,  0.69498503084920045E-007,  0.69638539410090036E-007,  0.69642718908126078E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69630259480316248E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642719516516863E-007,  0.69642719860901957E-007,  0.69642720595905400E-007,  0.69642720447228354E-007,  0.69642720699399274E-007,  0.69642722558863386E-007,  0.69642722311383123E-007,  0.69642720654018438E-007,  0.69642719724316597E-007,  0.69642719307053411E-007,  0.69642719175294405E-007,  0.69642719182319842E-007,  0.69642719189211553E-007,  0.69642719185663266E-007,  0.69642719180272365E-007,  0.69642719169682798E-007,  0.69642719170774955E-007,  0.69642719173448786E-007,  0.69642719219337326E-007,  0.69642719398261746E-007,  0.69642719666398920E-007,  0.69642719724295104E-007,  0.69642719653346936E-007,  0.69642719545653566E-007,  0.69642719459176822E-007,  0.69642719522622356E-007,  0.69642719683110416E-007,  0.69642719810377924E-007,],]
input.density_part=[[  0.10461975184793453E+004,  0.10463273836066423E+004,  0.10464498890236187E+004,  0.10462838026982888E+004,  0.10451776706293369E+004,  0.10451238341814360E+004,  0.10452840262313648E+004,  0.10448919814407679E+004,  0.10445441477552627E+004,  0.10446534924448874E+004,  0.10437297388132235E+004,  0.10421239897661162E+004,  0.10404731316334478E+004,  0.10368343815185099E+004,  0.10333749842137092E+004,  0.10389445619845185E+004,  0.10505568731571893E+004,  0.10665229375609806E+004,  0.10676443475626525E+004,  0.10623709955786726E+004,  0.10578163516399850E+004,  0.10561534098995648E+004,  0.10558536005619305E+004,  0.10579940786181546E+004,  0.10590802418064941E+004,  0.10592067155426662E+004,  0.10628808543891191E+004,  0.10644603303454344E+004,  0.10635718609197995E+004,  0.10625042810353359E+004,  0.10622203572429310E+004,  0.10609175467216915E+004,  0.10589255064314034E+004,  0.10585232865561297E+004,  0.10584868136452260E+004,  0.10577860130821998E+004,  0.10568647761874370E+004,  0.10565435390527043E+004,  0.10564603744959347E+004,  0.10560460301047256E+004,  0.10571244806682955E+004,  0.10567482568684004E+004,  0.10556685503587319E+004,  0.10552998124623562E+004,  0.10550019038787564E+004,  0.10544426241071669E+004,  0.10532233665809536E+004,  0.10505080185972847E+004,  0.10479374373705443E+004,  0.10447108616104995E+004,  0.10439111223705925E+004,  0.10436631493793609E+004,  0.10437306800066578E+004,  0.10438041852592803E+004,  0.10437236073068982E+004,  0.10436326013716719E+004,  0.10439234961244219E+004,  0.10441297075114255E+004,  0.10442064210723333E+004,  0.10442650144447139E+004,  0.10445113082555836E+004,  0.10449213505755749E+004,  0.10470183174707431E+004,  0.10506901395870179E+004,  0.10553816134413457E+004,  0.10582023825274182E+004,  0.10594181575151049E+004,  0.10602973463184505E+004,  0.10607373677120588E+004,  0.10618433536342384E+004,  0.10623143216103629E+004,  0.10624048020420582E+004,],]
input.sig_part=[[  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.48945426855763717E-002,  0.34841514090475545E-002,  0.27739903800772991E-002,  0.21081138577933116E-002,  0.14931997623858289E-002,  0.11586492996257041E-002,  0.88763159580540745E-003,  0.63198009524642780E-003,  0.43878331806485764E-003,  0.30355240216193240E-003,  0.21595085712300261E-003,  0.15911599302271000E-003,  0.11871302869483039E-003,  0.89828042444888243E-004,  0.71150587098680714E-004,  0.60427153650850990E-004,  0.52651195052991575E-004,  0.45687400700402056E-004,  0.38943217987918491E-004,  0.33671372809142156E-004,  0.29318924407465572E-004,  0.26168677816977124E-004,  0.23887695623406703E-004,  0.22148933054812763E-004,  0.20584759220451445E-004,  0.19127093754424375E-004,  0.17772789060921046E-004,  0.16570907319943917E-004,  0.15493331862431055E-004,  0.14494232947692820E-004,  0.13586096359812994E-004,  0.12734622013338408E-004,  0.11932477333673915E-004,  0.11229398783454609E-004,  0.10603826324355774E-004,  0.10013940192591662E-004,  0.94533385371366909E-005,  0.89312616817377104E-005,  0.84416097057475656E-005,  0.79756268318639405E-005,  0.75455181886359654E-005,  0.71275661643743342E-005,  0.67315906768626401E-005,  0.63657700262637911E-005,  0.60247721389517735E-005,  0.57071173198680612E-005,  0.54163606740343122E-005,  0.51571467003991564E-005,  0.49334318572869061E-005,  0.47389329019794618E-005,  0.45814115212561119E-005,  0.44483401053159996E-005,  0.43360406780020880E-005,  0.42413192033792072E-005,  0.41621933567312874E-005,  0.40982332007733743E-005,  0.40491991494137463E-005,  0.40090401205852548E-005,  0.39724784781274833E-005,  0.39377342182415982E-005,  0.39055346709382566E-005,  0.38757453595246199E-005,  0.38538702933979634E-005,  0.38394161001459433E-005,  0.38300735080012943E-005,  0.38152188725376416E-005,  0.37959689048687179E-005,  0.37769714099413623E-005,  0.37579537856534917E-005,  0.37429830746926656E-005,  0.37287171069347008E-005,  0.37190143370404409E-005,],]