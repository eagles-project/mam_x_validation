# To run this script:
# get python files from e3sm_mam4_refator : e3sm_mam4_refactor/components/eam/src/physics/yaml/nucleate_ice 
# get merge_ensembles script from skywalker: skywalker_repo/tools/merge_ensembles 

merge_files(){
  echo "Working on " $case_name
  this=""
  for ts in "${list[@]}" ;do
      this+=${case_name}_output_ts_${ts}.py" " 
  done
  ./merge_ensembles.py $this
  
  mv merged.py mam_${case_name}_merged.py
  mv merged.yaml ${case_name}_merged.yaml
}

list=("1402" "1403" "1410" "1410")
case_name=hetero 
merge_files

list=("1402" "1403" "1404" "1406")
case_name=hf 
merge_files

list=("1402" "1403" "1404" "1406" "1410")
case_name=nucleati 
merge_files

