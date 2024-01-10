# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1388 ] 
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
input.tair=[[  0.25318555702947307E+003,  0.26346079788871816E+003,  0.26529643429967541E+003,  0.26292479014276523E+003,  0.26492640909518741E+003,  0.26713115839323200E+003,  0.26485881969255104E+003,  0.25900640611258183E+003,  0.24845116962080573E+003,  0.24013513139192264E+003,  0.23594691863020864E+003,  0.23594636462882659E+003,  0.23463235118128634E+003,  0.23144822552072054E+003,  0.22409302469104605E+003,  0.21584898464029027E+003,  0.21006226543087715E+003,  0.20621513088826612E+003,  0.20163419510415102E+003,  0.19707692185778032E+003,  0.19217872352382344E+003,  0.18919155308225154E+003,  0.18824305259886270E+003,  0.18830309539303519E+003,  0.18856745625607249E+003,  0.18882372743518872E+003,  0.18677022669794331E+003,  0.18802740712788696E+003,  0.19133491326552118E+003,  0.19508481040438991E+003,  0.19931069308333494E+003,  0.20356419510073565E+003,  0.20797316901158115E+003,  0.21234598132945283E+003,  0.21671629644385445E+003,  0.22123631674532294E+003,  0.22591525220990704E+003,  0.23056996296996400E+003,  0.23522079389933967E+003,  0.23981163827495016E+003,  0.24436980846980933E+003,  0.24832677064235551E+003,  0.25248433644059165E+003,  0.25699120611339583E+003,  0.26181887248847448E+003,  0.26560568647660449E+003,  0.26788029057956095E+003,  0.27029536335129626E+003,  0.27139606423566437E+003,  0.27323284748095642E+003,  0.27539166126815752E+003,  0.27896232078256816E+003,  0.28163368925804457E+003,  0.28400938856411244E+003,  0.28605002823956028E+003,  0.28762899756631799E+003,  0.28884375073724908E+003,  0.28980636897875530E+003,  0.29064696927919255E+003,  0.29143228080267903E+003,  0.29221728640491938E+003,  0.29291127763945178E+003,  0.29350138516001482E+003,  0.29401248929861526E+003,  0.29447215408416588E+003,  0.29492384586096699E+003,  0.29543429129897328E+003,  0.29595523959982518E+003,  0.29644876242257982E+003,  0.29494377899669843E+003,  0.29386300564920026E+003,  0.29372011965820894E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18474134462859154E+005,  0.19920281499644407E+005,  0.21468149776477287E+005,  0.23147564836852936E+005,  0.24969706405782075E+005,  0.26946704334881644E+005,  0.29091719044027304E+005,  0.31419029014330416E+005,  0.33944126668413403E+005,  0.36683822039046914E+005,  0.39656353338680070E+005,  0.42881507709325233E+005,  0.46331421061076311E+005,  0.49880846038598727E+005,  0.53413454425494238E+005,  0.56858484686969066E+005,  0.60181849959001971E+005,  0.63369465365441021E+005,  0.66378437466228163E+005,  0.69166638063830789E+005,  0.71693673431735500E+005,  0.73921856074347234E+005,  0.75817138690852415E+005,  0.77378081589019392E+005,  0.78697967707180782E+005,  0.79922627802553063E+005,  0.81118205074029494E+005,  0.82282780201103407E+005,  0.83414463405405564E+005,  0.84511402903589886E+005,  0.85571786360807746E+005,  0.86593840564906772E+005,  0.87575836026372548E+005,  0.88516098693964625E+005,  0.89413021427973537E+005,  0.90265060503291883E+005,  0.91075417542213938E+005,  0.91769991565216711E+005,  0.92207666319979267E+005,],]
input.radius_part=[[  0.13708537388918799E-007,  0.13627905297436729E-007,  0.17183422426006798E-007,  0.19470122347717653E-007,  0.19913695458775617E-007,  0.24062462964281364E-007,  0.27296260148081912E-007,  0.29561975769279196E-007,  0.32510358110968297E-007,  0.34345048613251129E-007,  0.35627296782463030E-007,  0.36296793013751620E-007,  0.36998665056072292E-007,  0.37972512819785613E-007,  0.37933491699181077E-007,  0.37266991632939036E-007,  0.38188876061298721E-007,  0.40048211919767911E-007,  0.39275970625087913E-007,  0.33335241828349830E-007,  0.29528412171078474E-007,  0.27841078745315106E-007,  0.27650980869530226E-007,  0.27341564700891363E-007,  0.25905350026522072E-007,  0.19115487620906566E-007,  0.14098739261988878E-007,  0.14932614557481654E-007,  0.16627961116549585E-007,  0.18756180877415768E-007,  0.19984406496683258E-007,  0.21267935477116965E-007,  0.22318757352695905E-007,  0.23966339405969286E-007,  0.25375438285630906E-007,  0.27307726621331126E-007,  0.29450871502988382E-007,  0.31580083132062970E-007,  0.32554232335364732E-007,  0.33230960044367542E-007,  0.33515681172933576E-007,  0.32861256211928088E-007,  0.32016479763958203E-007,  0.32027435503821685E-007,  0.35588679931152605E-007,  0.36475482131435461E-007,  0.39718790167333283E-007,  0.42034118871949860E-007,  0.43888621750592620E-007,  0.43763313640068060E-007,  0.44558854562085931E-007,  0.36924812519439019E-007,  0.33135848039260259E-007,  0.30875863474926209E-007,  0.28893414221206220E-007,  0.26101312293122855E-007,  0.23439282982173622E-007,  0.21854223828151507E-007,  0.21117432016307520E-007,  0.20752525367742681E-007,  0.20600592371762419E-007,  0.20517740206243386E-007,  0.20519283502864804E-007,  0.21059457021873121E-007,  0.21807674221822902E-007,  0.22957600948163153E-007,  0.24230853401637844E-007,  0.26085635093950385E-007,  0.26104581996386674E-007,  0.32171586933004309E-007,  0.41249590922262679E-007,  0.45169526453468698E-007,],]
input.density_part=[[  0.17711575544920647E+004,  0.17717074696030072E+004,  0.17718352603305227E+004,  0.17718816463510889E+004,  0.17718684644846992E+004,  0.17718335660339656E+004,  0.17715262527954355E+004,  0.17027403588843517E+004,  0.15914351580821824E+004,  0.15642511955443724E+004,  0.15500050469261419E+004,  0.15454410688826147E+004,  0.15394091109026128E+004,  0.15344505183791161E+004,  0.15184729988087945E+004,  0.14584169638402200E+004,  0.13539324901352852E+004,  0.12636475845135078E+004,  0.12205312096647219E+004,  0.11921961756035098E+004,  0.11837252517973322E+004,  0.11703638806163542E+004,  0.11508665644257730E+004,  0.11496383125081945E+004,  0.11506621303512700E+004,  0.11695879876911827E+004,  0.12088664552151477E+004,  0.11698382604600954E+004,  0.11567502612235528E+004,  0.11473675751108688E+004,  0.11310970108124766E+004,  0.10981231027696970E+004,  0.10799204428390360E+004,  0.10641621395224781E+004,  0.10454610714432183E+004,  0.10309085368790184E+004,  0.10203119904182499E+004,  0.10177623498794873E+004,  0.10192232596618799E+004,  0.10197857654568020E+004,  0.10239671698650137E+004,  0.10430220647746507E+004,  0.10578390763918546E+004,  0.10611170121009322E+004,  0.10470947763520787E+004,  0.10531706001802272E+004,  0.10442457475453966E+004,  0.10399206631626196E+004,  0.10499689286460198E+004,  0.10597836247964979E+004,  0.10734623665673146E+004,  0.11611322214374318E+004,  0.12234877557522718E+004,  0.12700457785035969E+004,  0.13003029014608346E+004,  0.13108835588794961E+004,  0.13437529716212985E+004,  0.13910888020802979E+004,  0.14285742838091171E+004,  0.14624257884988413E+004,  0.14881705589463766E+004,  0.15073753549766172E+004,  0.15252087810201181E+004,  0.15188702346848315E+004,  0.14807782941997568E+004,  0.14143008115365210E+004,  0.13677636456178263E+004,  0.13468463169438630E+004,  0.13486785276048847E+004,  0.11987287402132538E+004,  0.10998502358588908E+004,  0.10766245503959617E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.26716016408536609E-002,  0.18354749984988228E-002,  0.15730265583378184E-002,  0.12017841408811715E-002,  0.83565009815056684E-003,  0.68672712569829112E-003,  0.52529963026800945E-003,  0.36626175859622744E-003,  0.24976110654631591E-003,  0.17273085075556111E-003,  0.12182113789328315E-003,  0.88200870498797654E-004,  0.65244625436498152E-004,  0.49644801862639792E-004,  0.37070672025989669E-004,  0.27012628877803936E-004,  0.20451647091136586E-004,  0.16366655674163562E-004,  0.12902195350937064E-004,  0.90618932211744374E-005,  0.68802371210154025E-005,  0.56758693563491380E-005,  0.50310152278688653E-005,  0.45752753550193358E-005,  0.40033344581735906E-005,  0.27606878578897103E-005,  0.19246472430028326E-005,  0.18268017600774441E-005,  0.18739753233268011E-005,  0.19563690380608324E-005,  0.19181658263291176E-005,  0.18501067312104435E-005,  0.17825962278811663E-005,  0.17667660200409777E-005,  0.17267159461988869E-005,  0.17241838251057144E-005,  0.17321567143552918E-005,  0.17432083178106742E-005,  0.16901198038345528E-005,  0.16198814990479373E-005,  0.15379861287707744E-005,  0.14359726308639718E-005,  0.13260556141693774E-005,  0.12457297126430973E-005,  0.12881117697826400E-005,  0.12453612901337458E-005,  0.12695896101747983E-005,  0.12686272578265605E-005,  0.12722919366211084E-005,  0.12201287172567038E-005,  0.12083250532279669E-005,  0.10220630062854700E-005,  0.92448884948243947E-006,  0.86260941316065193E-006,  0.80116964325254483E-006,  0.70837569649146037E-006,  0.63574428482662298E-006,  0.60189431859953632E-006,  0.58807163944399653E-006,  0.58343455769937381E-006,  0.58193282310904612E-006,  0.58005022703540305E-006,  0.58033592825424199E-006,  0.58777384350097255E-006,  0.58875314900556116E-006,  0.58851245296978964E-006,  0.59788654332352786E-006,  0.63253189529279838E-006,  0.62886031449694063E-006,  0.69713257357910008E-006,  0.84141637682237731E-006,  0.91142718029215150E-006,],]
