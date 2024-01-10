# Data at [lat=  -4.98879105856447      , lon=   28.0026147968828      , k=          52 , time step=        1399 ] 
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
input.tair=[[  0.25106150734556880E+003,  0.25358590510502427E+003,  0.26088053377168751E+003,  0.26412591401951693E+003,  0.26831783648551072E+003,  0.26835232090573948E+003,  0.26540598605688638E+003,  0.26122190002652911E+003,  0.25415494810369276E+003,  0.24569465978019412E+003,  0.23755139621200831E+003,  0.23400649595550598E+003,  0.23162528504630330E+003,  0.22871336865182977E+003,  0.22266886288884729E+003,  0.21554317174431526E+003,  0.20962424792050180E+003,  0.20564997566190289E+003,  0.20139758995287994E+003,  0.19765142094376955E+003,  0.19370106176836683E+003,  0.19095115516058536E+003,  0.18977841092785249E+003,  0.18986605616574491E+003,  0.19029492680366619E+003,  0.19179174013810970E+003,  0.19033270867461476E+003,  0.18852605745373182E+003,  0.19133605694726464E+003,  0.19531796806056434E+003,  0.19913473679182295E+003,  0.20293390432945534E+003,  0.20728510997707045E+003,  0.21190952476290721E+003,  0.21651996722397774E+003,  0.22106342037868947E+003,  0.22564734231229332E+003,  0.23015000800985612E+003,  0.23468705368684505E+003,  0.23944999726186546E+003,  0.24412035207508578E+003,  0.24858553004218786E+003,  0.25345035043835335E+003,  0.25761175013406626E+003,  0.26094953734937769E+003,  0.26401029108225873E+003,  0.26678474522190453E+003,  0.26880889498660815E+003,  0.27021476055419873E+003,  0.27291232080672040E+003,  0.27520231164056753E+003,  0.27770227017222891E+003,  0.28106096539122592E+003,  0.28394827328696306E+003,  0.28631104361705013E+003,  0.28782587223269815E+003,  0.28899155644261214E+003,  0.28995345645037958E+003,  0.29078669200131134E+003,  0.29154074271743946E+003,  0.29222182287361710E+003,  0.29280943507700340E+003,  0.29334081808190547E+003,  0.29384527051102560E+003,  0.29419541315209966E+003,  0.29438193499561231E+003,  0.29430944346660215E+003,  0.29335755817498426E+003,  0.29279030584250899E+003,  0.29329781874223119E+003,  0.29389879217947407E+003,  0.29433696772563007E+003,],]
input.pmid=[[  0.12382541305561677E+002,  0.18282923550684863E+002,  0.26994886212093746E+002,  0.39858170362288227E+002,  0.58850914656475304E+002,  0.86893857004050020E+002,  0.12829949082549251E+003,  0.18943524794063876E+003,  0.27970269352932593E+003,  0.41298331550248361E+003,  0.59684493671180769E+003,  0.83774043789417703E+003,  0.11473787230534558E+004,  0.15333938222216857E+004,  0.19996337978167076E+004,  0.25444696509961595E+004,  0.31593251291285251E+004,  0.38366283094427008E+004,  0.45671197939426802E+004,  0.53309561434392535E+004,  0.61015181670369457E+004,  0.68476390229712551E+004,  0.75355335897260984E+004,  0.81946275124734711E+004,  0.88910543149560908E+004,  0.96466673444937041E+004,  0.10466496728675462E+005,  0.11356000142146328E+005,  0.12321099142746600E+005,  0.13368217993210610E+005,  0.14504326553270042E+005,  0.15736987784007928E+005,  0.17074407952158203E+005,  0.18474845077873411E+005,  0.19922766816387884E+005,  0.21472853699110929E+005,  0.23154675916067310E+005,  0.24979429215801516E+005,  0.26959260835985620E+005,  0.29107350059404700E+005,  0.31437995832159912E+005,  0.33966712784043179E+005,  0.36710335042959960E+005,  0.39687126961339134E+005,  0.42916904042071830E+005,  0.46371762258147231E+005,  0.49926274734310718E+005,  0.53463946516050310E+005,  0.56913914643301730E+005,  0.60242043395012413E+005,  0.63434227705970668E+005,  0.66447512656299135E+005,  0.69239709665680508E+005,  0.71770367110059742E+005,  0.74001743474469346E+005,  0.75899742657169001E+005,  0.77462922902247607E+005,  0.78784700852906448E+005,  0.80011116289561687E+005,  0.81208407217192987E+005,  0.82374651564666186E+005,  0.83507956844497996E+005,  0.84606468619853316E+005,  0.85668371957287745E+005,  0.86691891102043926E+005,  0.87675294086801310E+005,  0.88616904461853061E+005,  0.89515112782815166E+005,  0.90368373110889646E+005,  0.91179820097007745E+005,  0.91875232486523804E+005,  0.92313409162378841E+005,],]
input.radius_part=[[  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.15003125160918092E-005,  0.19319691870791303E-005,  0.22385103510206568E-005,  0.25525685413420608E-005,  0.28448842430076654E-005,  0.30733575604328735E-005,  0.32180304213351841E-005,  0.33287531164126566E-005,  0.33581389134597751E-005,  0.26120765925471572E-005,  0.14754717171792994E-005,  0.10031522562338434E-005,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.83953472836494377E-006,  0.86742263188006414E-006,  0.90073255988495732E-006,  0.90611041052707521E-006,  0.91761213593716772E-006,  0.94139873269431582E-006,  0.95659847127378364E-006,  0.96423405948533167E-006,  0.96569512741438009E-006,  0.96088786003839239E-006,  0.95752134606479641E-006,  0.94115303232304393E-006,  0.92953968563473623E-006,  0.92154252328135806E-006,  0.91755205747595158E-006,  0.92205925490820993E-006,  0.93089760104563923E-006,  0.10996733506171920E-005,  0.96512049610901028E-006,  0.95616236427520514E-006,  0.11868776836562081E-005,  0.15995531049610267E-005,  0.18243561070835822E-005,  0.27311331244183304E-005,  0.28269173943806742E-005,  0.17318621288726751E-005,  0.13261910862477757E-005,  0.11701554766516967E-005,  0.11040290046748486E-005,  0.10885213664393922E-005,  0.10842263186254916E-005,  0.10865119793836107E-005,  0.10914022671771333E-005,  0.10976735213166822E-005,  0.11053906888469141E-005,  0.11181437464489082E-005,  0.11321396209082578E-005,  0.11461383628240768E-005,  0.11552078891092572E-005,  0.11713168025285482E-005,  0.12399093336863538E-005,  0.15591938702365323E-005,  0.28249630321868904E-005,  0.27409149376583133E-005,  0.22826888573358650E-005,  0.21011935827460710E-005,],]
input.density_part=[[  0.10000000000000000E+001,  0.17699903515711060E+004,  0.17699999673131395E+004,  0.17699999997279788E+004,  0.17699999999991323E+004,  0.17699999999999980E+004,  0.17700000000000002E+004,  0.17700000000000000E+004,  0.17700000000000000E+004,  0.17700000000000000E+004,  0.17700000000000002E+004,  0.17700000000001448E+004,  0.17700000000288474E+004,  0.17700000028829281E+004,  0.17700001845130951E+004,  0.17700191703681169E+004,  0.17711132230962751E+004,  0.17850220422562586E+004,  0.18446650839300014E+004,  0.18701517204524873E+004,  0.18779658013338833E+004,  0.18695084577874063E+004,  0.17618794790115135E+004,  0.18145251808494870E+004,  0.19161890447485839E+004,  0.19141064098213167E+004,  0.18328851557126079E+004,  0.17660756655940284E+004,  0.17779963021240658E+004,  0.17972133048481128E+004,  0.18283516120835061E+004,  0.18486990905210366E+004,  0.18532834536122634E+004,  0.18562604648006811E+004,  0.18607610552504709E+004,  0.18698551372412153E+004,  0.18737360337108537E+004,  0.18874173943060280E+004,  0.19062739679065828E+004,  0.19255727404704603E+004,  0.19336650280458639E+004,  0.19184343233434060E+004,  0.18983338418076385E+004,  0.15480327070240216E+004,  0.18134802398132917E+004,  0.18249176150499452E+004,  0.14285470079738029E+004,  0.11651695007791518E+004,  0.11131912921408407E+004,  0.10433363666518565E+004,  0.10452225144266088E+004,  0.12119891861999595E+004,  0.14715394886098618E+004,  0.16822278694855770E+004,  0.18015401936036676E+004,  0.18071854912862507E+004,  0.17984180499717258E+004,  0.17836618096770803E+004,  0.17692300901209230E+004,  0.17536397987203052E+004,  0.17339821030374894E+004,  0.17005548355193710E+004,  0.16678183330602935E+004,  0.16397113981836587E+004,  0.16214341022835251E+004,  0.15884998539969888E+004,  0.14783600026830588E+004,  0.12182581889450425E+004,  0.10338721198107739E+004,  0.10362981847023837E+004,  0.10623178980485250E+004,  0.10796516939932537E+004,],]
input.sig_part=[[  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,  0.18000000000000000E+001,],]
# Output data is stored here.
output = Object()
output.vlc_grv=[[  0.27630922641798763E-003,  0.33305811246408190E+000,  0.22894825296714910E+000,  0.15618263550306516E+000,  0.10677190578291076E+000,  0.72483768389384889E-001,  0.88299223089424186E-001,  0.77813951916692797E-001,  0.62063407304893223E-001,  0.49722876928020965E-001,  0.41108554516318202E-001,  0.35231696211491519E-001,  0.30834182065988692E-001,  0.28002999541852092E-001,  0.25673090869525409E-001,  0.15778308125098207E-001,  0.58578080507196342E-002,  0.30016423371828633E-002,  0.21852426915514303E-002,  0.20708694045960649E-002,  0.19796377011666077E-002,  0.18991527714854312E-002,  0.17380126515235911E-002,  0.17436895326737921E-002,  0.17963798353758335E-002,  0.17479847135742823E-002,  0.16460405913357515E-002,  0.16576273885604731E-002,  0.17392246780610569E-002,  0.17266837565668911E-002,  0.17487763743083893E-002,  0.18045511227007419E-002,  0.18130702301831830E-002,  0.17941882348814255E-002,  0.17582877056538063E-002,  0.17082131701227758E-002,  0.16601481020692515E-002,  0.15819892479648422E-002,  0.15257004129468079E-002,  0.14817785471610701E-002,  0.14433721250365701E-002,  0.14149852050885725E-002,  0.13950500188818734E-002,  0.15329400982472868E-002,  0.13773535202893940E-002,  0.13411228931665246E-002,  0.15695220323093109E-002,  0.22631625900304208E-002,  0.27772992079463494E-002,  0.57012289128953036E-002,  0.60664209151723011E-002,  0.26585492563051712E-002,  0.18944159272404983E-002,  0.16811034188966316E-002,  0.15953994348518910E-002,  0.15488703291184928E-002,  0.15233782404003085E-002,  0.15120511900749063E-002,  0.15085989345309245E-002,  0.15080687535360250E-002,  0.15079870069847413E-002,  0.15091046670220566E-002,  0.15134180384381937E-002,  0.15211962379977515E-002,  0.15253756620492880E-002,  0.15338454105640780E-002,  0.15950302613818180E-002,  0.20642978749547650E-002,  0.56697093719614523E-002,  0.53449785929540862E-002,  0.38085385783083519E-002,  0.32821023998034328E-002,],]
