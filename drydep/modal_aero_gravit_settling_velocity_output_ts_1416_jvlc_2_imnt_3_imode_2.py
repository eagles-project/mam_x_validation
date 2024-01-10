# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1416 ] 
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
input.tair=[[  0.25144410893671036E+003,  0.25812433827533152E+003,  0.26580775404125166E+003,  0.27323771278935965E+003,  0.27177715881621037E+003,  0.26540996998296708E+003,  0.26164230554443100E+003,  0.25758674211237144E+003,  0.25180556738828949E+003,  0.24384210606168361E+003,  0.23647419617832571E+003,  0.23330229939472315E+003,  0.23117205435857420E+003,  0.22866485826241600E+003,  0.22430471396568103E+003,  0.21905327760613466E+003,  0.21334979432186518E+003,  0.20731716174920092E+003,  0.20114144719238047E+003,  0.19613560078802192E+003,  0.19100703009995300E+003,  0.18764402381548081E+003,  0.18686407761529486E+003,  0.18768216754254274E+003,  0.18936395947578876E+003,  0.19175716997635283E+003,  0.19343366942391191E+003,  0.19018833183371356E+003,  0.19085206940362684E+003,  0.19393682039533110E+003,  0.19802159127821966E+003,  0.20274314757214617E+003,  0.20759224249302881E+003,  0.21231648303463595E+003,  0.21686026064036477E+003,  0.22142788815031270E+003,  0.22581042517750851E+003,  0.23007958152692535E+003,  0.23445404112066024E+003,  0.23869818498189213E+003,  0.24289670228816374E+003,  0.24736665011643021E+003,  0.25197256256794370E+003,  0.25647062315835262E+003,  0.26076928659937062E+003,  0.26425417370680253E+003,  0.26669346442502336E+003,  0.26914521902341966E+003,  0.27074913014395344E+003,  0.27314029392270254E+003,  0.27513968991062910E+003,  0.27820159717926134E+003,  0.28160446485959284E+003,  0.28400566772826198E+003,  0.28599477737936888E+003,  0.28769590644672650E+003,  0.28906273331673344E+003,  0.29017823563791183E+003,  0.29111809314535492E+003,  0.29195725292208363E+003,  0.29269824537746325E+003,  0.29337239462779701E+003,  0.29395778163080297E+003,  0.29443688390465218E+003,  0.29472532865076897E+003,  0.29479015230497123E+003,  0.29482937810614197E+003,  0.29468111518867778E+003,  0.29437876148125508E+003,  0.29284891410254369E+003,  0.29278536368806635E+003,  0.29292335014772743E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472897414197338E+005,  0.19915955025125808E+005,  0.21459961121463657E+005,  0.23135185769636846E+005,  0.24952780800662033E+005,  0.26924845800265597E+005,  0.29064508351503828E+005,  0.31386011309744608E+005,  0.33904808439055749E+005,  0.36637667827056655E+005,  0.39602782181350143E+005,  0.42819889272929940E+005,  0.46261194534966373E+005,  0.49801763122939345E+005,  0.53325557080515900E+005,  0.56761991435446929E+005,  0.60077064374721893E+005,  0.63256726167589492E+005,  0.66258190398930179E+005,  0.69039433986416479E+005,  0.71560163992393995E+005,  0.73782786958954661E+005,  0.75673340538628050E+005,  0.77230388631664930E+005,  0.78546981421072473E+005,  0.79768585793526523E+005,  0.80961179908144899E+005,  0.82122849232752269E+005,  0.83251708705043318E+005,  0.84345911160903197E+005,  0.85403648789155573E+005,  0.86423152803850739E+005,  0.87402698028874220E+005,  0.88340614588269804E+005,  0.89235299354337985E+005,  0.90085212455595218E+005,  0.90893672099031319E+005,  0.91586786681756945E+005,  0.92023587685186707E+005,],]
input.radius_part=[[  0.13169245886353107E-007,  0.13334770837093341E-007,  0.15488483409692411E-007,  0.17571204878831349E-007,  0.20794216591469485E-007,  0.24571083966615453E-007,  0.27536355286326726E-007,  0.29491601128383754E-007,  0.32135730148792194E-007,  0.33884945279978616E-007,  0.35426531134934687E-007,  0.36335508773693986E-007,  0.37075026640938847E-007,  0.38010559493013459E-007,  0.38008466730312609E-007,  0.37230842918133734E-007,  0.38206631322899042E-007,  0.39812058273284293E-007,  0.38979165906536778E-007,  0.34256333584309985E-007,  0.30050788570000314E-007,  0.28291368600919693E-007,  0.28209342367541173E-007,  0.27190012572889746E-007,  0.26377463998718347E-007,  0.24103807659852563E-007,  0.16298714568311347E-007,  0.16375558736143899E-007,  0.18966542932118892E-007,  0.25519702592914620E-007,  0.27419270840259343E-007,  0.27792273029274507E-007,  0.28089701057367317E-007,  0.28696816343352385E-007,  0.29085661439834247E-007,  0.29591301483669763E-007,  0.32168921094719572E-007,  0.34483963519939182E-007,  0.35142810331214729E-007,  0.35506050525140942E-007,  0.36428606821358460E-007,  0.36653681291670408E-007,  0.36860170947370751E-007,  0.37097359814497866E-007,  0.39407212424841675E-007,  0.38613532067811526E-007,  0.40946175577709327E-007,  0.43306764887236211E-007,  0.44898078051390377E-007,  0.44192660335526461E-007,  0.50092274834061926E-007,  0.39667788748390104E-007,  0.35383509824998987E-007,  0.33074727676709900E-007,  0.31474610773042009E-007,  0.27243413883448939E-007,  0.24514962508771954E-007,  0.23318678805390745E-007,  0.22221203831782592E-007,  0.21606992630154708E-007,  0.21036738840298818E-007,  0.20513443303585104E-007,  0.20046235425112762E-007,  0.19759470654702138E-007,  0.19330665087440513E-007,  0.19996122137905889E-007,  0.21654401402050209E-007,  0.23755100867223210E-007,  0.26151998696246538E-007,  0.42240759017729134E-007,  0.42693148646832506E-007,  0.42804806300252946E-007,],]
input.density_part=[[  0.17708595331284173E+004,  0.17717729725513916E+004,  0.17719099500381260E+004,  0.17718900461632813E+004,  0.17718538995731155E+004,  0.17718434938569217E+004,  0.17715317786489095E+004,  0.17041631764010986E+004,  0.16000758408516597E+004,  0.15705919733705562E+004,  0.15520014311015982E+004,  0.15452602364626887E+004,  0.15389659230398249E+004,  0.15347832411278789E+004,  0.15220075294146304E+004,  0.14738203064840234E+004,  0.13559325277372345E+004,  0.12551663622203189E+004,  0.12179558518591305E+004,  0.11940702318338788E+004,  0.11807859026084382E+004,  0.11569083153242816E+004,  0.11398271918873913E+004,  0.11473042023245698E+004,  0.11522811485377379E+004,  0.11559674104748487E+004,  0.11977772340989068E+004,  0.11581554297758289E+004,  0.11306302678710567E+004,  0.10750450006860924E+004,  0.10632069526299899E+004,  0.10600626084929575E+004,  0.10586652753156097E+004,  0.10570141663970951E+004,  0.10557351013091286E+004,  0.10535897088435254E+004,  0.10454175285829756E+004,  0.10427278614757504E+004,  0.10419561568157437E+004,  0.10400825393761631E+004,  0.10380507446784350E+004,  0.10388677311817282E+004,  0.10402748839502253E+004,  0.10444863904139945E+004,  0.10392841972092758E+004,  0.10395222331073908E+004,  0.10310124740443107E+004,  0.10328684847530915E+004,  0.10489725245542093E+004,  0.10648424618657230E+004,  0.10598506186172519E+004,  0.11461915288258811E+004,  0.12260242656265941E+004,  0.12712241136670680E+004,  0.12906229717687479E+004,  0.13172955147152061E+004,  0.13534265339476301E+004,  0.14106298742109318E+004,  0.14647525111247799E+004,  0.15051384981950678E+004,  0.15379667153778726E+004,  0.15629213919974827E+004,  0.15836218466825087E+004,  0.15852689659269945E+004,  0.15822370430890628E+004,  0.15323914835340088E+004,  0.14298688637948383E+004,  0.12897822844223003E+004,  0.12201508142510406E+004,  0.10649565941510637E+004,  0.10651356963559879E+004,  0.10649999726827416E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.49611682332788157E-002,  0.34489999212643893E-002,  0.27535271540793092E-002,  0.21450469622114471E-002,  0.17146965287562468E-002,  0.13561761640457875E-002,  0.10219575396841147E-002,  0.70767956155305841E-003,  0.48498177025173696E-003,  0.33470679371372576E-003,  0.23579806515960136E-003,  0.17055992236414110E-003,  0.12612314645694904E-003,  0.96122952362498310E-004,  0.72535195514095496E-004,  0.53552466584285380E-004,  0.40316734259093731E-004,  0.31701072872132706E-004,  0.25015635547339735E-004,  0.18258421706844782E-004,  0.13669292206114124E-004,  0.11157646289902190E-004,  0.99664867594259086E-005,  0.89218068919433283E-005,  0.80572043070906031E-005,  0.68451095376603571E-005,  0.44028972510990801E-005,  0.39189698398692706E-005,  0.41163434226726221E-005,  0.49579603922240911E-005,  0.49356241184316982E-005,  0.46670142177688846E-005,  0.44080398649996706E-005,  0.42203440958896239E-005,  0.40202965150561452E-005,  0.38444964419305914E-005,  0.39234969271374931E-005,  0.39667827535633306E-005,  0.38042463865568482E-005,  0.36092241334645754E-005,  0.34825037955812772E-005,  0.32988892980196942E-005,  0.31255560443121524E-005,  0.29718954896031780E-005,  0.29797699915839707E-005,  0.27382323547759285E-005,  0.27435153302359317E-005,  0.27870193565117503E-005,  0.28190229118688600E-005,  0.26908435242115152E-005,  0.30165466811503738E-005,  0.23608837133799322E-005,  0.21343087690934735E-005,  0.19872919910998291E-005,  0.18586398177156249E-005,  0.15699676102900231E-005,  0.14050234132335289E-005,  0.13644709555708826E-005,  0.13245803021926486E-005,  0.13027873601115084E-005,  0.12765922787220377E-005,  0.12468741331466889E-005,  0.12177764292988421E-005,  0.11870550190784247E-005,  0.11442615992800341E-005,  0.11404318546543967E-005,  0.11550046882867020E-005,  0.11497587034748210E-005,  0.12079851911804266E-005,  0.18937173452767791E-005,  0.19102050273236200E-005,  0.19102271434559615E-005,],]
