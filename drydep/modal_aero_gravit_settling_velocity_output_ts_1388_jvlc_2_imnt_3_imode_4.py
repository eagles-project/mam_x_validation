# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1388 ] 
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
input.tair=[[  0.25318555702947307E+003,  0.26346079788871816E+003,  0.26529643429967541E+003,  0.26292479014276523E+003,  0.26492640909518741E+003,  0.26713115839323200E+003,  0.26485881969255104E+003,  0.25900640611258183E+003,  0.24845116962080573E+003,  0.24013513139192264E+003,  0.23594691863020864E+003,  0.23594636462882659E+003,  0.23463235118128634E+003,  0.23144822552072054E+003,  0.22409302469104605E+003,  0.21584898464029027E+003,  0.21006226543087715E+003,  0.20621513088826612E+003,  0.20163419510415102E+003,  0.19707692185778032E+003,  0.19217872352382344E+003,  0.18919155308225154E+003,  0.18824305259886270E+003,  0.18830309539303519E+003,  0.18856745625607249E+003,  0.18882372743518872E+003,  0.18677022669794331E+003,  0.18802740712788696E+003,  0.19133491326552118E+003,  0.19508481040438991E+003,  0.19931069308333494E+003,  0.20356419510073565E+003,  0.20797316901158115E+003,  0.21234598132945283E+003,  0.21671629644385445E+003,  0.22123631674532294E+003,  0.22591525220990704E+003,  0.23056996296996400E+003,  0.23522079389933967E+003,  0.23981163827495016E+003,  0.24436980846980933E+003,  0.24832677064235551E+003,  0.25248433644059165E+003,  0.25699120611339583E+003,  0.26181887248847448E+003,  0.26560568647660449E+003,  0.26788029057956095E+003,  0.27029536335129626E+003,  0.27139606423566437E+003,  0.27323284748095642E+003,  0.27539166126815752E+003,  0.27896232078256816E+003,  0.28163368925804457E+003,  0.28400938856411244E+003,  0.28605002823956028E+003,  0.28762899756631799E+003,  0.28884375073724908E+003,  0.28980636897875530E+003,  0.29064696927919255E+003,  0.29143228080267903E+003,  0.29221728640491938E+003,  0.29291127763945178E+003,  0.29350138516001482E+003,  0.29401248929861526E+003,  0.29447215408416588E+003,  0.29492384586096699E+003,  0.29543429129897328E+003,  0.29595523959982518E+003,  0.29644876242257982E+003,  0.29494377899669843E+003,  0.29386300564920026E+003,  0.29372011965820894E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18474134462859154E+005,  0.19920281499644407E+005,  0.21468149776477287E+005,  0.23147564836852936E+005,  0.24969706405782075E+005,  0.26946704334881644E+005,  0.29091719044027304E+005,  0.31419029014330416E+005,  0.33944126668413403E+005,  0.36683822039046914E+005,  0.39656353338680070E+005,  0.42881507709325233E+005,  0.46331421061076311E+005,  0.49880846038598727E+005,  0.53413454425494238E+005,  0.56858484686969066E+005,  0.60181849959001971E+005,  0.63369465365441021E+005,  0.66378437466228163E+005,  0.69166638063830789E+005,  0.71693673431735500E+005,  0.73921856074347234E+005,  0.75817138690852415E+005,  0.77378081589019392E+005,  0.78697967707180782E+005,  0.79922627802553063E+005,  0.81118205074029494E+005,  0.82282780201103407E+005,  0.83414463405405564E+005,  0.84511402903589886E+005,  0.85571786360807746E+005,  0.86593840564906772E+005,  0.87575836026372548E+005,  0.88516098693964625E+005,  0.89413021427973537E+005,  0.90265060503291883E+005,  0.91075417542213938E+005,  0.91769991565216711E+005,  0.92207666319979267E+005,],]
input.radius_part=[[  0.21758038061490874E-007,  0.22427040849038145E-007,  0.25931699603934035E-007,  0.29240259026343045E-007,  0.31076965340382122E-007,  0.35437873966325513E-007,  0.40120766413816111E-007,  0.42618838150743423E-007,  0.44696780719937899E-007,  0.46432755244133769E-007,  0.48149627538965352E-007,  0.49777621449172406E-007,  0.51064229139237456E-007,  0.52190830357550930E-007,  0.54772058701654169E-007,  0.59571528026996999E-007,  0.64294429408002418E-007,  0.66856316194612974E-007,  0.67993953677075239E-007,  0.69199553400264523E-007,  0.69502063013188938E-007,  0.69642718844414656E-007,  0.69642719129925507E-007,  0.69642718866042808E-007,  0.69642718832189588E-007,  0.69601493785545731E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642719654629463E-007,  0.69642719836615603E-007,  0.69642720356033227E-007,  0.69642720179954625E-007,  0.69642720777363270E-007,  0.69642722783765920E-007,  0.69642722440716796E-007,  0.69642720088645373E-007,  0.69642719528049720E-007,  0.69642719272596375E-007,  0.69642719159327159E-007,  0.69642719155264590E-007,  0.69642719173012101E-007,  0.69642719178618930E-007,  0.69642719185970607E-007,  0.69642719188029572E-007,  0.69642719174466311E-007,  0.69642719182712309E-007,  0.69642719206243917E-007,  0.69642719279307655E-007,  0.69642719426021954E-007,  0.69642719665745950E-007,  0.69642719826437616E-007,  0.69642719843166993E-007,  0.69642719650367828E-007,  0.69642719990219430E-007,  0.69642720897789015E-007,  0.69642721560341654E-007,],]
input.density_part=[[  0.10464944694716296E+004,  0.10463835506154117E+004,  0.10464888429926268E+004,  0.10462512397632959E+004,  0.10451735889975464E+004,  0.10451505704329682E+004,  0.10453133080369294E+004,  0.10449781689918284E+004,  0.10445759263611103E+004,  0.10446888840656650E+004,  0.10436846538574437E+004,  0.10421572591256356E+004,  0.10406520878496447E+004,  0.10370737556898350E+004,  0.10334155800071724E+004,  0.10379739409392967E+004,  0.10501878255120048E+004,  0.10663328664277537E+004,  0.10681124007344354E+004,  0.10626792009818546E+004,  0.10575965697793902E+004,  0.10564529237557297E+004,  0.10564358758384865E+004,  0.10581326174660073E+004,  0.10591111459652311E+004,  0.10592586644778155E+004,  0.10634488371044947E+004,  0.10645044511981348E+004,  0.10637878816961763E+004,  0.10633637865201761E+004,  0.10621080891353392E+004,  0.10614835960167168E+004,  0.10612859702067703E+004,  0.10605766913275816E+004,  0.10596285998606711E+004,  0.10598938283284660E+004,  0.10595619575078656E+004,  0.10582365354144733E+004,  0.10575621145346186E+004,  0.10574328849499136E+004,  0.10567029089735422E+004,  0.10572430539139154E+004,  0.10570909114911262E+004,  0.10569723275088265E+004,  0.10568793398181122E+004,  0.10575789365478179E+004,  0.10559468574749308E+004,  0.10496089026651694E+004,  0.10474460558299636E+004,  0.10448295007787021E+004,  0.10437376736324361E+004,  0.10432995736174173E+004,  0.10433081180581626E+004,  0.10433399202753728E+004,  0.10436141817094547E+004,  0.10434513893593860E+004,  0.10438159106500511E+004,  0.10442743738907764E+004,  0.10444364917819310E+004,  0.10445704873674886E+004,  0.10449898063213996E+004,  0.10451778468155487E+004,  0.10456994537553087E+004,  0.10476337747715197E+004,  0.10504393526648594E+004,  0.10536585715751626E+004,  0.10575468647620107E+004,  0.10595100264021451E+004,  0.10597964318505808E+004,  0.10614108123030926E+004,  0.10636977364424565E+004,  0.10639131591483010E+004,],]
input.sig_part=[[  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.48606939634240681E-002,  0.34610800366819579E-002,  0.27201713619650282E-002,  0.20676591226372098E-002,  0.14925288735580127E-002,  0.11575744200099530E-002,  0.88409987721506681E-003,  0.62895320845809694E-003,  0.43756423305491525E-003,  0.30289987161141025E-003,  0.21543322199754059E-003,  0.15863703218613187E-003,  0.11851313613661303E-003,  0.89906707396631075E-004,  0.71183829439832504E-004,  0.60287703945105739E-004,  0.52645704527670532E-004,  0.45663750994978762E-004,  0.38934261763083869E-004,  0.33680212526219601E-004,  0.29308410462574833E-004,  0.26155689112125696E-004,  0.23876406643022985E-004,  0.22134602366892865E-004,  0.20569065018046993E-004,  0.19097506009638352E-004,  0.17754931510448725E-004,  0.16563867201343620E-004,  0.15491825351067690E-004,  0.14508492522114033E-004,  0.13591113378826348E-004,  0.12742982015340699E-004,  0.11958634075966893E-004,  0.11246301687719937E-004,  0.10607512202607129E-004,  0.10025575840636062E-004,  0.94709102290969132E-005,  0.89378023340440427E-005,  0.84400422096936130E-005,  0.79744515358506325E-005,  0.75314242893823201E-005,  0.71200829539597232E-005,  0.67306201946185608E-005,  0.63670572539170989E-005,  0.60273143840756396E-005,  0.57144373618928754E-005,  0.54208823293910580E-005,  0.51439648040278539E-005,  0.49227999653255617E-005,  0.47316027017854089E-005,  0.45728704968701735E-005,  0.44394998593127475E-005,  0.43270219953239525E-005,  0.42322525766607340E-005,  0.41546953684640880E-005,  0.40905614368527180E-005,  0.40418982985653926E-005,  0.40027794520349465E-005,  0.39666130664533888E-005,  0.39322351418221468E-005,  0.39007348124232999E-005,  0.38701611814417068E-005,  0.38425733280551961E-005,  0.38218249971517421E-005,  0.38057897143011094E-005,  0.37926926770313929E-005,  0.37833352410482861E-005,  0.37684511374663155E-005,  0.37490370288575955E-005,  0.37373875103259995E-005,  0.37307550805722792E-005,  0.37218886805592564E-005,],]