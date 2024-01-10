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
input.moment=[[         0],]
input.ncol=[[         4],]
input.pcols=[[         4],]
input.nver=[[        72],]
input.radius_max=[[  0.50000000000000002E-004],]
input.tair=[[  0.25232232923622604E+003,  0.25522850512227134E+003,  0.26176226900334717E+003,  0.26457486529546043E+003,  0.26793180799705624E+003,  0.26738902284023789E+003,  0.26535302872108713E+003,  0.26142672726892107E+003,  0.25388280936575069E+003,  0.24523836651544980E+003,  0.23748249607705534E+003,  0.23407073249899270E+003,  0.23181877734084958E+003,  0.22906960716189772E+003,  0.22322239956364686E+003,  0.21605832956074806E+003,  0.20959245596895690E+003,  0.20508043272871981E+003,  0.20062832746428623E+003,  0.19674105362241701E+003,  0.19280715340680251E+003,  0.19033589213142096E+003,  0.18952171047901805E+003,  0.18988191314754633E+003,  0.19055861118063132E+003,  0.19249933242357099E+003,  0.19222372632229619E+003,  0.18959277255089239E+003,  0.19127406447560395E+003,  0.19537034573403014E+003,  0.19916617913783080E+003,  0.20298917487640657E+003,  0.20746834534468334E+003,  0.21218901888406791E+003,  0.21680267600651410E+003,  0.22127269780566485E+003,  0.22578082437477312E+003,  0.23034575687204193E+003,  0.23511925810334233E+003,  0.23999181860768829E+003,  0.24470926070671629E+003,  0.24922826392790057E+003,  0.25374017446819812E+003,  0.25761338118511446E+003,  0.26149186960175479E+003,  0.26470836184862856E+003,  0.26718132860967387E+003,  0.26902831999029996E+003,  0.27047534528594178E+003,  0.27312051529546841E+003,  0.27524743223929107E+003,  0.27783230633111083E+003,  0.28097073046738933E+003,  0.28376825188748217E+003,  0.28609385939223745E+003,  0.28780138977040508E+003,  0.28896323227885756E+003,  0.28989401324620326E+003,  0.29076038024008557E+003,  0.29156578095749529E+003,  0.29229989738437251E+003,  0.29294965383799780E+003,  0.29349146382376227E+003,  0.29398511017304327E+003,  0.29411890340867870E+003,  0.29404348358960658E+003,  0.29473857219311213E+003,  0.29553850120759466E+003,  0.29633692812215287E+003,  0.29712029375206879E+003,  0.29781940614560722E+003,  0.29829626824169117E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473554968189153E+005,  0.19918254765368849E+005,  0.21464313806170401E+005,  0.23141765870577179E+005,  0.24961777616675870E+005,  0.26936464718045965E+005,  0.29078972212175671E+005,  0.31403561891319154E+005,  0.33925708068523170E+005,  0.36662201127378568E+005,  0.39631257963617754E+005,  0.42852642591430355E+005,  0.46298523488951840E+005,  0.49843799696342743E+005,  0.53372278969350395E+005,  0.56813282483794377E+005,  0.60132763217746084E+005,  0.63316652758894466E+005,  0.66322107802946819E+005,  0.69107049393522466E+005,  0.71631131018585816E+005,  0.73856709234437323E+005,  0.75749776536603735E+005,  0.77308894915749552E+005,  0.78627238276121090E+005,  0.79850466920008257E+005,  0.81044646733524962E+005,  0.82207860639255348E+005,  0.83338221068067360E+005,  0.84433878400490925E+005,  0.85493022420788824E+005,  0.86513881990260576E+005,  0.87494729640001242E+005,  0.88433893274679664E+005,  0.89329767634009942E+005,  0.90180810798112332E+005,  0.90990279003308649E+005,  0.91684169352428667E+005,  0.92121434798927206E+005,],]
input.radius_part=[[  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.15441481793762473E-005,  0.19688809097530009E-005,  0.22695789207418349E-005,  0.25689617987519848E-005,  0.28490575514483289E-005,  0.30755973253136908E-005,  0.32232685540058583E-005,  0.33327883341664542E-005,  0.33581389134597751E-005,  0.25908337972859629E-005,  0.14663869755516159E-005,  0.99150484891052332E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.88320320659120629E-006,  0.89725954783537648E-006,  0.90600282642823166E-006,  0.91952392141054406E-006,  0.94377384427490810E-006,  0.95841365752749982E-006,  0.96250832810762637E-006,  0.96114175154427303E-006,  0.95371832206373081E-006,  0.93857336876980859E-006,  0.92950509978326314E-006,  0.92040555542027122E-006,  0.91529903931393948E-006,  0.91648987138194392E-006,  0.92322561760449679E-006,  0.93880645627860421E-006,  0.10757647524582827E-005,  0.95656456712501590E-006,  0.11427146788344377E-005,  0.14431094354352871E-005,  0.15678377278619547E-005,  0.15508701679586136E-005,  0.17205124640451447E-005,  0.20773239319748418E-005,  0.16570612964549649E-005,  0.13330810812722344E-005,  0.11789865912434959E-005,  0.11078394364448144E-005,  0.10800362373685587E-005,  0.10732018978316916E-005,  0.10749031618321165E-005,  0.10777990230334663E-005,  0.10815308841547457E-005,  0.10848165108537945E-005,  0.10939623948399083E-005,  0.11057512964893475E-005,  0.11289747832852708E-005,  0.11797083707086011E-005,  0.14036491655315690E-005,  0.14256444154234519E-005,  0.13832820723134159E-005,  0.13363866250771940E-005,  0.12943152350509159E-005,  0.12617071606636510E-005,  0.12422117431183407E-005,],]
input.density_part=[[  0.10000000000000000E+001,  0.10000000000000000E+001,  0.17699999490651269E+004,  0.17699999999427903E+004,  0.17699999999999218E+004,  0.17699999999999995E+004,  0.17700000000000000E+004,  0.17700000000000002E+004,  0.17700000000000000E+004,  0.17700000000000000E+004,  0.17700000000000005E+004,  0.17700000000001457E+004,  0.17700000000250252E+004,  0.17700000025111008E+004,  0.17700001581428135E+004,  0.17700165791495942E+004,  0.17711576892265773E+004,  0.17858121102806290E+004,  0.18462339545598431E+004,  0.18703711852699366E+004,  0.18775897056639960E+004,  0.18600690202435767E+004,  0.17684320284815826E+004,  0.18093119877965116E+004,  0.19016201909741042E+004,  0.19247114692850091E+004,  0.18814036671742285E+004,  0.17131505677432749E+004,  0.17755713220822768E+004,  0.17882674162576127E+004,  0.18331004583211584E+004,  0.18491363925538822E+004,  0.18540668135991102E+004,  0.18628366248244683E+004,  0.18686704256823484E+004,  0.18778132377036295E+004,  0.18902815993283432E+004,  0.19049020540775916E+004,  0.19253876490226546E+004,  0.19344817788376465E+004,  0.19280756214109281E+004,  0.19032764662361542E+004,  0.18579085958037190E+004,  0.15700842331442016E+004,  0.18159319111529460E+004,  0.14736552636867621E+004,  0.12314798432969089E+004,  0.11709335294382108E+004,  0.11780415841858965E+004,  0.11593101120019865E+004,  0.11079936721848030E+004,  0.12455436973362562E+004,  0.14725835514555240E+004,  0.16750146901655971E+004,  0.18017780814636124E+004,  0.18417037893530969E+004,  0.18318393763872793E+004,  0.18115056021801011E+004,  0.17973179212464217E+004,  0.17825220784545334E+004,  0.17644897548390488E+004,  0.17342930195281831E+004,  0.16991217406125709E+004,  0.16505794707946709E+004,  0.15458869038836656E+004,  0.13083479460915594E+004,  0.12910239668958611E+004,  0.13171070631186985E+004,  0.13506626712383108E+004,  0.13852719150268426E+004,  0.14155071249446871E+004,  0.14352063409649943E+004,],]
input.sig_part=[[  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.98183505050811683E-004,  0.66890640121017219E-004,  0.81226134256419016E-001,  0.55327251751078131E-001,  0.37728541444409736E-001,  0.25547436040656738E-001,  0.31842573229266792E-001,  0.27469216042731139E-001,  0.21354513940579963E-001,  0.16385254795389811E-001,  0.12740263562466443E-001,  0.10129303038604416E-001,  0.81322840000510512E-002,  0.66989030656644062E-002,  0.55616720078543831E-002,  0.33448966458943926E-002,  0.13765930868528532E-002,  0.73629715771826620E-003,  0.53983617705764852E-003,  0.48413091054640568E-003,  0.43964512373654581E-003,  0.40209948121427297E-003,  0.35913651817631953E-003,  0.34867617494993135E-003,  0.34888572499661142E-003,  0.33657981373142745E-003,  0.31453529559424787E-003,  0.29677749840015320E-003,  0.30243975438303824E-003,  0.29635600147924767E-003,  0.29850375300844112E-003,  0.30173191059452135E-003,  0.29827543325883541E-003,  0.29074597743142635E-003,  0.28099791325991063E-003,  0.26954013425133176E-003,  0.25555990463110970E-003,  0.24520744608689393E-003,  0.23595510312911195E-003,  0.22741665800664080E-003,  0.22019985892916106E-003,  0.21362048771128860E-003,  0.20852021023357639E-003,  0.21820246278404814E-003,  0.19975362969226418E-003,  0.21787840187790958E-003,  0.27433655919426774E-003,  0.30020934720899009E-003,  0.29258450701132586E-003,  0.34555832464484160E-003,  0.46767720887182712E-003,  0.33829050295534679E-003,  0.26225676819442505E-003,  0.23454299576230011E-003,  0.22262623723372886E-003,  0.21550000161199239E-003,  0.21070110877434786E-003,  0.20806983440107584E-003,  0.20665253568904928E-003,  0.20550470341929500E-003,  0.20386758931417983E-003,  0.20289211937993932E-003,  0.20221823854388630E-003,  0.20369157891045463E-003,  0.20680828856500764E-003,  0.24276960690417963E-003,  0.24608200222658969E-003,  0.23641542056684041E-003,  0.22646712027944171E-003,  0.21803613869013374E-003,  0.21180083080533737E-003,  0.20819688487914932E-003,],]
