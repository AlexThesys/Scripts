#!/bin/bash
path=$1
ext="*.${2}"
echo $path
echo $ext
match="*."
files_checked=0
folders_checked=0
max_file_size=0

for j in $path/*; do
    dir=${j##*/}
    if [[ -d $path/$dir ]]; then
        let folders_checked++
        for i in $path/$dir/*.*; do 
            file=${i##*/}
            if [[ -f $i ]] && [[ $file == $ext ]]; then
                let files_checked++
                fsize_str=`wc -c  $path/$dir/$file | awk '{print $1}'` 
                echo $fsize_str
                file_size=$((fsize_str))
                if (( file_size > max_file_size )); then
                    let max_file_size=$file_size
                    #echo "mfs " $max_file_size
                fi
            fi
        done
    fi
done
echo "//=============================="
echo "folders checked: " $folders_checked
echo "files checked: " $files_checked
echo "max file size: " $max_file_size
