# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1408 ] 
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
input.tair=[[  0.25464290538607142E+003,  0.26922448325197570E+003,  0.27502108171299699E+003,  0.27607716909929991E+003,  0.27250566764625347E+003,  0.26798938248513730E+003,  0.26474504405723610E+003,  0.25910417133189543E+003,  0.25035211088870707E+003,  0.24207365450588458E+003,  0.23615314766504372E+003,  0.23403038149285652E+003,  0.23236901536518707E+003,  0.22997554731546683E+003,  0.22477121047552438E+003,  0.21806522007814900E+003,  0.21092594972933009E+003,  0.20482436991241110E+003,  0.19932676770121552E+003,  0.19467059727969561E+003,  0.19010639623091208E+003,  0.18770951752088550E+003,  0.18744853558639622E+003,  0.18829009131033175E+003,  0.18968147254989009E+003,  0.19201113108478648E+003,  0.19250578303123217E+003,  0.18951413479131284E+003,  0.19096317190184936E+003,  0.19534411211728246E+003,  0.19902435514990231E+003,  0.20316971218886795E+003,  0.20772362556973323E+003,  0.21230821662618345E+003,  0.21674050331223842E+003,  0.22137888797208441E+003,  0.22615351646741053E+003,  0.23091635516538767E+003,  0.23559403628707901E+003,  0.24019823131810182E+003,  0.24462072957506399E+003,  0.24883032989574724E+003,  0.25293776183398208E+003,  0.25699130483627420E+003,  0.26101961952621701E+003,  0.26526995616736781E+003,  0.26770652587811793E+003,  0.26962864620116653E+003,  0.27141666064238956E+003,  0.27344679132791578E+003,  0.27540210799430503E+003,  0.27867029051427210E+003,  0.28138097500807214E+003,  0.28388149217476246E+003,  0.28608741189962268E+003,  0.28792579927294332E+003,  0.28932278535866743E+003,  0.29037792833448327E+003,  0.29126643813713878E+003,  0.29213211720197182E+003,  0.29291196685905567E+003,  0.29360532870020177E+003,  0.29420630028400620E+003,  0.29472717716344641E+003,  0.29491925415905746E+003,  0.29519109401410742E+003,  0.29574086849557176E+003,  0.29636749798147343E+003,  0.29695721033273668E+003,  0.29730725445066599E+003,  0.29683140620759536E+003,  0.29650034957011866E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472666521875730E+005,  0.19915147498488572E+005,  0.21458432727613603E+005,  0.23132875244871673E+005,  0.24949621674928825E+005,  0.26920765954451756E+005,  0.29059429537579035E+005,  0.31379848630214477E+005,  0.33897469780894535E+005,  0.36629053248271426E+005,  0.39592783246571846E+005,  0.42808388331801063E+005,  0.46248086913453641E+005,  0.49787002476442838E+005,  0.53309151240817293E+005,  0.56743981189325612E+005,  0.60057506383535154E+005,  0.63235683652503765E+005,  0.66235746557073464E+005,  0.69015691634430957E+005,  0.71535244758933317E+005,  0.73756830024593102E+005,  0.75646500940288301E+005,  0.77202822076798373E+005,  0.78518800173877898E+005,  0.79739834202593222E+005,  0.80931871517763080E+005,  0.82092998480943337E+005,  0.83221330910071265E+005,  0.84315022503201079E+005,  0.85372266293489520E+005,  0.86391294321127629E+005,  0.87370382215087171E+005,  0.88307860878719279E+005,  0.89202127933156968E+005,  0.90051644226186851E+005,  0.90859749725067217E+005,  0.91552591906581598E+005,  0.91989229826310650E+005,],]
input.radius_part=[[  0.20686480766155457E-007,  0.21634483169277813E-007,  0.24050319216319459E-007,  0.27127366230720922E-007,  0.30837630019640208E-007,  0.35695066821044968E-007,  0.40332978152286830E-007,  0.42905172271071422E-007,  0.44488355835444761E-007,  0.46480517265793399E-007,  0.48215934906262320E-007,  0.49870440006359799E-007,  0.51173219163237739E-007,  0.52322634526363929E-007,  0.54585825355503153E-007,  0.59298297558745196E-007,  0.64851419182591902E-007,  0.67151523728276276E-007,  0.68182577873766177E-007,  0.69256806973075586E-007,  0.69561659196919138E-007,  0.69642719469155267E-007,  0.69642719638282230E-007,  0.69642718983781103E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69541144543376698E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718859952032E-007,  0.69642719410970629E-007,  0.69642719462751023E-007,  0.69642720062017794E-007,  0.69642720247360197E-007,  0.69642719762983850E-007,  0.69642720565789845E-007,  0.69642721596386016E-007,  0.69642720338032665E-007,  0.69642719775575206E-007,  0.69642719446512224E-007,  0.69642719262403392E-007,  0.69642719153207571E-007,  0.69642719099453470E-007,  0.69642719075842850E-007,  0.69642719068698022E-007,  0.69642719063924488E-007,  0.69642719069438315E-007,  0.69642719076581344E-007,  0.69642719091990938E-007,  0.69642719134701264E-007,  0.69642719283774417E-007,  0.69642719499310593E-007,  0.69642719540125127E-007,  0.69642719500630853E-007,  0.69642719439133415E-007,  0.69642719399286246E-007,  0.69642719452267985E-007,  0.69642719387604497E-007,],]
input.density_part=[[  0.10469509352576040E+004,  0.10465647543810635E+004,  0.10464271835671784E+004,  0.10464569296513478E+004,  0.10458839712043077E+004,  0.10452445299770532E+004,  0.10452871146768034E+004,  0.10449956697935861E+004,  0.10446334744747983E+004,  0.10446656441789535E+004,  0.10436885157394047E+004,  0.10421449842796385E+004,  0.10403299810681845E+004,  0.10367300731081486E+004,  0.10326692678244433E+004,  0.10366222849614917E+004,  0.10523903554023386E+004,  0.10678239520976545E+004,  0.10679641819839474E+004,  0.10633151935067269E+004,  0.10572138635756278E+004,  0.10566653132800373E+004,  0.10571550800675329E+004,  0.10583794146526557E+004,  0.10583107110600918E+004,  0.10584129066982639E+004,  0.10593444809992839E+004,  0.10647851478340983E+004,  0.10659133556466793E+004,  0.10653572021854213E+004,  0.10632874524296947E+004,  0.10620972130614441E+004,  0.10592375094275608E+004,  0.10579772845477196E+004,  0.10585234581043137E+004,  0.10584376425058867E+004,  0.10581038087550480E+004,  0.10580526583336493E+004,  0.10579145948057082E+004,  0.10579860652364534E+004,  0.10584413949157392E+004,  0.10592511480714702E+004,  0.10602010852088797E+004,  0.10607688337593120E+004,  0.10585463836026722E+004,  0.10595675532537773E+004,  0.10549894489939320E+004,  0.10491071624619938E+004,  0.10451887956492360E+004,  0.10439165257843565E+004,  0.10435071290361636E+004,  0.10432894705382430E+004,  0.10430916458319339E+004,  0.10429190083455019E+004,  0.10427711542176471E+004,  0.10427562774787243E+004,  0.10427604028611195E+004,  0.10429887050708412E+004,  0.10434672417647512E+004,  0.10439477364159825E+004,  0.10443933313735645E+004,  0.10444992400443200E+004,  0.10458339471463489E+004,  0.10489712136566789E+004,  0.10541713501100380E+004,  0.10598684352719599E+004,  0.10623498890715193E+004,  0.10634437011689315E+004,  0.10635567817528847E+004,  0.10634350536335508E+004,  0.10643538907715031E+004,  0.10662286858216150E+004,],]
input.sig_part=[[  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.46366072425686805E-002,  0.33756682706161415E-002,  0.25684728987825011E-002,  0.19660059601196707E-002,  0.15030815390030350E-002,  0.11679529526919287E-002,  0.88856516052473740E-003,  0.63331157823824061E-003,  0.43720378821977341E-003,  0.30442085624859261E-003,  0.21582507716153348E-003,  0.15829243098856491E-003,  0.11816542243283069E-003,  0.89824643587838648E-004,  0.70991779786377083E-004,  0.60221727650925481E-004,  0.53326187085492393E-004,  0.45793446581994136E-004,  0.38840601534847813E-004,  0.33550032029139380E-004,  0.29190771496129456E-004,  0.26076977604393578E-004,  0.23852408751936786E-004,  0.22139169076340947E-004,  0.20599674908537654E-004,  0.19213765518406952E-004,  0.17850957815906361E-004,  0.16613395065226530E-004,  0.15512659377782850E-004,  0.14542000129300009E-004,  0.13599997611824038E-004,  0.12742736907218220E-004,  0.11931280883210420E-004,  0.11218915199415975E-004,  0.10599064777600216E-004,  0.10017294165253909E-004,  0.94653840428572181E-005,  0.89454119914632651E-005,  0.84525395859529009E-005,  0.79885148643667733E-005,  0.75527960620576154E-005,  0.71439689251390696E-005,  0.67602210335551730E-005,  0.63975534824488207E-005,  0.60416698621896365E-005,  0.57316412994934876E-005,  0.54227268972644007E-005,  0.51472890541055532E-005,  0.49188267172616634E-005,  0.47340383528846049E-005,  0.45780645463565147E-005,  0.44453999314125708E-005,  0.43319779244389301E-005,  0.42363093101100674E-005,  0.41569934705756999E-005,  0.40933493077330482E-005,  0.40431815229354549E-005,  0.40031014129262003E-005,  0.39680760572838069E-005,  0.39349138590859321E-005,  0.39034465718981737E-005,  0.38725010146002646E-005,  0.38478358345454460E-005,  0.38313983147648850E-005,  0.38241255433924689E-005,  0.38199506058848472E-005,  0.38053537229846361E-005,  0.37871514327517472E-005,  0.37669217634486345E-005,  0.37473766681352114E-005,  0.37351595864166631E-005,  0.37321626849382853E-005,],]
