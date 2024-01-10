# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1395 ] 
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
input.tair=[[  0.25005945970182350E+003,  0.25432958655802358E+003,  0.26103897304230861E+003,  0.26203784366399361E+003,  0.26542765390621605E+003,  0.26655621605513392E+003,  0.26497509918168697E+003,  0.26086517213279376E+003,  0.25249007394953776E+003,  0.24301480517030149E+003,  0.23550840992002352E+003,  0.23328947657272721E+003,  0.23149879073057281E+003,  0.22884791137467033E+003,  0.22277742016377397E+003,  0.21560631414350442E+003,  0.20994542382872888E+003,  0.20608843524255192E+003,  0.20174403697271427E+003,  0.19778564134582302E+003,  0.19338352190848366E+003,  0.19022477469066700E+003,  0.18886392326351523E+003,  0.18884856779370384E+003,  0.18917630354094044E+003,  0.18979447362175253E+003,  0.18728843123728859E+003,  0.18777697973952908E+003,  0.19132440119815533E+003,  0.19522856580462974E+003,  0.19914364942905326E+003,  0.20299991222704452E+003,  0.20730468821866538E+003,  0.21181043049799072E+003,  0.21640349002218119E+003,  0.22097349169008086E+003,  0.22552793704852081E+003,  0.23019076017692564E+003,  0.23465569108913780E+003,  0.23911503283746140E+003,  0.24375432942537628E+003,  0.24825076012680580E+003,  0.25306408972252916E+003,  0.25757741805370932E+003,  0.26109889069595687E+003,  0.26451340624795233E+003,  0.26710051130795694E+003,  0.26908419442758571E+003,  0.27049469079307596E+003,  0.27274494400631937E+003,  0.27504180583943196E+003,  0.27760814705769542E+003,  0.28104680277193063E+003,  0.28393922231887854E+003,  0.28592985090216757E+003,  0.28746222664867753E+003,  0.28868249760259539E+003,  0.28964315578892246E+003,  0.29047669703958707E+003,  0.29123592057001883E+003,  0.29192546208948693E+003,  0.29255356940631100E+003,  0.29316704999294154E+003,  0.29366410611803781E+003,  0.29400854299691213E+003,  0.29433744658436513E+003,  0.29451136182445941E+003,  0.29421855472693744E+003,  0.29340617727604240E+003,  0.29180246792237381E+003,  0.29218756330146539E+003,  0.29248154010725563E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473145914336663E+005,  0.19916824133636925E+005,  0.21461606070425303E+005,  0.23137672494713112E+005,  0.24956180840903209E+005,  0.26929236774578225E+005,  0.29069974475102601E+005,  0.31392643954395531E+005,  0.33912706742311668E+005,  0.36646939352473550E+005,  0.39613543633563902E+005,  0.42832267274298676E+005,  0.46275301741951203E+005,  0.49817649414373212E+005,  0.53343214027366521E+005,  0.56781375140540520E+005,  0.60098113855713615E+005,  0.63279373382075166E+005,  0.66282345805179895E+005,  0.69064986927004618E+005,  0.71586983563281930E+005,  0.73810723365676095E+005,  0.75702226921165187E+005,  0.77260057408336870E+005,  0.78577311766427549E+005,  0.79799529976957943E+005,  0.80992723352476649E+005,  0.82154976398921397E+005,  0.83284403106617014E+005,  0.84379155383530800E+005,  0.85437424509764489E+005,  0.86457440810226355E+005,  0.87437478242319849E+005,  0.88375866091351549E+005,  0.89271000423683581E+005,  0.90121340593710775E+005,  0.90930181388719284E+005,  0.91623589145936261E+005,  0.92060565669808057E+005,],]
input.radius_part=[[  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.42516037301564181E-007,  0.47047027154843608E-007,  0.50068087848914882E-007,  0.54144311484538793E-007,  0.59015860021177523E-007,  0.64805822193360292E-007,  0.72330655764717181E-007,  0.84731264886683497E-007,  0.10012111470407485E-006,  0.11520429188542057E-006,  0.12431629019851716E-006,  0.12599525654140836E-006,  0.12642330535909688E-006,  0.12675382961961920E-006,  0.12649833353143937E-006,  0.12581356676987757E-006,  0.12541044269367456E-006,  0.12522850922595812E-006,  0.12302501147249064E-006,  0.12128128354849934E-006,  0.12153641767195800E-006,  0.12231624670234981E-006,  0.12330838631661835E-006,  0.12377892229408748E-006,  0.12396555520570165E-006,  0.12265459725026354E-006,  0.12069333806606107E-006,  0.11677473567507992E-006,  0.11483961608054486E-006,  0.11477150508934097E-006,  0.11713366078491774E-006,  0.11986805097084274E-006,  0.12070940455846244E-006,  0.12193271425012833E-006,  0.13090126772731432E-006,  0.12574046701206732E-006,  0.14581704874312377E-006,  0.15669161354196467E-006,  0.18944824312501783E-006,  0.17902111274929284E-006,  0.14735732658617412E-006,  0.24672679371742648E-006,  0.16366789936800052E-006,  0.13940294616838317E-006,  0.13185380245684318E-006,  0.13022397002985120E-006,  0.12925958203058911E-006,  0.12888528489564626E-006,  0.12868366280485071E-006,  0.12857909321878093E-006,  0.12857319111835390E-006,  0.12863873189022074E-006,  0.12880885394014455E-006,  0.12889085630106020E-006,  0.12828899892440534E-006,  0.12727762671038176E-006,  0.12619270777573278E-006,  0.12895871242251144E-006,  0.13710288454366459E-006,  0.15241814117170252E-006,  0.17818355530149026E-006,  0.15158614219365741E-006,  0.23738490036915714E-006,],]
input.density_part=[[  0.16440985160980633E+004,  0.16651557919322770E+004,  0.16834725811448764E+004,  0.16955838492462999E+004,  0.17006849974444433E+004,  0.17002556273076489E+004,  0.17109398459589554E+004,  0.16886987650904591E+004,  0.15865044907909819E+004,  0.15678011505482229E+004,  0.15546909833621849E+004,  0.15377835505453379E+004,  0.15168107027432702E+004,  0.15134320152073021E+004,  0.15501557328979723E+004,  0.15372234336920119E+004,  0.14084968536633739E+004,  0.13314959626420284E+004,  0.13435884109621697E+004,  0.13011167210369008E+004,  0.12615734873968806E+004,  0.12298802918678318E+004,  0.12139035556972510E+004,  0.12089008252977160E+004,  0.12000993707555856E+004,  0.11895813946287865E+004,  0.11813930147034278E+004,  0.12016049234665995E+004,  0.11956604299805063E+004,  0.11876429403503053E+004,  0.11879388944437762E+004,  0.11776077677602102E+004,  0.11576048065947543E+004,  0.11402506018383024E+004,  0.11318756235320707E+004,  0.11239412001016724E+004,  0.11191225044261455E+004,  0.11147323913180037E+004,  0.11117143633345768E+004,  0.11129940312681265E+004,  0.11207928848269062E+004,  0.11274973002617121E+004,  0.11272909391880155E+004,  0.11079161419746983E+004,  0.11305229186526301E+004,  0.10882206047365469E+004,  0.10722342087770869E+004,  0.10403744394671160E+004,  0.10540560620094575E+004,  0.10251640432053298E+004,  0.10228498613951343E+004,  0.10799501477705383E+004,  0.11295163321266255E+004,  0.11527723149316275E+004,  0.11573135333150933E+004,  0.11584908299921963E+004,  0.11569199816466448E+004,  0.11548021486278951E+004,  0.11529529176823116E+004,  0.11508966921412775E+004,  0.11480272601717541E+004,  0.11449585991471833E+004,  0.11414896597489176E+004,  0.11381049552499289E+004,  0.11371259457860508E+004,  0.11392485660921841E+004,  0.11307086025671283E+004,  0.11092329950928668E+004,  0.10825873323955575E+004,  0.10251105348709445E+004,  0.10526621651205048E+004,  0.10237674971346994E+004,],]
input.sig_part=[[  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.24230351525552654E-001,  0.16762508264867727E-001,  0.11628515150007354E-001,  0.79479586705840499E-002,  0.54343836219969367E-002,  0.36878952273388366E-002,  0.25064074961829007E-002,  0.16628880907502673E-002,  0.10414307724026281E-002,  0.64768947311004518E-003,  0.48474955056918489E-003,  0.36242067887324464E-003,  0.28185583538266725E-003,  0.22885467705350778E-003,  0.19578995610483854E-003,  0.16887375981611158E-003,  0.14587050542932693E-003,  0.13532637328110607E-003,  0.13365636408356504E-003,  0.12132520987134313E-003,  0.10516149159984225E-003,  0.92679220539733948E-004,  0.84448561876397923E-004,  0.78263918792033347E-004,  0.72258962791483039E-004,  0.66884734657132646E-004,  0.62035812361622535E-004,  0.58015560772246461E-004,  0.53484582741403070E-004,  0.50279580819836126E-004,  0.47895412245496198E-004,  0.45355742806679158E-004,  0.42405759997474545E-004,  0.39720225135938950E-004,  0.37003872678224698E-004,  0.34256675832082130E-004,  0.31082565660565980E-004,  0.28836731699319626E-004,  0.27384741480893616E-004,  0.26893347456397433E-004,  0.26704193563469100E-004,  0.25926699354890882E-004,  0.25153222067891529E-004,  0.26295624716731601E-004,  0.24241288895246447E-004,  0.28192012590821290E-004,  0.30134896869421127E-004,  0.38902770188629617E-004,  0.35057855978776310E-004,  0.24141575513306843E-004,  0.57046152713459102E-004,  0.29112498643730177E-004,  0.22874356893560530E-004,  0.20959200269595833E-004,  0.20344763599186866E-004,  0.19902545597152222E-004,  0.19611588682571330E-004,  0.19388528652341878E-004,  0.19209702388733512E-004,  0.19059547999919194E-004,  0.18920711732555337E-004,  0.18810824051074561E-004,  0.18678309614796634E-004,  0.18390724005756052E-004,  0.18055082355491641E-004,  0.17758621926292121E-004,  0.18210578830962321E-004,  0.19757353874057553E-004,  0.23080557144544590E-004,  0.28709265557274703E-004,  0.22172138497932107E-004,  0.47728085355023703E-004,],]
