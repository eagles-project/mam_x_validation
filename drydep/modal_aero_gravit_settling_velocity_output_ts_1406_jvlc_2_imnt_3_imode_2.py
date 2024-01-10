# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1406 ] 
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
input.tair=[[  0.25435033558770152E+003,  0.26658416567070367E+003,  0.27161465885213585E+003,  0.27305969079622753E+003,  0.27224151832595254E+003,  0.26925616778151590E+003,  0.26635165683534740E+003,  0.26072780995730903E+003,  0.25153551063929930E+003,  0.24279542054437644E+003,  0.23636440233214500E+003,  0.23395470415890776E+003,  0.23218520518246595E+003,  0.22974729767387228E+003,  0.22434270552939736E+003,  0.21738764821491546E+003,  0.21026584643346985E+003,  0.20461023502760023E+003,  0.19946752148828986E+003,  0.19505257968636212E+003,  0.19073518286535349E+003,  0.18841583687591014E+003,  0.18806462515941431E+003,  0.18879792677321109E+003,  0.18999822369749231E+003,  0.19226085255536481E+003,  0.19260413418220514E+003,  0.18972449120883414E+003,  0.19104797174976594E+003,  0.19535525682088607E+003,  0.19906590137890106E+003,  0.20323923582030059E+003,  0.20782809651035029E+003,  0.21249863164057479E+003,  0.21693078725658029E+003,  0.22133492789758645E+003,  0.22600610306910096E+003,  0.23075819017782857E+003,  0.23556745536079134E+003,  0.24018267757731826E+003,  0.24472307382594502E+003,  0.24913081538966273E+003,  0.25331075011291634E+003,  0.25720073501317131E+003,  0.26104834105318724E+003,  0.26514892124293834E+003,  0.26761586708570343E+003,  0.26954547512086526E+003,  0.27119243167189433E+003,  0.27329908456006791E+003,  0.27532326908953598E+003,  0.27836308137437925E+003,  0.28116363937249344E+003,  0.28375208753045194E+003,  0.28600310197217686E+003,  0.28785124346207078E+003,  0.28920833148502106E+003,  0.29023206521350198E+003,  0.29112467266593546E+003,  0.29199643644298487E+003,  0.29275298925834494E+003,  0.29345940788283258E+003,  0.29405480897617321E+003,  0.29451529676170168E+003,  0.29458768505772565E+003,  0.29502364158678398E+003,  0.29572951515597663E+003,  0.29638024543271678E+003,  0.29700920812845578E+003,  0.29767336741838551E+003,  0.29825388939585036E+003,  0.29860278995839013E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18472001195671415E+005,  0.19912820575580547E+005,  0.21454028594674601E+005,  0.23126217367895570E+005,  0.24940518517585202E+005,  0.26909009702400515E+005,  0.29044794715738790E+005,  0.31362090602785724E+005,  0.33876323120212270E+005,  0.36604229967163395E+005,  0.39563970883835282E+005,  0.42775247872845750E+005,  0.46210316735528482E+005,  0.49744469035580070E+005,  0.53261877104634288E+005,  0.56692083886690103E+005,  0.60001149186597140E+005,  0.63175048735786884E+005,  0.66171073656698005E+005,  0.68947277020995258E+005,  0.71463438910659941E+005,  0.73682033996322411E+005,  0.75569161477614034E+005,  0.77123387857471651E+005,  0.78437594692039871E+005,  0.79656985250620666E+005,  0.80847418124113727E+005,  0.82006982249399880E+005,  0.83133795980873518E+005,  0.84226015500966125E+005,  0.85281836275816924E+005,  0.86299492726177006E+005,  0.87277262800909113E+005,  0.88213479648972061E+005,  0.89106543049292231E+005,  0.89954915922264190E+005,  0.90762000938300407E+005,  0.91454058183950910E+005,  0.91890226170947557E+005,],]
input.radius_part=[[  0.13519782934072435E-007,  0.13069253879256358E-007,  0.16013189366228184E-007,  0.18333048641768384E-007,  0.20330479491000463E-007,  0.24466396642530169E-007,  0.27608393165687633E-007,  0.29661728961209558E-007,  0.32239096467705368E-007,  0.34181571171289709E-007,  0.35566047698334309E-007,  0.36390316068485100E-007,  0.37106836831169658E-007,  0.38029562345544454E-007,  0.37955908291131520E-007,  0.37279147721546508E-007,  0.38528322900770527E-007,  0.39987461153156028E-007,  0.38900941229073896E-007,  0.34117639526944618E-007,  0.29873283862990465E-007,  0.28051203771979101E-007,  0.27813532626623562E-007,  0.27170548973216452E-007,  0.26545617289375636E-007,  0.23556719824682772E-007,  0.15371597071215864E-007,  0.15270117479593467E-007,  0.17271984057656936E-007,  0.20152445277881454E-007,  0.23150246125685923E-007,  0.26416651616234924E-007,  0.27642853281036603E-007,  0.28678571751044957E-007,  0.30051114427726438E-007,  0.30998418564205640E-007,  0.31955709307362774E-007,  0.32890384128997052E-007,  0.33123414731888596E-007,  0.33476010947260660E-007,  0.33740829783169223E-007,  0.34531645048675784E-007,  0.36523681324304951E-007,  0.38315524256116126E-007,  0.39423456545512070E-007,  0.37627222367184588E-007,  0.42944266022617821E-007,  0.45777781955245808E-007,  0.41863032166422551E-007,  0.39742323034222017E-007,  0.43210865041027247E-007,  0.39641396994413991E-007,  0.37191297695758876E-007,  0.34947500177927161E-007,  0.34353763334197152E-007,  0.32954800840447612E-007,  0.30648275757185697E-007,  0.28146325747820501E-007,  0.26258142999201174E-007,  0.24684966522576171E-007,  0.23936364041144785E-007,  0.23280058432139407E-007,  0.22527000300557237E-007,  0.22853137275432622E-007,  0.25399847179506729E-007,  0.27661474956208318E-007,  0.27733041280302996E-007,  0.27711494290645262E-007,  0.27691282774935816E-007,  0.27369856780301994E-007,  0.27054299304157724E-007,  0.26839650193758067E-007,],]
input.density_part=[[  0.17708797823481582E+004,  0.17717041854492684E+004,  0.17718552981597750E+004,  0.17718842918886667E+004,  0.17718637190029945E+004,  0.17718551302818619E+004,  0.17709544482827880E+004,  0.16985696158006165E+004,  0.15964243164978589E+004,  0.15669107466165624E+004,  0.15505065209567504E+004,  0.15447515590431617E+004,  0.15387644242305778E+004,  0.15345682750330225E+004,  0.15200482836721260E+004,  0.14595132346311407E+004,  0.13330705090738741E+004,  0.12500475037119436E+004,  0.12192408945162556E+004,  0.11945704217307086E+004,  0.11807651955054905E+004,  0.11639165171169545E+004,  0.11482329047670519E+004,  0.11505384518458814E+004,  0.11512052693869398E+004,  0.11562050030107141E+004,  0.12129053716718051E+004,  0.11729010197485941E+004,  0.11531108908257881E+004,  0.11175413308918439E+004,  0.10692541670648216E+004,  0.10432977359551167E+004,  0.10365023218332110E+004,  0.10290953546256380E+004,  0.10238366669970139E+004,  0.10270523986418671E+004,  0.10327572108534080E+004,  0.10417857017287604E+004,  0.10471687182983760E+004,  0.10504863428334991E+004,  0.10530630708647000E+004,  0.10505630200603246E+004,  0.10436749094183426E+004,  0.10413220117507869E+004,  0.10428673158815352E+004,  0.10521722917073491E+004,  0.10330919496421686E+004,  0.10316723627818103E+004,  0.10581440734952566E+004,  0.10950757042625769E+004,  0.10902313253225877E+004,  0.11571777447870479E+004,  0.12249570555217017E+004,  0.12840067652810365E+004,  0.13182092320137374E+004,  0.13485526740524056E+004,  0.13798832451751741E+004,  0.14116237189970695E+004,  0.14444252213759021E+004,  0.14984902236798489E+004,  0.15198122928949672E+004,  0.15328346851670149E+004,  0.15549432708441893E+004,  0.15403382653724664E+004,  0.14109733503031935E+004,  0.13317091495714344E+004,  0.13358804848886784E+004,  0.13396167600210636E+004,  0.13411955619105215E+004,  0.13536366623323868E+004,  0.13662680488711553E+004,  0.13751644181003426E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.51226328014921238E-002,  0.34351342913247966E-002,  0.28776486450109973E-002,  0.22373198076300082E-002,  0.16778935895135803E-002,  0.13601510894198422E-002,  0.10334681132768736E-002,  0.71373466107167076E-003,  0.48517278631918676E-003,  0.33612789651846990E-003,  0.23644591345411351E-003,  0.17099842969792430E-003,  0.12648847920948425E-003,  0.96381603267199566E-004,  0.72346868539515687E-004,  0.52905366353536675E-004,  0.39695900517113290E-004,  0.31515760234662690E-004,  0.24892666915324968E-004,  0.18143311935429905E-004,  0.13577360914113947E-004,  0.11148730204075369E-004,  0.99243792653160135E-005,  0.89646987372186377E-005,  0.81149865826041463E-005,  0.66945754885025593E-005,  0.41911912343384608E-005,  0.36906438200375651E-005,  0.38144576355397220E-005,  0.40456299125456230E-005,  0.41678089229813454E-005,  0.43588000210445256E-005,  0.42452630315952940E-005,  0.41077511085508602E-005,  0.40381803896673887E-005,  0.39393807733776288E-005,  0.38509128691115507E-005,  0.37700497742091666E-005,  0.35915885882198484E-005,  0.34262441969145179E-005,  0.32557861125189960E-005,  0.31309859053746268E-005,  0.31114225456167962E-005,  0.30793613001164157E-005,  0.29950548159089087E-005,  0.26948374653305214E-005,  0.29141701174543856E-005,  0.29807847602695959E-005,  0.26153291593850008E-005,  0.24345012745623133E-005,  0.25822916184715730E-005,  0.23843101398656260E-005,  0.22663679185051072E-005,  0.21463027352712013E-005,  0.21105228093476617E-005,  0.20158308408924427E-005,  0.18627040736473505E-005,  0.17008629680042617E-005,  0.15853861775811015E-005,  0.15131680047949001E-005,  0.14644449829047280E-005,  0.14149752792338703E-005,  0.13677014549550511E-005,  0.13636070434703697E-005,  0.13984022896418487E-005,  0.14468148486616877E-005,  0.14441701558411661E-005,  0.14359341497444632E-005,  0.14261924712021445E-005,  0.14101089517313935E-005,  0.13958296174717698E-005,  0.13867206554266444E-005,],]
