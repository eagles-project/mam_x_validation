# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1411 ] 
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
input.tair=[[  0.25394083062695589E+003,  0.26751362259083652E+003,  0.27388042092793557E+003,  0.27617138358200071E+003,  0.27035675600840830E+003,  0.26476449254984669E+003,  0.26194283323908667E+003,  0.25736141591327902E+003,  0.25002805290549796E+003,  0.24219551643255957E+003,  0.23628344673444050E+003,  0.23411787340843426E+003,  0.23243293089644669E+003,  0.23005071087319817E+003,  0.22513967977537035E+003,  0.21889155934893213E+003,  0.21208180033614127E+003,  0.20566446638961833E+003,  0.19973221828634843E+003,  0.19482379345112986E+003,  0.18992649516743523E+003,  0.18723356739558616E+003,  0.18692003534863903E+003,  0.18783026249575823E+003,  0.18938740613995986E+003,  0.19173207839313730E+003,  0.19250052397599049E+003,  0.18940332942605531E+003,  0.19086938521861421E+003,  0.19517256564845462E+003,  0.19871484088159150E+003,  0.20287278426450567E+003,  0.20752087807219556E+003,  0.21226022125716656E+003,  0.21691797657541377E+003,  0.22155076002342085E+003,  0.22625702653276093E+003,  0.23080554891574084E+003,  0.23532044915708056E+003,  0.23967899812111199E+003,  0.24395212028708448E+003,  0.24815015340507429E+003,  0.25272175827410643E+003,  0.25692377507348607E+003,  0.26114363287502658E+003,  0.26502876123017171E+003,  0.26734561156591650E+003,  0.26949992074297995E+003,  0.27148971089815990E+003,  0.27363793502505769E+003,  0.27524083875421582E+003,  0.27894023574839935E+003,  0.28166058743743690E+003,  0.28405354833962707E+003,  0.28616958834829620E+003,  0.28795561725266958E+003,  0.28936054378642189E+003,  0.29045482930947514E+003,  0.29135491023753173E+003,  0.29219186734457207E+003,  0.29296005216841183E+003,  0.29366578130222484E+003,  0.29423129820980057E+003,  0.29471188927798505E+003,  0.29500379976493815E+003,  0.29516019898507079E+003,  0.29545637441298680E+003,  0.29590943404686692E+003,  0.29631991458781619E+003,  0.29575492064702803E+003,  0.29435712980973739E+003,  0.29380496765606171E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473986823456678E+005,  0.19919765143148121E+005,  0.21467172476092419E+005,  0.23146087418750150E+005,  0.24967686367036957E+005,  0.26944095560393362E+005,  0.29088471499683154E+005,  0.31415088414153044E+005,  0.33939434112600560E+005,  0.36678313621722424E+005,  0.39649959723050983E+005,  0.42874153666261533E+005,  0.46323039658894762E+005,  0.49871407643186816E+005,  0.53402964044725581E+005,  0.56846968401120816E+005,  0.60169343999027471E+005,  0.63356010156830263E+005,  0.66364086207693777E+005,  0.69151456499384993E+005,  0.71677739334348968E+005,  0.73905258440209509E+005,  0.75799976655172781E+005,  0.77360454715763102E+005,  0.78679947781408133E+005,  0.79904243182068152E+005,  0.81099464419453434E+005,  0.82263692744535554E+005,  0.83395038941798499E+005,  0.84491651779192660E+005,  0.85551719461761095E+005,  0.86573469305610270E+005,  0.87555172336021846E+005,  0.88495155000067622E+005,  0.89391810636863840E+005,  0.90243595981225793E+005,  0.91053726569609193E+005,  0.91748126411193647E+005,  0.92185696885398225E+005,],]
input.radius_part=[[  0.13543564280494455E-007,  0.12899237995106649E-007,  0.15186912187224891E-007,  0.17812921695783254E-007,  0.20737179397085340E-007,  0.24777147160249672E-007,  0.27707889021862043E-007,  0.29705954767181937E-007,  0.32291295898521373E-007,  0.34112874756079696E-007,  0.35511955343851976E-007,  0.36348332679570162E-007,  0.37067961894627744E-007,  0.37995903762007764E-007,  0.38009477646921635E-007,  0.37243655809839643E-007,  0.38371450084890791E-007,  0.39899531950960726E-007,  0.38741628002777134E-007,  0.33914413229872564E-007,  0.29749884831639094E-007,  0.28426761166729155E-007,  0.28213852271744312E-007,  0.27214021828888831E-007,  0.26278089249997775E-007,  0.23309060045270119E-007,  0.15485232800983568E-007,  0.15726714349979436E-007,  0.18673383779443186E-007,  0.21667210087113774E-007,  0.25311398947506111E-007,  0.27011205037898162E-007,  0.28339794216838854E-007,  0.29206968828531247E-007,  0.29739192664717775E-007,  0.30673097885686052E-007,  0.32327434967672635E-007,  0.33314052949798551E-007,  0.34189970989325325E-007,  0.34971762764030879E-007,  0.35840705449686389E-007,  0.37162097883143907E-007,  0.37755612098418399E-007,  0.37753563619194112E-007,  0.39622645972486050E-007,  0.40589900528651470E-007,  0.42658094909754150E-007,  0.44577905209687059E-007,  0.41859455191771330E-007,  0.39715267330900248E-007,  0.44104692462681151E-007,  0.37675671666843738E-007,  0.37306672932470817E-007,  0.35707305064161460E-007,  0.33565021605777059E-007,  0.30032857891462941E-007,  0.26915592909124075E-007,  0.25539068372810596E-007,  0.24062143374301335E-007,  0.23162360725005872E-007,  0.22740592952579672E-007,  0.22332248139958041E-007,  0.21817484822155058E-007,  0.21432593654925124E-007,  0.21439424782749993E-007,  0.22804922982250911E-007,  0.24209949562901449E-007,  0.24734240708356136E-007,  0.25447275402050076E-007,  0.29956374299931945E-007,  0.39774876553258334E-007,  0.51739835249133733E-007,],]
input.density_part=[[  0.17707365844818112E+004,  0.17716265039153288E+004,  0.17718755670183152E+004,  0.17718865759504931E+004,  0.17718610205247901E+004,  0.17718315562572286E+004,  0.17708967800820972E+004,  0.16954957111636693E+004,  0.15951589816426385E+004,  0.15677315226084283E+004,  0.15510877736908021E+004,  0.15451294152160572E+004,  0.15389749865030524E+004,  0.15348843224800094E+004,  0.15220089373202613E+004,  0.14699926528431447E+004,  0.13441879538329447E+004,  0.12506403421879518E+004,  0.12171722841875064E+004,  0.11938873386564935E+004,  0.11798701463787183E+004,  0.11530191623767578E+004,  0.11399148528109090E+004,  0.11475410990344512E+004,  0.11519878047874647E+004,  0.11570656967340458E+004,  0.12098980928668736E+004,  0.11678818316767959E+004,  0.11348387745385414E+004,  0.10926124315924453E+004,  0.10622463134344821E+004,  0.10473203329605942E+004,  0.10435251486470443E+004,  0.10422413308065063E+004,  0.10418068355555286E+004,  0.10416543754262639E+004,  0.10426383974426562E+004,  0.10432322464209676E+004,  0.10444195165087428E+004,  0.10469905227159018E+004,  0.10422380355559653E+004,  0.10392881318522479E+004,  0.10381350015998012E+004,  0.10411987899825444E+004,  0.10408204775644740E+004,  0.10389209230360891E+004,  0.10299670820911056E+004,  0.10318092349238814E+004,  0.10595733454053454E+004,  0.10829624102437588E+004,  0.10787066814216701E+004,  0.11688221361513624E+004,  0.12298833446261417E+004,  0.12754407961926972E+004,  0.13045669443850788E+004,  0.13389778798806981E+004,  0.13769576996364451E+004,  0.14150829131377861E+004,  0.14567459559531187E+004,  0.14890857836944283E+004,  0.15063948050027020E+004,  0.15413655311268576E+004,  0.15665177449287539E+004,  0.15747475211043593E+004,  0.15557214929555860E+004,  0.14646254258795850E+004,  0.13815389241013893E+004,  0.13442799218565663E+004,  0.13232489305146835E+004,  0.12302163983809060E+004,  0.11143904876764284E+004,  0.10539227447040212E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.51270965468823045E-002,  0.33962024329580410E-002,  0.27405476406332559E-002,  0.21861934124955992E-002,  0.17055263881516473E-002,  0.13658791993672570E-002,  0.10285466860443433E-002,  0.70889028464843080E-003,  0.48411961385113044E-003,  0.33521373781889680E-003,  0.23613385364029495E-003,  0.17090145015765000E-003,  0.12643935634650292E-003,  0.96378235328070471E-004,  0.72669263937089854E-004,  0.53412762668478525E-004,  0.40027147112010936E-004,  0.31537087967438502E-004,  0.24761896603942233E-004,  0.18012553590848207E-004,  0.13482916294781719E-004,  0.11163398362787437E-004,  0.99702658735649052E-005,  0.89349948104461691E-005,  0.80243184637974148E-005,  0.66186873572242973E-005,  0.42112808880025622E-005,  0.37843129576131187E-005,  0.40660444107247600E-005,  0.42619217792669307E-005,  0.45413677824932159E-005,  0.44757677878688438E-005,  0.43852940936064381E-005,  0.42392948248887875E-005,  0.40621180123451873E-005,  0.39496984071437706E-005,  0.39352486886226137E-005,  0.38246913572130312E-005,  0.37026521484272508E-005,  0.35755352648214271E-005,  0.34361923892277761E-005,  0.33522143684137310E-005,  0.32049480905050728E-005,  0.30208747118872713E-005,  0.30010925882960314E-005,  0.28997139809257878E-005,  0.28756595200596645E-005,  0.28806196909685331E-005,  0.26135906999280733E-005,  0.24009423613006577E-005,  0.26145849415650470E-005,  0.22597672750883150E-005,  0.22796452170608675E-005,  0.21834538512140409E-005,  0.20264654238247899E-005,  0.17874875119110220E-005,  0.15912080439922783E-005,  0.15184009106792940E-005,  0.14414916067473932E-005,  0.13938213559624812E-005,  0.13650301899466595E-005,  0.13531555521583244E-005,  0.13249207337696791E-005,  0.12918455604205702E-005,  0.12641883641037887E-005,  0.12657996622601302E-005,  0.12688297488383396E-005,  0.12559390730409097E-005,  0.12688225234807857E-005,  0.14226678035282158E-005,  0.18227516330758445E-005,  0.24302630321048436E-005,],]
