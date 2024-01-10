# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1382 ] 
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
input.tair=[[  0.25488464159051330E+003,  0.26514355629868112E+003,  0.26223422970233742E+003,  0.26523455837928498E+003,  0.26909834129732053E+003,  0.27169396733500452E+003,  0.26791088147886416E+003,  0.26003982672777465E+003,  0.24915549393594921E+003,  0.24201278468675505E+003,  0.23819425269348622E+003,  0.23734000388934825E+003,  0.23424544360695259E+003,  0.22908441644539397E+003,  0.22061535213187651E+003,  0.21322167926850065E+003,  0.20912770565766911E+003,  0.20621744759604195E+003,  0.20184010321116983E+003,  0.19723360040718919E+003,  0.19254051458955183E+003,  0.18984419841112413E+003,  0.18894989373826365E+003,  0.18887140576199107E+003,  0.18913657486157302E+003,  0.18962837883628012E+003,  0.18783746401043149E+003,  0.18837329952206409E+003,  0.19157198489702827E+003,  0.19503946680894219E+003,  0.19891885070009181E+003,  0.20337913848595903E+003,  0.20795708581022424E+003,  0.21258895389999148E+003,  0.21710567844408379E+003,  0.22162934767325095E+003,  0.22602918933089580E+003,  0.23063682393059949E+003,  0.23552700732539185E+003,  0.24026576265280502E+003,  0.24470251660236144E+003,  0.24868619042923004E+003,  0.25269974916300566E+003,  0.25680890439434876E+003,  0.26137371926712615E+003,  0.26568985471378494E+003,  0.26819429952425349E+003,  0.27066210670610889E+003,  0.27143265602865370E+003,  0.27309854917546124E+003,  0.27538947509962981E+003,  0.27806183911939229E+003,  0.28103371474571412E+003,  0.28372694356456657E+003,  0.28591947226768144E+003,  0.28747345961748312E+003,  0.28864395037892666E+003,  0.28959712824133527E+003,  0.29047351787284089E+003,  0.29132156566504040E+003,  0.29209723458124284E+003,  0.29277458458547494E+003,  0.29341907495290087E+003,  0.29383743453896795E+003,  0.29437693700645923E+003,  0.29511574746867797E+003,  0.29590588122545620E+003,  0.29665828035753538E+003,  0.29730556887206399E+003,  0.29784028553946160E+003,  0.29835931827879205E+003,  0.29871851355075250E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472144164360336E+005,  0.19913320596645735E+005,  0.21454974977228059E+005,  0.23127648046465114E+005,  0.24942474650474625E+005,  0.26911535945815376E+005,  0.29047939520914832E+005,  0.31365906538311549E+005,  0.33880867222538596E+005,  0.36609564120442956E+005,  0.39570162231325339E+005,  0.42782369263730914E+005,  0.46218432984044230E+005,  0.49753608838335465E+005,  0.53272035612184583E+005,  0.56703235843832626E+005,  0.60013259508579373E+005,  0.63188078276017834E+005,  0.66184970899457127E+005,  0.68961978302144984E+005,  0.71478868917651838E+005,  0.73698106548446434E+005,  0.75585780575897938E+005,  0.77140457087751362E+005,  0.78455044540244038E+005,  0.79674788256071450E+005,  0.80865565900177025E+005,  0.82025465856042618E+005,  0.83152605933015788E+005,  0.84245141779672354E+005,  0.85301268339339862E+005,  0.86319219521222505E+005,  0.87297272775673002E+005,  0.88233760769102562E+005,  0.89127082816759896E+005,  0.89975701393667026E+005,  0.90783005696262742E+005,  0.91475231612935997E+005,  0.91911500581475528E+005,],]
input.radius_part=[[  0.21792159531840985E-007,  0.22572365991989665E-007,  0.26754511784398576E-007,  0.29757092554524117E-007,  0.30853755524109972E-007,  0.35154460023559122E-007,  0.40054931309638186E-007,  0.42783249022746213E-007,  0.44819382145471829E-007,  0.46401365511169422E-007,  0.48057730391740349E-007,  0.49799732398316909E-007,  0.51186926381263410E-007,  0.52357804968374052E-007,  0.55193212740455011E-007,  0.60007510317766977E-007,  0.64405269258570793E-007,  0.66891294731835243E-007,  0.68023657363359652E-007,  0.69203696762534606E-007,  0.69493656039103140E-007,  0.69634961406031231E-007,  0.69642718835049145E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69637697131517685E-007,  0.69642719505620949E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642719474302104E-007,  0.69642719628401075E-007,  0.69642720431142788E-007,  0.69642720178698118E-007,  0.69642720700405099E-007,  0.69642722380507126E-007,  0.69642722690024969E-007,  0.69642720906893719E-007,  0.69642719782007972E-007,  0.69642719317061806E-007,  0.69642719173159114E-007,  0.69642719157785175E-007,  0.69642719172927517E-007,  0.69642719178627652E-007,  0.69642719178909674E-007,  0.69642719171173298E-007,  0.69642719207143333E-007,  0.69642719218595656E-007,  0.69642719244678447E-007,  0.69642719489446074E-007,  0.69642719774939019E-007,  0.69642719787631781E-007,  0.69642719670933722E-007,  0.69642719546514085E-007,  0.69642719448599472E-007,  0.69642719436851217E-007,  0.69642719460458833E-007,  0.69642719509152917E-007,],]
input.density_part=[[  0.10461096263341824E+004,  0.10463470084381997E+004,  0.10464348330263022E+004,  0.10462767432483799E+004,  0.10451620002726672E+004,  0.10451217217787132E+004,  0.10452811026949269E+004,  0.10448881126141105E+004,  0.10445399259795570E+004,  0.10446499112579668E+004,  0.10437489381729470E+004,  0.10420991748591016E+004,  0.10403703745499640E+004,  0.10367420647083716E+004,  0.10333556511822367E+004,  0.10391458903987527E+004,  0.10505723079901618E+004,  0.10664901728522655E+004,  0.10676143767083861E+004,  0.10624169719488286E+004,  0.10579098223508365E+004,  0.10561380678153134E+004,  0.10557245849206799E+004,  0.10578932752587045E+004,  0.10590604684996213E+004,  0.10592959526873540E+004,  0.10626918966572098E+004,  0.10645790833165333E+004,  0.10636512185170193E+004,  0.10623738858397471E+004,  0.10621527678477455E+004,  0.10609000616828307E+004,  0.10592516144299627E+004,  0.10585721157183636E+004,  0.10584012775400438E+004,  0.10575203561359799E+004,  0.10568145190830478E+004,  0.10563210176929658E+004,  0.10562126450392091E+004,  0.10559043370244410E+004,  0.10570875361428382E+004,  0.10569721914068193E+004,  0.10558218018669374E+004,  0.10554504431372450E+004,  0.10551282724800765E+004,  0.10543268022611055E+004,  0.10533807448408854E+004,  0.10506998687585806E+004,  0.10481616377894504E+004,  0.10446294960010816E+004,  0.10438593239320498E+004,  0.10437318208535837E+004,  0.10438810904936181E+004,  0.10438390797755355E+004,  0.10438150631708577E+004,  0.10437592197327779E+004,  0.10439979703879890E+004,  0.10440570874925413E+004,  0.10441278376612652E+004,  0.10441676889864584E+004,  0.10443213961914269E+004,  0.10448123752333129E+004,  0.10472669201816602E+004,  0.10521235176978760E+004,  0.10566095781789359E+004,  0.10585612967650752E+004,  0.10593690631671202E+004,  0.10598946513053895E+004,  0.10605829732905790E+004,  0.10611929197155130E+004,  0.10613906671958239E+004,  0.10614641008935530E+004,],]
input.sig_part=[[  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.25168371145480434E-002,  0.18012153511983771E-002,  0.14381233517391620E-002,  0.10893481724889656E-002,  0.76972694041642343E-003,  0.59684608270426309E-003,  0.45746909537912512E-003,  0.32595977712511801E-003,  0.22635334123934588E-003,  0.15649163438831440E-003,  0.11121776956957155E-003,  0.81884231263351802E-004,  0.61002085571986552E-004,  0.46066021573965483E-004,  0.36490736684726409E-004,  0.30905871560943665E-004,  0.26833958134398724E-004,  0.23213581327266824E-004,  0.19714496522252649E-004,  0.16976534579090241E-004,  0.14719627683883334E-004,  0.13082544977906228E-004,  0.11898719594999990E-004,  0.10996993897520186E-004,  0.10187292323446124E-004,  0.94357675506596140E-005,  0.87242869220792436E-005,  0.81002824507677954E-005,  0.75475684845666684E-005,  0.70349534940232990E-005,  0.65698071245286428E-005,  0.61368984481072131E-005,  0.57317104073576273E-005,  0.53730791877864983E-005,  0.50548429724595415E-005,  0.47548781601670785E-005,  0.44706827582886398E-005,  0.42043150716872824E-005,  0.39558135851821078E-005,  0.37194409175609031E-005,  0.34999331786458385E-005,  0.32869496924134644E-005,  0.30840644283278758E-005,  0.28963878954178246E-005,  0.27220800357390348E-005,  0.25590054319585617E-005,  0.24087772448000876E-005,  0.22750256349748031E-005,  0.21569618775712974E-005,  0.20555129254856237E-005,  0.19741838322264584E-005,  0.19063563169699664E-005,  0.18498507390608441E-005,  0.18019797979710887E-005,  0.17621427652766696E-005,  0.17295633407069891E-005,  0.17042191697796853E-005,  0.16832797732940365E-005,  0.16644694537486250E-005,  0.16465847338792046E-005,  0.16297731505393182E-005,  0.16143212501623766E-005,  0.16027505907097876E-005,  0.15954196340846392E-005,  0.15884114751136029E-005,  0.15785692023205928E-005,  0.15678676857751959E-005,  0.15575045071525007E-005,  0.15480584401819936E-005,  0.15390947171581542E-005,  0.15311196340785652E-005,  0.15261084272961734E-005,],]
