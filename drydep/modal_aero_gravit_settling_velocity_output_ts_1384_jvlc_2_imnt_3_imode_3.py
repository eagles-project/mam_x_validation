# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1384 ] 
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
input.tair=[[  0.25477870294269471E+003,  0.26728863299837877E+003,  0.26588084118231484E+003,  0.26597196496795988E+003,  0.26921950622316371E+003,  0.27114346543028915E+003,  0.26665762820701570E+003,  0.25861571471037172E+003,  0.24756196991309008E+003,  0.24055091296048951E+003,  0.23724658908046337E+003,  0.23718339650487442E+003,  0.23503360713328212E+003,  0.23065907693214132E+003,  0.22237909692188057E+003,  0.21432338044349257E+003,  0.20940432256272808E+003,  0.20606173887499139E+003,  0.20153421178594257E+003,  0.19688143812268669E+003,  0.19211148976588822E+003,  0.18939650635317284E+003,  0.18855782975324561E+003,  0.18853549027081530E+003,  0.18882021623529715E+003,  0.18922533645468809E+003,  0.18735591454905386E+003,  0.18820838636334366E+003,  0.19144092876699997E+003,  0.19497003103872083E+003,  0.19909682651733110E+003,  0.20353886199329725E+003,  0.20800599409502760E+003,  0.21258032908187531E+003,  0.21701193456624236E+003,  0.22143880559051382E+003,  0.22594169981352260E+003,  0.23063824293355029E+003,  0.23547417940324257E+003,  0.24015041602158459E+003,  0.24457523758158624E+003,  0.24849908133117151E+003,  0.25258064350542651E+003,  0.25695077009667062E+003,  0.26158255844357785E+003,  0.26581737260419982E+003,  0.26806164628354645E+003,  0.27029728590062382E+003,  0.27150120138888860E+003,  0.27316890507259677E+003,  0.27553107336188930E+003,  0.27845593810191031E+003,  0.28125785301252722E+003,  0.28382938932904142E+003,  0.28596705445234602E+003,  0.28752748924166428E+003,  0.28872631549569962E+003,  0.28969321930198379E+003,  0.29055914814508753E+003,  0.29139878729518648E+003,  0.29219338293526113E+003,  0.29287440960937670E+003,  0.29351783619243048E+003,  0.29401440081843657E+003,  0.29450695813158222E+003,  0.29514350583068068E+003,  0.29585632850809407E+003,  0.29656971738776565E+003,  0.29717832022759239E+003,  0.29727449326496713E+003,  0.29679300414091142E+003,  0.29667601968526003E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472716182478998E+005,  0.19915321182306558E+005,  0.21458761456434455E+005,  0.23133372195367501E+005,  0.24950301143560006E+005,  0.26921643452685341E+005,  0.29060521895097201E+005,  0.31381174106874278E+005,  0.33899048188478344E+005,  0.36630906082425470E+005,  0.39594933829708076E+005,  0.42810861968302444E+005,  0.46250906116739432E+005,  0.49790177214366340E+005,  0.53312679828909313E+005,  0.56747854855115693E+005,  0.60061712940229183E+005,  0.63240209502415848E+005,  0.66240573806063432E+005,  0.69020798168569512E+005,  0.71540604418180694E+005,  0.73762412873820955E+005,  0.75652273633965437E+005,  0.77208751125175477E+005,  0.78524861431033642E+005,  0.79746018129978678E+005,  0.80938175202255748E+005,  0.82099418817195910E+005,  0.83227864603412745E+005,  0.84321666073524102E+005,  0.85379016079086563E+005,  0.86398146482603770E+005,  0.87377332739888559E+005,  0.88314905586677691E+005,  0.89209262483044382E+005,  0.90058864122073719E+005,  0.90867045790798787E+005,  0.91559946560699245E+005,  0.91996619556670354E+005,],]
input.radius_part=[[  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.14976935405519906E-005,  0.19724714389321446E-005,  0.23424587867262416E-005,  0.26553762056303234E-005,  0.28761311934429532E-005,  0.30416355267373991E-005,  0.31806349756391270E-005,  0.33168777545485677E-005,  0.33581389134597751E-005,  0.26192269999696791E-005,  0.14234682354017847E-005,  0.10037364207078011E-005,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.84993643626415447E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.88321560546576884E-006,  0.89524142136182742E-006,  0.89989634903275015E-006,  0.93235931069589744E-006,  0.95533458210242816E-006,  0.96114658314557478E-006,  0.96548397016770171E-006,  0.96632571340708209E-006,  0.96490918314902171E-006,  0.96223235930079118E-006,  0.95895982215330597E-006,  0.95574738314460023E-006,  0.95319719890688179E-006,  0.95468681426302000E-006,  0.95603198500192607E-006,  0.95426969929160634E-006,  0.95487647824483357E-006,  0.12300693396496194E-005,  0.13766902199892228E-005,  0.15475795098812892E-005,  0.15976687564082668E-005,  0.15260305488061843E-005,  0.19300660044723118E-005,  0.18601105198741957E-005,  0.15104150592138217E-005,  0.12943713654873578E-005,  0.11627568212441247E-005,  0.11044130783068370E-005,  0.11014641942015772E-005,  0.10991441574002703E-005,  0.10944385838517202E-005,  0.10966780902241914E-005,  0.10979391352987346E-005,  0.10994548945198437E-005,  0.11014989779525512E-005,  0.11044887603749028E-005,  0.11510403812418981E-005,  0.12327486741018604E-005,  0.12889458463744311E-005,  0.12944321423560553E-005,  0.12773844827260145E-005,  0.12625012962629548E-005,  0.13163418212329512E-005,  0.14252108924203408E-005,  0.14831042261222456E-005,],]
input.density_part=[[  0.10000000000000000E+001,  0.10000000000000000E+001,  0.17699993364461316E+004,  0.17699999986911521E+004,  0.17699999999992654E+004,  0.17699999999999980E+004,  0.17700000000000000E+004,  0.17700000000000000E+004,  0.17700000000000000E+004,  0.17700000000000000E+004,  0.17700000000000002E+004,  0.17700000000000291E+004,  0.17700000000080088E+004,  0.17700000024145081E+004,  0.17700005670420617E+004,  0.17700529054365029E+004,  0.17718346921423695E+004,  0.17870213650940773E+004,  0.18397286250479722E+004,  0.18699371817872727E+004,  0.18812101804858294E+004,  0.18623794300847194E+004,  0.17765457374224045E+004,  0.18477770779225386E+004,  0.19190066416132879E+004,  0.19391597824736273E+004,  0.18451862238859167E+004,  0.17705332236175464E+004,  0.17894330313086500E+004,  0.18392147332411225E+004,  0.18473254742580555E+004,  0.18485618643384882E+004,  0.18410246190135383E+004,  0.18320275838335840E+004,  0.18361499461756493E+004,  0.18451073445397171E+004,  0.18537961923522232E+004,  0.18616802403036284E+004,  0.18711950250096240E+004,  0.18791508601535602E+004,  0.18823627742324747E+004,  0.18810745290980574E+004,  0.18888423158679304E+004,  0.18963991813500063E+004,  0.14238923261541024E+004,  0.13120786765897167E+004,  0.11988773124560500E+004,  0.11813391553627828E+004,  0.12179788826863260E+004,  0.11318725818038199E+004,  0.11566514418328566E+004,  0.12978826636808312E+004,  0.14779649147245582E+004,  0.16497375288987434E+004,  0.17331089518460099E+004,  0.17227310579111243E+004,  0.17232920979764936E+004,  0.17335369910175866E+004,  0.17381263347157937E+004,  0.17498086503640793E+004,  0.17547561954431831E+004,  0.17516407214658043E+004,  0.17478832476106559E+004,  0.16539069123854201E+004,  0.15199686278420065E+004,  0.14510915977662030E+004,  0.14435008233336607E+004,  0.14624985362002838E+004,  0.14794548171601812E+004,  0.14213442755629626E+004,  0.13279756032102991E+004,  0.12891751271865048E+004,],]
input.sig_part=[[  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.27834136208216859E-003,  0.19316591840461310E-003,  0.23111897176658242E+000,  0.15672278089133601E+000,  0.10694891371913658E+000,  0.72852803806522246E-001,  0.88339255320389373E-001,  0.79152380933833394E-001,  0.64471090118149499E-001,  0.51633073679832428E-001,  0.41645960936650205E-001,  0.34790481211535586E-001,  0.30291536712937491E-001,  0.27796175799583513E-001,  0.25685128573053939E-001,  0.15883996294584500E-001,  0.55454645738354947E-002,  0.30065368928402008E-002,  0.21791069299580417E-002,  0.20728795992117038E-002,  0.19887973529819814E-002,  0.18982034815482969E-002,  0.17943369771468219E-002,  0.17815748388790957E-002,  0.18060306002591604E-002,  0.17833636390674980E-002,  0.16715417305142775E-002,  0.17177804933046948E-002,  0.17307192622552630E-002,  0.17471182938453259E-002,  0.18191197205740244E-002,  0.18500838453579204E-002,  0.18127845098088625E-002,  0.17713831389160944E-002,  0.17346411625559621E-002,  0.16969930106752586E-002,  0.16563475728083497E-002,  0.16139883355508148E-002,  0.15744222846433655E-002,  0.15380045009993671E-002,  0.15124753703467885E-002,  0.14862326679983514E-002,  0.14585778411588209E-002,  0.14375911563156117E-002,  0.17187924687451510E-002,  0.19353487671528737E-002,  0.21960586046553443E-002,  0.22802429076128868E-002,  0.21360451102469696E-002,  0.31212527708418046E-002,  0.29417373178435655E-002,  0.21736107898615996E-002,  0.18139990085877496E-002,  0.16291855865102724E-002,  0.15374499308047577E-002,  0.15122297398292195E-002,  0.15003353391138618E-002,  0.14917295822894870E-002,  0.14971688134716001E-002,  0.15062772031709840E-002,  0.15104952417078728E-002,  0.15096683884359523E-002,  0.15109985491091223E-002,  0.15468048975690641E-002,  0.16224626597522325E-002,  0.16865935851380705E-002,  0.16880244882866771E-002,  0.16627705958268395E-002,  0.16407687358198874E-002,  0.17096317700703964E-002,  0.18683884329569501E-002,  0.19615401834888455E-002,],]
