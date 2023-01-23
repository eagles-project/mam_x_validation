# To run this script:
# get python files from e3sm_mam4_refator : https://github.com/eagles-project/e3sm_mam4_refactor/pull/51/files
# get merge_ensembles script from skywalker: https://github.com/eagles-project/skywalker/blob/c92dfb45e39b7e2fac33b3d1017163cf6e5b3b52/tools/merge_ensembles

merge_files_w_modes(){
  echo "Working on " $case_name
  this=""
  for ts in "378" "379";do
    for imode in "1" "2" "3" "4"; do
      this+=$first_name$imode${second_name}${ts}.py" " 
    done
  done
  ./merge_ensembles.py $this
  
  mv merged.py mam_$case_name.py
  mv merged.yaml $case_name.yaml
}
merge_files(){
  echo "Working on " $case_name
  this=""
  for ts in "378" "379";do
      this+=$first_name${second_name}${ts}.py" " 
  done
  ./merge_ensembles.py $this
  
  mv merged.py mam_$case_name.py
  mv merged.yaml $case_name.yaml
}

case_name=calcsize_compute_dry_volume
first_name=${case_name}_mode
second_name=_output_ts_
merge_files_w_modes

case_name=calcsize_set_initial_sz_and_volumes
first_name=${case_name}_mode
second_name=_output_ts_
merge_files_w_modes

case_name=calcsize_sub
first_name=${case_name}
second_name=_output_ts_
merge_files
