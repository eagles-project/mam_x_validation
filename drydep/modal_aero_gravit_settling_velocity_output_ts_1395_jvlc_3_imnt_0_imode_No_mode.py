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
input.moment=[[         0],]
input.ncol=[[         4],]
input.pcols=[[         4],]
input.nver=[[        72],]
input.radius_max=[[  0.50000000000000002E-004],]
input.tair=[[  0.25005945970182350E+003,  0.25432958655802358E+003,  0.26103897304230861E+003,  0.26203784366399361E+003,  0.26542765390621605E+003,  0.26655621605513392E+003,  0.26497509918168697E+003,  0.26086517213279376E+003,  0.25249007394953776E+003,  0.24301480517030149E+003,  0.23550840992002352E+003,  0.23328947657272721E+003,  0.23149879073057281E+003,  0.22884791137467033E+003,  0.22277742016377397E+003,  0.21560631414350442E+003,  0.20994542382872888E+003,  0.20608843524255192E+003,  0.20174403697271427E+003,  0.19778564134582302E+003,  0.19338352190848366E+003,  0.19022477469066700E+003,  0.18886392326351523E+003,  0.18884856779370384E+003,  0.18917630354094044E+003,  0.18979447362175253E+003,  0.18728843123728859E+003,  0.18777697973952908E+003,  0.19132440119815533E+003,  0.19522856580462974E+003,  0.19914364942905326E+003,  0.20299991222704452E+003,  0.20730468821866538E+003,  0.21181043049799072E+003,  0.21640349002218119E+003,  0.22097349169008086E+003,  0.22552793704852081E+003,  0.23019076017692564E+003,  0.23465569108913780E+003,  0.23911503283746140E+003,  0.24375432942537628E+003,  0.24825076012680580E+003,  0.25306408972252916E+003,  0.25757741805370932E+003,  0.26109889069595687E+003,  0.26451340624795233E+003,  0.26710051130795694E+003,  0.26908419442758571E+003,  0.27049469079307596E+003,  0.27274494400631937E+003,  0.27504180583943196E+003,  0.27760814705769542E+003,  0.28104680277193063E+003,  0.28393922231887854E+003,  0.28592985090216757E+003,  0.28746222664867753E+003,  0.28868249760259539E+003,  0.28964315578892246E+003,  0.29047669703958707E+003,  0.29123592057001883E+003,  0.29192546208948693E+003,  0.29255356940631100E+003,  0.29316704999294154E+003,  0.29366410611803781E+003,  0.29400854299691213E+003,  0.29433744658436513E+003,  0.29451136182445941E+003,  0.29421855472693744E+003,  0.29340617727604240E+003,  0.29180246792237381E+003,  0.29218756330146539E+003,  0.29248154010725563E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473145914336663E+005,  0.19916824133636925E+005,  0.21461606070425303E+005,  0.23137672494713112E+005,  0.24956180840903209E+005,  0.26929236774578225E+005,  0.29069974475102601E+005,  0.31392643954395531E+005,  0.33912706742311668E+005,  0.36646939352473550E+005,  0.39613543633563902E+005,  0.42832267274298676E+005,  0.46275301741951203E+005,  0.49817649414373212E+005,  0.53343214027366521E+005,  0.56781375140540520E+005,  0.60098113855713615E+005,  0.63279373382075166E+005,  0.66282345805179895E+005,  0.69064986927004618E+005,  0.71586983563281930E+005,  0.73810723365676095E+005,  0.75702226921165187E+005,  0.77260057408336870E+005,  0.78577311766427549E+005,  0.79799529976957943E+005,  0.80992723352476649E+005,  0.82154976398921397E+005,  0.83284403106617014E+005,  0.84379155383530800E+005,  0.85437424509764489E+005,  0.86457440810226355E+005,  0.87437478242319849E+005,  0.88375866091351549E+005,  0.89271000423683581E+005,  0.90121340593710775E+005,  0.90930181388719284E+005,  0.91623589145936261E+005,  0.92060565669808057E+005,],]
input.radius_part=[[  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,],]
input.density_part=[[  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,],]
input.sig_part=[[  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.52758075079055389E+000,  0.36085980524766287E+000,  0.24808690502442235E+000,  0.16886146559039206E+000,  0.11560640230777830E+000,  0.78984393087583579E-001,  0.53883528850835832E-001,  0.36795117003442915E-001,  0.25169691669460335E-001,  0.17445255278116814E-001,  0.12631017162122143E-001,  0.96685311633682627E-002,  0.77482139799318252E-002,  0.64926063778247348E-002,  0.56876325402755896E-002,  0.51866969239248006E-002,  0.48665676782473129E-002,  0.46473033874072861E-002,  0.45108170782078892E-002,  0.44238977614554330E-002,  0.43833322538133334E-002,  0.43543116038118621E-002,  0.43186016925739869E-002,  0.42730144291249720E-002,  0.42266211490748886E-002,  0.41786655265715024E-002,  0.41853572039870397E-002,  0.41451025990297498E-002,  0.40567574646781799E-002,  0.39670439697151874E-002,  0.38815305425681876E-002,  0.38009682074037162E-002,  0.37179853966282008E-002,  0.36370749061136565E-002,  0.35597668058595026E-002,  0.34864993761558492E-002,  0.34166893944851981E-002,  0.33487502452844101E-002,  0.32859374527382957E-002,  0.32258583566582085E-002,  0.31665188201241679E-002,  0.31110709193798367E-002,  0.30549885799651079E-002,  0.30039471027974614E-002,  0.29635133246384781E-002,  0.29255371481546463E-002,  0.28960875887123223E-002,  0.28729918086048949E-002,  0.28557070204324282E-002,  0.28326553648455924E-002,  0.28102093952560407E-002,  0.27865973862849147E-002,  0.27573423512719845E-002,  0.27332217531164452E-002,  0.27164997620134361E-002,  0.27036822644008881E-002,  0.26935727780986779E-002,  0.26856247517047247E-002,  0.26787277964706807E-002,  0.26724357980053835E-002,  0.26667065495838797E-002,  0.26614744314213041E-002,  0.26564101143565231E-002,  0.26522089003047137E-002,  0.26491090987256199E-002,  0.26461655268598255E-002,  0.26443272956426915E-002,  0.26457191924478614E-002,  0.26507247018742234E-002,  0.26612918674029816E-002,  0.26581715848207014E-002,  0.26558567985766391E-002,],]
