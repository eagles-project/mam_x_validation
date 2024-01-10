# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1391 ] 
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
input.tair=[[  0.25165191658166566E+003,  0.25822278697420967E+003,  0.26215237651436564E+003,  0.26002049169276108E+003,  0.26192990786858309E+003,  0.26411170622772170E+003,  0.26361761077523028E+003,  0.25948421597319225E+003,  0.25002940735549723E+003,  0.24095301690692685E+003,  0.23543569082577849E+003,  0.23478473925440008E+003,  0.23353786634630603E+003,  0.23087025506402867E+003,  0.22425358728272840E+003,  0.21638842017102206E+003,  0.21044232485570450E+003,  0.20643499859197129E+003,  0.20188968092453118E+003,  0.19751950158038346E+003,  0.19266189342000234E+003,  0.18942931619310878E+003,  0.18825051220613710E+003,  0.18830186068686584E+003,  0.18856613379368295E+003,  0.18878192006352316E+003,  0.18651632024255932E+003,  0.18790938474920824E+003,  0.19135265458112704E+003,  0.19521523923991580E+003,  0.19935263326268870E+003,  0.20340769502577893E+003,  0.20767422117556558E+003,  0.21205446483832674E+003,  0.21655267676225228E+003,  0.22117544618415852E+003,  0.22573890210521816E+003,  0.23034117079818955E+003,  0.23502722133177514E+003,  0.23955304788859874E+003,  0.24396965874764118E+003,  0.24842453365762080E+003,  0.25271064131769865E+003,  0.25703363505675048E+003,  0.26152165666969881E+003,  0.26505670142288642E+003,  0.26770682135268873E+003,  0.27005750218743231E+003,  0.27136363143965997E+003,  0.27299220564867983E+003,  0.27516559920870009E+003,  0.27846341101057254E+003,  0.28164340742628468E+003,  0.28392103643285623E+003,  0.28588688259438334E+003,  0.28746695727120073E+003,  0.28869785593260491E+003,  0.28967025926953409E+003,  0.29051333775751732E+003,  0.29127946112755893E+003,  0.29201259996471373E+003,  0.29271343274368570E+003,  0.29332799518181469E+003,  0.29380435051650602E+003,  0.29421984471528083E+003,  0.29462683391983035E+003,  0.29495604251668607E+003,  0.29505679164484121E+003,  0.29454190550964336E+003,  0.29283672829872791E+003,  0.29276452873885415E+003,  0.29289582251285674E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473132410323138E+005,  0.19916776904475933E+005,  0.21461516680483379E+005,  0.23137537360909366E+005,  0.24955996075657116E+005,  0.26928998159917246E+005,  0.29069677434597121E+005,  0.31392283522714071E+005,  0.33912277532113760E+005,  0.36646435518532249E+005,  0.39612958833906974E+005,  0.42831594628004284E+005,  0.46274535127033341E+005,  0.49816786120312550E+005,  0.53342254512214153E+005,  0.56780321789760019E+005,  0.60096969983212221E+005,  0.63278142685418388E+005,  0.66281033150251256E+005,  0.69063598327158368E+005,  0.71585526132115338E+005,  0.73809205243331467E+005,  0.75700657175162327E+005,  0.77258445145412261E+005,  0.78575663552487109E+005,  0.79797848405781944E+005,  0.80991009216219099E+005,  0.82153230542007237E+005,  0.83282626424953254E+005,  0.84377348823449385E+005,  0.85435589066979242E+005,  0.86455577528768918E+005,  0.87435588213308263E+005,  0.88373950451482626E+005,  0.89269060353450448E+005,  0.90119377315673977E+005,  0.90928197398114673E+005,  0.91621589223621078E+005,  0.92058556209347618E+005,],]
input.radius_part=[[  0.13577808477305034E-007,  0.13914007941326571E-007,  0.17266098075731190E-007,  0.19335603674501505E-007,  0.20067470467452444E-007,  0.24329806467963328E-007,  0.27322291609900765E-007,  0.29379461892547077E-007,  0.32237138097129219E-007,  0.34260018558712093E-007,  0.35613517023733366E-007,  0.36313333746283625E-007,  0.37015172693347990E-007,  0.37971644128213124E-007,  0.37948497294151004E-007,  0.37273913903098345E-007,  0.38178237307010995E-007,  0.40024204517318180E-007,  0.39514000147715497E-007,  0.33812030348636241E-007,  0.29592778816984726E-007,  0.27816169299460131E-007,  0.27639110131464859E-007,  0.27292433206170913E-007,  0.25404539686865648E-007,  0.18368642935594248E-007,  0.14469210424652440E-007,  0.15268157037914279E-007,  0.17502430592369148E-007,  0.18999648449174546E-007,  0.19947168414288848E-007,  0.21387045986489649E-007,  0.22495631819593682E-007,  0.23792132671363930E-007,  0.25584277562544089E-007,  0.28718549750236936E-007,  0.31467707654446133E-007,  0.32612114360184294E-007,  0.32891746713612241E-007,  0.33460999155005634E-007,  0.33057576653013957E-007,  0.32590980666017325E-007,  0.31955440287066624E-007,  0.32080051214101573E-007,  0.32189493297967066E-007,  0.36876219266243253E-007,  0.40909570918124504E-007,  0.43508660063602255E-007,  0.43162481319476552E-007,  0.48435870515764863E-007,  0.49575101099196288E-007,  0.37577067138978378E-007,  0.33270992621788429E-007,  0.30221242378019906E-007,  0.28229505360093879E-007,  0.25823109222164596E-007,  0.23543239324936206E-007,  0.21948201899375183E-007,  0.20806580809860566E-007,  0.20032858173237547E-007,  0.19872977860429966E-007,  0.19822031484103014E-007,  0.19904147435679564E-007,  0.20603240695753002E-007,  0.20777916198690810E-007,  0.21430173731176326E-007,  0.23239301544435400E-007,  0.26625415248294257E-007,  0.29522710120965446E-007,  0.45056118477460787E-007,  0.46065379043806467E-007,  0.46035499779151653E-007,],]
input.density_part=[[  0.17711749562714742E+004,  0.17717672693892137E+004,  0.17718329934664557E+004,  0.17718799959691507E+004,  0.17718697029002310E+004,  0.17718348129114340E+004,  0.17715378284965786E+004,  0.17095675763748825E+004,  0.15985719055087570E+004,  0.15651985174725305E+004,  0.15501434616203524E+004,  0.15453313887147699E+004,  0.15392885397740235E+004,  0.15345241196813347E+004,  0.15192385107390817E+004,  0.14603161232014695E+004,  0.13547597424694932E+004,  0.12648672472143219E+004,  0.12228027846763159E+004,  0.11931402237811581E+004,  0.11835904448328681E+004,  0.11709447972239675E+004,  0.11504685332639981E+004,  0.11491717038513248E+004,  0.11512236580605536E+004,  0.11734323148413016E+004,  0.12010308917174204E+004,  0.11668385920960779E+004,  0.11576200782006074E+004,  0.11449054979350574E+004,  0.11193135814135876E+004,  0.10930967356473122E+004,  0.10768114634175095E+004,  0.10547208879348673E+004,  0.10337334986783019E+004,  0.10192999707079573E+004,  0.10172307614693428E+004,  0.10186379456557470E+004,  0.10196256453324509E+004,  0.10196909070221698E+004,  0.10280561391280967E+004,  0.10481324618124131E+004,  0.10610082800323426E+004,  0.10641918483642905E+004,  0.10662025020667045E+004,  0.10535307575172822E+004,  0.10425672699650095E+004,  0.10364999409540908E+004,  0.10523001987165319E+004,  0.10453958838400940E+004,  0.10549897100389292E+004,  0.11513433811882157E+004,  0.12347665961630089E+004,  0.12839625785192559E+004,  0.13122670451075066E+004,  0.13240523527466698E+004,  0.13451681932588954E+004,  0.13950252461687032E+004,  0.14449957607578147E+004,  0.14722492255919647E+004,  0.14877752059314003E+004,  0.15041278994380166E+004,  0.15197365192436550E+004,  0.15184935689202600E+004,  0.15162294907943092E+004,  0.14700898265508222E+004,  0.13835200602181096E+004,  0.12880540804137916E+004,  0.12334959503021612E+004,  0.10661462989664030E+004,  0.10615708228368926E+004,  0.10616232749319258E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.51181103790589946E-002,  0.35994957284504327E-002,  0.30482520173949852E-002,  0.23026510688218880E-002,  0.16245302995002533E-002,  0.13395633876694102E-002,  0.10178317828237824E-002,  0.70981997684169400E-003,  0.48434239310324453E-003,  0.33525729434983475E-003,  0.23624371196674337E-003,  0.17099985623684157E-003,  0.12658077421686051E-003,  0.96462471343159895E-004,  0.72280039635616708E-004,  0.52808547366624140E-004,  0.39986362365398619E-004,  0.32054246012000141E-004,  0.25511806698271415E-004,  0.18061691790168843E-004,  0.13542545143972976E-004,  0.11147467948518292E-004,  0.98841126127104628E-005,  0.89845668161725747E-005,  0.77290296950627675E-005,  0.52189871249460772E-005,  0.38430377835956876E-005,  0.36546003550857700E-005,  0.38847596932196253E-005,  0.38986560297618520E-005,  0.37399456485951075E-005,  0.36631129046953458E-005,  0.35506398656311188E-005,  0.34530340944338151E-005,  0.34332063502694009E-005,  0.36002859705568960E-005,  0.37271140075195158E-005,  0.36478057369075569E-005,  0.34650839031174219E-005,  0.33183820197173788E-005,  0.31013760136587199E-005,  0.29238033776057943E-005,  0.27189550493404395E-005,  0.25716883849136560E-005,  0.24291313657872628E-005,  0.26328584228334520E-005,  0.27734032730916035E-005,  0.28140425191699409E-005,  0.26959972669638190E-005,  0.29586095948324439E-005,  0.29627874521362868E-005,  0.22202607462957249E-005,  0.19963229291247916E-005,  0.18028051995899079E-005,  0.16615253346615038E-005,  0.14820146570420040E-005,  0.13321134871727859E-005,  0.12581156459790517E-005,  0.12114146889371370E-005,  0.11683737905261516E-005,  0.11565984235251799E-005,  0.11530668795386268E-005,  0.11580833553188717E-005,  0.11910880617198341E-005,  0.11891404698366599E-005,  0.11834759180166830E-005,  0.12123412495069944E-005,  0.13131045968330159E-005,  0.14116279902367849E-005,  0.20619590116418625E-005,  0.21030361300294183E-005,  0.20946614592865433E-005,],]
