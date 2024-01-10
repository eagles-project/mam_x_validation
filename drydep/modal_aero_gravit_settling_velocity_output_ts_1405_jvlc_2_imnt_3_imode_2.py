# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1405 ] 
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
input.tair=[[  0.25384416891070546E+003,  0.26356632525125451E+003,  0.26845381240517162E+003,  0.27021433011023140E+003,  0.27069503286800062E+003,  0.26855836545796956E+003,  0.26611364909314426E+003,  0.26096252914582851E+003,  0.25200441826947772E+003,  0.24317420640652514E+003,  0.23642753042828500E+003,  0.23380741055017373E+003,  0.23194539804839442E+003,  0.22945682317454330E+003,  0.22394342131867992E+003,  0.21690879692933819E+003,  0.20990850819531613E+003,  0.20455147787471608E+003,  0.19961216288061877E+003,  0.19534831517876560E+003,  0.19116206336686074E+003,  0.18885204581830698E+003,  0.18842235163874540E+003,  0.18908301400097545E+003,  0.19016415131242027E+003,  0.19236966810367599E+003,  0.19262343575565754E+003,  0.18980852348935539E+003,  0.19111543742324292E+003,  0.19535759392744322E+003,  0.19905344808726545E+003,  0.20316300538844195E+003,  0.20776985209022337E+003,  0.21246773038825913E+003,  0.21697062587987011E+003,  0.22131055939871888E+003,  0.22592950719911912E+003,  0.23067318739873906E+003,  0.23551340279885918E+003,  0.24025514843062916E+003,  0.24488210785198146E+003,  0.24930432323388112E+003,  0.25351084136195743E+003,  0.25734766384739805E+003,  0.26113778464177011E+003,  0.26502330653098380E+003,  0.26760127883410399E+003,  0.26951204132226923E+003,  0.27104335639225917E+003,  0.27323134028071013E+003,  0.27524731125096389E+003,  0.27818376138548302E+003,  0.28105386028894020E+003,  0.28370576484256475E+003,  0.28596640482364137E+003,  0.28779736489682330E+003,  0.28912012734339220E+003,  0.29012523541416601E+003,  0.29102152801282534E+003,  0.29189770654268006E+003,  0.29265158828638766E+003,  0.29334745650342677E+003,  0.29392760893272219E+003,  0.29434314002211835E+003,  0.29436656288638329E+003,  0.29494058519816127E+003,  0.29574619218240605E+003,  0.29657039772439589E+003,  0.29737421962049115E+003,  0.29815143606393582E+003,  0.29883326574447437E+003,  0.29929135037143590E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472056368176716E+005,  0.19913013536816165E+005,  0.21454393809581721E+005,  0.23126769475644156E+005,  0.24941273401420403E+005,  0.26909984595429501E+005,  0.29046008315594449E+005,  0.31363563196013001E+005,  0.33878076717531862E+005,  0.36606288450054308E+005,  0.39566360163297650E+005,  0.42777996061832520E+005,  0.46213448846255800E+005,  0.49747996142247663E+005,  0.53265797335811301E+005,  0.56696387496236915E+005,  0.60005822635089782E+005,  0.63180076916312675E+005,  0.66176436689020338E+005,  0.68952950336727896E+005,  0.71469393446222544E+005,  0.73688236494043551E+005,  0.75575574890893869E+005,  0.77129974979485269E+005,  0.78444328696875265E+005,  0.79663855541031648E+005,  0.80854421463646097E+005,  0.82014115188039315E+005,  0.83141054858268762E+005,  0.84233396450747692E+005,  0.85289335229859062E+005,  0.86307105418944819E+005,  0.87284984774489611E+005,  0.88221306259234116E+005,  0.89114469473168647E+005,  0.89962937164815710E+005,  0.90770106804897630E+005,  0.91462229141743737E+005,  0.91898436098145175E+005,],]
input.radius_part=[[  0.13427635885681739E-007,  0.13257620360673384E-007,  0.16385466860656933E-007,  0.18488921031492816E-007,  0.20339962242075343E-007,  0.24487165320938457E-007,  0.27605598575995798E-007,  0.29634081089172348E-007,  0.32190524152971987E-007,  0.34160107484091380E-007,  0.35565059421066772E-007,  0.36392802212429977E-007,  0.37112706453067470E-007,  0.38036135829985480E-007,  0.37941221930888696E-007,  0.37291214628338167E-007,  0.38542970879783231E-007,  0.40001070490079219E-007,  0.38984017140302692E-007,  0.34223766359290565E-007,  0.29959600426892062E-007,  0.27973188965332357E-007,  0.27719910882343892E-007,  0.27222572023244706E-007,  0.26593507259396079E-007,  0.23533437707553779E-007,  0.15383553932997832E-007,  0.15133605823238543E-007,  0.17075900908658655E-007,  0.19820161843261172E-007,  0.22440137707144770E-007,  0.26037088900274608E-007,  0.27935908035554780E-007,  0.28845413757770167E-007,  0.30013485051636589E-007,  0.30829637381533000E-007,  0.31713063173393280E-007,  0.32768689372534451E-007,  0.33077976336141940E-007,  0.33413164628598842E-007,  0.33537778116595588E-007,  0.34011616509283738E-007,  0.35635402266953607E-007,  0.38055700961982773E-007,  0.39268450923500411E-007,  0.37572792970246385E-007,  0.42965834663889008E-007,  0.45363866587082776E-007,  0.42120797915824763E-007,  0.39438263039245849E-007,  0.44245325277399119E-007,  0.39735080725567513E-007,  0.36320279828406220E-007,  0.33742917680262744E-007,  0.33046143602281202E-007,  0.32041731182081895E-007,  0.30002484103412150E-007,  0.28172586015387228E-007,  0.26343919875734697E-007,  0.24629256254189536E-007,  0.23562961024134918E-007,  0.22872637882068231E-007,  0.22111286998189359E-007,  0.22896773106116371E-007,  0.26311899191243931E-007,  0.28028078087732949E-007,  0.27774081692322476E-007,  0.27173946346325906E-007,  0.26556736232993097E-007,  0.26009892218864540E-007,  0.25586330647282297E-007,  0.25318702291231058E-007,],]
input.density_part=[[  0.17709454728101964E+004,  0.17717503483893186E+004,  0.17718542719283237E+004,  0.17718846897961187E+004,  0.17718646787092227E+004,  0.17718544065558729E+004,  0.17709363934253199E+004,  0.16998081716933982E+004,  0.15978018572888461E+004,  0.15671074721867274E+004,  0.15505179466603413E+004,  0.15447210375562074E+004,  0.15387405610866315E+004,  0.15344772384945004E+004,  0.15195042836455627E+004,  0.14569765848533855E+004,  0.13318844604732908E+004,  0.12506216179349965E+004,  0.12199389678052928E+004,  0.11948526545575401E+004,  0.11812372472062088E+004,  0.11671714547684810E+004,  0.11505502042653090E+004,  0.11504646231381332E+004,  0.11510505110470642E+004,  0.11562180033968034E+004,  0.12130314825444418E+004,  0.11757017856159878E+004,  0.11552209145883387E+004,  0.11235376435121589E+004,  0.10767698461411521E+004,  0.10422914596242067E+004,  0.10343157019836030E+004,  0.10288599709734397E+004,  0.10230337775014738E+004,  0.10247021944979481E+004,  0.10276849115168604E+004,  0.10365971362936241E+004,  0.10455530550653698E+004,  0.10501269326426975E+004,  0.10535004699513029E+004,  0.10537966828933897E+004,  0.10469500011714063E+004,  0.10428967395150523E+004,  0.10441248425054569E+004,  0.10519527125199918E+004,  0.10335595581311143E+004,  0.10329240188943986E+004,  0.10563066838175503E+004,  0.10991075894680500E+004,  0.10867393647875431E+004,  0.11536989293088639E+004,  0.12304369370949144E+004,  0.12947139448588607E+004,  0.13298465895977818E+004,  0.13564557149007908E+004,  0.13852818733673464E+004,  0.14098153498422389E+004,  0.14376972268670031E+004,  0.14903262233937239E+004,  0.15125615138427311E+004,  0.15246049998977351E+004,  0.15408730257560178E+004,  0.15124631676842921E+004,  0.13689137427488884E+004,  0.13127475945146100E+004,  0.13245139470162674E+004,  0.13485768533541284E+004,  0.13748800036064329E+004,  0.13999903109844911E+004,  0.14207187911059978E+004,  0.14344123082909807E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.50828417113929257E-002,  0.34649570297752698E-002,  0.29273675631568494E-002,  0.22445588038356714E-002,  0.16739036572752390E-002,  0.13595409767173845E-002,  0.10328914864562609E-002,  0.71390976549541530E-003,  0.48531004639730985E-003,  0.33621980028636448E-003,  0.23647247504529842E-003,  0.17095335018885166E-003,  0.12644198774421452E-003,  0.96332630253264019E-004,  0.72229763833021955E-004,  0.52774074115642429E-004,  0.39643402939598211E-004,  0.31536854141339780E-004,  0.24969774815423763E-004,  0.18218268524906020E-004,  0.13637201367536637E-004,  0.11160009385979708E-004,  0.99186910785116473E-005,  0.89880168081409481E-005,  0.81322324313922155E-005,  0.66895771265124436E-005,  0.41951529762774352E-005,  0.36663994495976412E-005,  0.37774771994640748E-005,  0.39980281345787186E-005,  0.40630067771055914E-005,  0.42881906159406354E-005,  0.42832731443388158E-005,  0.41319245524250821E-005,  0.40298832860983302E-005,  0.39071609274184367E-005,  0.38000015435909107E-005,  0.37355624834020254E-005,  0.35802486275440297E-005,  0.34182655265191389E-005,  0.32361317902497139E-005,  0.30886882315920370E-005,  0.30365615086147596E-005,  0.30605610009072752E-005,  0.29852032821242446E-005,  0.26892395997571824E-005,  0.29170243247677167E-005,  0.29514340743150153E-005,  0.26297306685384697E-005,  0.24206588184408195E-005,  0.26500781606714081E-005,  0.23835300537642327E-005,  0.22117573616473483E-005,  0.20746218402023414E-005,  0.20318893548446093E-005,  0.19602727833291292E-005,  0.18230037212568272E-005,  0.17002590499883230E-005,  0.15837449196539280E-005,  0.15007319271855307E-005,  0.14310021366352928E-005,  0.13788045074068030E-005,  0.13263883364279849E-005,  0.13415404893086357E-005,  0.14137523758365768E-005,  0.14485364785476078E-005,  0.14343242858907270E-005,  0.14123509007808257E-005,  0.13913863662414690E-005,  0.13732289251966781E-005,  0.13591457069491796E-005,  0.13506063989081135E-005,],]
