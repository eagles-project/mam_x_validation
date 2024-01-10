# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1391 ] 
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
input.tair=[[  0.25165191658166566E+003,  0.25822278697420967E+003,  0.26215237651436564E+003,  0.26002049169276108E+003,  0.26192990786858309E+003,  0.26411170622772170E+003,  0.26361761077523028E+003,  0.25948421597319225E+003,  0.25002940735549723E+003,  0.24095301690692685E+003,  0.23543569082577849E+003,  0.23478473925440008E+003,  0.23353786634630603E+003,  0.23087025506402867E+003,  0.22425358728272840E+003,  0.21638842017102206E+003,  0.21044232485570450E+003,  0.20643499859197129E+003,  0.20188968092453118E+003,  0.19751950158038346E+003,  0.19266189342000234E+003,  0.18942931619310878E+003,  0.18825051220613710E+003,  0.18830186068686584E+003,  0.18856613379368295E+003,  0.18878192006352316E+003,  0.18651632024255932E+003,  0.18790938474920824E+003,  0.19135265458112704E+003,  0.19521523923991580E+003,  0.19935263326268870E+003,  0.20340769502577893E+003,  0.20767422117556558E+003,  0.21205446483832674E+003,  0.21655267676225228E+003,  0.22117544618415852E+003,  0.22573890210521816E+003,  0.23034117079818955E+003,  0.23502722133177514E+003,  0.23955304788859874E+003,  0.24396965874764118E+003,  0.24842453365762080E+003,  0.25271064131769865E+003,  0.25703363505675048E+003,  0.26152165666969881E+003,  0.26505670142288642E+003,  0.26770682135268873E+003,  0.27005750218743231E+003,  0.27136363143965997E+003,  0.27299220564867983E+003,  0.27516559920870009E+003,  0.27846341101057254E+003,  0.28164340742628468E+003,  0.28392103643285623E+003,  0.28588688259438334E+003,  0.28746695727120073E+003,  0.28869785593260491E+003,  0.28967025926953409E+003,  0.29051333775751732E+003,  0.29127946112755893E+003,  0.29201259996471373E+003,  0.29271343274368570E+003,  0.29332799518181469E+003,  0.29380435051650602E+003,  0.29421984471528083E+003,  0.29462683391983035E+003,  0.29495604251668607E+003,  0.29505679164484121E+003,  0.29454190550964336E+003,  0.29283672829872791E+003,  0.29276452873885415E+003,  0.29289582251285674E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473132410323138E+005,  0.19916776904475933E+005,  0.21461516680483379E+005,  0.23137537360909366E+005,  0.24955996075657116E+005,  0.26928998159917246E+005,  0.29069677434597121E+005,  0.31392283522714071E+005,  0.33912277532113760E+005,  0.36646435518532249E+005,  0.39612958833906974E+005,  0.42831594628004284E+005,  0.46274535127033341E+005,  0.49816786120312550E+005,  0.53342254512214153E+005,  0.56780321789760019E+005,  0.60096969983212221E+005,  0.63278142685418388E+005,  0.66281033150251256E+005,  0.69063598327158368E+005,  0.71585526132115338E+005,  0.73809205243331467E+005,  0.75700657175162327E+005,  0.77258445145412261E+005,  0.78575663552487109E+005,  0.79797848405781944E+005,  0.80991009216219099E+005,  0.82153230542007237E+005,  0.83282626424953254E+005,  0.84377348823449385E+005,  0.85435589066979242E+005,  0.86455577528768918E+005,  0.87435588213308263E+005,  0.88373950451482626E+005,  0.89269060353450448E+005,  0.90119377315673977E+005,  0.90928197398114673E+005,  0.91621589223621078E+005,  0.92058556209347618E+005,],]
input.radius_part=[[  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.40892390868573417E-007,  0.44915107967524496E-007,  0.42825435101729700E-007,  0.47230937933605668E-007,  0.49977444329418512E-007,  0.53952523215365919E-007,  0.58774419244295775E-007,  0.64634622877473248E-007,  0.71905853195866435E-007,  0.83770128808553223E-007,  0.99718508179019669E-007,  0.11558564321195025E-006,  0.12442687357851479E-006,  0.12597876817807057E-006,  0.12649015907363378E-006,  0.12762042173566145E-006,  0.12676969869321272E-006,  0.12553367177130933E-006,  0.12552807865703652E-006,  0.12527459783441246E-006,  0.12310456363381561E-006,  0.12149583349669027E-006,  0.12167350084814210E-006,  0.12213943042178165E-006,  0.12264540112036727E-006,  0.12303455909927460E-006,  0.12341198066521092E-006,  0.12394068737170478E-006,  0.12434842580452338E-006,  0.12318390876427874E-006,  0.12156348988675153E-006,  0.11764146320308011E-006,  0.11585912077759799E-006,  0.11652671799054591E-006,  0.11883285509716669E-006,  0.12056957012094559E-006,  0.12196062067067157E-006,  0.12302980849859560E-006,  0.14321838433537626E-006,  0.15766538375743207E-006,  0.15882631446227792E-006,  0.15924757932241005E-006,  0.21374504770629151E-006,  0.20646413656025370E-006,  0.14810641776397628E-006,  0.13602105791067733E-006,  0.13211261766987815E-006,  0.12980537484348216E-006,  0.12884398764518737E-006,  0.12864726080248488E-006,  0.12848827528466125E-006,  0.12836083300805483E-006,  0.12826638362147631E-006,  0.12808271744625293E-006,  0.12787715767596767E-006,  0.12796828784735943E-006,  0.12775449840561798E-006,  0.12650414085846028E-006,  0.12697549775602062E-006,  0.13023815278657600E-006,  0.13540147180167160E-006,  0.14131933921137496E-006,  0.22484818913422677E-006,  0.23438157456786201E-006,  0.23454249923546298E-006,],]
input.density_part=[[  0.16406454499626400E+004,  0.16683263699473282E+004,  0.16822340490329254E+004,  0.16954324608819109E+004,  0.17033924162412143E+004,  0.17038345679641238E+004,  0.17135536665443606E+004,  0.16816587242926778E+004,  0.15807401379011831E+004,  0.15665069715908476E+004,  0.15541242015227508E+004,  0.15382928776823251E+004,  0.15175257279858747E+004,  0.15122997875065396E+004,  0.15485433045236703E+004,  0.15424779690741166E+004,  0.14158657770701168E+004,  0.13318619936663847E+004,  0.13414117424118508E+004,  0.12971464887786613E+004,  0.12594740006126665E+004,  0.12281886651338079E+004,  0.12103716302999967E+004,  0.12086758774413622E+004,  0.12010549076764530E+004,  0.11840907624769445E+004,  0.11825961195731006E+004,  0.11992856920756080E+004,  0.12015558382776462E+004,  0.11844112126434320E+004,  0.11735985819737189E+004,  0.11678647751099863E+004,  0.11624085306408795E+004,  0.11493155869503248E+004,  0.11392261470365061E+004,  0.11298393390280435E+004,  0.11236492389135803E+004,  0.11183400227624397E+004,  0.11161349069612086E+004,  0.11144819278957502E+004,  0.11169456430454211E+004,  0.11248075783362265E+004,  0.11281898298438693E+004,  0.11281019377398434E+004,  0.11291944565255396E+004,  0.10924432794921584E+004,  0.10720898200286731E+004,  0.10688282725080239E+004,  0.10748951855422570E+004,  0.10333376602184289E+004,  0.10384986111928799E+004,  0.11054960964039381E+004,  0.11357442300417911E+004,  0.11470551694830122E+004,  0.11535763886221946E+004,  0.11547924889951437E+004,  0.11535630456757751E+004,  0.11525672940624086E+004,  0.11519436312689522E+004,  0.11507150812975990E+004,  0.11493247696534070E+004,  0.11472011910607346E+004,  0.11432582375590835E+004,  0.11404654391955985E+004,  0.11432353143923233E+004,  0.11408142215146900E+004,  0.11295052040500095E+004,  0.11181693631899577E+004,  0.11043608004240532E+004,  0.10269547816140616E+004,  0.10240372973038372E+004,  0.10240345100954494E+004,],]
input.sig_part=[[  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.24256318104661178E-001,  0.16922450651125714E-001,  0.11644706990230645E-001,  0.79166125445491401E-002,  0.54070769547811155E-002,  0.36786900420643998E-002,  0.25038077834577946E-002,  0.15035416477697766E-002,  0.10325959144846550E-002,  0.64911665260178146E-003,  0.48639873829008995E-003,  0.36302394909988578E-003,  0.28219315732419276E-003,  0.22871255648990231E-003,  0.19567811826994827E-003,  0.16871668300244818E-003,  0.14506295851362828E-003,  0.13488494628712138E-003,  0.13395475590984059E-003,  0.12101604472741724E-003,  0.10484376889546131E-003,  0.92493051375802142E-004,  0.84798748960742394E-004,  0.78389824453832107E-004,  0.72070340314245459E-004,  0.66575497077566017E-004,  0.62079923882976998E-004,  0.57956811368588966E-004,  0.53868405625049018E-004,  0.50213766614612857E-004,  0.47235638025927539E-004,  0.44676480884653384E-004,  0.42252622007412944E-004,  0.39802254523145625E-004,  0.37768044557419171E-004,  0.35850227280727757E-004,  0.33553029086775051E-004,  0.31267488058474281E-004,  0.28443612882504965E-004,  0.26521426746906078E-004,  0.25569858317211009E-004,  0.25289247726183924E-004,  0.24768635922068673E-004,  0.24110708153706395E-004,  0.23428698306795004E-004,  0.27501910991348983E-004,  0.30412507827831865E-004,  0.29814892336213536E-004,  0.29393878349379579E-004,  0.45562635429678583E-004,  0.42377571021212124E-004,  0.25183903556882495E-004,  0.22072771080757263E-004,  0.20923117019576767E-004,  0.20173177706449987E-004,  0.19734098944373383E-004,  0.19494902654311458E-004,  0.19301963290108782E-004,  0.19138245204607119E-004,  0.18980273026103653E-004,  0.18804324955451096E-004,  0.18617678958198303E-004,  0.18480867267622585E-004,  0.18297760106491080E-004,  0.17963610869227110E-004,  0.17961537255989205E-004,  0.18485186414602508E-004,  0.19477165943480260E-004,  0.20644530564318975E-004,  0.43473830605917103E-004,  0.46667940524007714E-004,  0.46672678273936816E-004,],]
