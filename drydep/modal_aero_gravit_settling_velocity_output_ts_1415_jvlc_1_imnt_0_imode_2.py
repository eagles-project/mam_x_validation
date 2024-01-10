# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1415 ] 
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
input.tair=[[  0.25205902783646221E+003,  0.26028670735281298E+003,  0.26722028708467542E+003,  0.27346557807535220E+003,  0.27046276211867075E+003,  0.26428473664744274E+003,  0.26112747502070664E+003,  0.25721295252469872E+003,  0.25120187173240046E+003,  0.24322661695839642E+003,  0.23624791507254696E+003,  0.23341539863247849E+003,  0.23147007655252119E+003,  0.22907170437314105E+003,  0.22465383376140622E+003,  0.21921200107022815E+003,  0.21326640824312426E+003,  0.20709062752935444E+003,  0.20090291606549405E+003,  0.19587405462478506E+003,  0.19073486045546608E+003,  0.18747938658476986E+003,  0.18680967005491061E+003,  0.18766362501921475E+003,  0.18932759531597441E+003,  0.19169678327222798E+003,  0.19310988510951725E+003,  0.18983684707564697E+003,  0.19082307290696986E+003,  0.19424030811043181E+003,  0.19799524089197891E+003,  0.20267760615698913E+003,  0.20760115204741470E+003,  0.21239352811989161E+003,  0.21692240825531891E+003,  0.22150896338577149E+003,  0.22597574791808529E+003,  0.23024744424286550E+003,  0.23465586018988276E+003,  0.23879208544918470E+003,  0.24299209468931090E+003,  0.24747335336575890E+003,  0.25215922924013321E+003,  0.25673066463284727E+003,  0.26090645516874361E+003,  0.26443420437887431E+003,  0.26675925319137019E+003,  0.26910300175744351E+003,  0.27093172711145104E+003,  0.27325736221769557E+003,  0.27515579300886895E+003,  0.27845924974434053E+003,  0.28168315971246534E+003,  0.28401430329329713E+003,  0.28603873829268611E+003,  0.28775496567470799E+003,  0.28913059063448691E+003,  0.29025206950617149E+003,  0.29118583778306117E+003,  0.29202224033701157E+003,  0.29276711098899227E+003,  0.29345249651016428E+003,  0.29404396551175256E+003,  0.29451318817158432E+003,  0.29479034804077133E+003,  0.29488057073854242E+003,  0.29496746255399677E+003,  0.29500341428532386E+003,  0.29477995291576144E+003,  0.29337445652319354E+003,  0.29314469701932870E+003,  0.29307482472540300E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473218866045947E+005,  0.19917079276155611E+005,  0.21462088974937011E+005,  0.23138402517824285E+005,  0.24957178984195634E+005,  0.26930525824485419E+005,  0.29071579154523624E+005,  0.31394591087164485E+005,  0.33915025432049784E+005,  0.36649661176407666E+005,  0.39616702852450137E+005,  0.42835901060419841E+005,  0.46279443167648526E+005,  0.49822313122480016E+005,  0.53348397543387939E+005,  0.56787065577667454E+005,  0.60104293311476060E+005,  0.63286021881395027E+005,  0.66289437061463250E+005,  0.69072488454763268E+005,  0.71594856933268355E+005,  0.73818924603016087E+005,  0.75710707041083355E+005,  0.77268767214200590E+005,  0.78586215787740701E+005,  0.79808614201537857E+005,  0.81001983500929709E+005,  0.82164407909474685E+005,  0.83294001139380096E+005,  0.84388914826206121E+005,  0.85447339983282800E+005,  0.86467506674494653E+005,  0.87447688602873633E+005,  0.88386214807499899E+005,  0.89281481118137744E+005,  0.90131946661924623E+005,  0.90940899350869222E+005,  0.91634393174759316E+005,  0.92071421225830636E+005,],]
input.radius_part=[[  0.13228719119515343E-007,  0.13209941342649694E-007,  0.15409149940597150E-007,  0.17643907474875849E-007,  0.20892709252197936E-007,  0.24697008672293503E-007,  0.27604320365996567E-007,  0.29559908648252491E-007,  0.32183819465576984E-007,  0.33945946365765312E-007,  0.35451301166423549E-007,  0.36337866795543404E-007,  0.37071444098440387E-007,  0.38002933448063113E-007,  0.38014566040129920E-007,  0.37234710366962508E-007,  0.38225673126630029E-007,  0.39825757745271422E-007,  0.38938437681268849E-007,  0.34182781829053431E-007,  0.29971955760022872E-007,  0.28342617224690674E-007,  0.28239217644223589E-007,  0.27205498725276965E-007,  0.26333134482645913E-007,  0.23776539474052554E-007,  0.16013590229161345E-007,  0.16308815400266119E-007,  0.18892330347339106E-007,  0.24376171608404120E-007,  0.27299207588906338E-007,  0.27823545625803293E-007,  0.28129419314576007E-007,  0.28745674646535325E-007,  0.29205825599491477E-007,  0.29609311668850366E-007,  0.31801541297754552E-007,  0.34247575038173317E-007,  0.35093957179932978E-007,  0.35602653024021566E-007,  0.36505714408910606E-007,  0.36717601108784673E-007,  0.36847621291261995E-007,  0.36995139065809294E-007,  0.39709891609984879E-007,  0.39020989187081668E-007,  0.40853016959627979E-007,  0.43193550664780764E-007,  0.43939883149664641E-007,  0.42949680029782355E-007,  0.49598558970773718E-007,  0.38760059361105438E-007,  0.35851128708676060E-007,  0.33400075065657059E-007,  0.31486226975551814E-007,  0.27464137044144536E-007,  0.24881161574743779E-007,  0.23670288986468582E-007,  0.22514767297346335E-007,  0.21918975756144034E-007,  0.21311564028730152E-007,  0.20759407549615097E-007,  0.20239124866548652E-007,  0.19937703854778333E-007,  0.19551958152471259E-007,  0.20359785267107008E-007,  0.21940481710856295E-007,  0.23705970873969026E-007,  0.25654941762208201E-007,  0.36937225088498575E-007,  0.43232626458218845E-007,  0.45378179487883512E-007,],]
input.density_part=[[  0.17708174412616895E+004,  0.17717455682260704E+004,  0.17719064749075362E+004,  0.17718891963390076E+004,  0.17718553200411552E+004,  0.17718366341484682E+004,  0.17715062209118760E+004,  0.17011910973562794E+004,  0.15985888365465410E+004,  0.15698018121463754E+004,  0.15517371964324227E+004,  0.15452452416230726E+004,  0.15389755727602630E+004,  0.15348308047220107E+004,  0.15222162183374194E+004,  0.14738459732729582E+004,  0.13545429763965576E+004,  0.12544442786384682E+004,  0.12177586303724213E+004,  0.11940341689314137E+004,  0.11805576374790876E+004,  0.11553905313541397E+004,  0.11392719024688029E+004,  0.11471421861095334E+004,  0.11522498479941307E+004,  0.11565727653616584E+004,  0.12012715305134348E+004,  0.11581061486546598E+004,  0.11303561282529295E+004,  0.10775439231401961E+004,  0.10639823138561433E+004,  0.10611898539818158E+004,  0.10600030441106226E+004,  0.10586341781986428E+004,  0.10574926768694827E+004,  0.10554491308105146E+004,  0.10449157336501523E+004,  0.10437132289284423E+004,  0.10435495641913485E+004,  0.10406666711549792E+004,  0.10379271066521969E+004,  0.10386823955349396E+004,  0.10404115973373787E+004,  0.10451039023278875E+004,  0.10389745954508965E+004,  0.10391739716797229E+004,  0.10311715004545326E+004,  0.10329988383346392E+004,  0.10527833410701787E+004,  0.10695705258717906E+004,  0.10603419619461704E+004,  0.11536613952158193E+004,  0.12287498493719042E+004,  0.12721474672620236E+004,  0.12935308007589374E+004,  0.13205852703123039E+004,  0.13598136049993827E+004,  0.14130654919743031E+004,  0.14645632341326723E+004,  0.15040574187044203E+004,  0.15402580810570767E+004,  0.15685753692930887E+004,  0.15902126836562929E+004,  0.15917768482895858E+004,  0.15849893272521369E+004,  0.15281465992609410E+004,  0.14245572046840587E+004,  0.13059955421958196E+004,  0.12365896279711114E+004,  0.10953058191318873E+004,  0.10643826594532613E+004,  0.10628610275112983E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.25718553554959895E-002,  0.17684692754341758E-002,  0.14157631101819695E-002,  0.11106775509176631E-002,  0.88584086077279358E-003,  0.70107508541638209E-003,  0.52746917941343325E-003,  0.36463470343695069E-003,  0.24973246037843130E-003,  0.17242546736573580E-003,  0.12143136130430863E-003,  0.87816725729248561E-004,  0.64915414776192353E-004,  0.49443219735492078E-004,  0.37287868362157703E-004,  0.27483294929025850E-004,  0.20633399209240708E-004,  0.16189801827926020E-004,  0.12738585691610566E-004,  0.92817312400296955E-005,  0.69407887151987253E-005,  0.56805715725647110E-005,  0.50691775449876721E-005,  0.45348839947195051E-005,  0.40839537813698664E-005,  0.34306463236434289E-005,  0.22107479175764232E-005,  0.19864018191008008E-005,  0.20817632406258004E-005,  0.23945891625320449E-005,  0.24737136859127133E-005,  0.23491038034532685E-005,  0.22165547880294746E-005,  0.21192852351208480E-005,  0.20201630194178582E-005,  0.19208533420100035E-005,  0.19221291036118115E-005,  0.19452419604472302E-005,  0.18711896053171142E-005,  0.17751280179071488E-005,  0.17031019253883656E-005,  0.16069641075665058E-005,  0.15142229513224099E-005,  0.14310402135884628E-005,  0.14371257715086655E-005,  0.13206329625112770E-005,  0.12920859307436321E-005,  0.12978392679414800E-005,  0.12780088379081253E-005,  0.12073122019628033E-005,  0.13484500833902295E-005,  0.10721229949169331E-005,  0.10138347785392950E-005,  0.94291869222634589E-006,  0.87648729725688346E-006,  0.75514028776360148E-006,  0.68716266352929272E-006,  0.66729949780106905E-006,  0.64698852005790770E-006,  0.63752884652676869E-006,  0.62585005658934255E-006,  0.61248452115227210E-006,  0.59751728016973174E-006,  0.58218461865889635E-006,  0.56171278119651497E-006,  0.55965238291410194E-006,  0.55978725459999627E-006,  0.55279853579221764E-006,  0.56529834035263403E-006,  0.74383563659864580E-006,  0.86019573499270707E-006,  0.90519004314816101E-006,],]
