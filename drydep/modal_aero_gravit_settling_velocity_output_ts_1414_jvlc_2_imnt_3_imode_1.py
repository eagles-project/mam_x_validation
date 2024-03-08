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
input.radius_part=[[  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.44915107967524496E-007,  0.40899509518237430E-007,  0.42563225077915481E-007,  0.46941968515756258E-007,  0.49929334037219247E-007,  0.54130428385858686E-007,  0.58746993553315794E-007,  0.64024848382995354E-007,  0.70300211214176739E-007,  0.84309947491547869E-007,  0.10326671840408671E-006,  0.11726710481950916E-006,  0.12503425852860554E-006,  0.12637448462806921E-006,  0.12952484754591479E-006,  0.13058547983809851E-006,  0.12740894548301692E-006,  0.12599740107401036E-006,  0.12600313964246951E-006,  0.12590309720241517E-006,  0.12444466103312591E-006,  0.12444163050663873E-006,  0.11960409250330577E-006,  0.11820386186855567E-006,  0.11846018132245984E-006,  0.11869727698454843E-006,  0.11897923926223475E-006,  0.11937851063803304E-006,  0.11973996388098783E-006,  0.12315800823430032E-006,  0.12642170086285220E-006,  0.12784238086829153E-006,  0.12881597220117997E-006,  0.12996127242467761E-006,  0.13023453974116777E-006,  0.13043907779104342E-006,  0.12925631193725937E-006,  0.13930753969772612E-006,  0.14514896519678505E-006,  0.15524172655114472E-006,  0.16324852908237522E-006,  0.15541711231625251E-006,  0.16806149889499528E-006,  0.19818259384774792E-006,  0.14553227788190586E-006,  0.13853649334130841E-006,  0.13537680273514840E-006,  0.13265668691736630E-006,  0.13060555240573743E-006,  0.12917741196764771E-006,  0.12812504983062569E-006,  0.12741180020240778E-006,  0.12680796425974732E-006,  0.12610125817528466E-006,  0.12540954682889649E-006,  0.12483710549498465E-006,  0.12430312649464229E-006,  0.12381140759004219E-006,  0.12401817599610857E-006,  0.12770154485740754E-006,  0.13327998598466565E-006,  0.13949669599951002E-006,  0.18490381434288755E-006,  0.23219532509279334E-006,  0.23248971943976886E-006,],]
input.density_part=[[  0.16342590748501884E+004,  0.16746474585280471E+004,  0.16886941819652216E+004,  0.16956023717984128E+004,  0.16968651846839418E+004,  0.17029708038313706E+004,  0.17127243738509903E+004,  0.16796897405276236E+004,  0.15810270319209949E+004,  0.15683710983262558E+004,  0.15554927461978361E+004,  0.15386156069530202E+004,  0.15163856307855044E+004,  0.15135655526422170E+004,  0.15478847645085107E+004,  0.15568147329360850E+004,  0.14107944908053200E+004,  0.13319836408013791E+004,  0.13373690128339776E+004,  0.12961182289987910E+004,  0.12533452928661911E+004,  0.12089325860229351E+004,  0.11921661251516771E+004,  0.12004524867785424E+004,  0.12015481442845485E+004,  0.11953451865098821E+004,  0.11768353446437761E+004,  0.11893596168883280E+004,  0.12061684427779269E+004,  0.11877860770626478E+004,  0.11524269898800947E+004,  0.11456047333678728E+004,  0.11425133554894635E+004,  0.11408330946310468E+004,  0.11389414400822782E+004,  0.11372454825387770E+004,  0.11249312123862721E+004,  0.11194930681660185E+004,  0.11190682732103166E+004,  0.11168281319033522E+004,  0.11157303897180184E+004,  0.11164747729372541E+004,  0.11184775538451856E+004,  0.11263656274379746E+004,  0.11042367912945581E+004,  0.10986209295983947E+004,  0.10737929057944827E+004,  0.10670181723015826E+004,  0.10824520607103843E+004,  0.10695640222456570E+004,  0.10436621506283159E+004,  0.11115010692660364E+004,  0.11314272243803514E+004,  0.11422794875855891E+004,  0.11510088538714176E+004,  0.11590391323326162E+004,  0.11650615797861617E+004,  0.11694590352072403E+004,  0.11714528988131508E+004,  0.11718977454209955E+004,  0.11701172862204367E+004,  0.11657874067161990E+004,  0.11599416943368235E+004,  0.11548555005639878E+004,  0.11517042146035030E+004,  0.11448753147057228E+004,  0.11313796573819459E+004,  0.11183463874879581E+004,  0.11029667811937927E+004,  0.10466749503017925E+004,  0.10240974531865018E+004,  0.10241038227677554E+004,],]
input.sig_part=[[  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.24208101370061283E-001,  0.17121094465807233E-001,  0.11836931248104702E-001,  0.81264091300450852E-002,  0.54660649932408208E-002,  0.36746072415255264E-002,  0.24899118830718965E-002,  0.16417090994518524E-002,  0.94153971446805788E-003,  0.64824916793384017E-003,  0.48451232145189585E-003,  0.36179262076335288E-003,  0.28183117612936740E-003,  0.22806949625585486E-003,  0.19396360773676731E-003,  0.16740081778459745E-003,  0.14630752104474786E-003,  0.14005725484201714E-003,  0.13530650922586340E-003,  0.12114120095348258E-003,  0.10431075777011824E-003,  0.93255138733743881E-004,  0.85614334645979124E-004,  0.78252154407848482E-004,  0.72483198879883079E-004,  0.67733832396634988E-004,  0.62550445098791933E-004,  0.58340835706173033E-004,  0.55700544417123659E-004,  0.49256339366750871E-004,  0.44451519136523468E-004,  0.41890131108880670E-004,  0.39629488988617884E-004,  0.37653192053532007E-004,  0.35920971202803606E-004,  0.34296016503839038E-004,  0.33578622726814162E-004,  0.33033889415344712E-004,  0.32013414484918575E-004,  0.30850147792267348E-004,  0.29842920898108621E-004,  0.28661571980836059E-004,  0.27557730333997374E-004,  0.26240870041080830E-004,  0.27663646872520927E-004,  0.28249039514291033E-004,  0.29731429041908128E-004,  0.31164939981302337E-004,  0.28438050414741017E-004,  0.31281155462023477E-004,  0.39671169531569759E-004,  0.24583224150843237E-004,  0.22655123025173547E-004,  0.21682274479313281E-004,  0.20852155906334602E-004,  0.20242421946784011E-004,  0.19807400404252213E-004,  0.19474429081376556E-004,  0.19203985048996458E-004,  0.18944626707311382E-004,  0.18633399359884412E-004,  0.18294943951579253E-004,  0.17972651322687356E-004,  0.17682128572772174E-004,  0.17442043305934370E-004,  0.17318966271911015E-004,  0.17907376245188755E-004,  0.18958887323159854E-004,  0.20151188111755841E-004,  0.31197699753768499E-004,  0.45831810445186088E-004,  0.45898360493155170E-004,],]