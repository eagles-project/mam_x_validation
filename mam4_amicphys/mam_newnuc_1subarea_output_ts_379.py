# Data at [lat=  -5.57727434969463      , lon=   184.674947489650      , k=           7 , time step=         379 ] 
# This file was generated by E3SM.

from math import nan as nan, inf as inf

# Object is just a dynamic container that stores input/output data.
class Object(object):
    pass
# Settings are stored here.
settings = Object()
# Input is stored here.
input = Object()
input.nstep=[[       379],]
input.lchnk=[[       149],]
input.i=[[         2],]
input.k=[[         7],]
input.jsub=[[         1],]
input.latndx=[[        40],]
input.lonndx=[[         1],]
input.lund=[[         6],]
input.n_mode=[[         4],]
input.deltat=[[  0.36000000000000000E+004],]
input.temp=[[  0.25995373754907484E+003],]
input.pmid=[[  0.12829949082549251E+003],]
input.aircon=[[  0.59360072406377424E-004],]
input.zmid=[[  0.45289866857352390E+005],]
input.pblh=[[  0.79393332557991255E+003],]
input.relhum=[[  0.24854031730334133E-005],]
input.del_h2so4_gasprod=[[  0.57113125173361250E-024],]
input.del_h2so4_aeruptk=[[ -0.34160551047908708E-023],]
input.uptkrate_h2so4=[[  0.13822881997464704E-007],]
input.qgas_avg=[[  0.13828832072212411E-012,  0.68647348385388545E-019,],]
input.dnclusterdt=[[  0.00000000000000000E+000],]
input.qgas_cur=[[  0.13835924320997904E-012,  0.68645925935259890E-019,],]
input.qnum_cur=[[  0.48466036652806262E+007,  0.93682582559041488E+009,  0.28753230515972595E-003,  0.38881705045598288E+002,  0.00000000000000000E+000,],]
input.qaer_cur=[[  0.18646182671130300E-015,  0.10699261810997502E-013,  0.24151407684770937E-014,  0.59404583322596666E-014,  0.37213194077909832E-014,  0.30718174305573901E-014,  0.42629305177426783E-026,  0.12198714405758272E-015,  0.95092954863016933E-012,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.28905273200087140E-013,  0.00000000000000000E+000,  0.10460641838443952E-025,  0.00000000000000000E+000,  0.64915118209793495E-019,  0.19293354301817811E-036,  0.24116700315277469E-035,  0.49564257801905307E-036,  0.21446538904102464E-036,  0.11582334282467170E-039,  0.55542343687615469E-024,  0.34129306330310126E-030,  0.62183783368425671E-019,  0.86052456241078875E-019,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.54095777109620501E-029,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,],]
input.qwtr_cur=[[  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,],]
input.max_gas=[[         2],]
input.max_aer=[[         7],]
input.max_mode=[[         5],]
input.iaer_so4=[[         2],]
input.iaer_nh4=[[         0],]
input.igas_h2so4=[[         2],]
input.igas_nh3=[[         0],]
input.nait=[[         2],]
input.dgnum_aer=[[  0.26000000000000001E-007],]
input.dgnumlo_aer=[[  0.87000000000000001E-008],]
input.dgnumhi_aer=[[  0.52000000000000002E-007],]
input.gaexch_h2so4_uptake_optaa=[[         2],]
input.newnuc_h2so4_conc_optaa=[[         2],]
input.dens_so4a_host=[[  0.17700000000000000E+004],]
input.mwso4a_host=[[  0.11500000000000000E+003],]
input.newnuc_adjust_factor_dnaitdt=[[  0.10000000000000000E+001],]
input.mw_nh4a_host=[[  0.11500000000000000E+003],]
input.qh2so4_cutoff=[[  0.39999999999999999E-015],]
# Output data is stored here.
output = Object()
output.dnclusterdt=[[  0.00000000000000000E+000],]
output.qgas_cur=[[  0.13835924320997904E-012,  0.68645925935259890E-019,],]
output.qaer_cur=[[  0.18646182671130300E-015,  0.10699261810997502E-013,  0.24151407684770937E-014,  0.59404583322596666E-014,  0.37213194077909832E-014,  0.30718174305573901E-014,  0.42629305177426783E-026,  0.12198714405758272E-015,  0.95092954863016933E-012,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.28905273200087140E-013,  0.00000000000000000E+000,  0.10460641838443952E-025,  0.00000000000000000E+000,  0.64915118209793495E-019,  0.19293354301817811E-036,  0.24116700315277469E-035,  0.49564257801905307E-036,  0.21446538904102464E-036,  0.11582334282467170E-039,  0.55542343687615469E-024,  0.34129306330310126E-030,  0.62183783368425671E-019,  0.86052456241078875E-019,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.54095777109620501E-029,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,],]
output.qnum_cur=[[  0.48466036652806262E+007,  0.93682582559041488E+009,  0.28753230515972595E-003,  0.38881705045598288E+002,  0.00000000000000000E+000,],]
output.qwtr_cur=[[  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,  0.00000000000000000E+000,],]
