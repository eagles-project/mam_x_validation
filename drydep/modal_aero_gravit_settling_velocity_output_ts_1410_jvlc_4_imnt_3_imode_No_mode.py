# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1410 ] 
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
input.tair=[[  0.25425190590769432E+003,  0.26867365766471181E+003,  0.27499369167046177E+003,  0.27659787941855774E+003,  0.27105700007007169E+003,  0.26565715589566423E+003,  0.26268081440832935E+003,  0.25773721748988623E+003,  0.24994313884838843E+003,  0.24203196760972332E+003,  0.23621048172803458E+003,  0.23410452519960867E+003,  0.23243743191876754E+003,  0.23004253512817851E+003,  0.22502005024863223E+003,  0.21860515041854060E+003,  0.21164772843483908E+003,  0.20528817043238820E+003,  0.19948780068996274E+003,  0.19465216695449183E+003,  0.18986194473191424E+003,  0.18729749666189190E+003,  0.18703181637614802E+003,  0.18793384559406718E+003,  0.18945194847271159E+003,  0.19179849733389233E+003,  0.19245723263967091E+003,  0.18938678652794172E+003,  0.19088927680573960E+003,  0.19525170540777094E+003,  0.19885478419787083E+003,  0.20302306431689107E+003,  0.20756882509012462E+003,  0.21223398231548208E+003,  0.21685607523984004E+003,  0.22150917504043230E+003,  0.22624788151981227E+003,  0.23088512478386670E+003,  0.23548373907354284E+003,  0.23985832637499681E+003,  0.24413216500862353E+003,  0.24830421141515248E+003,  0.25268168308750148E+003,  0.25687720355592757E+003,  0.26107601949944655E+003,  0.26525661346270061E+003,  0.26763803123463572E+003,  0.26969498264609712E+003,  0.27166610769235700E+003,  0.27364088052166045E+003,  0.27537299883942927E+003,  0.27885096087063289E+003,  0.28157349249790116E+003,  0.28398351917682692E+003,  0.28611848648316055E+003,  0.28791906987207489E+003,  0.28932921413002930E+003,  0.29041733956494483E+003,  0.29131243869083733E+003,  0.29215777048100364E+003,  0.29293508195384510E+003,  0.29364252265878770E+003,  0.29422358191407835E+003,  0.29473703804672158E+003,  0.29502363267774967E+003,  0.29520206861211324E+003,  0.29556264062110802E+003,  0.29607244280795169E+003,  0.29657063692818002E+003,  0.29599099309050143E+003,  0.29488797385232471E+003,  0.29434353631871016E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18473503838286440E+005,  0.19918075942798609E+005,  0.21463975351308352E+005,  0.23141254216895351E+005,  0.24961078044727059E+005,  0.26935561257428097E+005,  0.29077847535269750E+005,  0.31402197198016987E+005,  0.33924082960874701E+005,  0.36660293473749705E+005,  0.39629043751560472E+005,  0.42850095767885425E+005,  0.46295620874399465E+005,  0.49840531028012527E+005,  0.53368645981549605E+005,  0.56809294208543004E+005,  0.60128432202406751E+005,  0.63311993003465381E+005,  0.66317137730998889E+005,  0.69101791773265897E+005,  0.71625612784052821E+005,  0.73850961206441585E+005,  0.75743833047264721E+005,  0.77302790445671839E+005,  0.78620997685627124E+005,  0.79844100029862268E+005,  0.81038156543039499E+005,  0.82201250345655120E+005,  0.83331494063502178E+005,  0.84427038268033444E+005,  0.85486072930484908E+005,  0.86506827095100627E+005,  0.87487573471257812E+005,  0.88426640136198883E+005,  0.89322421995462981E+005,  0.90173377288449003E+005,  0.90982767070176953E+005,  0.91676597097466714E+005,  0.92113826429928667E+005,],]
input.radius_part=[[  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,  0.50000000000000004E-005,],]
input.density_part=[[  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,  0.10000000000000000E+004,],]
input.sig_part=[[  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,  0.14600000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.81880599935278220E+000,  0.57108004369665732E+000,  0.39241096008547355E+000,  0.26771702492588573E+000,  0.18078784098535222E+000,  0.12256019874074789E+000,  0.83902955095327678E-001,  0.57755644725466279E-001,  0.40155624276153240E-001,  0.28568485814995000E-001,  0.21400719957770157E-001,  0.16997560085331338E-001,  0.14186185770711708E-001,  0.12384085570926065E-001,  0.11267365931677605E-001,  0.10601880025535219E-001,  0.10228304780540683E-001,  0.10021163730801882E-001,  0.99204304468048371E-002,  0.98758588238593188E-002,  0.98955989550431611E-002,  0.98780759843696761E-002,  0.98011511393843401E-002,  0.96948359525361426E-002,  0.95715598093676253E-002,  0.94217755975442158E-002,  0.93424382219713265E-002,  0.94128347731545214E-002,  0.93077097440233385E-002,  0.90978836298527179E-002,  0.89258448637273280E-002,  0.87417953452854705E-002,  0.85539016790006812E-002,  0.83724552674299488E-002,  0.82022695481330406E-002,  0.80392583143095598E-002,  0.78811658706912594E-002,  0.77328131066557613E-002,  0.75918601367898960E-002,  0.74623645530652550E-002,  0.73404781993567257E-002,  0.72256970797423296E-002,  0.71107589561156016E-002,  0.70041523207083614E-002,  0.69014438387437335E-002,  0.68030486942180545E-002,  0.67438531680226906E-002,  0.66933443320257848E-002,  0.66465421838243742E-002,  0.66014720446872354E-002,  0.65624824765434841E-002,  0.64930565349984306E-002,  0.64394218578954394E-002,  0.63929413840451473E-002,  0.63526074408385832E-002,  0.63191461612692309E-002,  0.62931950848869496E-002,  0.62732327629612308E-002,  0.62567775200299729E-002,  0.62413148064883245E-002,  0.62271255868511319E-002,  0.62142190446473284E-002,  0.62034923925204672E-002,  0.61939683598590083E-002,  0.61882016045669772E-002,  0.61842552822503416E-002,  0.61774491924167750E-002,  0.61683299425957672E-002,  0.61594876486798095E-002,  0.61679479419956829E-002,  0.61850175273146721E-002,  0.61934061818192821E-002,],]
