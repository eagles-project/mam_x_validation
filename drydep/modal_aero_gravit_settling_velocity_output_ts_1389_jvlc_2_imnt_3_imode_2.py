# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1389 ] 
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
input.tair=[[  0.25255095988639337E+003,  0.26107404234460671E+003,  0.26348899752764191E+003,  0.26106884668874710E+003,  0.26307855343404026E+003,  0.26540770958074438E+003,  0.26391778285816054E+003,  0.25882422327161731E+003,  0.24870197818809211E+003,  0.24018422563156011E+003,  0.23565178302108231E+003,  0.23551749575176052E+003,  0.23428151510000140E+003,  0.23131651710640051E+003,  0.22422576665846250E+003,  0.21608550184521152E+003,  0.21021292266057139E+003,  0.20629645031375955E+003,  0.20172601341021070E+003,  0.19722344949792395E+003,  0.19231887614256348E+003,  0.18924055680923709E+003,  0.18822281827066104E+003,  0.18828970532424825E+003,  0.18855128078255058E+003,  0.18878257596502124E+003,  0.18667113395685715E+003,  0.18799907344425731E+003,  0.19134279695252144E+003,  0.19513748524335679E+003,  0.19934710222395117E+003,  0.20353795447376979E+003,  0.20790319830536464E+003,  0.21223713737453176E+003,  0.21667152718647489E+003,  0.22121732000831378E+003,  0.22588248922357610E+003,  0.23048719793169269E+003,  0.23515835867395833E+003,  0.23977875002299015E+003,  0.24422700284787990E+003,  0.24822946396596251E+003,  0.25246309326692403E+003,  0.25701704885815030E+003,  0.26179574992192454E+003,  0.26551925040793628E+003,  0.26790748020975809E+003,  0.27032406351803269E+003,  0.27139982300974339E+003,  0.27319351071038614E+003,  0.27526240263210735E+003,  0.27899983325741732E+003,  0.28167977742252850E+003,  0.28401091565803796E+003,  0.28602366791747556E+003,  0.28760566081331478E+003,  0.28882984279587345E+003,  0.28979920941997568E+003,  0.29064136959715904E+003,  0.29141697872997099E+003,  0.29219013720989432E+003,  0.29289607515061869E+003,  0.29348934445837426E+003,  0.29398454640435665E+003,  0.29443691780866584E+003,  0.29486179442743378E+003,  0.29529757451005912E+003,  0.29573751046014809E+003,  0.29564280560384321E+003,  0.29419658512940970E+003,  0.29338902498761416E+003,  0.29326896336311432E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18474053418759373E+005,  0.19919998054664902E+005,  0.21467613304312126E+005,  0.23146753833705159E+005,  0.24968597540405488E+005,  0.26945272293188202E+005,  0.29089936360655087E+005,  0.31416865889929850E+005,  0.33941550770955429E+005,  0.36680798288504666E+005,  0.39652843673818730E+005,  0.42877470834413325E+005,  0.46326820235122439E+005,  0.49875664994468709E+005,  0.53407695912173796E+005,  0.56852163020775850E+005,  0.60174985028292002E+005,  0.63362079361088741E+005,  0.66370559590747958E+005,  0.69158304406262570E+005,  0.71684926684208127E+005,  0.73912745089781689E+005,  0.75807717887809456E+005,  0.77368405621417973E+005,  0.78688075980189780E+005,  0.79912535882699216E+005,  0.81107917715411153E+005,  0.82272302471522067E+005,  0.83403800681631241E+005,  0.84500560865017280E+005,  0.85560770983195776E+005,  0.86582658113992933E+005,  0.87564493050482721E+005,  0.88504602014964606E+005,  0.89401378130572251E+005,  0.90253277924664828E+005,  0.91063510657475214E+005,  0.91757989066597074E+005,  0.92195606578348583E+005,],]
input.radius_part=[[  0.13648446406183960E-007,  0.13769463112738821E-007,  0.17279628192900299E-007,  0.19444467240468725E-007,  0.20007922725229961E-007,  0.24231655683788209E-007,  0.27338063912470064E-007,  0.29513364214394903E-007,  0.32440058582604246E-007,  0.34330113278552142E-007,  0.35626661355664323E-007,  0.36302858873394848E-007,  0.37003240192438409E-007,  0.37970356790094899E-007,  0.37940344858356121E-007,  0.37268917031019701E-007,  0.38183675604863420E-007,  0.40041123608853328E-007,  0.39356742845961196E-007,  0.33473659407012347E-007,  0.29536223939632547E-007,  0.27824091830047267E-007,  0.27647606952845561E-007,  0.27316681284718263E-007,  0.25700924826488165E-007,  0.18797402066938915E-007,  0.14215053469397925E-007,  0.15047954902481827E-007,  0.16927748842594002E-007,  0.18894295768562513E-007,  0.19952130122487979E-007,  0.21252522102962709E-007,  0.22406355022417117E-007,  0.23910382073956329E-007,  0.25229739669964175E-007,  0.27546640974595248E-007,  0.30056422070608723E-007,  0.32047344445209582E-007,  0.32672713160233562E-007,  0.33377133070367051E-007,  0.33373271583674324E-007,  0.32717446197179666E-007,  0.32040520944475910E-007,  0.32044319558895981E-007,  0.35541144896926020E-007,  0.36308852858507051E-007,  0.39782287939753998E-007,  0.42518480050825674E-007,  0.43849776326809664E-007,  0.43896085191075196E-007,  0.45430839448071876E-007,  0.36831718354205261E-007,  0.33079427830954444E-007,  0.30489999230027493E-007,  0.28484082171872069E-007,  0.25776904507976771E-007,  0.23291009313168280E-007,  0.21733970476670109E-007,  0.20852505478804398E-007,  0.20418282822532352E-007,  0.20321758249567019E-007,  0.20402748673209501E-007,  0.20477307840250993E-007,  0.20938927685685419E-007,  0.21356957203429971E-007,  0.22278862614148911E-007,  0.23854149391267608E-007,  0.25689362665667194E-007,  0.27442448858065054E-007,  0.34309042639695322E-007,  0.46059270129767773E-007,  0.48788432405517029E-007,],]
input.density_part=[[  0.17711709168991424E+004,  0.17717372326065406E+004,  0.17718350211829286E+004,  0.17718811672970489E+004,  0.17718695130691301E+004,  0.17718336566051053E+004,  0.17714262151556786E+004,  0.17043781033462312E+004,  0.15932405926229865E+004,  0.15644173367612202E+004,  0.15500154544536792E+004,  0.15454044769034404E+004,  0.15393724223105507E+004,  0.15344882232405512E+004,  0.15188117595582644E+004,  0.14592529832132193E+004,  0.13543204919107693E+004,  0.12640668591602741E+004,  0.12212446338999048E+004,  0.11924432959939918E+004,  0.11836486431740630E+004,  0.11705951634737046E+004,  0.11506150803582400E+004,  0.11494562879490229E+004,  0.11508841209640211E+004,  0.11709092457647700E+004,  0.12070489563228587E+004,  0.11684967200655858E+004,  0.11571006797031055E+004,  0.11470839772162767E+004,  0.11269173722548533E+004,  0.10962013856618607E+004,  0.10797525808861812E+004,  0.10618833828393326E+004,  0.10426231626067001E+004,  0.10274437373917463E+004,  0.10181394122356937E+004,  0.10179635876951701E+004,  0.10195630457717383E+004,  0.10196403279833314E+004,  0.10247904793279763E+004,  0.10445754380364085E+004,  0.10588301365253717E+004,  0.10616532741696844E+004,  0.10471233033634387E+004,  0.10552217795238021E+004,  0.10440279563552967E+004,  0.10393764738889804E+004,  0.10506853250869663E+004,  0.10599031113205081E+004,  0.10698088907286874E+004,  0.11649598528651402E+004,  0.12307528994779100E+004,  0.12777912002347673E+004,  0.13065380451085289E+004,  0.13140157611236405E+004,  0.13453860635596802E+004,  0.13984925956366108E+004,  0.14413564893376285E+004,  0.14728640945790476E+004,  0.14947833902440761E+004,  0.15012287412716255E+004,  0.15166307040338631E+004,  0.15253648574263661E+004,  0.15035485677960637E+004,  0.14398138552620492E+004,  0.13727442715271986E+004,  0.13426981725535970E+004,  0.12997047289319462E+004,  0.11603227806881953E+004,  0.10689729463423919E+004,  0.10583892283206642E+004,],]
input.sig_part=[[  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,  0.16000000000000001E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.51539071615823743E-002,  0.35816520826397118E-002,  0.30584106832844712E-002,  0.23202804393973762E-002,  0.16232557463228725E-002,  0.13374254510843848E-002,  0.10189345313130031E-002,  0.70998857155381073E-003,  0.48447960611851953E-003,  0.33524221978537759E-003,  0.23641940276340198E-003,  0.17122297039434673E-003,  0.12674581103857389E-003,  0.96548675607475791E-004,  0.72239704732287335E-004,  0.52727037337675722E-004,  0.39958179683749222E-004,  0.32037514654894919E-004,  0.25366026762275583E-004,  0.17853920847618626E-004,  0.13505463516506422E-004,  0.11142225529053838E-004,  0.98878238963332260E-005,  0.89947488689765081E-005,  0.78193632714927643E-005,  0.53322503397722731E-005,  0.37945862315006259E-005,  0.36066173891911531E-005,  0.37519644356670940E-005,  0.38830130360954515E-005,  0.37662753007063704E-005,  0.36505103359375079E-005,  0.35472793147319602E-005,  0.34957755730098852E-005,  0.34122910301969739E-005,  0.34706369355311402E-005,  0.35501478274176254E-005,  0.35761396548012699E-005,  0.34385361639621445E-005,  0.33081561651265497E-005,  0.31231097723397234E-005,  0.29233271622125960E-005,  0.27181949074564613E-005,  0.25600289286995086E-005,  0.26671540627301831E-005,  0.25892758245962438E-005,  0.26852416696614175E-005,  0.27428218291395327E-005,  0.27414085358613688E-005,  0.26530659445712087E-005,  0.26900277095846129E-005,  0.21914308291635847E-005,  0.19740732039321205E-005,  0.18110549013060062E-005,  0.16700312534576765E-005,  0.14661970937022805E-005,  0.13145829005861994E-005,  0.12458959382070406E-005,  0.12100499204179914E-005,  0.11929851177980276E-005,  0.11904886490665108E-005,  0.11878193195225562E-005,  0.11922252653348110E-005,  0.12174136733564956E-005,  0.12155705052836727E-005,  0.12108041711402421E-005,  0.12388700308639813E-005,  0.13112909200979614E-005,  0.13620405574958206E-005,  0.15832727369544718E-005,  0.21155719646409524E-005,  0.22542811614604004E-005,],]
