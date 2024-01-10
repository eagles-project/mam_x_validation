# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1390 ] 
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
input.tair=[[  0.25203776810924032E+003,  0.25926847504423802E+003,  0.26232505621396643E+003,  0.25993306836297830E+003,  0.26192248137612501E+003,  0.26425131815689878E+003,  0.26339003694172453E+003,  0.25889555623257098E+003,  0.24917251706090389E+003,  0.24042713925235751E+003,  0.23546621843594886E+003,  0.23512373907622037E+003,  0.23391440464929994E+003,  0.23112587289016383E+003,  0.22428611646547273E+003,  0.21627426122881226E+003,  0.21034744044963628E+003,  0.20637545015341217E+003,  0.20181552840156129E+003,  0.19737421315704822E+003,  0.19248047225016484E+003,  0.18931654555907866E+003,  0.18821976782763750E+003,  0.18828365572618691E+003,  0.18854483441028935E+003,  0.18875954215013780E+003,  0.18657885540232482E+003,  0.18795909147936877E+003,  0.19134875166117359E+003,  0.19518033631596103E+003,  0.19935951649756038E+003,  0.20348455311523142E+003,  0.20779707197505027E+003,  0.21213609498783296E+003,  0.21660219376243788E+003,  0.22120453473407116E+003,  0.22582532400362612E+003,  0.23040335200676685E+003,  0.23509029511401147E+003,  0.23967348127412268E+003,  0.24410629241914810E+003,  0.24841130100215054E+003,  0.25266235022193959E+003,  0.25710457961860504E+003,  0.26178722225634544E+003,  0.26531688213458978E+003,  0.26786130145179459E+003,  0.27029857345653943E+003,  0.27153807847815852E+003,  0.27316285243452052E+003,  0.27517262399402262E+003,  0.27885342752822208E+003,  0.28169347895787172E+003,  0.28397996196715292E+003,  0.28596423554423848E+003,  0.28754696756384766E+003,  0.28878001414783046E+003,  0.28975533383185024E+003,  0.29060085045589079E+003,  0.29137251863441026E+003,  0.29212535740267691E+003,  0.29283264489614282E+003,  0.29344079135443860E+003,  0.29392730390371145E+003,  0.29436404540985387E+003,  0.29477776469510582E+003,  0.29513779941204990E+003,  0.29515286934840253E+003,  0.29504910864433560E+003,  0.29346256028745967E+003,  0.29310669960630935E+003,  0.29319032320828143E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473666246925062E+005,  0.19918643953466486E+005,  0.21465050416787955E+005,  0.23142879429804132E+005,  0.24963300159806477E+005,  0.26938431002943238E+005,  0.29081419950539334E+005,  0.31406531999563373E+005,  0.33929244940593118E+005,  0.36666352930396293E+005,  0.39636076958094622E+005,  0.42858185479048661E+005,  0.46304840717444204E+005,  0.49850913601525535E+005,  0.53380185776690276E+005,  0.56821962536070954E+005,  0.60142189206973671E+005,  0.63326794215582209E+005,  0.66332924630173467E+005,  0.69118492038726486E+005,  0.71643140862741973E+005,  0.73869219199358427E+005,  0.75762711902123017E+005,  0.77322180638538412E+005,  0.78640820250360674E+005,  0.79864323771861091E+005,  0.81058771935309705E+005,  0.82222247232556270E+005,  0.83352861670235070E+005,  0.84448765213352992E+005,  0.85508147239245824E+005,  0.86529236211053911E+005,  0.87510304271860368E+005,  0.88449678950746253E+005,  0.89345754626525217E+005,  0.90196989032664729E+005,  0.91006627918108075E+005,  0.91700649551205992E+005,  0.92137993596022294E+005,],]
input.radius_part=[[  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,],]
input.density_part=[[  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,],]
input.sig_part=[[  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.52964624525465875E+000,  0.36430514001657177E+000,  0.24868683365099803E+000,  0.16819920010225572E+000,  0.11486898556743616E+000,  0.78660935518498787E-001,  0.53735447676036205E-001,  0.36673597157650541E-001,  0.25037160854339071E-001,  0.17381959433052502E-001,  0.12630436655547264E-001,  0.96805283674451601E-002,  0.77516497450499863E-002,  0.64871952066871260E-002,  0.56792295152843942E-002,  0.51811912728251010E-002,  0.48624609335839713E-002,  0.46439782576574197E-002,  0.45099006790837283E-002,  0.44296138779645377E-002,  0.43968716044222528E-002,  0.43686582263728589E-002,  0.43290309786639261E-002,  0.42822270055261962E-002,  0.42369511237775959E-002,  0.41956143746527718E-002,  0.41973775942686174E-002,  0.41420367015480150E-002,  0.40563621914089147E-002,  0.39677958866614947E-002,  0.38783020209186172E-002,  0.37940042840909054E-002,  0.37112052295428040E-002,  0.36327720706350397E-002,  0.35572354271500559E-002,  0.34836680842494686E-002,  0.34131915892905680E-002,  0.33463277926976676E-002,  0.32812244417205509E-002,  0.32200406910727008E-002,  0.31629593815290721E-002,  0.31094641101132303E-002,  0.30586234643340312E-002,  0.30080869947584567E-002,  0.29575007238743590E-002,  0.29187097390576473E-002,  0.28897387236766535E-002,  0.28630575125395603E-002,  0.28472398887911649E-002,  0.28292731946842980E-002,  0.28091250229566678E-002,  0.27770181123872462E-002,  0.27524512454334166E-002,  0.27328652547112843E-002,  0.27161943577306401E-002,  0.27030200481299050E-002,  0.26928257267708334E-002,  0.26847795356793125E-002,  0.26778037232859102E-002,  0.26714300107376150E-002,  0.26652668520167960E-002,  0.26594947150319886E-002,  0.26544754446993562E-002,  0.26503530923111850E-002,  0.26466273040562814E-002,  0.26431116321346420E-002,  0.26400118125420122E-002,  0.26393008609290371E-002,  0.26394391795277203E-002,  0.26497592774432977E-002,  0.26517647013211297E-002,  0.26509114146188771E-002,],]
