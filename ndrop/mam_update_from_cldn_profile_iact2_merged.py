# This file was automatically generated using the following command:
# ./merge_ensembles.py update_from_cldn_profile_output_ts_1407_iact2.py update_from_cldn_profile_output_ts_1408_iact2.py update_from_cldn_profile_output_ts_1409_iact2.py update_from_cldn_profile_output_ts_1410_iact2.py update_from_cldn_profile_output_ts_1411_iact2.py update_from_cldn_profile_output_ts_1412_iact2.py update_from_cldn_profile_output_ts_1413_iact2.py update_from_cldn_profile_output_ts_1414_iact2.py

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass

# Settings are stored here.
settings = Object()

# Input is stored here.
input = Object()
input.cldn_col_in_kk = [[0.01039108176], [0.01223419135], [0.1100616471], [0.8013471903], [0.8630285664], [0.9540708903], [0.9783240361], [0.9952246508]]
input.cldn_col_in_kp1 = [[0.007718600708], [0.01716052889], [0.2005190482], [0.795052646], [0.9108239355], [0.9921712816], [0.9961193049], [0.993893376]]
input.cs_col_in_kk = [[1.019785295], [1.021001531], [1.022282793], [1.022631545], [1.022183277], [1.021711436], [1.022039241], [1.022116147]]
input.cs_col_in_kp1 = [[1.043123949], [1.04519056], [1.046899745], [1.047031646], [1.046720427], [1.046317376], [1.04620916], [1.046256426]]
input.csbot_cscen = [[1.012601494], [1.013001959], [1.013195115], [1.013085603], [1.01315724], [1.013196023], [1.012980336], [1.012965073]]
input.dt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
input.dtinv = [[0.001666666667], [0.001666666667], [0.001666666667], [0.001666666667], [0.001666666667], [0.001666666667], [0.001666666667], [0.001666666667]]
input.dz = [[248.1310921], [248.0032392], [247.7328726], [247.5294513], [247.5363705], [247.5353173], [247.4433789], [247.442943]]
input.ekd = [[11.07826123], [13.01678513], [19.68795132], [23.93825076], [23.93334729], [21.86194472], [26.02797166], [15.53073251]]
input.factnum_col = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.785150017, 0.02922287322, 0.9999999255, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]
input.mact = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]
input.nact = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]
input.nsource_col = [[-18699.78447], [0.0], [-10582.57307], [36707.44753], [-14618.21691], [-4485.838512], [-1808.308093], [-20.26852044]]
input.nspec_amode = [[7, 4, 7, 3], [7, 4, 7, 3], [7, 4, 7, 3], [7, 4, 7, 3], [7, 4, 7, 3], [7, 4, 7, 3], [7, 4, 7, 3], [7, 4, 7, 3]]
input.ntot_amode = [[4], [4], [4], [4], [4], [4], [4], [4]]
input.pver = [[72], [72], [72], [72], [72], [72], [72], [72]]
input.qcld = [[5085392.165], [888594.0101], [10052044.03], [64632541.14], [61701502.59], [64015087.47], [65187628.94], [71883802.87]]
input.raercol_cw_nsav = [[1134680.896, 1.520647155e-11, 7.197496425e-13, 4.356489469e-12, 1.990914694e-13, 2.152389254e-14, 1.574103036e-12, 1.503592461e-13, 300472.8886, 6.154576005e-13, 6.733091102e-14, 2.02631516e-16, 2.178077467e-17, 1202.415656, 5.328399796e-14, 1.570151623e-11, 3.516486909e-13, 4.635977147e-15, 1.976336973e-14, 1.366849015e-13, 3.622121304e-15, 0.0, 0.0, 0.0, 0.0], [53707.68193, 3.983450695e-13, 1.853625957e-14, 1.086869894e-13, 5.046331623e-15, 5.287365464e-16, 3.783278666e-14, 3.617263964e-15, 13912.76986, 1.65469807e-14, 1.726114774e-15, 5.005522886e-18, 5.355292629e-19, 53.61412692, 1.316283147e-15, 3.864054548e-13, 9.835278449e-15, 1.263283064e-16, 5.370576649e-16, 3.626712818e-15, 9.512701468e-17, 0.0, 0.0, 0.0, 0.0], [7050680.841, 4.641123024e-11, 2.162485941e-12, 1.268519143e-11, 5.868507421e-13, 6.07614882e-14, 4.344087087e-12, 4.151001826e-13, 3534952.75, 3.190879755e-12, 3.208813989e-13, 8.618120045e-16, 9.189200822e-17, 6156.207967, 1.485264338e-13, 4.446237688e-11, 1.130579368e-12, 1.460595658e-14, 6.264094137e-14, 4.224832411e-13, 1.098493541e-14, 0.0, 0.0, 0.0, 0.0], [50098060.92, 3.421453785e-10, 1.444036085e-11, 7.559169239e-11, 3.800198109e-12, 3.351676143e-13, 2.417620352e-11, 2.296031677e-12, 30668823.16, 3.271839388e-11, 2.340012444e-12, 5.652488077e-15, 5.984708015e-16, 33628.46871, 8.295783186e-13, 2.554977122e-10, 9.049222767e-12, 1.108373697e-13, 4.688964771e-13, 2.916362322e-12, 7.556264068e-14, 0.0, 0.0, 0.0, 0.0], [54678157.52, 4.067349819e-10, 1.597805644e-11, 8.070079038e-11, 4.181117668e-12, 3.53067914e-13, 2.557489289e-11, 2.416879283e-12, 31637028.76, 4.946912864e-11, 2.220314587e-12, 5.438894652e-15, 5.759816008e-16, 35571.75328, 8.753115414e-13, 2.716965384e-10, 1.030799198e-11, 1.250891631e-13, 5.266464341e-13, 3.239761088e-12, 8.391870738e-14, 0.0, 0.0, 0.0, 0.0], [62445526.58, 4.986480902e-10, 1.855044528e-11, 9.071305738e-11, 4.813188229e-12, 3.933174871e-13, 2.878440417e-11, 2.70734599e-12, 33032772.82, 6.660209781e-11, 2.238536031e-12, 5.61779278e-15, 5.959693636e-16, 39931.04838, 9.769935101e-13, 3.068490669e-10, 1.23419123e-11, 1.488938305e-13, 6.253710329e-13, 3.785394733e-12, 9.815446838e-14, 0.0, 0.0, 0.0, 0.0], [65357442.52, 5.333217189e-10, 1.95895211e-11, 9.333334984e-11, 5.059040858e-12, 3.991353827e-13, 2.926372992e-11, 2.741809515e-12, 30873220.4, 6.911668032e-11, 2.114100722e-12, 5.300528657e-15, 5.639021004e-16, 40722.93133, 9.889569598e-13, 3.123432042e-10, 1.328356922e-11, 1.592776747e-13, 6.65485822e-13, 4.002059437e-12, 1.03492015e-13, 0.0, 0.0, 0.0, 0.0], [68421521.86, 5.656870088e-10, 2.066460915e-11, 9.606721672e-11, 5.323176057e-12, 4.042313332e-13, 2.96902809e-11, 2.774437623e-12, 28577708.43, 6.864108254e-11, 1.998478064e-12, 4.99265112e-15, 5.318320014e-16, 41587.85612, 9.901053524e-13, 3.168880323e-10, 1.428672548e-11, 1.706578945e-13, 7.097997832e-13, 4.237580248e-12, 1.094283671e-13, 0.0, 0.0, 0.0, 0.0]]
input.raercol_nsav_kk = [[96544090.28, 4.950663634e-10, 2.337809451e-11, 1.437013909e-10, 6.510821703e-12, 7.071779738e-13, 5.305065654e-11, 5.067547101e-12, 1710098188.0, 1.053993054e-10, 1.255626988e-11, 3.849164436e-14, 4.118001049e-15, 70330.94018, 1.702486633e-12, 5.231687739e-10, 1.160833062e-11, 1.520954679e-13, 6.516092126e-13, 4.5130864e-12, 1.189271575e-13, 59498352.14, 7.637095297e-11, 2.077809203e-11, 1.693268405e-16], [103604466.8, 5.147830377e-10, 2.555669766e-11, 1.577513799e-10, 7.06927457e-12, 7.749274864e-13, 5.629436205e-11, 5.388019541e-12, 1668134718.0, 1.018843146e-10, 1.448971099e-11, 3.97227584e-14, 4.24770028e-15, 76801.38996, 1.856233188e-12, 5.636848595e-10, 1.235584764e-11, 1.635268638e-13, 7.059906874e-13, 4.931281328e-12, 1.282921355e-13, 57974706.1, 7.433464272e-11, 2.021730405e-11, 1.682673894e-16], [102774602.2, 4.969825098e-10, 2.47700505e-11, 1.505647384e-10, 6.808433008e-12, 7.170484343e-13, 5.178202683e-11, 4.942144026e-12, 1661382373.0, 9.977833899e-11, 1.543059111e-11, 3.898554687e-14, 4.153419587e-15, 71022.22811, 1.669666037e-12, 5.08199167e-10, 1.182462094e-11, 1.534655067e-13, 6.625060838e-13, 4.635038995e-12, 1.187210017e-13, 57726922.99, 7.412694585e-11, 2.008389407e-11, 1.639898396e-16], [91005276.21, 4.135697113e-10, 1.902534725e-11, 1.064971384e-10, 5.071908925e-12, 4.86634679e-13, 3.496084312e-11, 3.319365125e-12, 1822656190.0, 9.946101877e-11, 1.271479104e-11, 3.212361911e-14, 3.420807838e-15, 48124.00085, 1.159312411e-12, 3.601224952e-10, 1.106195337e-11, 1.389732053e-13, 5.970028127e-13, 3.810609815e-12, 9.788536388e-14, 62013156.18, 8.088488579e-11, 2.154418124e-11, 1.502247844e-16], [97258129.17, 4.120987679e-10, 1.920947344e-11, 1.100257483e-10, 5.122082947e-12, 5.075331066e-13, 3.559331204e-11, 3.396937917e-12, 1817412558.0, 9.444244216e-11, 1.194924106e-11, 3.213734619e-14, 3.363873158e-15, 49021.77289, 1.129336567e-12, 3.637854715e-10, 1.099030876e-11, 1.38168414e-13, 5.955276454e-13, 3.819645986e-12, 9.795582523e-14, 61170106.7, 7.982575536e-11, 2.124037919e-11, 1.509650084e-16], [100356936.0, 3.773327596e-10, 1.771146459e-11, 1.023564041e-10, 4.741014622e-12, 4.691925769e-13, 3.231929532e-11, 3.026971643e-12, 1880089970.0, 8.897591263e-11, 1.106329752e-11, 3.090135016e-14, 3.25376296e-15, 44865.93754, 1.009546441e-12, 3.360355355e-10, 1.027351012e-11, 1.251610641e-13, 5.292283289e-13, 3.527908265e-12, 8.830285232e-14, 61638732.86, 8.083046414e-11, 2.147716921e-11, 1.48457224e-16], [101410983.2, 3.621208289e-10, 1.741337947e-11, 1.017278831e-10, 4.570671093e-12, 4.798567539e-13, 3.170449103e-11, 2.953838902e-12, 1955616658.0, 8.940553124e-11, 1.072620079e-11, 3.008307346e-14, 3.172288719e-15, 44374.96443, 1.047616584e-12, 3.602335961e-10, 1.089655895e-11, 1.30570917e-13, 5.52982955e-13, 3.762216681e-12, 9.518468347e-14, 61795127.68, 8.134597114e-11, 2.158986092e-11, 1.455970265e-16], [101336833.8, 3.407292355e-10, 1.659758921e-11, 9.693000168e-11, 4.291370229e-12, 4.599613843e-13, 3.007317449e-11, 2.785194671e-12, 2024426158.0, 9.014731574e-11, 9.953129444e-12, 2.806773933e-14, 2.993235729e-15, 41977.78291, 1.00169988e-12, 3.54534221e-10, 1.05496895e-11, 1.238248964e-13, 5.198517326e-13, 3.660838764e-12, 9.249568703e-14, 62124312.68, 8.198840536e-11, 2.173206367e-11, 1.438507105e-16]]
input.raercol_nsav_kp1 = [[110124282.0, 5.643795263e-10, 2.715156736e-11, 1.604202975e-10, 7.480198785e-12, 7.615811872e-13, 5.646422312e-11, 5.380242278e-12, 1740581997.0, 1.082173115e-10, 1.439554006e-11, 3.763225242e-14, 4.019374946e-15, 76902.6209, 1.834021917e-12, 5.521518393e-10, 1.319401506e-11, 1.74854942e-13, 7.56610322e-13, 5.039609e-12, 1.325530478e-13, 60327092.64, 7.768613647e-11, 2.102838949e-11, 1.634896327e-16], [116740499.3, 6.18458516e-10, 2.903683294e-11, 1.616097566e-10, 7.792026659e-12, 7.436601206e-13, 5.426093226e-11, 5.190759119e-12, 1798025357.0, 1.114309631e-10, 1.487407414e-11, 3.632022709e-14, 3.855864538e-15, 74414.29007, 1.857881195e-12, 5.537007049e-10, 1.58305467e-11, 2.045719226e-13, 8.851057917e-13, 5.635569071e-12, 1.476781113e-13, 62035060.78, 8.038872153e-11, 2.153502548e-11, 1.544654703e-16], [117831943.4, 6.062536132e-10, 2.799307464e-11, 1.500052628e-10, 7.408610593e-12, 6.663225042e-13, 4.838988039e-11, 4.607219313e-12, 1846162195.0, 1.122346852e-10, 1.546931081e-11, 3.428717726e-14, 3.643917359e-15, 66873.02512, 1.636632085e-12, 5.053001906e-10, 1.612060337e-11, 2.014646121e-13, 8.641573864e-13, 5.475933681e-12, 1.412117363e-13, 63203016.99, 8.236321236e-11, 2.187543477e-11, 1.468502094e-16], [94121474.56, 4.33494078e-10, 1.935124218e-11, 1.030608415e-10, 5.097439772e-12, 4.567456432e-13, 3.321665886e-11, 3.155922225e-12, 1916088329.0, 1.042710336e-10, 1.249056967e-11, 3.012692408e-14, 3.208358425e-15, 45518.54242, 1.116385844e-12, 3.45498772e-10, 1.204801122e-11, 1.492850804e-13, 6.38557104e-13, 3.924829705e-12, 1.012030441e-13, 64448214.66, 8.460533581e-11, 2.239629516e-11, 1.429980194e-16], [102591608.1, 4.214910441e-10, 1.883712167e-11, 9.392039959e-11, 4.878147314e-12, 3.989908621e-13, 2.994531133e-11, 2.797945873e-12, 2102390708.0, 1.005784448e-10, 1.131328967e-11, 2.611895931e-14, 2.998911746e-15, 39782.88121, 9.799608007e-13, 3.15702787e-10, 1.275442331e-11, 1.587680461e-13, 6.87799494e-13, 3.919651048e-12, 1.02011841e-13, 67742946.43, 8.994305267e-11, 2.357987498e-11, 1.314050927e-16], [108962774.7, 3.807324206e-10, 1.77006546e-11, 9.261629628e-11, 4.546868947e-12, 4.128304826e-13, 2.92642707e-11, 2.794782931e-12, 2152752187.0, 9.233534977e-11, 1.057225269e-11, 2.537716396e-14, 2.907141133e-15, 37904.07709, 9.136700299e-13, 2.923413527e-10, 1.152839908e-11, 1.418944235e-13, 6.066558649e-13, 3.589965839e-12, 9.283489071e-14, 67312070.1, 8.975298119e-11, 2.351962626e-11, 1.281988945e-16], [110414288.4, 3.537303344e-10, 1.563717025e-11, 7.799219171e-11, 4.010723134e-12, 3.195200473e-13, 2.44042294e-11, 2.353296197e-12, 2254613736.0, 9.292996994e-11, 9.789625159e-12, 2.299154049e-14, 2.627401842e-15, 31935.64639, 7.274621858e-13, 2.625535311e-10, 1.124706005e-11, 1.331112174e-13, 5.569552093e-13, 3.378401329e-12, 8.682697905e-14, 67889344.45, 9.083787335e-11, 2.375102028e-11, 1.254821018e-16], [108302060.7, 3.458397069e-10, 1.576828732e-11, 7.992464882e-11, 4.074690284e-12, 3.406417611e-13, 2.344459788e-11, 2.239685739e-12, 2301234445.0, 9.773120563e-11, 9.909258697e-12, 2.278659413e-14, 2.502448013e-15, 31850.77119, 7.712161591e-13, 2.559132771e-10, 1.067550604e-11, 1.246513772e-13, 5.16436593e-13, 3.257793e-12, 8.476412301e-14, 67548349.04, 9.0402371e-11, 2.361898188e-11, 1.258472109e-16]]
input.state_q_col_in_kp1 = [[0.0009835697905, 1.964915056e-06, 3.039515269e-09, 4436142.764, 9.941028606, 1.099371079e-07, 7.027088905e-06, 31.66404135, 158.5115583, 1.056331714e-07, 1.065035071e-10, 7.096024095e-13, 1.222776307e-10, 3.321189866e-16, 2.95557524e-12, 5.64325949e-10, 2.714910582e-11, 1.604060271e-10, 7.479525638e-12, 7.615125088e-13, 5.645916519e-11, 5.379759402e-12, 110117175.9, 1.08215266e-10, 1.439530828e-11, 3.763158354e-14, 4.01930325e-15, 1740580083.0, 1.833849293e-12, 5.521007058e-10, 1.319269717e-11, 1.748380042e-13, 7.565384866e-13, 5.039131292e-12, 1.325403859e-13, 76895.63198, 7.768613647e-11, 2.102838949e-11, 1.634896327e-16, 60327092.64], [0.0009769230536, 3.589337173e-06, 1.323470673e-08, 104579.4929, 1.208436538, 1.161337695e-10, 3.374947303e-06, 4.433250828, 120.6711053, 1.059019435e-07, 1.059974643e-10, 5.714023921e-13, 1.346214559e-10, 2.271631942e-15, 2.387373862e-12, 6.18458516e-10, 2.903683294e-11, 1.616097566e-10, 7.792026659e-12, 7.436601206e-13, 5.426093226e-11, 5.190759119e-12, 116740499.3, 1.114309631e-10, 1.487407414e-11, 3.632022709e-14, 3.855864538e-15, 1798025357.0, 1.857881195e-12, 5.537007049e-10, 1.58305467e-11, 2.045719226e-13, 8.851057917e-13, 5.635569071e-12, 1.476781113e-13, 74414.29007, 8.038872153e-11, 2.153502548e-11, 1.544654703e-16, 62035060.78], [0.001002218998, 1.06151662e-05, 1.720067856e-09, 22283902.01, 0.9316700295, 1.024705871e-07, 4.400928998e-06, 12.65592098, 173.8855864, 1.059518261e-07, 9.999331391e-11, 2.237437206e-13, 1.473538386e-10, 1.04224647e-14, 2.029443419e-12, 5.29440679e-10, 2.479230808e-11, 1.334796786e-10, 6.56644555e-12, 5.932921507e-13, 4.304169252e-11, 4.096482073e-12, 107072340.5, 1.061134916e-10, 1.503371457e-11, 3.325036989e-14, 3.534597175e-15, 1840722961.0, 1.44884616e-12, 4.487332447e-10, 1.410696015e-11, 1.766422843e-13, 7.589812362e-13, 4.830424881e-12, 1.242685602e-13, 59288.2142, 8.236321236e-11, 2.187543477e-11, 1.468502094e-16, 63203016.99], [0.001039495712, 3.687148135e-05, 4.162738941e-08, 44993167.49, 0.6603315943, 3.849202777e-09, 1.250039678e-06, 133.3792408, 160.7674471, 1.057112696e-07, 8.478034375e-11, 1.632386084e-13, 1.720298119e-10, 4.76961399e-14, 4.12973926e-12, 5.232757865e-10, 2.335911143e-11, 1.244059506e-10, 6.153179342e-12, 5.513430236e-13, 4.009621854e-11, 3.809550737e-12, 108871072.2, 1.102705263e-10, 1.32092456e-11, 3.186035144e-14, 3.392959291e-15, 1925835116.0, 1.349098527e-12, 4.175186267e-10, 1.455944133e-11, 1.804038301e-13, 7.716655072e-13, 4.742967678e-12, 1.222990048e-13, 55006.96554, 8.460533581e-11, 2.239629516e-11, 1.429980194e-16, 64448214.66], [0.001043380745, 5.352383479e-05, 2.758173036e-09, 83855555.41, 0.1594316651, 3.129711354e-08, 4.350308547e-06, 166.6209867, 183.6133505, 1.060304383e-07, 7.53313934e-11, 2.185505081e-13, 1.617901112e-10, 7.102593735e-14, 5.197427762e-12, 3.776614782e-10, 1.717151521e-11, 8.645110526e-11, 4.452758317e-12, 3.689398586e-13, 2.768994061e-11, 2.584104568e-12, 96976575.57, 9.531741823e-11, 1.110526672e-11, 2.567425212e-14, 2.952241351e-15, 2099183872.0, 9.008832706e-13, 2.911618794e-10, 1.154157928e-11, 1.443265324e-13, 6.274542267e-13, 3.575031942e-12, 9.300764956e-14, 36671.68808, 8.994305267e-11, 2.357987498e-11, 1.314050927e-16, 67742946.43], [0.001053518465, 8.387580175e-05, 3.989109096e-09, 80323960.27, 0.3829964164, 2.393095319e-08, 3.655454939e-06, 624.2089496, 168.4421209, 1.061420681e-07, 6.41326075e-11, 2.022628269e-13, 1.62218934e-10, 1.139862141e-13, 5.961657393e-12, 3.786214394e-10, 1.762699826e-11, 9.228976861e-11, 4.528119408e-12, 4.11513967e-13, 2.916532101e-11, 2.785425537e-12, 108719817.0, 9.204504439e-11, 1.056447713e-11, 2.53603065e-14, 2.905363854e-15, 2152629661.0, 9.102170711e-13, 2.912672319e-10, 1.147477884e-11, 1.412553447e-13, 6.03984221e-13, 3.57477394e-12, 9.243751342e-14, 37767.50963, 8.975298119e-11, 2.351962626e-11, 1.281988945e-16, 67312070.1], [0.001059082976, 0.0001069309716, 3.679691498e-09, 80887614.82, 0.6839655813, 4.269662909e-08, 5.526108449e-06, 1029.137231, 168.1961152, 1.064581169e-07, 5.728400767e-11, 1.879991698e-13, 1.414017101e-10, 1.331939962e-13, 6.732608523e-12, 3.537303344e-10, 1.563717025e-11, 7.799219171e-11, 4.010723134e-12, 3.195200473e-13, 2.44042294e-11, 2.353296197e-12, 110414288.4, 9.292996994e-11, 9.789625159e-12, 2.299154049e-14, 2.627401842e-15, 2254613736.0, 7.274621858e-13, 2.625535311e-10, 1.124706005e-11, 1.331112174e-13, 5.569552093e-13, 3.378401329e-12, 8.682697905e-14, 31935.64639, 9.083787335e-11, 2.375102028e-11, 1.254821018e-16, 67889344.45], [0.001058438327, 7.76908465e-05, 8.097456383e-08, 81077687.95, 49.39782494, 8.532059007e-09, 6.152151069e-06, 1189.758759, 179.5176848, 1.070607209e-07, 5.7346104e-11, 1.442992572e-13, 1.343239786e-10, 1.247614308e-13, 6.911316133e-12, 3.443372938e-10, 1.571441721e-11, 7.969376927e-11, 4.061025141e-12, 3.397273936e-13, 2.33762571e-11, 2.233275802e-12, 108128250.2, 9.756631048e-11, 9.904653104e-12, 2.277657006e-14, 2.501384057e-15, 2301169204.0, 7.68881074e-13, 2.551703681e-10, 1.063539267e-11, 1.241762855e-13, 5.144713816e-13, 3.246581056e-12, 8.447273586e-14, 31756.20113, 9.0402371e-11, 2.361898188e-11, 1.258472109e-16, 67548349.04]]
input.temp_col_in = [[252.1759162], [252.003983], [251.7191301], [251.5421904], [251.57466], [251.6024778], [251.5121714], [251.5071732]]
input.top_lev = [[7], [7], [7], [7], [7], [7], [7], [7]]
input.wtke_col_in = [[0.2330456614], [0.2744434054], [0.3760692874], [0.3945409021], [0.4069090994], [0.3600135653], [0.3450696613], [0.2639808362]]
input.zs = [[0.004359578575], [0.004363439669], [0.004368917849], [0.004371955058], [0.004372106459], [0.004372264142], [0.004373040817], [0.004372981945]]

