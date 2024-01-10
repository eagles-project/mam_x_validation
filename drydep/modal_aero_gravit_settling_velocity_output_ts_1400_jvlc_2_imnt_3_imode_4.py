# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1400 ] 
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
input.tair=[[  0.25143236121305881E+003,  0.25383982688822439E+003,  0.26105094678227255E+003,  0.26439278100322070E+003,  0.26850325516631881E+003,  0.26840733639492652E+003,  0.26571074356296373E+003,  0.26168781957191635E+003,  0.25462663783799380E+003,  0.24615682495556598E+003,  0.23800180507769215E+003,  0.23431359900233798E+003,  0.23188662948394759E+003,  0.22898120391932090E+003,  0.22296945564416848E+003,  0.21579655814937499E+003,  0.20968658086499204E+003,  0.20555944399763769E+003,  0.20126316692897527E+003,  0.19749133957256734E+003,  0.19357285613706910E+003,  0.19091419748166172E+003,  0.18983696817384543E+003,  0.18999641866883405E+003,  0.19047841336952459E+003,  0.19214948854555453E+003,  0.19112667192999152E+003,  0.18891065268113616E+003,  0.19132521374302948E+003,  0.19534080592527243E+003,  0.19915290105468048E+003,  0.20294970067986188E+003,  0.20733082619987269E+003,  0.21198693198028548E+003,  0.21660308866949219E+003,  0.22114213119213809E+003,  0.22569590699079296E+003,  0.23019280773565262E+003,  0.23480548868186213E+003,  0.23965054422568670E+003,  0.24429769341959403E+003,  0.24871376974252652E+003,  0.25356937869886573E+003,  0.25767261309325158E+003,  0.26100009366371364E+003,  0.26400283744806654E+003,  0.26670456736492446E+003,  0.26868731076659441E+003,  0.27025017176030792E+003,  0.27300215761107125E+003,  0.27525377490214362E+003,  0.27770764369092495E+003,  0.28108466479044904E+003,  0.28396718568415770E+003,  0.28633718041295685E+003,  0.28790789322254250E+003,  0.28905308482275160E+003,  0.29001124833810638E+003,  0.29084976345296536E+003,  0.29160029186182561E+003,  0.29227885493216729E+003,  0.29286808543617065E+003,  0.29338513973510095E+003,  0.29388117882770939E+003,  0.29423542939321248E+003,  0.29431618687679651E+003,  0.29378471992852729E+003,  0.29347084783559859E+003,  0.29408063515400812E+003,  0.29481401687193875E+003,  0.29552701271291829E+003,  0.29609528017143850E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18474678442333348E+005,  0.19922184022484762E+005,  0.21471750653618299E+005,  0.23153008404824875E+005,  0.24977149267213306E+005,  0.26956316401515789E+005,  0.29103684667262849E+005,  0.31433548211621535E+005,  0.33961416456917555E+005,  0.36704117880872058E+005,  0.39679910706224066E+005,  0.42908603785385538E+005,  0.46362302456389851E+005,  0.49915621940473779E+005,  0.53452106382349368E+005,  0.56900916605652892E+005,  0.60227928346052591E+005,  0.63419041272566697E+005,  0.66431314882017032E+005,  0.69222574753536552E+005,  0.71752382839743819E+005,  0.73983010292934385E+005,  0.75880372454932469E+005,  0.77443028053749105E+005,  0.78764362379486440E+005,  0.79990366197702984E+005,  0.81187255281842212E+005,  0.82353108205777855E+005,  0.83486033117299841E+005,  0.84584176201802504E+005,  0.85645723135198685E+005,  0.86668898758958749E+005,  0.87651971686794801E+005,  0.88593266031427993E+005,  0.89491172888908550E+005,  0.90344146839537454E+005,  0.91155338238683689E+005,  0.91850554035594876E+005,  0.92288613013553535E+005,],]
input.radius_part=[[  0.21247677954333995E-007,  0.22751205717771553E-007,  0.25745284212170793E-007,  0.28299601387563797E-007,  0.30659894508822966E-007,  0.34851880407998540E-007,  0.39976675930383497E-007,  0.42521383944811447E-007,  0.44164428191785671E-007,  0.46134334938186512E-007,  0.48019834244375552E-007,  0.49825311957359049E-007,  0.51166439561105297E-007,  0.52377568386699924E-007,  0.54904906092000448E-007,  0.59955706431015670E-007,  0.64773659701244987E-007,  0.66956862098902238E-007,  0.67940158648991988E-007,  0.69117957588074263E-007,  0.69484140570636468E-007,  0.69634090794096467E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69585523442116724E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642719163182032E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642722447534987E-007,  0.69642721447274389E-007,  0.69642725871849562E-007,  0.69642726919938723E-007,  0.69642721295700463E-007,  0.69642719710757731E-007,  0.69642719268391068E-007,  0.69642719116669137E-007,  0.69642719117599126E-007,  0.69642719135252643E-007,  0.69642719151498563E-007,  0.69642719175723176E-007,  0.69642719195539617E-007,  0.69642719217052587E-007,  0.69642719260654455E-007,  0.69642719307333143E-007,  0.69642719353280644E-007,  0.69642719419131963E-007,  0.69642719528036935E-007,  0.69642719671352236E-007,  0.69642720712118016E-007,  0.69642720607445483E-007,  0.69642720254393297E-007,  0.69642720006926401E-007,  0.69642719883410693E-007,],]
input.density_part=[[  0.10466978070443934E+004,  0.10463668764379495E+004,  0.10464854004959029E+004,  0.10463531747469699E+004,  0.10457126549853883E+004,  0.10452243126689073E+004,  0.10452961399900462E+004,  0.10450545554578314E+004,  0.10446313071538955E+004,  0.10447401463523374E+004,  0.10438108615224946E+004,  0.10421946121529124E+004,  0.10404126036577870E+004,  0.10366553938674995E+004,  0.10328119860339532E+004,  0.10384772066480875E+004,  0.10520668289301366E+004,  0.10669358214836234E+004,  0.10688092722039523E+004,  0.10647585445815828E+004,  0.10577651032362110E+004,  0.10567322517364837E+004,  0.10565806734671719E+004,  0.10579390353066408E+004,  0.10580415664448997E+004,  0.10588263423524227E+004,  0.10608545662564636E+004,  0.10641756885240502E+004,  0.10645525441903910E+004,  0.10653555610116084E+004,  0.10646558094608376E+004,  0.10614899440867637E+004,  0.10614431422859852E+004,  0.10611658627972495E+004,  0.10590541867282179E+004,  0.10579506083045203E+004,  0.10576741645174532E+004,  0.10575429064968212E+004,  0.10581754157671642E+004,  0.10581004760269429E+004,  0.10578549532308093E+004,  0.10579833789831735E+004,  0.10582884939882808E+004,  0.10584368465409359E+004,  0.10573143589341587E+004,  0.10556410148434318E+004,  0.10537912527796229E+004,  0.10490673137002439E+004,  0.10444319456824003E+004,  0.10435404474434199E+004,  0.10434589567811690E+004,  0.10434167059952542E+004,  0.10433877760742421E+004,  0.10433438644008334E+004,  0.10433344101281434E+004,  0.10435829339143268E+004,  0.10439235004883130E+004,  0.10439076217352442E+004,  0.10439022826813728E+004,  0.10443371489808599E+004,  0.10447261768409646E+004,  0.10455056895096382E+004,  0.10454966666156574E+004,  0.10452436003810622E+004,  0.10441655509111563E+004,  0.10460735435105075E+004,  0.10613865328353966E+004,  0.10644024025219517E+004,  0.10649275150972376E+004,  0.10651598735837847E+004,  0.10652819237318370E+004,  0.10653327713164638E+004,],]
input.sig_part=[[  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.47311353808850891E-002,  0.34463548883773057E-002,  0.26789142978062451E-002,  0.20069093536251087E-002,  0.14831630920531037E-002,  0.11412232301946490E-002,  0.88232296232068413E-003,  0.63079429806165062E-003,  0.43769513295429313E-003,  0.30469722183700291E-003,  0.21580379231654617E-003,  0.15825078836740971E-003,  0.11803823432199194E-003,  0.89722801688495366E-004,  0.71143223529545940E-004,  0.60705356840416301E-004,  0.53097679607114166E-004,  0.45693606852023559E-004,  0.38895583201140327E-004,  0.33735286857046046E-004,  0.29394691537955518E-004,  0.26256559627173680E-004,  0.23960290731915797E-004,  0.22208071221739188E-004,  0.20627427224251453E-004,  0.19226441409493987E-004,  0.17842451269226088E-004,  0.16585562414444858E-004,  0.15502697325498619E-004,  0.14541897269578143E-004,  0.13620289592525975E-004,  0.12731210299454556E-004,  0.11949392101079468E-004,  0.11246785136054158E-004,  0.10599372367131011E-004,  0.10004659935323459E-004,  0.94498438253243685E-005,  0.89261780064686187E-005,  0.84390193882235740E-005,  0.79756968287068198E-005,  0.75364507890729887E-005,  0.71244289342427860E-005,  0.67405844607889098E-005,  0.63758003667250745E-005,  0.60242924581729375E-005,  0.56969459817549218E-005,  0.54047125167874469E-005,  0.51362057329666654E-005,  0.49048793952672255E-005,  0.47232187697769407E-005,  0.45692881904945175E-005,  0.44373739023887242E-005,  0.43250911822722718E-005,  0.42301363782766443E-005,  0.41514633438230184E-005,  0.40889669246218349E-005,  0.40402291899506232E-005,  0.39992997427099170E-005,  0.39625209732276066E-005,  0.39293177640667931E-005,  0.38977749549266877E-005,  0.38694714260361491E-005,  0.38399889666295001E-005,  0.38113000205137271E-005,  0.37813518760526679E-005,  0.37639805832466194E-005,  0.37965237517999526E-005,  0.37861021637574278E-005,  0.37674212919208722E-005,  0.37488827266336146E-005,  0.37328813234128341E-005,  0.37227038067332269E-005,],]
