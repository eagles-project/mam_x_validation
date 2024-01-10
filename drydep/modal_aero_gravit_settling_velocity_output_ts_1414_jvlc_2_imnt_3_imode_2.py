# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1414 ] 
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
input.tair=[[  0.25261542362362934E+003,  0.26232991620503481E+003,  0.26881229168639805E+003,  0.27393619075525561E+003,  0.26974470810656129E+003,  0.26379285455471341E+003,  0.26094815493436948E+003,  0.25698867981978464E+003,  0.25067174445798815E+003,  0.24271643480674300E+003,  0.23609716450647397E+003,  0.23353227603810780E+003,  0.23171194771091058E+003,  0.22936281618307657E+003,  0.22484303385648545E+003,  0.21919864761534279E+003,  0.21301659385949353E+003,  0.20672640742141670E+003,  0.20056310845961679E+003,  0.19553857478238498E+003,  0.19042588637129077E+003,  0.18731417761970704E+003,  0.18676363348885624E+003,  0.18765192558750232E+003,  0.18929933701378633E+003,  0.19165055258954808E+003,  0.19282399178608640E+003,  0.18959603438374020E+003,  0.19081557970202087E+003,  0.19458486156002286E+003,  0.19805906009256219E+003,  0.20262955284710816E+003,  0.20754023539801486E+003,  0.21239034696611625E+003,  0.21696727606980411E+003,  0.22154728690685360E+003,  0.22610356352492670E+003,  0.23044751341765766E+003,  0.23475523526683332E+003,  0.23886805846190319E+003,  0.24312749577804945E+003,  0.24758718808208437E+003,  0.25226733608936246E+003,  0.25669829426418522E+003,  0.26099149628783050E+003,  0.26460346667521355E+003,  0.26690626219921410E+003,  0.26900356617630001E+003,  0.27125603637039814E+003,  0.27343091581183802E+003,  0.27517112963023908E+003,  0.27870078743572418E+003,  0.28172904373390571E+003,  0.28404305237799332E+003,  0.28608205623220152E+003,  0.28781162583498485E+003,  0.28919651270856849E+003,  0.29031248507981104E+003,  0.29124460670642600E+003,  0.29207916143990462E+003,  0.29282727013872511E+003,  0.29352474341838143E+003,  0.29411401162463920E+003,  0.29457632668325942E+003,  0.29486028007480479E+003,  0.29497093825877420E+003,  0.29509558118156104E+003,  0.29521225689953025E+003,  0.29496690920126559E+003,  0.29354935234105011E+003,  0.29332523265432405E+003,  0.29329703608700385E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473529832612167E+005,  0.19918166855784784E+005,  0.21464147420986988E+005,  0.23141514340458274E+005,  0.24961433705507603E+005,  0.26936020574742186E+005,  0.29078419318439293E+005,  0.31402891004974044E+005,  0.33924909161890479E+005,  0.36661263320496415E+005,  0.39630169451911832E+005,  0.42851390567157228E+005,  0.46297096557006611E+005,  0.49842192811524044E+005,  0.53370492984247649E+005,  0.56811321838569238E+005,  0.60130634080710675E+005,  0.63314362012479905E+005,  0.66319664504222645E+005,  0.69104464735392845E+005,  0.71628418241882508E+005,  0.73853883490742737E+005,  0.75746854703666249E+005,  0.77305893944313138E+005,  0.78624170387577076E+005,  0.79847336942266760E+005,  0.81041456141054892E+005,  0.82204611003819678E+005,  0.83334914057254689E+005,  0.84430515775747932E+005,  0.85489606035478690E+005,  0.86510413787682410E+005,  0.87491211651098070E+005,  0.88430327615232076E+005,  0.89326156501318488E+005,  0.90177156467779336E+005,  0.90986586119819432E+005,  0.91680446814589886E+005,  0.92117694507345528E+005,],]
input.radius_part=[[  0.13297023529528638E-007,  0.13105393934594826E-007,  0.15336859251477701E-007,  0.17701464906478404E-007,  0.20918897379637395E-007,  0.24768952271290938E-007,  0.27651043554022279E-007,  0.29614135377373920E-007,  0.32226658024788570E-007,  0.34000791295316552E-007,  0.35472315558967854E-007,  0.36340455404557510E-007,  0.37069798326673240E-007,  0.37998963856840536E-007,  0.38015919692796200E-007,  0.37237232527877086E-007,  0.38258735671700353E-007,  0.39843106721059688E-007,  0.38873921379511947E-007,  0.34084120160228883E-007,  0.29889204456779281E-007,  0.28402590207599922E-007,  0.28268287966112642E-007,  0.27218698373978546E-007,  0.26289337836904643E-007,  0.23504762378038955E-007,  0.15800261598512398E-007,  0.16053279285448394E-007,  0.18899977271756700E-007,  0.23106355436086488E-007,  0.27237228485459855E-007,  0.27971176280499139E-007,  0.28346014315615880E-007,  0.28782405193380606E-007,  0.29254133309967063E-007,  0.29550527379224812E-007,  0.31838754317374966E-007,  0.33852535239335809E-007,  0.35005191298934080E-007,  0.35577842562948888E-007,  0.36614696672701023E-007,  0.36812310516153772E-007,  0.36856407753076483E-007,  0.36878590131264945E-007,  0.39700676074680965E-007,  0.39379279455642181E-007,  0.41397573643437267E-007,  0.43607416900109436E-007,  0.42472576140863786E-007,  0.41488477906597459E-007,  0.49737206074510024E-007,  0.37648078868799834E-007,  0.36076682824591085E-007,  0.33943398234481056E-007,  0.31610855897324669E-007,  0.27998035842562302E-007,  0.25338618632796041E-007,  0.24122600039584005E-007,  0.22890145085280559E-007,  0.22248870247642441E-007,  0.21582658863910471E-007,  0.21072940902474295E-007,  0.20543079650320642E-007,  0.20205863334345687E-007,  0.19872913920210814E-007,  0.20756903928566801E-007,  0.22504531690319168E-007,  0.23807448284989215E-007,  0.26170013750908171E-007,  0.36536036371044545E-007,  0.43809320542713148E-007,  0.43968830584098317E-007,],]
input.density_part=[[  0.17707838484018371E+004,  0.17717152057993292E+004,  0.17719009312635094E+004,  0.17718886570496243E+004,  0.17718567204935414E+004,  0.17718321233983083E+004,  0.17714261937009392E+004,  0.16989100129900128E+004,  0.15973411633082130E+004,  0.15691023854580994E+004,  0.15515132288882103E+004,  0.15452230987925416E+004,  0.15389773257035067E+004,  0.15348551228017795E+004,  0.15222590521416216E+004,  0.14732304919329658E+004,  0.13521513832767223E+004,  0.12533493244296460E+004,  0.12174361944447382E+004,  0.11939300664962052E+004,  0.11802976874915821E+004,  0.11537804623936649E+004,  0.11387785556359743E+004,  0.11470050939051039E+004,  0.11522184926405614E+004,  0.11569811537983346E+004,  0.12041376348915505E+004,  0.11634694476631132E+004,  0.11306833855279181E+004,  0.10834030142636022E+004,  0.10551624101063521E+004,  0.10509309211719092E+004,  0.10493121457509164E+004,  0.10485599134102326E+004,  0.10477821870378020E+004,  0.10471635594281711E+004,  0.10436679708108866E+004,  0.10433841627142124E+004,  0.10442239651393813E+004,  0.10419241417561745E+004,  0.10380647868707858E+004,  0.10384133311289270E+004,  0.10399438804719052E+004,  0.10456740436600446E+004,  0.10395598821096344E+004,  0.10393771432079000E+004,  0.10303960472628316E+004,  0.10319845244744520E+004,  0.10575443951233233E+004,  0.10756137212553554E+004,  0.10592697576276344E+004,  0.11629159810118388E+004,  0.12294893308366434E+004,  0.12739487976702737E+004,  0.12971462377067151E+004,  0.13236509587045432E+004,  0.13626308799287292E+004,  0.14095617882865881E+004,  0.14594048626116444E+004,  0.14971069817103487E+004,  0.15348473940476958E+004,  0.15666414909005168E+004,  0.15884766061820440E+004,  0.15905276356615050E+004,  0.15828408944129837E+004,  0.15186108578087387E+004,  0.14083786000838986E+004,  0.13128611187804049E+004,  0.12347892610584026E+004,  0.11030360404880528E+004,  0.10630748442412009E+004,  0.10629936916404104E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.50207447630267335E-002,  0.34170603066316380E-002,  0.27419218545244716E-002,  0.21637078062003929E-002,  0.17185209848610396E-002,  0.13629212136507479E-002,  0.10247929766407024E-002,  0.70760889027027881E-003,  0.48443180873606028E-003,  0.33476127550566829E-003,  0.23584191844469549E-003,  0.17066250260969659E-003,  0.12625175191524008E-003,  0.96242227697105031E-004,  0.72646713799808332E-004,  0.53557593871088389E-004,  0.40229560064026816E-004,  0.31637316872229101E-004,  0.24902243268509679E-004,  0.18136487817619429E-004,  0.13569102625354919E-004,  0.11163250930044631E-004,  0.99762546046921155E-005,  0.89285134624758047E-005,  0.80277612752996547E-005,  0.66741088217895405E-005,  0.42816886402624958E-005,  0.38520074853635403E-005,  0.41012886420739054E-005,  0.45117688137668105E-005,  0.48645228712082408E-005,  0.46571025739053518E-005,  0.44108103662668000E-005,  0.42003216243533058E-005,  0.40150484389029171E-005,  0.38155543287706550E-005,  0.38745154775278862E-005,  0.38912055841526142E-005,  0.37965088316084779E-005,  0.36230711560612355E-005,  0.35018722854494095E-005,  0.33127327547715459E-005,  0.31236526968848981E-005,  0.29544078537477129E-005,  0.30051122314706651E-005,  0.28003271405915961E-005,  0.27764086990962070E-005,  0.28057136274550660E-005,  0.26556504193125485E-005,  0.25150114000521106E-005,  0.29858873102128098E-005,  0.22471067915701478E-005,  0.21895612191030409E-005,  0.20528364076539193E-005,  0.18763403423722409E-005,  0.16276161575279460E-005,  0.14685816372589583E-005,  0.14165858517436627E-005,  0.13642782510436368E-005,  0.13388618457214823E-005,  0.13107492927109261E-005,  0.12877389840979263E-005,  0.12550247943835433E-005,  0.12206546789912841E-005,  0.11802599135522154E-005,  0.11784846082832890E-005,  0.11885764080016044E-005,  0.11729484321868641E-005,  0.12230970002260489E-005,  0.16287890738972339E-005,  0.19708228528985077E-005,  0.19735682814115861E-005,],]
