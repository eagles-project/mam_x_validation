# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1396 ] 
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
input.tair=[[  0.25017801421020238E+003,  0.25364407365515046E+003,  0.26055662006161799E+003,  0.26224004535986239E+003,  0.26600323758534392E+003,  0.26676034464812381E+003,  0.26457747314922312E+003,  0.26039652051931699E+003,  0.25248200785911231E+003,  0.24334212320151610E+003,  0.23563199279269139E+003,  0.23307520970962511E+003,  0.23112443962790019E+003,  0.22840205093842820E+003,  0.22236106566485006E+003,  0.21529329318234255E+003,  0.20968596164244289E+003,  0.20588045032087035E+003,  0.20159911060422971E+003,  0.19774179423007288E+003,  0.19349166678860456E+003,  0.19043657244094155E+003,  0.18909796042137089E+003,  0.18908890763807690E+003,  0.18944131617003933E+003,  0.19026547020290525E+003,  0.18786386079997638E+003,  0.18783076792308648E+003,  0.19132590132751562E+003,  0.19524145773830642E+003,  0.19910955553911299E+003,  0.20293541766963443E+003,  0.20724837858967035E+003,  0.21176115477350450E+003,  0.21635129667909030E+003,  0.22091868874018084E+003,  0.22551135546425095E+003,  0.23012676367173461E+003,  0.23456971521423534E+003,  0.23910258785412614E+003,  0.24371751542562930E+003,  0.24820936701291882E+003,  0.25312288548702691E+003,  0.25756897533877611E+003,  0.26089651042353540E+003,  0.26417249795851359E+003,  0.26714454512014396E+003,  0.26911900654949045E+003,  0.27041221157797867E+003,  0.27273018653299846E+003,  0.27502762959186259E+003,  0.27763124142970497E+003,  0.28101229609743581E+003,  0.28388354226753944E+003,  0.28599694670121914E+003,  0.28749418070664387E+003,  0.28870992411686120E+003,  0.28967330543590327E+003,  0.29050627622167974E+003,  0.29126852012604877E+003,  0.29195641640822896E+003,  0.29256714533745651E+003,  0.29316375253593833E+003,  0.29367551751438657E+003,  0.29402036669888724E+003,  0.29432061539633543E+003,  0.29448384993828279E+003,  0.29415546689834258E+003,  0.29326078745325555E+003,  0.29159172838885468E+003,  0.29199128568792764E+003,  0.29234453477708468E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473577468995587E+005,  0.19918333460062677E+005,  0.21464462750465900E+005,  0.23141991034714920E+005,  0.24962085478263187E+005,  0.26936862305199600E+005,  0.29079467150284690E+005,  0.31404162453772969E+005,  0.33926423231875655E+005,  0.36663040631128286E+005,  0.39632232374955653E+005,  0.42853763375561961E+005,  0.46299800846520229E+005,  0.49845238143699360E+005,  0.53373877743276273E+005,  0.56815037609556079E+005,  0.60134669173608527E+005,  0.63318703383859232E+005,  0.66324294989327784E+005,  0.69109363121682123E+005,  0.71633559435627656E+005,  0.73859238777003586E+005,  0.75752392096111493E+005,  0.77311581318271856E+005,  0.78629984581341734E+005,  0.79853268806090055E+005,  0.81047502880556291E+005,  0.82210769640229191E+005,  0.83341181430195677E+005,  0.84436888546966002E+005,  0.85496080692521413E+005,  0.86516986647652782E+005,  0.87497878864998274E+005,  0.88437085173282059E+005,  0.89333000239243367E+005,  0.90184082072908495E+005,  0.90993584790028137E+005,  0.91687501685058742E+005,  0.92124783024310906E+005,],]
input.radius_part=[[  0.13413575869436158E-007,  0.14034257632472540E-007,  0.17174447731934887E-007,  0.18986505742964985E-007,  0.19982130893912050E-007,  0.23852993104604052E-007,  0.27201629151547371E-007,  0.29239888769735473E-007,  0.31855912409109710E-007,  0.34030522880115819E-007,  0.35560180978739410E-007,  0.36349988338627600E-007,  0.37078298732815317E-007,  0.38026572168675040E-007,  0.37905945936170970E-007,  0.37290989274630355E-007,  0.38316150929454784E-007,  0.40028116264067964E-007,  0.39653126301559563E-007,  0.34570834045007373E-007,  0.29971257793658797E-007,  0.27902031348473355E-007,  0.27492959937367910E-007,  0.27380279471070912E-007,  0.25872397901768179E-007,  0.19681252183755255E-007,  0.14614699724034658E-007,  0.15459307165382840E-007,  0.17773613821805467E-007,  0.18977355602642338E-007,  0.20563951813582920E-007,  0.21779245086466977E-007,  0.23352786259560269E-007,  0.26603356377392070E-007,  0.29693131312535989E-007,  0.31590921365192947E-007,  0.32143276927061296E-007,  0.32452221179476613E-007,  0.33102541474613661E-007,  0.32975199102322298E-007,  0.32993829742426780E-007,  0.32277983499567781E-007,  0.31914031483446613E-007,  0.34463325758483822E-007,  0.34107882452188432E-007,  0.34419961552646075E-007,  0.42143526811930563E-007,  0.44061265858211627E-007,  0.46907555771913505E-007,  0.54014843204682061E-007,  0.55975747268216285E-007,  0.40841635614329699E-007,  0.33626163331538200E-007,  0.30504338021190139E-007,  0.28174101173663503E-007,  0.25886267601928353E-007,  0.23359518765837054E-007,  0.21996831248814622E-007,  0.20506545458881631E-007,  0.19463524173574520E-007,  0.18840254591671016E-007,  0.18607671311425720E-007,  0.18612341551879881E-007,  0.18900767398400147E-007,  0.19263720928030297E-007,  0.20321413433896803E-007,  0.23294942602366146E-007,  0.27294242076034416E-007,  0.34469301647350908E-007,  0.44723014279525545E-007,  0.25170322239762033E-007,  0.44879204624164457E-007,],]
input.density_part=[[  0.17711770554447783E+004,  0.17717920837768868E+004,  0.17718318919610540E+004,  0.17718804483851811E+004,  0.17718618807377948E+004,  0.17718611463544150E+004,  0.17714799698388460E+004,  0.17160065499056934E+004,  0.16087957434093055E+004,  0.15681398670055958E+004,  0.15506112323236489E+004,  0.15450094550980439E+004,  0.15389424468753198E+004,  0.15342189423735349E+004,  0.15178309853410931E+004,  0.14546229681579387E+004,  0.13459165210823376E+004,  0.12621522027387061E+004,  0.12248012824359005E+004,  0.11952346907923513E+004,  0.11837035066859244E+004,  0.11729180277618962E+004,  0.11549215867697321E+004,  0.11496611691182925E+004,  0.11508875633470363E+004,  0.11680335917394489E+004,  0.12057722406310072E+004,  0.11683201617006287E+004,  0.11567922059395210E+004,  0.11368883022824355E+004,  0.11109651045817966E+004,  0.10833567363167660E+004,  0.10512883578619244E+004,  0.10253500639073920E+004,  0.10179434287771022E+004,  0.10181101824777877E+004,  0.10195307012933215E+004,  0.10197670411926491E+004,  0.10194713629396034E+004,  0.10237438349396932E+004,  0.10422892896117678E+004,  0.10598678671058701E+004,  0.10678771232802599E+004,  0.10546287020812267E+004,  0.10668014231193449E+004,  0.10669843057992780E+004,  0.10375128932476093E+004,  0.10360282076151359E+004,  0.10429937737898001E+004,  0.10377154752628960E+004,  0.10404173463521174E+004,  0.11229291556612347E+004,  0.12244224963807878E+004,  0.12981062515436593E+004,  0.13414066848011655E+004,  0.13672711363389228E+004,  0.13856302512017621E+004,  0.14142720688444269E+004,  0.14598885211235001E+004,  0.14868506166326988E+004,  0.14879139223813013E+004,  0.14802639325562589E+004,  0.14882062597734073E+004,  0.14931008669542107E+004,  0.15005465554120972E+004,  0.14863492190672530E+004,  0.14034215843455579E+004,  0.12816728916671545E+004,  0.11759940856582084E+004,  0.10643313408065051E+004,  0.13615352961267420E+004,  0.10642438633987613E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.25985735859491307E-002,  0.18547453329073697E-002,  0.15580948424832161E-002,  0.11704044682630127E-002,  0.84022110828236110E-003,  0.68028652518727171E-003,  0.52318658031722952E-003,  0.36607056783046914E-003,  0.24939768862933162E-003,  0.17271327143447988E-003,  0.12155798275137568E-003,  0.87768889882471534E-004,  0.64877831203359108E-004,  0.49382582842299003E-004,  0.36886162890267551E-004,  0.26925567933689864E-004,  0.20380861590015263E-004,  0.16326076497792648E-004,  0.13071941099167483E-004,  0.94410345616190187E-005,  0.70075611814932063E-005,  0.57189322351107078E-005,  0.50304273111114024E-005,  0.45910915464749564E-005,  0.40078025025943130E-005,  0.28500990775813411E-005,  0.19963587024352059E-005,  0.18885888597283464E-005,  0.20049893373357592E-005,  0.19624862967401074E-005,  0.19387582296503154E-005,  0.18673071197295783E-005,  0.18146818298541180E-005,  0.18926530095171198E-005,  0.19756626150222825E-005,  0.19789952931471764E-005,  0.18943801569485977E-005,  0.17959430632326896E-005,  0.17188277651673169E-005,  0.16116150823093856E-005,  0.15387982505470586E-005,  0.14323099882692064E-005,  0.13362718319600121E-005,  0.13402916508279032E-005,  0.12530468732814945E-005,  0.11836643555289219E-005,  0.13451641252416556E-005,  0.13300119273055637E-005,  0.13603449363377159E-005,  0.15155884405361136E-005,  0.15191479265993160E-005,  0.11044929340312462E-005,  0.94015579975650247E-006,  0.87061206212016571E-006,  0.80472727565685695E-006,  0.73271369870197688E-006,  0.65356181912903866E-006,  0.61657415618694198E-006,  0.58280208678565069E-006,  0.55436122438563948E-006,  0.52932248517609952E-006,  0.51353620210234844E-006,  0.51057297176455664E-006,  0.51501568016656666E-006,  0.52258912905599400E-006,  0.54253455955762042E-006,  0.58759479181450630E-006,  0.63156621531704736E-006,  0.74386089122417213E-006,  0.89865067204350241E-006,  0.59801939835601429E-006,  0.89366566132364321E-006,],]
