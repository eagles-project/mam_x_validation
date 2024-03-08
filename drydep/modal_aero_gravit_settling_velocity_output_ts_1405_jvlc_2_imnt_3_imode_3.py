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
input.radius_part=[[  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.15507013561669922E-005,  0.19967139343075537E-005,  0.23040601339914650E-005,  0.25954778750586167E-005,  0.28618686002148983E-005,  0.30800298295442990E-005,  0.32274249144782024E-005,  0.33366403312424592E-005,  0.33581389134597751E-005,  0.25930485354647458E-005,  0.14627155168821498E-005,  0.97402402155482787E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.84869095899149001E-006,  0.86035427984885842E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.87147260377642965E-006,  0.90111042353765009E-006,  0.90943702046916251E-006,  0.92872106147052146E-006,  0.94823892257148755E-006,  0.95330265209984266E-006,  0.95519761403940249E-006,  0.94384040954479001E-006,  0.93321398097459835E-006,  0.92714802273576396E-006,  0.92090587597854738E-006,  0.91574132731280097E-006,  0.91530207607218283E-006,  0.91883758772898352E-006,  0.93293937773576205E-006,  0.94231126315663476E-006,  0.10721158934091714E-005,  0.11720139459290531E-005,  0.11315618189390085E-005,  0.14821449738430213E-005,  0.16057029732790002E-005,  0.13719367588569893E-005,  0.15386220670514912E-005,  0.18795800021479666E-005,  0.15755023258378349E-005,  0.13496145689131575E-005,  0.12127914720159543E-005,  0.11380956150810943E-005,  0.10970687926654394E-005,  0.10795341253582327E-005,  0.10697376389688133E-005,  0.10660560459619513E-005,  0.10649342920693056E-005,  0.10774078575502816E-005,  0.10827432557477542E-005,  0.10893358074884867E-005,  0.11166734388420963E-005,  0.12600083344865446E-005,  0.13442934547045939E-005,  0.13266850708106793E-005,  0.12917508978111610E-005,  0.12570156119670814E-005,  0.12268306964693086E-005,  0.12038020904921124E-005,  0.11894178515949897E-005,],]
input.density_part=[[  0.10000000000000000E+001,  0.10000000000000000E+001,  0.17699994058057098E+004,  0.17699999998075593E+004,  0.17699999999998959E+004,  0.17699999999999989E+004,  0.17700000000000000E+004,  0.17700000000000002E+004,  0.17700000000000002E+004,  0.17700000000000000E+004,  0.17700000000000007E+004,  0.17700000000001239E+004,  0.17700000000178950E+004,  0.17700000019318800E+004,  0.17700001419425009E+004,  0.17700171632760037E+004,  0.17711813633687957E+004,  0.17873955836611594E+004,  0.18501197882368288E+004,  0.18685689103035393E+004,  0.18753603004651086E+004,  0.18024677657706857E+004,  0.17219708373822511E+004,  0.18211995499580632E+004,  0.18951308898558459E+004,  0.19200472172395403E+004,  0.19044562458487928E+004,  0.17333294626368131E+004,  0.17782713606937102E+004,  0.17890869409525092E+004,  0.18373570366871975E+004,  0.18525026150788581E+004,  0.18611793818885280E+004,  0.18742583698754495E+004,  0.18890668588423446E+004,  0.19004114060851862E+004,  0.19122338168497063E+004,  0.19254707095560589E+004,  0.19325793787616899E+004,  0.19267540709636287E+004,  0.19043577325989145E+004,  0.18573458150710189E+004,  0.18185899532116664E+004,  0.15605192574974833E+004,  0.14390540759667033E+004,  0.15016499856510609E+004,  0.12115664291187550E+004,  0.11579207461144049E+004,  0.12544080027582424E+004,  0.12316761621560693E+004,  0.11397907420267447E+004,  0.12713764700368472E+004,  0.14461735742275803E+004,  0.16138978016601966E+004,  0.17320998786913583E+004,  0.18001196473392636E+004,  0.18225765870531584E+004,  0.18295673882071499E+004,  0.18255613460909378E+004,  0.18175715609597928E+004,  0.17826999023431499E+004,  0.17667991833884614E+004,  0.17413077471251743E+004,  0.16762669271812078E+004,  0.14525494178828556E+004,  0.13693209468189420E+004,  0.13829665226122704E+004,  0.14140975150523234E+004,  0.14488718445992295E+004,  0.14824959775029013E+004,  0.15105431216948898E+004,  0.15292224563549842E+004,],]
input.sig_part=[[  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.27783186093255580E-003,  0.19182146677337785E-003,  0.23222813156436378E+000,  0.15795713582531368E+000,  0.10723795388757769E+000,  0.72511073850166530E-001,  0.91439271422536522E-001,  0.80488968471799718E-001,  0.63791184614141835E-001,  0.50493861800471794E-001,  0.41364728318864355E-001,  0.35330559715513403E-001,  0.30959801277087876E-001,  0.28084554809064220E-001,  0.25620757180228600E-001,  0.15553063080939429E-001,  0.57777969141564502E-002,  0.28788738213446721E-002,  0.21955779294328742E-002,  0.20759378500933446E-002,  0.19861070493860317E-002,  0.18726782732953072E-002,  0.17759062130876667E-002,  0.17535298197251981E-002,  0.17772462660478761E-002,  0.17506832944044128E-002,  0.16992405267400560E-002,  0.16339777487794267E-002,  0.17420192193699441E-002,  0.17300799462254450E-002,  0.17967239404370916E-002,  0.18310586236248043E-002,  0.18065508108351506E-002,  0.17773664628911428E-002,  0.17087755282038800E-002,  0.16434680657164563E-002,  0.15945511697311226E-002,  0.15477092440153684E-002,  0.15009422115750662E-002,  0.14610267348882401E-002,  0.14226715662726595E-002,  0.13982755886013348E-002,  0.13678342053740032E-002,  0.14735898796504100E-002,  0.15848676266991036E-002,  0.15205259330557273E-002,  0.20431425155696694E-002,  0.22619967927491394E-002,  0.17902234047543100E-002,  0.21788153939129190E-002,  0.29611169491646772E-002,  0.23142245336763598E-002,  0.19268991910708268E-002,  0.17306825588519811E-002,  0.16291130856245783E-002,  0.15669446061164585E-002,  0.15307443358749981E-002,  0.15044338034683794E-002,  0.14865341418574341E-002,  0.14726114738301188E-002,  0.14735970625439233E-002,  0.14709854960010343E-002,  0.14639237284034183E-002,  0.14765657191911754E-002,  0.16189011602012766E-002,  0.17290911656792365E-002,  0.16976356620227323E-002,  0.16434060824560540E-002,  0.15925163147885242E-002,  0.15502213201981031E-002,  0.15190273865830946E-002,  0.15000867406198036E-002,],]