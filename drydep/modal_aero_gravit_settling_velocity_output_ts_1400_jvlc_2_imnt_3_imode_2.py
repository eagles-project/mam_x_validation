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
input.radius_part=[[  0.13298254601145984E-007,  0.13977923178237305E-007,  0.17193654367132568E-007,  0.18821831287401135E-007,  0.20040946569514457E-007,  0.24034883884665561E-007,  0.27357021705569404E-007,  0.29363039825447076E-007,  0.31834491021184605E-007,  0.33916333993305506E-007,  0.35486379201833991E-007,  0.36339148222259241E-007,  0.37073085297197697E-007,  0.38023438418706302E-007,  0.37915744568642140E-007,  0.37307618510566125E-007,  0.38432243406627256E-007,  0.40013154628004638E-007,  0.39541945932319692E-007,  0.34854803178005175E-007,  0.30331777033678859E-007,  0.28061349509229307E-007,  0.27522338733980520E-007,  0.27450997451167922E-007,  0.26559395550254966E-007,  0.22327182836711884E-007,  0.14785984098151886E-007,  0.14923890012529946E-007,  0.17080114066609630E-007,  0.19143708471404132E-007,  0.21016926607105060E-007,  0.22635526062317954E-007,  0.25933829118356934E-007,  0.29388929681120223E-007,  0.30541353749725841E-007,  0.30770402753369790E-007,  0.31604160516214675E-007,  0.32357615488556915E-007,  0.32837136457370913E-007,  0.33096763123421259E-007,  0.33114447803302676E-007,  0.32623634825204092E-007,  0.32904741500682243E-007,  0.35982534276278711E-007,  0.34987991355273520E-007,  0.35754571235565882E-007,  0.35327415147019832E-007,  0.52274326363192402E-007,  0.47627301853016368E-007,  0.52535953828231711E-007,  0.56193125884055893E-007,  0.41005816543284369E-007,  0.33602522384189177E-007,  0.30520015324014825E-007,  0.28583750304998902E-007,  0.26392911229368179E-007,  0.23439288839679336E-007,  0.22012947675187945E-007,  0.20505975318447903E-007,  0.19363469750454105E-007,  0.18523001944451596E-007,  0.18018988298497415E-007,  0.17860805829698912E-007,  0.17885729096054954E-007,  0.18588138582250334E-007,  0.22026887546674690E-007,  0.27796852780524625E-007,  0.35795661373978188E-007,  0.35929671456694340E-007,  0.34311910343433698E-007,  0.32941053171900166E-007,  0.32173379736069479E-007,],]
input.density_part=[[  0.17711751030146431E+004,  0.17717885545820466E+004,  0.17718442173181720E+004,  0.17718842165445096E+004,  0.17718601939658049E+004,  0.17718719702835772E+004,  0.17713002318844538E+004,  0.17115417066049076E+004,  0.16088353382998162E+004,  0.15697008350399115E+004,  0.15513505921190554E+004,  0.15450677437093971E+004,  0.15389930213900946E+004,  0.15343998345902087E+004,  0.15184542178091626E+004,  0.14534897988774178E+004,  0.13383480751582947E+004,  0.12579717454867343E+004,  0.12244356741357826E+004,  0.11964857304602033E+004,  0.11835195148130579E+004,  0.11735961994200063E+004,  0.11568190905465999E+004,  0.11500977141013241E+004,  0.11505583616120632E+004,  0.11583889678035941E+004,  0.12190750977383957E+004,  0.11806616116671455E+004,  0.11576651698249311E+004,  0.11340731287496660E+004,  0.11067278295560795E+004,  0.10643123883207427E+004,  0.10321155257038392E+004,  0.10224466501520986E+004,  0.10206398650675854E+004,  0.10208037799836711E+004,  0.10205564513094478E+004,  0.10203910114049160E+004,  0.10246800253253373E+004,  0.10402805639580617E+004,  0.10546575691923097E+004,  0.10610318670328918E+004,  0.10611845454657512E+004,  0.10509091302581194E+004,  0.10626010701671526E+004,  0.10601298846883378E+004,  0.10628011666898956E+004,  0.10220137903297632E+004,  0.10423041194609227E+004,  0.10424622348565658E+004,  0.10438614659898653E+004,  0.11286483550212522E+004,  0.12394654678046306E+004,  0.13200921232962030E+004,  0.13708359652885447E+004,  0.14050856798388836E+004,  0.14337910615193337E+004,  0.14563994061075471E+004,  0.14963965637254862E+004,  0.15182345300275742E+004,  0.15186653634782519E+004,  0.14892298463603970E+004,  0.14843443688408108E+004,  0.14853944010743819E+004,  0.14887930216671202E+004,  0.14715543928509746E+004,  0.13165370292180096E+004,  0.11529515211085436E+004,  0.11519330256867781E+004,  0.11747083148053325E+004,  0.11975425415229477E+004,  0.12120544776376464E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.50105452810020427E-002,  0.35852557170133084E-002,  0.30290983092183927E-002,  0.22602318450133337E-002,  0.16426003465472637E-002,  0.13340639947668285E-002,  0.10230236412553046E-002,  0.71324797654130645E-003,  0.48575507805023488E-003,  0.33640727241964874E-003,  0.23685545779470824E-003,  0.17092216471690681E-003,  0.12631133629432262E-003,  0.96197126886363938E-004,  0.71977281467704726E-004,  0.52539711737502064E-004,  0.39699564248644465E-004,  0.31806191377023210E-004,  0.25527009010530997E-004,  0.18682566595411226E-004,  0.13918590750170730E-004,  0.11314695675113133E-004,  0.99339469070408701E-005,  0.90828526933109137E-005,  0.81241291521243526E-005,  0.63456700137382176E-005,  0.40341429423471880E-005,  0.36216471879884789E-005,  0.37883487178745863E-005,  0.38931446968005245E-005,  0.39019874974905464E-005,  0.37801344838992346E-005,  0.39481066161748181E-005,  0.41839546354691520E-005,  0.40914833822327746E-005,  0.38801758859999014E-005,  0.37542078811788329E-005,  0.36194250512506980E-005,  0.34715129674633269E-005,  0.33419277645020538E-005,  0.31854618706019637E-005,  0.29604742525414688E-005,  0.28088490508478795E-005,  0.28878761679428137E-005,  0.26544530064356347E-005,  0.25496064976273713E-005,  0.23752829295449193E-005,  0.34645987934131378E-005,  0.30051477552177035E-005,  0.32632478551262198E-005,  0.34371159331417994E-005,  0.24154644509214473E-005,  0.20229911426904786E-005,  0.18716622326339654E-005,  0.17585549173924874E-005,  0.16105511623988671E-005,  0.14103588287308054E-005,  0.13156518947901387E-005,  0.12319187760520961E-005,  0.11576063893871300E-005,  0.10888602832350886E-005,  0.10236278726202881E-005,  0.99929673997627158E-006,  0.99119692249252847E-006,  0.10270326724621037E-005,  0.12196663329650962E-005,  0.14198617312348739E-005,  0.16798365032286347E-005,  0.16749092800375075E-005,  0.16024702615420612E-005,  0.15448696146741873E-005,  0.15138298128414719E-005,],]
