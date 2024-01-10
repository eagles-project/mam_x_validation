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
input.moment=[[         0],]
input.ncol=[[         4],]
input.pcols=[[         4],]
input.nver=[[        72],]
input.radius_max=[[  0.50000000000000002E-004],]
input.tair=[[  0.25143236121305881E+003,  0.25383982688822439E+003,  0.26105094678227255E+003,  0.26439278100322070E+003,  0.26850325516631881E+003,  0.26840733639492652E+003,  0.26571074356296373E+003,  0.26168781957191635E+003,  0.25462663783799380E+003,  0.24615682495556598E+003,  0.23800180507769215E+003,  0.23431359900233798E+003,  0.23188662948394759E+003,  0.22898120391932090E+003,  0.22296945564416848E+003,  0.21579655814937499E+003,  0.20968658086499204E+003,  0.20555944399763769E+003,  0.20126316692897527E+003,  0.19749133957256734E+003,  0.19357285613706910E+003,  0.19091419748166172E+003,  0.18983696817384543E+003,  0.18999641866883405E+003,  0.19047841336952459E+003,  0.19214948854555453E+003,  0.19112667192999152E+003,  0.18891065268113616E+003,  0.19132521374302948E+003,  0.19534080592527243E+003,  0.19915290105468048E+003,  0.20294970067986188E+003,  0.20733082619987269E+003,  0.21198693198028548E+003,  0.21660308866949219E+003,  0.22114213119213809E+003,  0.22569590699079296E+003,  0.23019280773565262E+003,  0.23480548868186213E+003,  0.23965054422568670E+003,  0.24429769341959403E+003,  0.24871376974252652E+003,  0.25356937869886573E+003,  0.25767261309325158E+003,  0.26100009366371364E+003,  0.26400283744806654E+003,  0.26670456736492446E+003,  0.26868731076659441E+003,  0.27025017176030792E+003,  0.27300215761107125E+003,  0.27525377490214362E+003,  0.27770764369092495E+003,  0.28108466479044904E+003,  0.28396718568415770E+003,  0.28633718041295685E+003,  0.28790789322254250E+003,  0.28905308482275160E+003,  0.29001124833810638E+003,  0.29084976345296536E+003,  0.29160029186182561E+003,  0.29227885493216729E+003,  0.29286808543617065E+003,  0.29338513973510095E+003,  0.29388117882770939E+003,  0.29423542939321248E+003,  0.29431618687679651E+003,  0.29378471992852729E+003,  0.29347084783559859E+003,  0.29408063515400812E+003,  0.29481401687193875E+003,  0.29552701271291829E+003,  0.29609528017143850E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18474678442333348E+005,  0.19922184022484762E+005,  0.21471750653618299E+005,  0.23153008404824875E+005,  0.24977149267213306E+005,  0.26956316401515789E+005,  0.29103684667262849E+005,  0.31433548211621535E+005,  0.33961416456917555E+005,  0.36704117880872058E+005,  0.39679910706224066E+005,  0.42908603785385538E+005,  0.46362302456389851E+005,  0.49915621940473779E+005,  0.53452106382349368E+005,  0.56900916605652892E+005,  0.60227928346052591E+005,  0.63419041272566697E+005,  0.66431314882017032E+005,  0.69222574753536552E+005,  0.71752382839743819E+005,  0.73983010292934385E+005,  0.75880372454932469E+005,  0.77443028053749105E+005,  0.78764362379486440E+005,  0.79990366197702984E+005,  0.81187255281842212E+005,  0.82353108205777855E+005,  0.83486033117299841E+005,  0.84584176201802504E+005,  0.85645723135198685E+005,  0.86668898758958749E+005,  0.87651971686794801E+005,  0.88593266031427993E+005,  0.89491172888908550E+005,  0.90344146839537454E+005,  0.91155338238683689E+005,  0.91850554035594876E+005,  0.92288613013553535E+005,],]
input.radius_part=[[  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,],]
input.density_part=[[  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,],]
input.sig_part=[[  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.52901500654061040E+000,  0.36051638010373543E+000,  0.24809249707229475E+000,  0.16959946369155043E+000,  0.11624975678582364E+000,  0.79243279329855379E-001,  0.53952133081231639E-001,  0.36845779444075903E-001,  0.25254848126031095E-001,  0.17522167674395954E-001,  0.12665448089018696E-001,  0.96752036255245803E-002,  0.77487341260470939E-002,  0.64922762535701908E-002,  0.56865489655355895E-002,  0.51851230432158309E-002,  0.48692237833929909E-002,  0.46534638392904341E-002,  0.45170020851856346E-002,  0.44279836778205565E-002,  0.43805124816222096E-002,  0.43435274486628228E-002,  0.43030025064528729E-002,  0.42544890263580895E-002,  0.42055673043230185E-002,  0.41408706516451602E-002,  0.41220850008003755E-002,  0.41261253061546706E-002,  0.40567442730748901E-002,  0.39652957091255393E-002,  0.38813920147710377E-002,  0.38016918189124516E-002,  0.37176245800274181E-002,  0.36347244156058425E-002,  0.35571831152569964E-002,  0.34843552559005423E-002,  0.34146039745053766E-002,  0.33485679668518900E-002,  0.32841532324401814E-002,  0.32201491608693949E-002,  0.31609319918080550E-002,  0.31064382868561846E-002,  0.30501328705750306E-002,  0.30028894094780594E-002,  0.29641591705936118E-002,  0.29296478121370148E-002,  0.28991700837519658E-002,  0.28760415445067983E-002,  0.28574959747249321E-002,  0.28304260750856903E-002,  0.28083718446264461E-002,  0.27856573891484552E-002,  0.27568861373713700E-002,  0.27328470933712496E-002,  0.27133905068750870E-002,  0.27003331442419435E-002,  0.26907837585845472E-002,  0.26828722516358946E-002,  0.26759568003417293E-002,  0.26697402350801648E-002,  0.26641002592744374E-002,  0.26591479560387171E-002,  0.26547564034759604E-002,  0.26505683861927187E-002,  0.26474060835072247E-002,  0.26461607499483732E-002,  0.26491492316813455E-002,  0.26506981418712452E-002,  0.26459499056378623E-002,  0.26404137335185270E-002,  0.26351232463641340E-002,  0.26310011504441229E-002,],]
