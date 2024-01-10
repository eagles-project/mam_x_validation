# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1381 ] 
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
input.tair=[[  0.25460309442606984E+003,  0.26232594349041563E+003,  0.25907252914908048E+003,  0.26401720675566264E+003,  0.26801906997128464E+003,  0.27097968314326658E+003,  0.26780938843155076E+003,  0.26041625487648383E+003,  0.24990975553101219E+003,  0.24272154267136011E+003,  0.23856286947219155E+003,  0.23720510017043335E+003,  0.23358277872897611E+003,  0.22808561869160343E+003,  0.21968433703091077E+003,  0.21274622235304736E+003,  0.20910651340284969E+003,  0.20643184786656187E+003,  0.20214574979914110E+003,  0.19755636841761850E+003,  0.19287401577962646E+003,  0.19014369715804796E+003,  0.18919299881755478E+003,  0.18907721253350772E+003,  0.18931462030161984E+003,  0.18983378632016283E+003,  0.18807666077983569E+003,  0.18846085109538529E+003,  0.19162142395048443E+003,  0.19512588868394639E+003,  0.19885635541061541E+003,  0.20325299907828347E+003,  0.20790046618354498E+003,  0.21253485142348367E+003,  0.21708915805088449E+003,  0.22167334120106679E+003,  0.22611550729262018E+003,  0.23062039335797971E+003,  0.23552321601003933E+003,  0.24031622788587663E+003,  0.24472307681359473E+003,  0.24878009048525277E+003,  0.25279990351744769E+003,  0.25683467711955416E+003,  0.26132437713384627E+003,  0.26566208802118456E+003,  0.26803700254815436E+003,  0.27054247961892935E+003,  0.27120090883226209E+003,  0.27311297817101496E+003,  0.27526384739341097E+003,  0.27782472940477851E+003,  0.28090236919194541E+003,  0.28365238887345538E+003,  0.28585947070696864E+003,  0.28742844463226311E+003,  0.28858745858564924E+003,  0.28951837205702566E+003,  0.29038660907639797E+003,  0.29122837504858217E+003,  0.29198713852452653E+003,  0.29266045644050553E+003,  0.29327357037234464E+003,  0.29363992887012512E+003,  0.29423413042917593E+003,  0.29501277153643912E+003,  0.29584328239465862E+003,  0.29666259601138353E+003,  0.29745291963547322E+003,  0.29820927472611709E+003,  0.29885793412914222E+003,  0.29926108780163560E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472133993469968E+005,  0.19913285024804969E+005,  0.21454907650925546E+005,  0.23127546267012585E+005,  0.24942335489842189E+005,  0.26911356227130003E+005,  0.29047715797322453E+005,  0.31365635070046796E+005,  0.33880543951989341E+005,  0.36609184645128204E+005,  0.39569721774627833E+005,  0.42781862643109809E+005,  0.46217855588570448E+005,  0.49752958626512598E+005,  0.53271312929005457E+005,  0.56702442485969637E+005,  0.60012397971985833E+005,  0.63187151345609011E+005,  0.66183982240096637E+005,  0.68960932442943144E+005,  0.71477771216394875E+005,  0.73696963136089049E+005,  0.75584598281872706E+005,  0.77139242771027886E+005,  0.78453803146100952E+005,  0.79673521738080148E+005,  0.80864274854968404E+005,  0.82024150919616746E+005,  0.83151267780147755E+005,  0.84243781123116074E+005,  0.85299885929042473E+005,  0.86317816143522883E+005,  0.87295849252374435E+005,  0.88232317956337036E+005,  0.89125621603645806E+005,  0.89974222701006845E+005,  0.90781511403406650E+005,  0.91473725320707919E+005,  0.91909987105351378E+005,],]
input.radius_part=[[  0.21745972652797469E-007,  0.22837751938543537E-007,  0.27039856664840958E-007,  0.29868473014459483E-007,  0.30897419293299418E-007,  0.35166584999566097E-007,  0.40021123431704649E-007,  0.42755127930052313E-007,  0.44788715937364826E-007,  0.46361758560290355E-007,  0.48031161273414847E-007,  0.49815460530421959E-007,  0.51229960194440082E-007,  0.52397599689027148E-007,  0.55342547795612772E-007,  0.60053948576672709E-007,  0.64393840853206655E-007,  0.66872542840764307E-007,  0.67997274450048191E-007,  0.69189585193171716E-007,  0.69487468773289659E-007,  0.69630363499616880E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642719407870925E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642728682992063E-007,  0.69642718832189588E-007,  0.69642719445555977E-007,  0.69642719489347937E-007,  0.69642720391510633E-007,  0.69642720320732560E-007,  0.69642721138871440E-007,  0.69642721980451930E-007,  0.69642723271801409E-007,  0.69642721266776220E-007,  0.69642719844937729E-007,  0.69642719329277199E-007,  0.69642719181690787E-007,  0.69642719147049390E-007,  0.69642719148085986E-007,  0.69642719162495896E-007,  0.69642719171997832E-007,  0.69642719172574397E-007,  0.69642719212502352E-007,  0.69642719237704282E-007,  0.69642719293999826E-007,  0.69642719624601589E-007,  0.69642719883071456E-007,  0.69642719855584655E-007,  0.69642719730094249E-007,  0.69642719602222343E-007,  0.69642719493023756E-007,  0.69642719405522764E-007,  0.69642719342501607E-007,  0.69642719303267544E-007,],]
input.density_part=[[  0.10459572114872747E+004,  0.10463785051597272E+004,  0.10464165179372883E+004,  0.10462657676541539E+004,  0.10451367944177828E+004,  0.10451224232175502E+004,  0.10452787785495693E+004,  0.10448854286561377E+004,  0.10445348767209152E+004,  0.10446556373040298E+004,  0.10437649468226452E+004,  0.10420703675349441E+004,  0.10402629823455279E+004,  0.10366554589457953E+004,  0.10333523623960218E+004,  0.10392787955754900E+004,  0.10504818402419187E+004,  0.10663824622546745E+004,  0.10675930119106338E+004,  0.10624935534751978E+004,  0.10580286536938913E+004,  0.10561378451680985E+004,  0.10556219746985466E+004,  0.10577743502427343E+004,  0.10590263784843182E+004,  0.10594413290714974E+004,  0.10626433593676625E+004,  0.10646479318968325E+004,  0.10637354924883471E+004,  0.10622790247674477E+004,  0.10619123325144205E+004,  0.10605577625618030E+004,  0.10597307069542223E+004,  0.10586739663148903E+004,  0.10585378582436058E+004,  0.10575633142164029E+004,  0.10568711771531850E+004,  0.10561955380778727E+004,  0.10560538482061181E+004,  0.10558372541071772E+004,  0.10570248846488253E+004,  0.10573097464492669E+004,  0.10559218292542030E+004,  0.10554489509142466E+004,  0.10550125255323480E+004,  0.10545664271188057E+004,  0.10538335133226715E+004,  0.10509303828200307E+004,  0.10484116551437721E+004,  0.10444969039309776E+004,  0.10437364369674226E+004,  0.10436981997407217E+004,  0.10439305758772698E+004,  0.10439648054483409E+004,  0.10438836022864427E+004,  0.10438457404379360E+004,  0.10441467293488754E+004,  0.10441793922454156E+004,  0.10442040328856701E+004,  0.10441555483224479E+004,  0.10442207297780303E+004,  0.10445757516584847E+004,  0.10476836286156088E+004,  0.10537767799400513E+004,  0.10576553206153385E+004,  0.10588545921350690E+004,  0.10593551191365577E+004,  0.10596681765535257E+004,  0.10598661267993550E+004,  0.10599888855815816E+004,  0.10600518758661356E+004,  0.10600755174160240E+004,],]
input.sig_part=[[  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.25097496337355965E-002,  0.18127389175753396E-002,  0.14446486699847196E-002,  0.10909025340971308E-002,  0.76925077004323737E-003,  0.59626727593196775E-003,  0.45699533743668431E-003,  0.32598008520454521E-003,  0.22653889180239764E-003,  0.15658703254065596E-003,  0.11124356228033649E-003,  0.81884725164474005E-004,  0.60961480986781174E-004,  0.45997836904718392E-004,  0.36513901003462988E-004,  0.30900255852721766E-004,  0.26825514454766803E-004,  0.23216184114717263E-004,  0.19720438088956646E-004,  0.16987192450015026E-004,  0.14731679728039462E-004,  0.13091033609899490E-004,  0.11904445430887341E-004,  0.11001089696824909E-004,  0.10191186788682513E-004,  0.94422247471987115E-005,  0.87286482674909289E-005,  0.81023971225920024E-005,  0.75489805539062043E-005,  0.70356130709592159E-005,  0.65674771607806531E-005,  0.61333821362032566E-005,  0.57336801642423923E-005,  0.53730601775452835E-005,  0.50553539130923722E-005,  0.47554472634096313E-005,  0.44715860756546981E-005,  0.42037253653455925E-005,  0.39552193008025493E-005,  0.37195111313219894E-005,  0.34998562098080351E-005,  0.32884538336843578E-005,  0.30847943246417018E-005,  0.28965063240745497E-005,  0.27216469458416736E-005,  0.25595325881105135E-005,  0.24094250007596177E-005,  0.22752677270579180E-005,  0.21570078743403258E-005,  0.20553038637919391E-005,  0.19737526102140078E-005,  0.19059300481797717E-005,  0.18497602673967016E-005,  0.18021116422979131E-005,  0.17621982742378250E-005,  0.17296693248370691E-005,  0.17044121451305962E-005,  0.16834021016141278E-005,  0.16645090272217502E-005,  0.16464792041516843E-005,  0.16295136025124579E-005,  0.16138519252892885E-005,  0.16032541885731675E-005,  0.15977417356062190E-005,  0.15898583273295320E-005,  0.15789238425777636E-005,  0.15678055341402856E-005,  0.15571950383427890E-005,  0.15471690323773467E-005,  0.15377063298693894E-005,  0.15296581485896859E-005,  0.15246167769410761E-005,],]
