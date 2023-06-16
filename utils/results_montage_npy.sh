#!/bin/zsh

#
# Creates a montage from npy data files of results at given time points (see below).
# If inkscape available in PATH, converts the montage svg to png.
#
# Depends:
# - npy_to_png.py
# - make_montage.py
# - inkscape (optional)
#

# Relative time points to include in the montage. You may modify this as desired.
timePoints=(0 1/32 1/16 1/8 1/4 1/2 1)

rm -rf __pycache__

folders=(`ls -d */`)    # folders where to look for images
cnt=0                   # folder counter 
tmpFiles=()             # temporary files for creating a montage
basedir=$(dirname "$0") # location of the script

for folder in "${folders[@]}"
do
    cd $folder
    files=(`ls -Art | grep -E '^[0-9]+.npy' | sort -n`)
    
    # Make temporary copies of the requested time points.
    for t in "${timePoints[@]}"
    do
        idx=$(((${#files[*]}-1) * $t))
        file=${files[@]:$idx:1}
        cp $file ../$cnt"_"$file
        tmpFiles+=($cnt"_"$file)
    done
    
    cd ..
    cnt=$((cnt+1))
done

# Convert npys to pngs:
python $basedir/npy_to_png.py

# Create image montage with number of columns == number of time points.
# Font size 9. Row info expected to be given in 'info.txt' in the present folder.

outName=${PWD##*/}
echo $outName
python $basedir/make_montage.py . $outName".svg" ${#timePoints[*]} 9 info.txt

# Clean-up
for file in "${tmpFiles[@]}"
do
    file="${file%.*}"
    rm $file".png"
    rm $file".npy"
done

# Make a PNG copy of the SVG for easier viewing. ImageMagic doesn't work for
# unknown reason.
inkscape $outName".svg" -d 300 -o $outName".png"