# Output data is stored here.
output = Object()
output.ekd = [[11.07826123], [13.01678513], [19.68795132], [23.93825076], [23.93334729], [21.86194472], [26.02797166], [15.53073251]]
output.factnum_col = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.785150017, 0.02922287322, 0.9999999255, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]
output.mact = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]
output.nact = [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]
output.nsource_col = [[-18699.78447], [0.0], [-10582.57307], [36707.44753], [-14618.21691], [-4485.838512], [-1808.308093], [-20.26852044]]
output.qcld = [[5085392.165], [888594.0101], [10052044.03], [64632541.14], [61701502.59], [64015087.47], [65187628.94], [71883802.87]]
output.raercol_cw_nsav = [[1134680.896, 1.520647155e-11, 7.197496425e-13, 4.356489469e-12, 1.990914694e-13, 2.152389254e-14, 1.574103036e-12, 1.503592461e-13, 300472.8886, 6.154576005e-13, 6.733091102e-14, 2.02631516e-16, 2.178077467e-17, 1202.415656, 5.328399796e-14, 1.570151623e-11, 3.516486909e-13, 4.635977147e-15, 1.976336973e-14, 1.366849015e-13, 3.622121304e-15, 0.0, 0.0, 0.0, 0.0], [53707.68193, 3.983450695e-13, 1.853625957e-14, 1.086869894e-13, 5.046331623e-15, 5.287365464e-16, 3.783278666e-14, 3.617263964e-15, 13912.76986, 1.65469807e-14, 1.726114774e-15, 5.005522886e-18, 5.355292629e-19, 53.61412692, 1.316283147e-15, 3.864054548e-13, 9.835278449e-15, 1.263283064e-16, 5.370576649e-16, 3.626712818e-15, 9.512701468e-17, 0.0, 0.0, 0.0, 0.0], [7050680.841, 4.641123024e-11, 2.162485941e-12, 1.268519143e-11, 5.868507421e-13, 6.07614882e-14, 4.344087087e-12, 4.151001826e-13, 3534952.75, 3.190879755e-12, 3.208813989e-13, 8.618120045e-16, 9.189200822e-17, 6156.207967, 1.485264338e-13, 4.446237688e-11, 1.130579368e-12, 1.460595658e-14, 6.264094137e-14, 4.224832411e-13, 1.098493541e-14, 0.0, 0.0, 0.0, 0.0], [50098060.92, 3.421453785e-10, 1.444036085e-11, 7.559169239e-11, 3.800198109e-12, 3.351676143e-13, 2.417620352e-11, 2.296031677e-12, 30668823.16, 3.271839388e-11, 2.340012444e-12, 5.652488077e-15, 5.984708015e-16, 33628.46871, 8.295783186e-13, 2.554977122e-10, 9.049222767e-12, 1.108373697e-13, 4.688964771e-13, 2.916362322e-12, 7.556264068e-14, 0.0, 0.0, 0.0, 0.0], [54678157.52, 4.067349819e-10, 1.597805644e-11, 8.070079038e-11, 4.181117668e-12, 3.53067914e-13, 2.557489289e-11, 2.416879283e-12, 31637028.76, 4.946912864e-11, 2.220314587e-12, 5.438894652e-15, 5.759816008e-16, 35571.75328, 8.753115414e-13, 2.716965384e-10, 1.030799198e-11, 1.250891631e-13, 5.266464341e-13, 3.239761088e-12, 8.391870738e-14, 0.0, 0.0, 0.0, 0.0], [62445526.58, 4.986480902e-10, 1.855044528e-11, 9.071305738e-11, 4.813188229e-12, 3.933174871e-13, 2.878440417e-11, 2.70734599e-12, 33032772.82, 6.660209781e-11, 2.238536031e-12, 5.61779278e-15, 5.959693636e-16, 39931.04838, 9.769935101e-13, 3.068490669e-10, 1.23419123e-11, 1.488938305e-13, 6.253710329e-13, 3.785394733e-12, 9.815446838e-14, 0.0, 0.0, 0.0, 0.0], [65357442.52, 5.333217189e-10, 1.95895211e-11, 9.333334984e-11, 5.059040858e-12, 3.991353827e-13, 2.926372992e-11, 2.741809515e-12, 30873220.4, 6.911668032e-11, 2.114100722e-12, 5.300528657e-15, 5.639021004e-16, 40722.93133, 9.889569598e-13, 3.123432042e-10, 1.328356922e-11, 1.592776747e-13, 6.65485822e-13, 4.002059437e-12, 1.03492015e-13, 0.0, 0.0, 0.0, 0.0], [68421521.86, 5.656870088e-10, 2.066460915e-11, 9.606721672e-11, 5.323176057e-12, 4.042313332e-13, 2.96902809e-11, 2.774437623e-12, 28577708.43, 6.864108254e-11, 1.998478064e-12, 4.99265112e-15, 5.318320014e-16, 41587.85612, 9.901053524e-13, 3.168880323e-10, 1.428672548e-11, 1.706578945e-13, 7.097997832e-13, 4.237580248e-12, 1.094283671e-13, 0.0, 0.0, 0.0, 0.0]]
output.raercol_nsav = [[96544090.28, 4.950663634e-10, 2.337809451e-11, 1.437013909e-10, 6.510821703e-12, 7.071779738e-13, 5.305065654e-11, 5.067547101e-12, 1710098188.0, 1.053993054e-10, 1.255626988e-11, 3.849164436e-14, 4.118001049e-15, 70330.94018, 1.702486633e-12, 5.231687739e-10, 1.160833062e-11, 1.520954679e-13, 6.516092126e-13, 4.5130864e-12, 1.189271575e-13, 59498352.14, 7.637095297e-11, 2.077809203e-11, 1.693268405e-16], [103604466.8, 5.147830377e-10, 2.555669766e-11, 1.577513799e-10, 7.06927457e-12, 7.749274864e-13, 5.629436205e-11, 5.388019541e-12, 1668134718.0, 1.018843146e-10, 1.448971099e-11, 3.97227584e-14, 4.24770028e-15, 76801.38996, 1.856233188e-12, 5.636848595e-10, 1.235584764e-11, 1.635268638e-13, 7.059906874e-13, 4.931281328e-12, 1.282921355e-13, 57974706.1, 7.433464272e-11, 2.021730405e-11, 1.682673894e-16], [102774602.2, 4.969825098e-10, 2.47700505e-11, 1.505647384e-10, 6.808433008e-12, 7.170484343e-13, 5.178202683e-11, 4.942144026e-12, 1661382373.0, 9.977833899e-11, 1.543059111e-11, 3.898554687e-14, 4.153419587e-15, 71022.22811, 1.669666037e-12, 5.08199167e-10, 1.182462094e-11, 1.534655067e-13, 6.625060838e-13, 4.635038995e-12, 1.187210017e-13, 57726922.99, 7.412694585e-11, 2.008389407e-11, 1.639898396e-16], [91005276.21, 4.135697113e-10, 1.902534725e-11, 1.064971384e-10, 5.071908925e-12, 4.86634679e-13, 3.496084312e-11, 3.319365125e-12, 1822656190.0, 9.946101877e-11, 1.271479104e-11, 3.212361911e-14, 3.420807838e-15, 48124.00085, 1.159312411e-12, 3.601224952e-10, 1.106195337e-11, 1.389732053e-13, 5.970028127e-13, 3.810609815e-12, 9.788536388e-14, 62013156.18, 8.088488579e-11, 2.154418124e-11, 1.502247844e-16], [97258129.17, 4.120987679e-10, 1.920947344e-11, 1.100257483e-10, 5.122082947e-12, 5.075331066e-13, 3.559331204e-11, 3.396937917e-12, 1817412558.0, 9.444244216e-11, 1.194924106e-11, 3.213734619e-14, 3.363873158e-15, 49021.77289, 1.129336567e-12, 3.637854715e-10, 1.099030876e-11, 1.38168414e-13, 5.955276454e-13, 3.819645986e-12, 9.795582523e-14, 61170106.7, 7.982575536e-11, 2.124037919e-11, 1.509650084e-16], [100356936.0, 3.773327596e-10, 1.771146459e-11, 1.023564041e-10, 4.741014622e-12, 4.691925769e-13, 3.231929532e-11, 3.026971643e-12, 1880089970.0, 8.897591263e-11, 1.106329752e-11, 3.090135016e-14, 3.25376296e-15, 44865.93754, 1.009546441e-12, 3.360355355e-10, 1.027351012e-11, 1.251610641e-13, 5.292283289e-13, 3.527908265e-12, 8.830285232e-14, 61638732.86, 8.083046414e-11, 2.147716921e-11, 1.48457224e-16], [101410983.2, 3.621208289e-10, 1.741337947e-11, 1.017278831e-10, 4.570671093e-12, 4.798567539e-13, 3.170449103e-11, 2.953838902e-12, 1955616658.0, 8.940553124e-11, 1.072620079e-11, 3.008307346e-14, 3.172288719e-15, 44374.96443, 1.047616584e-12, 3.602335961e-10, 1.089655895e-11, 1.30570917e-13, 5.52982955e-13, 3.762216681e-12, 9.518468347e-14, 61795127.68, 8.134597114e-11, 2.158986092e-11, 1.455970265e-16], [101336833.8, 3.407292355e-10, 1.659758921e-11, 9.693000168e-11, 4.291370229e-12, 4.599613843e-13, 3.007317449e-11, 2.785194671e-12, 2024426158.0, 9.014731574e-11, 9.953129444e-12, 2.806773933e-14, 2.993235729e-15, 41977.78291, 1.00169988e-12, 3.54534221e-10, 1.05496895e-11, 1.238248964e-13, 5.198517326e-13, 3.660838764e-12, 9.249568703e-14, 62124312.68, 8.198840536e-11, 2.173206367e-11, 1.438507105e-16]]