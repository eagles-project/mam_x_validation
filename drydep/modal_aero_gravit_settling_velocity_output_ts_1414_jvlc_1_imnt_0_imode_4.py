# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1414 ] 
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
input.tair=[[  0.25261542362362934E+003,  0.26232991620503481E+003,  0.26881229168639805E+003,  0.27393619075525561E+003,  0.26974470810656129E+003,  0.26379285455471341E+003,  0.26094815493436948E+003,  0.25698867981978464E+003,  0.25067174445798815E+003,  0.24271643480674300E+003,  0.23609716450647397E+003,  0.23353227603810780E+003,  0.23171194771091058E+003,  0.22936281618307657E+003,  0.22484303385648545E+003,  0.21919864761534279E+003,  0.21301659385949353E+003,  0.20672640742141670E+003,  0.20056310845961679E+003,  0.19553857478238498E+003,  0.19042588637129077E+003,  0.18731417761970704E+003,  0.18676363348885624E+003,  0.18765192558750232E+003,  0.18929933701378633E+003,  0.19165055258954808E+003,  0.19282399178608640E+003,  0.18959603438374020E+003,  0.19081557970202087E+003,  0.19458486156002286E+003,  0.19805906009256219E+003,  0.20262955284710816E+003,  0.20754023539801486E+003,  0.21239034696611625E+003,  0.21696727606980411E+003,  0.22154728690685360E+003,  0.22610356352492670E+003,  0.23044751341765766E+003,  0.23475523526683332E+003,  0.23886805846190319E+003,  0.24312749577804945E+003,  0.24758718808208437E+003,  0.25226733608936246E+003,  0.25669829426418522E+003,  0.26099149628783050E+003,  0.26460346667521355E+003,  0.26690626219921410E+003,  0.26900356617630001E+003,  0.27125603637039814E+003,  0.27343091581183802E+003,  0.27517112963023908E+003,  0.27870078743572418E+003,  0.28172904373390571E+003,  0.28404305237799332E+003,  0.28608205623220152E+003,  0.28781162583498485E+003,  0.28919651270856849E+003,  0.29031248507981104E+003,  0.29124460670642600E+003,  0.29207916143990462E+003,  0.29282727013872511E+003,  0.29352474341838143E+003,  0.29411401162463920E+003,  0.29457632668325942E+003,  0.29486028007480479E+003,  0.29497093825877420E+003,  0.29509558118156104E+003,  0.29521225689953025E+003,  0.29496690920126559E+003,  0.29354935234105011E+003,  0.29332523265432405E+003,  0.29329703608700385E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473529832612167E+005,  0.19918166855784784E+005,  0.21464147420986988E+005,  0.23141514340458274E+005,  0.24961433705507603E+005,  0.26936020574742186E+005,  0.29078419318439293E+005,  0.31402891004974044E+005,  0.33924909161890479E+005,  0.36661263320496415E+005,  0.39630169451911832E+005,  0.42851390567157228E+005,  0.46297096557006611E+005,  0.49842192811524044E+005,  0.53370492984247649E+005,  0.56811321838569238E+005,  0.60130634080710675E+005,  0.63314362012479905E+005,  0.66319664504222645E+005,  0.69104464735392845E+005,  0.71628418241882508E+005,  0.73853883490742737E+005,  0.75746854703666249E+005,  0.77305893944313138E+005,  0.78624170387577076E+005,  0.79847336942266760E+005,  0.81041456141054892E+005,  0.82204611003819678E+005,  0.83334914057254689E+005,  0.84430515775747932E+005,  0.85489606035478690E+005,  0.86510413787682410E+005,  0.87491211651098070E+005,  0.88430327615232076E+005,  0.89326156501318488E+005,  0.90177156467779336E+005,  0.90986586119819432E+005,  0.91680446814589886E+005,  0.92117694507345528E+005,],]
input.radius_part=[[  0.20416120529950313E-007,  0.21912990235520273E-007,  0.23912337660552223E-007,  0.26615573206945496E-007,  0.30958083722489195E-007,  0.35845183184403298E-007,  0.40366787539515943E-007,  0.42901088943520604E-007,  0.44336667501713700E-007,  0.46352564188861419E-007,  0.48133785941078698E-007,  0.49795194288964727E-007,  0.51140440817870577E-007,  0.52298503012350926E-007,  0.54440141514350558E-007,  0.58444736529019172E-007,  0.64459452683143408E-007,  0.67015781416145668E-007,  0.68132813702559516E-007,  0.69218685459203905E-007,  0.69560475400070256E-007,  0.69642719741023303E-007,  0.69642720176757843E-007,  0.69642719235869569E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69504155741609220E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642719421833389E-007,  0.69642719715806788E-007,  0.69642719836006600E-007,  0.69642719965470451E-007,  0.69642719826189766E-007,  0.69642720747429258E-007,  0.69642723212166730E-007,  0.69642719954032184E-007,  0.69642719610686717E-007,  0.69642719456678882E-007,  0.69642719326981978E-007,  0.69642719227375668E-007,  0.69642719158760269E-007,  0.69642719111467018E-007,  0.69642719088021795E-007,  0.69642719075749425E-007,  0.69642719073720781E-007,  0.69642719074522472E-007,  0.69642719078353191E-007,  0.69642719113792057E-007,  0.69642719178863166E-007,  0.69642719375174249E-007,  0.69642719746287189E-007,  0.69642720051327352E-007,  0.69642720093653985E-007,  0.69642721084541343E-007,  0.69642722405788373E-007,  0.69642722325236069E-007,],]
input.density_part=[[  0.10470798640212661E+004,  0.10464818416737660E+004,  0.10464151908313495E+004,  0.10464326124305273E+004,  0.10459627560904257E+004,  0.10452581766510921E+004,  0.10453310987914926E+004,  0.10450425601842082E+004,  0.10446445602655876E+004,  0.10447579435021969E+004,  0.10438058076096670E+004,  0.10422816182077445E+004,  0.10403223784919655E+004,  0.10367393485857472E+004,  0.10326634987322325E+004,  0.10345818816178437E+004,  0.10504048313676551E+004,  0.10670718741374624E+004,  0.10678742582159848E+004,  0.10633450959429465E+004,  0.10573465658697010E+004,  0.10568095101923711E+004,  0.10574613811948775E+004,  0.10585037520842754E+004,  0.10584312014750276E+004,  0.10584556946543264E+004,  0.10584337196120764E+004,  0.10658393908197995E+004,  0.10647118146499738E+004,  0.10641679960490180E+004,  0.10607270294115499E+004,  0.10598992463334848E+004,  0.10595670806377357E+004,  0.10594103002372642E+004,  0.10592464737592979E+004,  0.10591205887264975E+004,  0.10585646916191602E+004,  0.10585268839241996E+004,  0.10586897065233497E+004,  0.10596650962228455E+004,  0.10604382004385775E+004,  0.10604091696024470E+004,  0.10600347158766085E+004,  0.10590838504930150E+004,  0.10606648673023753E+004,  0.10604185352566210E+004,  0.10526661105310034E+004,  0.10491114159864210E+004,  0.10453873590026424E+004,  0.10440684587825879E+004,  0.10434703572777307E+004,  0.10431314781870738E+004,  0.10429360991916058E+004,  0.10429171695341454E+004,  0.10429013196102576E+004,  0.10430870292095033E+004,  0.10433835738321500E+004,  0.10437660917107348E+004,  0.10440668879114685E+004,  0.10443399552139263E+004,  0.10447819925550182E+004,  0.10451617939880009E+004,  0.10447919987360301E+004,  0.10459942312314345E+004,  0.10491262283674812E+004,  0.10522640092742949E+004,  0.10563855523544814E+004,  0.10601788661640651E+004,  0.10616428126392573E+004,  0.10629307010068646E+004,  0.10631777642022487E+004,  0.10632170023246074E+004,],]
input.sig_part=[[  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.23495706055354244E-002,  0.17395199624384841E-002,  0.13013408715923671E-002,  0.99033771066203246E-003,  0.77384912678841599E-003,  0.59974156376261948E-003,  0.45502645239460743E-003,  0.32498446731579116E-003,  0.22461586804282843E-003,  0.15656963903453594E-003,  0.11091044812004142E-003,  0.81235125121437358E-004,  0.60615829198132400E-004,  0.46041155481923481E-004,  0.36303413537345983E-004,  0.30369674067365896E-004,  0.27093057440752295E-004,  0.23297625379395527E-004,  0.19692285664604409E-004,  0.16926748000555484E-004,  0.14651639264849912E-004,  0.13012810051690725E-004,  0.11856145754707638E-004,  0.10971681370576174E-004,  0.10185097112048649E-004,  0.94726947508310788E-005,  0.87694390827168681E-005,  0.81320951417959354E-005,  0.75426209701136981E-005,  0.70400456758981312E-005,  0.65494012817203679E-005,  0.61219826587360720E-005,  0.57288331678010186E-005,  0.53749828427159703E-005,  0.50564952106054447E-005,  0.47595366276769520E-005,  0.44762028529032312E-005,  0.42089128460912346E-005,  0.39570937877711077E-005,  0.37213901700762183E-005,  0.34994069549518960E-005,  0.32888618552528141E-005,  0.30907796135468616E-005,  0.29021349213629634E-005,  0.27313143168319933E-005,  0.25668641249998472E-005,  0.24001662292897786E-005,  0.22642010246598880E-005,  0.21475134815130913E-005,  0.20517863423606156E-005,  0.19698923805982944E-005,  0.19032090937904199E-005,  0.18462091951211060E-005,  0.17978751612761526E-005,  0.17579072529911365E-005,  0.17260180350066113E-005,  0.17010718037632133E-005,  0.16808711756835711E-005,  0.16625005476038042E-005,  0.16449699491497680E-005,  0.16285761547215432E-005,  0.16129696802608611E-005,  0.15970168528601358E-005,  0.15842269265601620E-005,  0.15750044524661233E-005,  0.15664067222697929E-005,  0.15600508277044131E-005,  0.15539426515754506E-005,  0.15448412168532144E-005,  0.15351523332786450E-005,  0.15266618035056843E-005,  0.15213133858480412E-005,],]
