# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1407 ] 
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
input.tair=[[  0.25477896837623877E+003,  0.26860601249891903E+003,  0.27400467048836009E+003,  0.27517864917334271E+003,  0.27295624456793695E+003,  0.26908798662533610E+003,  0.26584789639341676E+003,  0.26004785769689221E+003,  0.25094182594845006E+003,  0.24240807684352629E+003,  0.23627338900648212E+003,  0.23404243103915044E+003,  0.23234567173687194E+003,  0.22993897660641139E+003,  0.22463302421482223E+003,  0.21778596922408761E+003,  0.21061601584651328E+003,  0.20470733144953545E+003,  0.19937506175402771E+003,  0.19482732205955239E+003,  0.19038151928034114E+003,  0.18803184096886150E+003,  0.18773602212146236E+003,  0.18852908904211330E+003,  0.18983318316950948E+003,  0.19213596658539032E+003,  0.19255472436128315E+003,  0.18961958296666336E+003,  0.19099785932228468E+003,  0.19536506199346360E+003,  0.19906431060216212E+003,  0.20323332444807514E+003,  0.20778622394987534E+003,  0.21239951021525968E+003,  0.21677086333121861E+003,  0.22129626285625318E+003,  0.22606970282338722E+003,  0.23088014766713877E+003,  0.23566970607181776E+003,  0.24024102036377641E+003,  0.24478934469221036E+003,  0.24905952463095090E+003,  0.25311426743345260E+003,  0.25705960162861447E+003,  0.26101206369405458E+003,  0.26521700882055205E+003,  0.26768841368936785E+003,  0.26961218613870449E+003,  0.27131428386802924E+003,  0.27334496460451419E+003,  0.27537698124430568E+003,  0.27851238696170708E+003,  0.28126879412954361E+003,  0.28381177677033958E+003,  0.28605441773853897E+003,  0.28790134737231904E+003,  0.28928242241883771E+003,  0.29032067181710835E+003,  0.29120875791920440E+003,  0.29208223249489242E+003,  0.29286145894822920E+003,  0.29355002569512442E+003,  0.29415477279066840E+003,  0.29465368995805221E+003,  0.29478880867298068E+003,  0.29512834064072769E+003,  0.29575188433415673E+003,  0.29639498679444938E+003,  0.29697551318240016E+003,  0.29734625877408496E+003,  0.29755628612701025E+003,  0.29759020749642735E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472235836087180E+005,  0.19913641210864487E+005,  0.21455581799068455E+005,  0.23128565399600389E+005,  0.24943728925667761E+005,  0.26913155776688945E+005,  0.29049955974470155E+005,  0.31368353321602463E+005,  0.33883780907418499E+005,  0.36612984387118660E+005,  0.39574132132148974E+005,  0.42786935509703362E+005,  0.46223637134145523E+005,  0.49759469292872192E+005,  0.53278549261685861E+005,  0.56710386494626560E+005,  0.60021024664272707E+005,  0.63196432835760694E+005,  0.66193881831296196E+005,  0.68971404784544589E+005,  0.71488762660098757E+005,  0.73708412291746688E+005,  0.75596436765373874E+005,  0.77151401902503741E+005,  0.78466233407751381E+005,  0.79686203568508005E+005,  0.80877202280021083E+005,  0.82037317570932253E+005,  0.83164666901104269E+005,  0.84257405576803911E+005,  0.85313728206131156E+005,  0.86331868370285592E+005,  0.87310103199974619E+005,  0.88246765052199204E+005,  0.89140252944897307E+005,  0.89989029067517404E+005,  0.90796473976967231E+005,  0.91488808045740356E+005,  0.91925141763788924E+005,],]
input.radius_part=[[  0.20755988579182386E-007,  0.21715108281235642E-007,  0.24261096615276665E-007,  0.27298488392691016E-007,  0.30790072387320548E-007,  0.35593617445973092E-007,  0.40287446294200005E-007,  0.42870810008768723E-007,  0.44476547225730965E-007,  0.46473593839547104E-007,  0.48216413475112588E-007,  0.49885160628722108E-007,  0.51184570251038960E-007,  0.52343294284171138E-007,  0.54630963070981116E-007,  0.59453835002709772E-007,  0.64895504947234405E-007,  0.67149461581035266E-007,  0.68169513053688298E-007,  0.69249884577916529E-007,  0.69556492490965021E-007,  0.69642719286346830E-007,  0.69642719460984007E-007,  0.69642718907014096E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69543954837166253E-007,  0.69642718991944938E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718894623513E-007,  0.69642719400289027E-007,  0.69642719438318358E-007,  0.69642720089113055E-007,  0.69642720306288146E-007,  0.69642719772568901E-007,  0.69642720675307698E-007,  0.69642721779016484E-007,  0.69642720456761233E-007,  0.69642719796734063E-007,  0.69642719436807503E-007,  0.69642719244847589E-007,  0.69642719140226764E-007,  0.69642719096488564E-007,  0.69642719079957776E-007,  0.69642719076674226E-007,  0.69642719072446195E-007,  0.69642719079438373E-007,  0.69642719117833569E-007,  0.69642719135560778E-007,  0.69642719152273095E-007,  0.69642719341479040E-007,  0.69642719543993196E-007,  0.69642719543181500E-007,  0.69642719496891838E-007,  0.69642719438704711E-007,  0.69642719385688522E-007,  0.69642719426291522E-007,  0.69642719684416568E-007,],]
input.density_part=[[  0.10469594618660612E+004,  0.10465354845583201E+004,  0.10464261614303073E+004,  0.10464456877251027E+004,  0.10458453083580896E+004,  0.10452417092644814E+004,  0.10452854687474182E+004,  0.10449978134486837E+004,  0.10446352900791521E+004,  0.10446611578940108E+004,  0.10436824203261010E+004,  0.10421283588393758E+004,  0.10403165179587027E+004,  0.10366923160470612E+004,  0.10326605330068787E+004,  0.10370393544774993E+004,  0.10526060642445520E+004,  0.10678475831172732E+004,  0.10680555539634938E+004,  0.10634364387614667E+004,  0.10572384455890774E+004,  0.10566514085271374E+004,  0.10570589797187179E+004,  0.10583286003392700E+004,  0.10583160009288563E+004,  0.10583731310489497E+004,  0.10593835748122715E+004,  0.10643935100317603E+004,  0.10659918214884999E+004,  0.10655170875759552E+004,  0.10633266418288863E+004,  0.10621512202690765E+004,  0.10597857075105239E+004,  0.10578651762614272E+004,  0.10581529365086660E+004,  0.10584070172492391E+004,  0.10581614312450283E+004,  0.10580829339955865E+004,  0.10579175045912125E+004,  0.10579046321645085E+004,  0.10582088410612014E+004,  0.10589631794047320E+004,  0.10597618526992608E+004,  0.10611628939900338E+004,  0.10585690918214343E+004,  0.10588382356949160E+004,  0.10555318646038465E+004,  0.10490119126078062E+004,  0.10451079775278556E+004,  0.10438554331300063E+004,  0.10435855126041752E+004,  0.10434026445937859E+004,  0.10432873244378363E+004,  0.10430292739904730E+004,  0.10428442147815381E+004,  0.10427544868121447E+004,  0.10427048882002912E+004,  0.10429493518174525E+004,  0.10433780134918247E+004,  0.10438417163945376E+004,  0.10444040979571541E+004,  0.10445864165921371E+004,  0.10460801507986812E+004,  0.10491897092105517E+004,  0.10558139417176671E+004,  0.10607037213212407E+004,  0.10624699105198531E+004,  0.10631638114797934E+004,  0.10633051692031208E+004,  0.10637477713892358E+004,  0.10641657212944974E+004,  0.10642682650776526E+004,],]
input.sig_part=[[  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.23986155348210674E-002,  0.17443984720100050E-002,  0.13330250680498739E-002,  0.10180627370094848E-002,  0.77412937942429312E-003,  0.60146785087321645E-003,  0.45835316664618144E-003,  0.32666645626505854E-003,  0.22544408840714092E-003,  0.15686478007175594E-003,  0.11112926881129131E-003,  0.81458568603441070E-004,  0.60750198679764975E-004,  0.46135862235448131E-004,  0.36414532719555318E-004,  0.30874023268338817E-004,  0.27186106946073068E-004,  0.23252241500889772E-004,  0.19651123243701860E-004,  0.16907231161655294E-004,  0.14647707537094138E-004,  0.13033468905790538E-004,  0.11879298475111915E-004,  0.10992641212828200E-004,  0.10196632566732112E-004,  0.94824225705080668E-005,  0.87772888314451290E-005,  0.81214904592444684E-005,  0.75546994426444847E-005,  0.70606331396450713E-005,  0.65790319494358033E-005,  0.61423573731253381E-005,  0.57327212334132280E-005,  0.53675813667220639E-005,  0.50505501080767118E-005,  0.47559962265667958E-005,  0.44765225958202084E-005,  0.42127901486276463E-005,  0.39628632305581232E-005,  0.37261176019567004E-005,  0.35038405708191544E-005,  0.32945905943453664E-005,  0.30970201274321533E-005,  0.29127353593280306E-005,  0.27295138392922621E-005,  0.25683130992495603E-005,  0.24121235064616347E-005,  0.22686651098188733E-005,  0.21502036939829634E-005,  0.20542489677313774E-005,  0.19734336449535068E-005,  0.19062869526149613E-005,  0.18489566150360487E-005,  0.18005069405318879E-005,  0.17604941516272884E-005,  0.17282641667072777E-005,  0.17027195894053919E-005,  0.16821854861379457E-005,  0.16639563138541776E-005,  0.16467597269942374E-005,  0.16305733301343751E-005,  0.16146342462669165E-005,  0.16015348918961688E-005,  0.15916377615040236E-005,  0.15874564966778716E-005,  0.15816008444197880E-005,  0.15721320801552506E-005,  0.15618832313062813E-005,  0.15515499822985704E-005,  0.15421745011970817E-005,  0.15342262408918302E-005,  0.15289609583158509E-005,],]
