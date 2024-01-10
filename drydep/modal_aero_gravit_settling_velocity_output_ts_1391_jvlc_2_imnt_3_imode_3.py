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
input.radius_part=[[  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.14921706654341030E-005,  0.19158154580402645E-005,  0.22712408710205644E-005,  0.26193570138572948E-005,  0.28845767735329296E-005,  0.30674854167393665E-005,  0.31953714314334985E-005,  0.33144899934816558E-005,  0.33581389134597751E-005,  0.27270450070590210E-005,  0.14713939750398144E-005,  0.10033433948327495E-005,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.86274191756694692E-006,  0.84512087299098988E-006,  0.83953472836494377E-006,  0.85137342096826385E-006,  0.85111549758054440E-006,  0.88417676632045177E-006,  0.90017123252109278E-006,  0.92163554829399718E-006,  0.93023195417229230E-006,  0.93878770605232577E-006,  0.94998872357508960E-006,  0.95968607717878081E-006,  0.96361127693981737E-006,  0.96299686815897347E-006,  0.96140683903502645E-006,  0.96074524737982385E-006,  0.95539148599218339E-006,  0.94811358285479040E-006,  0.94171286956722177E-006,  0.93695433536330507E-006,  0.93717768033934695E-006,  0.94590056191124550E-006,  0.95256188994502113E-006,  0.13246838906207314E-005,  0.15429300145672176E-005,  0.15089086937637090E-005,  0.14850781995571050E-005,  0.22997482155155164E-005,  0.22817912217371005E-005,  0.14489573439114112E-005,  0.12420664075881921E-005,  0.11622513664343410E-005,  0.11095483170065225E-005,  0.10888279780520588E-005,  0.10881603828882001E-005,  0.10911575748271635E-005,  0.10934225108150334E-005,  0.10966142541829045E-005,  0.11000026575239206E-005,  0.11046684277434418E-005,  0.11158253869913305E-005,  0.11316375153675779E-005,  0.11425283940193191E-005,  0.11836961169311000E-005,  0.12584116976541568E-005,  0.13623614911922335E-005,  0.15029742557635085E-005,  0.26722772339110362E-005,  0.27716522150495129E-005,  0.27649690860394113E-005,],]
input.density_part=[[  0.10000000000000000E+001,  0.17699984131903684E+004,  0.17699999900857040E+004,  0.17699999999723752E+004,  0.17699999999999022E+004,  0.17699999999999986E+004,  0.17700000000000000E+004,  0.17700000000000000E+004,  0.17700000000000002E+004,  0.17700000000000000E+004,  0.17700000000000002E+004,  0.17700000000000330E+004,  0.17700000000039715E+004,  0.17700000007977080E+004,  0.17700001750071463E+004,  0.17700249084905431E+004,  0.17713355855007735E+004,  0.17863640732656218E+004,  0.18429971056379268E+004,  0.18641115442312002E+004,  0.18823239676883006E+004,  0.18551913954139332E+004,  0.17156466784570362E+004,  0.18662647817521761E+004,  0.19341913343744775E+004,  0.18823177593480202E+004,  0.18004323626404689E+004,  0.17599013094014422E+004,  0.17922790015718849E+004,  0.18239503818419694E+004,  0.18289971623364816E+004,  0.18281057621841830E+004,  0.18381461626474756E+004,  0.18493277916879415E+004,  0.18551343658704984E+004,  0.18605111390284947E+004,  0.18659869932976644E+004,  0.18681821229279362E+004,  0.18817263579650421E+004,  0.18892385328170947E+004,  0.18958950655866613E+004,  0.19039885847530500E+004,  0.19113590881060932E+004,  0.18995245025552674E+004,  0.18885006734700505E+004,  0.13383819833254620E+004,  0.12089542666768969E+004,  0.12018849306582877E+004,  0.12286672986396968E+004,  0.10744178821412172E+004,  0.10856370248463325E+004,  0.13471527246876037E+004,  0.15462145748421567E+004,  0.16587735759507314E+004,  0.17433846708196147E+004,  0.17660598034920665E+004,  0.17573101565456716E+004,  0.17502547504383308E+004,  0.17471888166154977E+004,  0.17415427866539237E+004,  0.17377581048261065E+004,  0.17318813769189162E+004,  0.17088285917646956E+004,  0.16745363505768551E+004,  0.16544084582133889E+004,  0.15822962448383046E+004,  0.14688145318940558E+004,  0.13634679066824697E+004,  0.12715084045577239E+004,  0.10421638047553404E+004,  0.10365122217765968E+004,  0.10365307775491181E+004,],]
input.sig_part=[[  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.27663298877032941E-003,  0.33607822004661708E+000,  0.22950234129439823E+000,  0.15497471958845480E+000,  0.10550948997069458E+000,  0.71919536312731264E-001,  0.87529465457914082E-001,  0.76907376925784490E-001,  0.62617826503613611E-001,  0.50867302026434233E-001,  0.41727585573706781E-001,  0.35151502018472933E-001,  0.30505105149667554E-001,  0.27759799542982602E-001,  0.25608166746735557E-001,  0.16916008996550089E-001,  0.58277989075559231E-002,  0.30026931665549611E-002,  0.21822324758684732E-002,  0.20645624452689275E-002,  0.19879681793278079E-002,  0.18907432460920286E-002,  0.17784273266039732E-002,  0.18209290074854526E-002,  0.18215537826470696E-002,  0.17760143006354614E-002,  0.16750251210023038E-002,  0.17123819293319174E-002,  0.17511416434773301E-002,  0.18076175821473480E-002,  0.17921569383861891E-002,  0.17727739604089634E-002,  0.17733373497039182E-002,  0.17711883592257298E-002,  0.17458738272661566E-002,  0.17061723588674871E-002,  0.16655260585924378E-002,  0.16266135156027886E-002,  0.15841367956387800E-002,  0.15333084888724221E-002,  0.14870056090160130E-002,  0.14483558965498896E-002,  0.14257154254495158E-002,  0.14139713920361923E-002,  0.13971128344769609E-002,  0.18361587704779226E-002,  0.22036801944949518E-002,  0.20766489985248990E-002,  0.20441697367885180E-002,  0.41831065024816169E-002,  0.41302771686395874E-002,  0.20800598922974950E-002,  0.17493544625416216E-002,  0.16362840241348753E-002,  0.15608413860175908E-002,  0.15160389946815311E-002,  0.15004010909477701E-002,  0.14973741548796912E-002,  0.14964082306706259E-002,  0.14960329327106381E-002,  0.14979360978381411E-002,  0.15015680358653025E-002,  0.15076004120793552E-002,  0.15157329659013204E-002,  0.15233253746003499E-002,  0.15588148116205355E-002,  0.16289049703746565E-002,  0.17652384509056851E-002,  0.19980503267430839E-002,  0.51183805712716494E-002,  0.54725951513300997E-002,  0.54442190624452843E-002,],]
