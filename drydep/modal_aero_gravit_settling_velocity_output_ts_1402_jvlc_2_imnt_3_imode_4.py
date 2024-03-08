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
input.radius_part=[[  0.21129217207483959E-007,  0.22671004185212538E-007,  0.25679557922434864E-007,  0.28318839442694632E-007,  0.30843852923578290E-007,  0.35382600730656210E-007,  0.40144266147579296E-007,  0.42655971411615332E-007,  0.44260059018536392E-007,  0.46248025384134963E-007,  0.48091038117430268E-007,  0.49865706927544524E-007,  0.51191898570917147E-007,  0.52397674275861967E-007,  0.54863986104297122E-007,  0.59984577545285604E-007,  0.64900684747003132E-007,  0.67031307009719440E-007,  0.68012662591007107E-007,  0.69155526764937788E-007,  0.69504126704678465E-007,  0.69639280191584522E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69567114822805721E-007,  0.69642718984836201E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642719104290200E-007,  0.69642718832189588E-007,  0.69642719232615004E-007,  0.69642720020108827E-007,  0.69642720359353437E-007,  0.69642720548464144E-007,  0.69642721714524943E-007,  0.69642723353659441E-007,  0.69642720974923276E-007,  0.69642719729524579E-007,  0.69642719292057778E-007,  0.69642719126340189E-007,  0.69642719092297511E-007,  0.69642719103726725E-007,  0.69642719124879533E-007,  0.69642719146690076E-007,  0.69642719162100742E-007,  0.69642719172731813E-007,  0.69642719198236239E-007,  0.69642719235880197E-007,  0.69642719306055500E-007,  0.69642719350336027E-007,  0.69642719841051316E-007,  0.69642719846902435E-007,  0.69642719701241845E-007,  0.69642719563613748E-007,  0.69642719452299206E-007,  0.69642719372731022E-007,  0.69642719327744427E-007,],]
input.density_part=[[  0.10467909958569928E+004,  0.10463768587383715E+004,  0.10464781820643482E+004,  0.10463158833514440E+004,  0.10456837861165677E+004,  0.10452359728579356E+004,  0.10452880708964869E+004,  0.10450304763874353E+004,  0.10446343999373314E+004,  0.10447096809958100E+004,  0.10437619282788366E+004,  0.10421511953142538E+004,  0.10403401717417826E+004,  0.10366011112871063E+004,  0.10327267431495727E+004,  0.10384985023408904E+004,  0.10526422088264819E+004,  0.10673472333051807E+004,  0.10686155735838138E+004,  0.10644725018762415E+004,  0.10576567937476668E+004,  0.10566941600766620E+004,  0.10566303704194088E+004,  0.10579787464086405E+004,  0.10581421324075161E+004,  0.10585661151188649E+004,  0.10601568315582908E+004,  0.10638325759292200E+004,  0.10648878977597833E+004,  0.10657331021325394E+004,  0.10646444419406569E+004,  0.10617635639224388E+004,  0.10614408840192837E+004,  0.10603324218645955E+004,  0.10580993789353736E+004,  0.10578778519790487E+004,  0.10576562977031524E+004,  0.10580909106060644E+004,  0.10582090492114974E+004,  0.10579803990507576E+004,  0.10578548311761162E+004,  0.10581285746926412E+004,  0.10583218589108355E+004,  0.10591708632133589E+004,  0.10609775969794537E+004,  0.10569786242650391E+004,  0.10526823438724864E+004,  0.10486149072785383E+004,  0.10443594325163674E+004,  0.10436210546914785E+004,  0.10435093563300320E+004,  0.10434478481860997E+004,  0.10434354353406293E+004,  0.10433323001409829E+004,  0.10432176758479204E+004,  0.10433540361298881E+004,  0.10436926383213693E+004,  0.10437068374551936E+004,  0.10437251768065760E+004,  0.10441449240378390E+004,  0.10445549585808951E+004,  0.10454856350389994E+004,  0.10457538018578466E+004,  0.10464197859975702E+004,  0.10552042122105395E+004,  0.10617291222406543E+004,  0.10628784615799489E+004,  0.10633417729082389E+004,  0.10636269618308372E+004,  0.10638087123985990E+004,  0.10639075295907448E+004,  0.10639468101216539E+004,],]
input.sig_part=[[  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.47134958187296959E-002,  0.34436184115617338E-002,  0.26756937932271405E-002,  0.20088934286249297E-002,  0.14904341658907301E-002,  0.11564203093388317E-002,  0.88542058598790896E-003,  0.63246242784487778E-003,  0.43800582525445098E-003,  0.30487271261392992E-003,  0.21588031159451440E-003,  0.15829178835853917E-003,  0.11807206956972250E-003,  0.89769770004806296E-004,  0.71122801065279907E-004,  0.60771483460273827E-004,  0.53222164966844892E-004,  0.45714703958898548E-004,  0.38876629799035438E-004,  0.33689564183021633E-004,  0.29351414227490061E-004,  0.26225017531630512E-004,  0.23945483340226118E-004,  0.22203666099295154E-004,  0.20632707234566560E-004,  0.19234785846287307E-004,  0.17862479683575588E-004,  0.16600919706431042E-004,  0.15506189848087734E-004,  0.14547769762545429E-004,  0.13620432377253875E-004,  0.12735252987065778E-004,  0.11951723399641975E-004,  0.11241612962739898E-004,  0.10594282153589613E-004,  0.10008431017277746E-004,  0.94543672287082743E-005,  0.89367285098584945E-005,  0.84469222102927874E-005,  0.79826857540312975E-005,  0.75447275171526054E-005,  0.71340477079954409E-005,  0.67474517751726120E-005,  0.63858101737590367E-005,  0.60525639041567881E-005,  0.57116620483923171E-005,  0.54054478916206508E-005,  0.51397583486256859E-005,  0.49098280268629680E-005,  0.47285574246442571E-005,  0.45742374219399612E-005,  0.44421472641936696E-005,  0.43297708834191737E-005,  0.42344911356107942E-005,  0.41553440014586155E-005,  0.40923429286095957E-005,  0.40435554136431221E-005,  0.40027162136851176E-005,  0.39659859645721709E-005,  0.39326711522381798E-005,  0.39011471556110062E-005,  0.38733373001553874E-005,  0.38448164416437830E-005,  0.38194332690728149E-005,  0.38253147567570859E-005,  0.38244112555390510E-005,  0.38049498357461088E-005,  0.37844013013607150E-005,  0.37646515924188721E-005,  0.37458436229730717E-005,  0.37297355597376272E-005,  0.37195835755859267E-005,],]