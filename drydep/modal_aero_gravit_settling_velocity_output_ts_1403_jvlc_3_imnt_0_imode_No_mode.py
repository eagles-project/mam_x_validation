# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1403 ] 
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
input.tair=[[  0.25281556696133487E+003,  0.25718902986876088E+003,  0.26306170108709108E+003,  0.26548835083556901E+003,  0.26810865709675392E+003,  0.26719425890566140E+003,  0.26527007462610862E+003,  0.26109773829825076E+003,  0.25309650755806592E+003,  0.24435123176634494E+003,  0.23692876993630969E+003,  0.23380072885277946E+003,  0.23169544898932588E+003,  0.22904884599711485E+003,  0.22331107048217055E+003,  0.21618309785117054E+003,  0.20954155597507264E+003,  0.20478477249755477E+003,  0.20020657803233487E+003,  0.19622177198764908E+003,  0.19223753804665265E+003,  0.18985017625879777E+003,  0.18918306943873708E+003,  0.18965427093258745E+003,  0.19046462348396946E+003,  0.19250991880546712E+003,  0.19247743676223939E+003,  0.18977293941010552E+003,  0.19122985333622506E+003,  0.19537397129921686E+003,  0.19914101701139518E+003,  0.20300921915673615E+003,  0.20757307135277469E+003,  0.21229081273002970E+003,  0.21687696844640612E+003,  0.22129012493047421E+003,  0.22581022935246463E+003,  0.23044149917435610E+003,  0.23527767093728843E+003,  0.24013166703828057E+003,  0.24486211762658380E+003,  0.24937316465864910E+003,  0.25370737023165194E+003,  0.25757752366731535E+003,  0.26134373696961961E+003,  0.26483173386860000E+003,  0.26733148670507626E+003,  0.26929402421255446E+003,  0.27066071774003501E+003,  0.27316739008333195E+003,  0.27525694398000468E+003,  0.27788274110068602E+003,  0.28092918534887446E+003,  0.28368644445668525E+003,  0.28600172165370867E+003,  0.28776244457351680E+003,  0.28898365304626856E+003,  0.28994274364161771E+003,  0.29081742252675230E+003,  0.29163593271481619E+003,  0.29237529852787441E+003,  0.29305594627777009E+003,  0.29362837888274959E+003,  0.29410269687695205E+003,  0.29417681480965138E+003,  0.29441860082566143E+003,  0.29518912066997325E+003,  0.29601164912937929E+003,  0.29682017769520303E+003,  0.29760980868181042E+003,  0.29831719880993217E+003,  0.29882252225585029E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472853679656728E+005,  0.19915802067217708E+005,  0.21459671620269175E+005,  0.23134748120872835E+005,  0.24952182413882831E+005,  0.26924073015007154E+005,  0.29063546346391249E+005,  0.31384844003892696E+005,  0.33903418384847209E+005,  0.36636036093947936E+005,  0.39600888230022232E+005,  0.42817710818603933E+005,  0.46258711750777831E+005,  0.49798967230511524E+005,  0.53322449563308161E+005,  0.56758580019099711E+005,  0.60073359791763738E+005,  0.63252740393077227E+005,  0.66253939191673562E+005,  0.69034936821461641E+005,  0.71555443908070025E+005,  0.73777870318193163E+005,  0.75668256707795750E+005,  0.77225167104136941E+005,  0.78541643461406798E+005,  0.79763139802024933E+005,  0.80955628450303295E+005,  0.82117195043352986E+005,  0.83245954685600052E+005,  0.84340060376237685E+005,  0.85397704464019174E+005,  0.86417118319478512E+005,  0.87396576918996871E+005,  0.88334410534230788E+005,  0.89229016179321101E+005,  0.90078854119025054E+005,  0.90887246682060446E+005,  0.91580309667826266E+005,  0.92017079780706350E+005,],]
input.radius_part=[[  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,],]
input.density_part=[[  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,],]
input.sig_part=[[  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.53045613844351447E+000,  0.36285847170473429E+000,  0.24902982243034721E+000,  0.16994173448266850E+000,  0.11616740562475329E+000,  0.79073715016599280E-001,  0.53911046728612744E-001,  0.36809445033722576E-001,  0.25193877866277865E-001,  0.17477962584276314E-001,  0.12650601020531834E-001,  0.96718538591773710E-002,  0.77484762017892362E-002,  0.64921093739451832E-002,  0.56846315155159406E-002,  0.51819393702870285E-002,  0.48707160518697556E-002,  0.46625608345005256E-002,  0.45307220220019298E-002,  0.44457789841839896E-002,  0.44005395321364375E-002,  0.43602094754268197E-002,  0.43134649158884366E-002,  0.42599840702001058E-002,  0.42057885503746333E-002,  0.41351789318441693E-002,  0.41004966458275576E-002,  0.41118620289292964E-002,  0.40582933016657706E-002,  0.39647795527266881E-002,  0.38815699612901118E-002,  0.38008341264709105E-002,  0.37142853313682027E-002,  0.36307470794457600E-002,  0.35538053659130301E-002,  0.34826879774962271E-002,  0.34134378727786745E-002,  0.33459879789702559E-002,  0.32793192110000865E-002,  0.32154450733126350E-002,  0.31556071496061599E-002,  0.31004160474262959E-002,  0.30491198680602941E-002,  0.30039866125855992E-002,  0.29614362528903012E-002,  0.29228942171930358E-002,  0.28942153477658273E-002,  0.28713175342895934E-002,  0.28544018053323116E-002,  0.28293355799917878E-002,  0.28085619641670567E-002,  0.27845243286454828E-002,  0.27582567566212242E-002,  0.27351104506262423E-002,  0.27160118213962361E-002,  0.27015672111466854E-002,  0.26914688158628268E-002,  0.26835456048991844E-002,  0.26763726782552538E-002,  0.26696803683587639E-002,  0.26636190614100596E-002,  0.26580379573973249E-002,  0.26532692836828894E-002,  0.26492338245737170E-002,  0.26479868850074928E-002,  0.26456400693554713E-002,  0.26397424308928692E-002,  0.26335630322262241E-002,  0.26275497386054427E-002,  0.26217294287926626E-002,  0.26165667328903711E-002,  0.26129335740718135E-002,],]