# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1402 ] 
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
input.tair=[[  0.25232232923622604E+003,  0.25522850512227134E+003,  0.26176226900334717E+003,  0.26457486529546043E+003,  0.26793180799705624E+003,  0.26738902284023789E+003,  0.26535302872108713E+003,  0.26142672726892107E+003,  0.25388280936575069E+003,  0.24523836651544980E+003,  0.23748249607705534E+003,  0.23407073249899270E+003,  0.23181877734084958E+003,  0.22906960716189772E+003,  0.22322239956364686E+003,  0.21605832956074806E+003,  0.20959245596895690E+003,  0.20508043272871981E+003,  0.20062832746428623E+003,  0.19674105362241701E+003,  0.19280715340680251E+003,  0.19033589213142096E+003,  0.18952171047901805E+003,  0.18988191314754633E+003,  0.19055861118063132E+003,  0.19249933242357099E+003,  0.19222372632229619E+003,  0.18959277255089239E+003,  0.19127406447560395E+003,  0.19537034573403014E+003,  0.19916617913783080E+003,  0.20298917487640657E+003,  0.20746834534468334E+003,  0.21218901888406791E+003,  0.21680267600651410E+003,  0.22127269780566485E+003,  0.22578082437477312E+003,  0.23034575687204193E+003,  0.23511925810334233E+003,  0.23999181860768829E+003,  0.24470926070671629E+003,  0.24922826392790057E+003,  0.25374017446819812E+003,  0.25761338118511446E+003,  0.26149186960175479E+003,  0.26470836184862856E+003,  0.26718132860967387E+003,  0.26902831999029996E+003,  0.27047534528594178E+003,  0.27312051529546841E+003,  0.27524743223929107E+003,  0.27783230633111083E+003,  0.28097073046738933E+003,  0.28376825188748217E+003,  0.28609385939223745E+003,  0.28780138977040508E+003,  0.28896323227885756E+003,  0.28989401324620326E+003,  0.29076038024008557E+003,  0.29156578095749529E+003,  0.29229989738437251E+003,  0.29294965383799780E+003,  0.29349146382376227E+003,  0.29398511017304327E+003,  0.29411890340867870E+003,  0.29404348358960658E+003,  0.29473857219311213E+003,  0.29553850120759466E+003,  0.29633692812215287E+003,  0.29712029375206879E+003,  0.29781940614560722E+003,  0.29829626824169117E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473554968189153E+005,  0.19918254765368849E+005,  0.21464313806170401E+005,  0.23141765870577179E+005,  0.24961777616675870E+005,  0.26936464718045965E+005,  0.29078972212175671E+005,  0.31403561891319154E+005,  0.33925708068523170E+005,  0.36662201127378568E+005,  0.39631257963617754E+005,  0.42852642591430355E+005,  0.46298523488951840E+005,  0.49843799696342743E+005,  0.53372278969350395E+005,  0.56813282483794377E+005,  0.60132763217746084E+005,  0.63316652758894466E+005,  0.66322107802946819E+005,  0.69107049393522466E+005,  0.71631131018585816E+005,  0.73856709234437323E+005,  0.75749776536603735E+005,  0.77308894915749552E+005,  0.78627238276121090E+005,  0.79850466920008257E+005,  0.81044646733524962E+005,  0.82207860639255348E+005,  0.83338221068067360E+005,  0.84433878400490925E+005,  0.85493022420788824E+005,  0.86513881990260576E+005,  0.87494729640001242E+005,  0.88433893274679664E+005,  0.89329767634009942E+005,  0.90180810798112332E+005,  0.90990279003308649E+005,  0.91684169352428667E+005,  0.92121434798927206E+005,],]
input.radius_part=[[  0.13258480054051913E-007,  0.13885693221370384E-007,  0.17139911485125618E-007,  0.18778453906301702E-007,  0.20272508350004758E-007,  0.24365443849964974E-007,  0.27523664526917532E-007,  0.29495239737280013E-007,  0.31977079081553197E-007,  0.34009966852376912E-007,  0.35516645720951672E-007,  0.36364446413434681E-007,  0.37094892051873635E-007,  0.38033188577163718E-007,  0.37918510480034694E-007,  0.37311551142033558E-007,  0.38500004242713164E-007,  0.40015242188362402E-007,  0.39334189054812393E-007,  0.34662569697474427E-007,  0.30272219191268518E-007,  0.28037675336852892E-007,  0.27543375838677484E-007,  0.27393018970274707E-007,  0.26656613892811949E-007,  0.23053694836467734E-007,  0.15222365754536820E-007,  0.14849126793274562E-007,  0.16821741694255478E-007,  0.19258337577115765E-007,  0.21247551645327680E-007,  0.23648267786727269E-007,  0.27437670795287736E-007,  0.29488990345564872E-007,  0.30161203055878820E-007,  0.30579758959993402E-007,  0.31512931034310665E-007,  0.32400885681034262E-007,  0.32982525015844627E-007,  0.33266346883277996E-007,  0.33222788927119268E-007,  0.32934949675623850E-007,  0.33732534142953226E-007,  0.36619168298466795E-007,  0.35842595541875410E-007,  0.38558037959782650E-007,  0.42460155543168828E-007,  0.44538560105672732E-007,  0.44452164402967798E-007,  0.42338510317926454E-007,  0.47708843282120728E-007,  0.39920485081103771E-007,  0.33689680497750504E-007,  0.30504227601628652E-007,  0.28371423957845386E-007,  0.26820235038786555E-007,  0.23890006444669367E-007,  0.22611915060257835E-007,  0.21347746775643577E-007,  0.20453207859983450E-007,  0.20246470655979785E-007,  0.19853930207590234E-007,  0.19321831345773588E-007,  0.20388779715159884E-007,  0.25018936632574035E-007,  0.30080221596742172E-007,  0.30540471344039692E-007,  0.29760311620309488E-007,  0.28880843165980555E-007,  0.28084110603893910E-007,  0.27463128206928697E-007,  0.27090898328440134E-007,],]
input.density_part=[[  0.17711420076083177E+004,  0.17717893760669724E+004,  0.17718507082349561E+004,  0.17718851872291405E+004,  0.17718638299812021E+004,  0.17718645615084536E+004,  0.17707233657541137E+004,  0.17061113164674039E+004,  0.16042517440003039E+004,  0.15686486847336291E+004,  0.15510422611408162E+004,  0.15448938427395819E+004,  0.15388620629947516E+004,  0.15343870827937853E+004,  0.15186289311171281E+004,  0.14532645423205570E+004,  0.13340634676422319E+004,  0.12546577887806741E+004,  0.12228079499002745E+004,  0.11960819340634835E+004,  0.11828406718518063E+004,  0.11721810891940952E+004,  0.11560024423252401E+004,  0.11502130369944850E+004,  0.11506964335910311E+004,  0.11570038898858793E+004,  0.12154204538289189E+004,  0.11782739538740648E+004,  0.11577334231357634E+004,  0.11326505214840658E+004,  0.10992695117546471E+004,  0.10531302226868604E+004,  0.10303834775073610E+004,  0.10252815819608822E+004,  0.10226179777374495E+004,  0.10219325306656389E+004,  0.10213885503127294E+004,  0.10227621324279726E+004,  0.10328448608662045E+004,  0.10466567046289379E+004,  0.10562338622824507E+004,  0.10592761734647156E+004,  0.10564611583513185E+004,  0.10487758325172167E+004,  0.10596025770710053E+004,  0.10471313861809672E+004,  0.10352661174103614E+004,  0.10360018699592115E+004,  0.10507778357250202E+004,  0.10800773196003327E+004,  0.10718727453702095E+004,  0.11439748954725774E+004,  0.12528959485217617E+004,  0.13389276773795996E+004,  0.13918326066760433E+004,  0.14269576990125602E+004,  0.14549204773277693E+004,  0.14593964538655177E+004,  0.14807482093691463E+004,  0.15029537441745094E+004,  0.15058403125660088E+004,  0.14792290322105480E+004,  0.14793835922016101E+004,  0.14860112881938292E+004,  0.14429103919516494E+004,  0.12790421703822074E+004,  0.12684674857832895E+004,  0.12904038915339413E+004,  0.13176694456078478E+004,  0.13452978429940986E+004,  0.13690991033803664E+004,  0.13844485748575344E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.50042981946435590E-002,  0.35713287612913576E-002,  0.30237516450880735E-002,  0.22558000090853784E-002,  0.16598162271200822E-002,  0.13498425159583719E-002,  0.10282295636576651E-002,  0.71383155292038889E-003,  0.48583259846157116E-003,  0.33648365394821117E-003,  0.23675341982721032E-003,  0.17093429028006537E-003,  0.12635690233611413E-003,  0.96239420724434239E-004,  0.72030816139858670E-004,  0.52568130615807336E-004,  0.39634636102679197E-004,  0.31688920693437172E-004,  0.25318592754002594E-004,  0.18537821297467557E-004,  0.13856961779296862E-004,  0.11275355338248234E-004,  0.99271039504179129E-005,  0.90615023458020901E-005,  0.81573420964132174E-005,  0.65557585982723829E-005,  0.41543998702918174E-005,  0.36018998866205622E-005,  0.37292523926415018E-005,  0.39125761245317231E-005,  0.39199731672796025E-005,  0.39157249154448417E-005,  0.41840529466075561E-005,  0.42126487971944474E-005,  0.40471552469694254E-005,  0.38607980050930455E-005,  0.37477947672362982E-005,  0.36360781057179209E-005,  0.35202187220993109E-005,  0.33856992787963776E-005,  0.32064386521172141E-005,  0.29918391860287665E-005,  0.28785017387916258E-005,  0.29428002656968790E-005,  0.27253963257717130E-005,  0.27531756264929559E-005,  0.28753591821658855E-005,  0.28894072640452869E-005,  0.27870928898832702E-005,  0.25878869339762107E-005,  0.28668298869084556E-005,  0.23722418772632702E-005,  0.20538036371065695E-005,  0.18994869633356104E-005,  0.17720522177916189E-005,  0.16686852107661935E-005,  0.14647712744745152E-005,  0.13611946220559766E-005,  0.12776770335765455E-005,  0.12207458782246122E-005,  0.11952301933803389E-005,  0.11356863863932189E-005,  0.10897124458820371E-005,  0.11513827947973226E-005,  0.14014621679179134E-005,  0.15320706079710425E-005,  0.15353853761845806E-005,  0.15027278082599494E-005,  0.14698172559737776E-005,  0.14416643113438561E-005,  0.14205684095019433E-005,  0.14084360366145254E-005,],]
