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
input.radius_part=[[  0.21056025973256349E-007,  0.22534604730179977E-007,  0.25523011337477904E-007,  0.28253847601223238E-007,  0.30892830987473554E-007,  0.35576932278598930E-007,  0.40215554046381987E-007,  0.42720903607433526E-007,  0.44325645736247197E-007,  0.46322316626047766E-007,  0.48140124801304080E-007,  0.49892546279156274E-007,  0.51207465806545648E-007,  0.52411177105168344E-007,  0.54838297622610625E-007,  0.59970481558696180E-007,  0.64953693976108498E-007,  0.67073302890792156E-007,  0.68058163260486119E-007,  0.69181375131581406E-007,  0.69517115473267940E-007,  0.69642718832189588E-007,  0.69642718838267420E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69561141791072966E-007,  0.69642718953771122E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642718832189588E-007,  0.69642719106336791E-007,  0.69642719209798967E-007,  0.69642719177700587E-007,  0.69642720040680028E-007,  0.69642720245519409E-007,  0.69642720262036485E-007,  0.69642721068533069E-007,  0.69642722442445259E-007,  0.69642720880426732E-007,  0.69642719790441614E-007,  0.69642719334016256E-007,  0.69642719149632205E-007,  0.69642719096175307E-007,  0.69642719097199463E-007,  0.69642719111323261E-007,  0.69642719128545426E-007,  0.69642719139470113E-007,  0.69642719155901400E-007,  0.69642719188818080E-007,  0.69642719267411144E-007,  0.69642719312890725E-007,  0.69642719423525166E-007,  0.69642719819902571E-007,  0.69642719736175535E-007,  0.69642719591840896E-007,  0.69642719469597061E-007,  0.69642719373893760E-007,  0.69642719306127352E-007,  0.69642719267636216E-007,],]
input.density_part=[[  0.10467964195798036E+004,  0.10464066156651877E+004,  0.10464724346942189E+004,  0.10463139667167509E+004,  0.10456825703305053E+004,  0.10452382099518711E+004,  0.10452845364202565E+004,  0.10450183886387538E+004,  0.10446369152778118E+004,  0.10446909884150821E+004,  0.10437277101120401E+004,  0.10421214182266324E+004,  0.10402958420329212E+004,  0.10365681784589328E+004,  0.10326701461840987E+004,  0.10384377546035537E+004,  0.10528812219675765E+004,  0.10675718624388160E+004,  0.10685023008483224E+004,  0.10642206542288427E+004,  0.10575476590202240E+004,  0.10566722059524739E+004,  0.10566913030219805E+004,  0.10580412195054059E+004,  0.10582018509177503E+004,  0.10584784163583226E+004,  0.10598807971826441E+004,  0.10637726512942834E+004,  0.10651614849826171E+004,  0.10658969371131461E+004,  0.10644371082940850E+004,  0.10617290438360019E+004,  0.10612861060646201E+004,  0.10597188870280395E+004,  0.10580486142824088E+004,  0.10577612213659427E+004,  0.10577531639677463E+004,  0.10582207700930985E+004,  0.10581449286008769E+004,  0.10579201140409343E+004,  0.10579114503239207E+004,  0.10581260250755795E+004,  0.10583983722329390E+004,  0.10598716966277725E+004,  0.10606966647046509E+004,  0.10570289853028332E+004,  0.10529365232422981E+004,  0.10485659440070633E+004,  0.10444677336498576E+004,  0.10436603945501963E+004,  0.10435364637111759E+004,  0.10435007154644818E+004,  0.10434584472280865E+004,  0.10432879305207289E+004,  0.10431137356574779E+004,  0.10432283247218018E+004,  0.10434979770798386E+004,  0.10437038219266069E+004,  0.10438593662572798E+004,  0.10446151769045644E+004,  0.10454928088871368E+004,  0.10457533268411171E+004,  0.10452885852170641E+004,  0.10477793775446492E+004,  0.10577975192581862E+004,  0.10616858374653013E+004,  0.10626327042899841E+004,  0.10630740423584145E+004,  0.10633466110893598E+004,  0.10635187484139792E+004,  0.10636108827564867E+004,  0.10636468988255392E+004,],]
input.sig_part=[[  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,  0.16000000238418579E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.24235178891896872E-002,  0.17711250079456137E-002,  0.13741371604692782E-002,  0.10348462502717311E-002,  0.76966674952308120E-003,  0.59906538407008083E-003,  0.45703744268571587E-003,  0.32618607909734159E-003,  0.22564023174151605E-003,  0.15698211314781071E-003,  0.11111121402666981E-003,  0.81428265000080345E-004,  0.60691814914361955E-004,  0.46101898248949496E-004,  0.36447829575770957E-004,  0.31074211153479915E-004,  0.27150625061951430E-004,  0.23223667538439711E-004,  0.19665292231246237E-004,  0.16958936826884503E-004,  0.14709018596680371E-004,  0.13090854554753950E-004,  0.11916223124527713E-004,  0.11018808387335806E-004,  0.10210470948293818E-004,  0.94914240621413771E-005,  0.87821650376177781E-005,  0.81195320915090841E-005,  0.75526425407033169E-005,  0.70632833647441727E-005,  0.65869392739077754E-005,  0.61371830172843041E-005,  0.57384892989513553E-005,  0.53757377120160831E-005,  0.50505099508976788E-005,  0.47522159345873712E-005,  0.44717655789343108E-005,  0.42090661595263834E-005,  0.39598540756747629E-005,  0.37240039071001055E-005,  0.35015865700826660E-005,  0.32917289925623717E-005,  0.30937594224152688E-005,  0.29093923245392074E-005,  0.27344048004719406E-005,  0.25611363435151457E-005,  0.24036499183847615E-005,  0.22654002109985096E-005,  0.21460034515338190E-005,  0.20520673386791986E-005,  0.19717138014476473E-005,  0.19040566369257968E-005,  0.18473918189941368E-005,  0.17994500984992231E-005,  0.17595769063608427E-005,  0.17275875510758840E-005,  0.17023748070566836E-005,  0.16816912985700709E-005,  0.16630225148167019E-005,  0.16462392215665800E-005,  0.16305121822660141E-005,  0.16146938712614955E-005,  0.15985705996099107E-005,  0.15877412894518243E-005,  0.15886295930501840E-005,  0.15811778024446454E-005,  0.15706503057596392E-005,  0.15602177144785310E-005,  0.15503037950181698E-005,  0.15409303884466543E-005,  0.15329669303267877E-005,  0.15280280641654571E-005,],]
