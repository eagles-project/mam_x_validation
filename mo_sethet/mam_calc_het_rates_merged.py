# This file was automatically generated using the following command:
# ./merge_ensembles.py mam_calc_het_rates_ts_340.py mam_calc_het_rates_ts_341.py mam_calc_het_rates_ts_342.py mam_calc_het_rates_ts_343.py mam_calc_het_rates_ts_344.py mam_calc_het_rates_ts_345.py mam_calc_het_rates_ts_346.py mam_calc_het_rates_ts_347.py mam_calc_het_rates_ts_348.py mam_calc_het_rates_ts_349.py mam_calc_het_rates_ts_350.py mam_calc_het_rates_ts_351.py mam_calc_het_rates_ts_352.py mam_calc_het_rates_ts_353.py mam_calc_het_rates_ts_354.py mam_calc_het_rates_ts_355.py

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass

# Settings are stored here.
settings = Object()

# Input is stored here.
input = Object()
input.rain = [[1299472042470.2769], [1276063460415.693], [1181216366326.5166], [1134671504112.2395], [1068915541292.0929], [1044385249585.5887], [871039703888.4596], [868269763186.0521], [1005820680045.5923], [1032304350340.2238], [1028026498220.75], [1115198612479.0989], [1125978510362.9744], [1140328606777.3682], [1136151041461.0425], [1111150971591.9458]]
input.satf = [[0.016], [0.016], [0.016], [0.016], [0.016], [0.016], [0.016], [0.016], [0.016], [0.016], [0.016], [0.016], [0.016], [0.016], [0.016], [0.016]]
input.tmp_hetrates = [[3.259368235301288e-05], [3.555662829567905e-05], [3.138876121226411e-05], [3.338612676068957e-05], [3.254618887392328e-05], [3.05033534785333e-05], [2.8344849183165465e-05], [3.813742963092593e-05], [3.228015519801562e-05], [4.117896433033026e-05], [3.0911128008984844e-05], [4.298889529363256e-05], [3.798123287188986e-05], [4.1044522278479e-05], [3.741122812522193e-05], [3.3326813518612723e-05]]
input.work1 = [[84205788352073.97], [82688912234936.89], [76542820537958.25], [73526713466473.12], [69265727075727.62], [67676164173146.13], [56443372811972.17], [56263880654456.164], [65177180066954.37], [66893321902046.484], [66616117084704.6], [72264870088645.6], [72963407471520.72], [73893293719173.44], [73622587486675.55], [72002582959158.06]]
input.work2 = [[3.870389133799473e-20], [3.871908177637599e-20], [3.8730961515416465e-20], [3.874360569363349e-20], [3.875719032545899e-20], [3.876309050183006e-20], [3.8760556209441924e-20], [3.8751893261241895e-20], [3.8748989715227705e-20], [3.874710698139505e-20], [3.873947402230487e-20], [3.8727556575077706e-20], [3.871916855854878e-20], [3.8713653207922946e-20], [3.8713773391432576e-20], [3.8717760536287645e-20]]
input.xhen = [[302167.02366970247], [299380.4596516486], [297220.640855261], [294940.3955723035], [292511.677479703], [291463.5843168697], [291913.2699605141], [293456.11882399657], [293975.21040674613], [294312.33501811733], [295683.40498611523], [297837.9494094691], [299364.6204606463], [300373.07302690804], [300351.0588783679], [299621.7202684875]]

# Output data is stored here.
output = Object()
output.het_rates = [[3.479887510365619e-05], [3.7731771691452433e-05], [3.3470563943107784e-05], [3.541536659139549e-05], [3.450111214319967e-05], [3.242913868310281e-05], [3.007701897650256e-05], [3.987156889847138e-05], [3.417391133074427e-05], [4.3102217118664846e-05], [3.2834706063132255e-05], [4.500937287237748e-05], [4.001771674499393e-05], [4.3098543630642055e-05], [3.946111788845816e-05], [3.534958568509605e-05]]
